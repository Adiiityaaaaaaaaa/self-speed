"""Static site generator for Self Speed.

Reads content/*.md, renders a markdown subset, wraps each page in
tools/template.html, and writes <slug>/index.html. Also emits sitemap.xml and
robots.txt.

No third-party dependencies — the markdown subset is deliberately small and we
control every input file.

    python tools/build.py
"""
import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
TEMPLATE = ROOT / "tools" / "template.html"

# Canonical origin. PREFIX is the path the site is served from — "/" on the
# custom domain. Change both together if the site ever moves to a subpath.
BASE = "https://selfspeed.app"
PREFIX = "/"

# Order matters: this is the nav and the sitemap priority order.
NAV = [
    ("", "Speedometer"),
    ("cycling-speedometer", "Cycling"),
    ("running-speed-tracker", "Running"),
    ("car-speedometer", "Driving"),
    ("boat-speedometer-knots", "Boating"),
    ("ski-speed-tracker", "Skiing"),
    ("train-speedometer", "Transit"),
]

# Footer is grouped; each group renders as a labelled row.
FOOTER_GROUPS = [
    ("Guides", [
        ("how-gps-speedometers-work", "How GPS speedometers work"),
        ("is-gps-speed-accurate", "Is GPS speed accurate?"),
        ("average-walking-speed", "Average walking speed"),
        ("average-cycling-speed", "Average cycling speed"),
        ("average-running-speed", "Average running speed"),
    ]),
    ("Tools", [
        ("calorie-calculator", "Calorie calculator"),
        ("running-pace-calculator", "Running pace calculator"),
    ]),
    ("Convert", [
        ("kmh-to-mph", "km/h → mph"),
        ("mph-to-kmh", "mph → km/h"),
        ("knots-to-kmh", "knots → km/h"),
        ("ms-to-kmh", "m/s → km/h"),
        ("mph-to-knots", "mph → knots"),
    ]),
    ("Site", [
        ("about", "About"),
        ("contact", "Contact"),
        ("privacy", "Privacy"),
        ("terms", "Terms"),
    ]),
]


# --------------------------------------------------------------- markdown
def inline(text):
    """Inline markdown. Escapes first, so content files are plain text."""
    out = html.escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<![*\w])\*([^*]+)\*(?!\w)", r"<em>\1</em>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    return out


