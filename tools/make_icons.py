"""Generate the PWA icon set with no third-party imaging dependency.

Renders a gauge mark (dark rounded square, 240-degree gradient arc, needle) at 4x
and box-downsamples for antialiasing, then writes PNGs via zlib + struct.
"""
import math
import struct
import zlib
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "icons"

BG = (11, 14, 20)          # --bg
TRACK = (30, 38, 54)
STOPS = [                  # matches the gauge gradient in index.html
    (0.00, (74, 168, 255)),
    (0.55, (55, 214, 122)),
    (1.00, (255, 178, 63)),
]
NEEDLE = (232, 236, 245)

START_DEG, SWEEP_DEG = 240.0, 240.0   # gap centred at the bottom
SS = 4                     # supersample factor


def lerp(a, b, t):
    return a + (b - a) * t


def gradient(t):
    """Sample the three-stop gradient at t in [0, 1]."""
    t = max(0.0, min(1.0, t))
    for i in range(len(STOPS) - 1):
        p0, c0 = STOPS[i]
        p1, c1 = STOPS[i + 1]
        if p0 <= t <= p1:
            k = 0.0 if p1 == p0 else (t - p0) / (p1 - p0)
            return tuple(int(round(lerp(c0[j], c1[j], k))) for j in range(3))
    return STOPS[-1][1]


def rounded_box(x, y, w, radius):
    """Is (x, y) inside a rounded square of side w? Standard rounded-box SDF."""
    half = w / 2.0
    dx = abs(x - half) - (half - radius)
    dy = abs(y - half) - (half - radius)
    outside = math.hypot(max(dx, 0.0), max(dy, 0.0))
    inside = min(max(dx, dy), 0.0)
    return outside + inside - radius <= 0.0


def render(size, padding_ratio=0.0):
    """Render one icon at `size` px. padding_ratio insets the art for maskable."""
    w = size * SS
    pad = w * padding_ratio
    inner = w - 2 * pad
    cx = cy = w / 2.0

    radius = inner * 0.23
    r_arc = inner * 0.305
    stroke = inner * 0.095
    fill_frac = 0.68                    # how much of the arc is lit

    start = math.radians(START_DEG - 90)
    sweep = math.radians(SWEEP_DEG)

    # Needle geometry, pointing at the end of the lit arc.
    n_ang = start + sweep * fill_frac
    n_len = r_arc * 0.66
    nx, ny = cx + n_len * math.cos(n_ang), cy + n_len * math.sin(n_ang)

    px = bytearray()
    for py_ in range(w):
        for px_ in range(w):
            x, y = px_ + 0.5, py_ + 0.5

            if not rounded_box(x - pad, y - pad, inner, radius):
                px += bytes((0, 0, 0, 0))
                continue

            color, alpha = BG, 255
            dx, dy = x - cx, y - cy
            dist = math.hypot(dx, dy)

            # Arc band
            if abs(dist - r_arc) <= stroke / 2.0:
                ang = math.atan2(dy, dx)
                rel = (ang - start) % (2 * math.pi)
                if rel <= sweep:
                    t = rel / sweep
                    color = gradient(t) if t <= fill_frac else TRACK

            # Needle: distance from the centre-to-tip segment
            vx, vy = nx - cx, ny - cy
            seg = vx * vx + vy * vy
            if seg > 0:
                u = max(0.0, min(1.0, (dx * vx + dy * vy) / seg))
                if math.hypot(dx - vx * u, dy - vy * u) <= stroke * 0.30:
                    color = NEEDLE
            if dist <= stroke * 0.55:
                color = NEEDLE

            px += bytes((color[0], color[1], color[2], alpha))

    return downsample(px, w, size)


def downsample(px, w, size):
    """Box-filter w*w RGBA down to size*size."""
    out = bytearray()
    for y in range(size):
        out.append(0)  # PNG filter byte: none
        for x in range(size):
            r = g = b = a = 0
            for sy in range(SS):
                row = (y * SS + sy) * w
                for sx in range(SS):
                    i = (row + x * SS + sx) * 4
                    af = px[i + 3]
                    r += px[i] * af
                    g += px[i + 1] * af
                    b += px[i + 2] * af
                    a += af
            if a:
                out += bytes((r // a, g // a, b // a, a // (SS * SS)))
            else:
                out += bytes((0, 0, 0, 0))
    return bytes(out)


def write_png(path, raw, size):
    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c))

    ihdr = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", ihdr)
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))
    path.write_bytes(png)
    return len(png)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    targets = [
        ("icon-192.png", 192, 0.0),
        ("icon-512.png", 512, 0.0),
        ("icon-maskable-512.png", 512, 0.14),   # safe zone for Android masking
        ("apple-touch-icon.png", 180, 0.0),
        ("favicon-32.png", 32, 0.0),
    ]
    for name, size, pad in targets:
        n = write_png(OUT / name, render(size, pad), size)
        print(f"{name:26} {size:>4}px  {n:>7,} bytes")