def render(md):
    """Render the markdown subset: headings, paragraphs, lists, tables, quotes."""
    lines = md.split("\n")
    out, i = [], 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Raw HTML passthrough: everything between ':::html' and ':::' is
        # emitted verbatim. Used for interactive widgets.
        if stripped == ":::html":
            i += 1
            raw = []
            while i < len(lines) and lines[i].strip() != ":::":
                raw.append(lines[i])
                i += 1
            i += 1  # skip closing :::
            out.append("\n".join(raw))
            continue

        # Heading
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            lvl = len(m.group(1))
            text = m.group(2)
            slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
            anchor = f' id="{slug}"' if lvl == 2 else ""
            out.append(f"<h{lvl}{anchor}>{inline(text)}</h{lvl}>")
            i += 1
            continue

        # Table
        if stripped.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            if len(rows) >= 2 and set("".join(rows[1]).replace(" ", "")) <= set("-:"):
                head, body = rows[0], rows[2:]
            else:
                head, body = None, rows
            t = ['<div class="table-wrap"><table>']
            if head:
                t.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
            t.append("<tbody>")
            for r in body:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue

        # Blockquote
        if stripped.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote><p>{inline(' '.join(buf))}</p></blockquote>")
            continue

        # Lists
        if re.match(r"^[-*]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
            ordered = bool(re.match(r"^\d+\.\s+", stripped))
            tag = "ol" if ordered else "ul"
            items = []
            pat = r"^\d+\.\s+" if ordered else r"^[-*]\s+"
            while i < len(lines) and re.match(pat, lines[i].strip()):
                items.append(re.sub(pat, "", lines[i].strip()))
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue

        # Paragraph
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#{1,4}\s|[-*]\s|\d+\.\s|\||>)", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")

    return "\n".join(out)


# ------------------------------------------------------------ front matter
def parse(path):
    raw = path.read_text(encoding="utf-8")
    meta, body = {}, raw
    if raw.startswith("---\n"):
        _, fm, body = raw.split("---\n", 2)
        for line in fm.strip().split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta, body.strip()


def url_for(slug):
    return f"{BASE}/" if slug == "" else f"{BASE}/{slug}/"


def nav_html(current):
    items = []
    for slug, label in NAV:
        href = PREFIX if slug == "" else f"{PREFIX}{slug}/"
        cls = ' class="here"' if slug == current else ""
        items.append(f'<a href="{href}"{cls}>{label}</a>')
    return "".join(items)


def footer_html():
    out = []
    for heading, items in FOOTER_GROUPS:
        links = "".join(f'<a href="{PREFIX}{slug}/">{label}</a>' for slug, label in items)
        out.append(f'<div class="fgroup"><h2>{heading}</h2><div class="links">{links}</div></div>')
    return "".join(out)



def extract_faq(md):
    """Pull question/answer pairs from a '## Frequently asked' section.

    Questions are h3 headings; the answer is the prose up to the next heading.
    Returns [] when the page has no FAQ, which is most of them.
    """
    m = re.search(r"^##\s+Frequently asked.*?$", md, re.M)
    if not m:
        return []
    section = md[m.end():]
    nxt = re.search(r"^##\s+", section, re.M)
    if nxt:
        section = section[:nxt.start()]

    pairs = []
    for qm in re.finditer(r"^###\s+(.+?)$", section, re.M):
        q = qm.group(1).strip()
        rest = section[qm.end():]
        stop = re.search(r"^#{2,3}\s+", rest, re.M)
        answer = rest[:stop.start()] if stop else rest
        # flatten markdown to plain text for the schema
        answer = re.sub(r"\*\*([^*]+)\*\*", r"\1", answer)
        answer = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", answer)
        answer = re.sub(r"`([^`]+)`", r"\1", answer)
        answer = " ".join(answer.split())
        if q and answer:
            pairs.append((q, answer))
    return pairs


def json_escape(t):
    return (t.replace("\\", "\\\\").replace('"', '\\"')
             .replace("\n", " ").replace("\r", " "))


def jsonld_for(slug, title, description, md):
    """Breadcrumbs for every page, FAQPage where questions exist, and
    SoftwareApplication on the home page."""
    blocks = []
    url = url_for(slug)

    if slug == "":
        blocks.append(
            '{"@context":"https://schema.org","@type":"SoftwareApplication",'
            f'"name":"Self Speed","url":"{BASE}/",'
            '"applicationCategory":"UtilitiesApplication",'
            '"operatingSystem":"Any device with a web browser",'
            f'"description":"{json_escape(description)}",'
            '"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},'
            '"featureList":"Live GPS speed, maximum and average speed, distance, '
            'trip history, GPX export, offline use"}')
    else:
        blocks.append(
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
            f'{{"@type":"ListItem","position":1,"name":"Self Speed","item":"{BASE}/"}},'
            f'{{"@type":"ListItem","position":2,"name":"{json_escape(title)}","item":"{url}"}}'
            "]}")

    faq = extract_faq(md)
    if faq:
        items = ",".join(
            f'{{"@type":"Question","name":"{json_escape(q)}",'
            f'"acceptedAnswer":{{"@type":"Answer","text":"{json_escape(a)}"}}}}'
            for q, a in faq)
        blocks.append(
            '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
            + items + "]}")

    return "\n".join(
        f'<script type="application/ld+json">{blk}</script>' for blk in blocks)

# --------------------------------------------------------------------- build
def main():
    template = TEMPLATE.read_text(encoding="utf-8")
    pages = []

    for path in sorted(CONTENT.glob("*.md")):
        meta, body = parse(path)
        slug = meta.get("slug", path.stem)
        page = (template
                .replace("{{title}}", html.escape(meta.get("title", slug)))
                .replace("{{description}}", html.escape(meta.get("description", "")))
                .replace("{{canonical}}", url_for(slug))
                .replace("{{nav}}", nav_html(slug))
                .replace("{{footer}}", footer_html())
                .replace("{{jsonld}}", jsonld_for(slug, meta.get("title", slug),
                                                  meta.get("description", ""), body))
                .replace("{{content}}", render(body)))

        out_dir = ROOT / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page, encoding="utf-8")
        pages.append((slug, meta.get("priority", "0.7")))
        print(f"  {slug + '/index.html':42} {len(page):>7,} bytes")

    # sitemap: the app itself first, then every generated page
    entries = [f"  <url><loc>{BASE}/</loc><priority>1.0</priority></url>"]
    for slug, prio in sorted(pages):
        entries.append(f"  <url><loc>{url_for(slug)}</loc><priority>{prio}</priority></url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries) + "\n</urlset>\n", encoding="utf-8")

    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")

    print(f"\n{len(pages)} pages + sitemap.xml + robots.txt")


if __name__ == "__main__":
    main()
