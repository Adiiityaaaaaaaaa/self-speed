---
title: Calorie Calculator for Walking, Running and Cycling — With Incline
description: Work out calories burned walking, running or cycling from your distance, time and incline. Uses ACSM metabolic equations and a physics power model, not a flat MET guess.
slug: calorie-calculator
priority: 0.9
---

# Calorie calculator

Enter your distance, time and the gradient you covered. Most calculators ignore
incline entirely, which is why they under-report hilly routes badly — walking up
a 10% gradient costs **2.3x** what the same walk costs on the flat.

:::html
<div class="calc">
  <div class="calc-modes" role="group" aria-label="Activity">
    <button type="button" data-act="walk" class="on">Walking</button>
    <button type="button" data-act="run">Running</button>
    <button type="button" data-act="bike">Cycling</button>
  </div>

  <div class="calc-grid">
    <label>Body weight
      <span class="row">
        <input type="number" id="c-weight" value="70" min="20" max="250" step="1">
        <select id="c-wunit"><option value="kg">kg</option><option value="lb">lb</option></select>
      </span>
    </label>

    <label>Distance
      <span class="row">
        <input type="number" id="c-dist" value="5" min="0.1" max="500" step="0.1">
        <select id="c-dunit"><option value="km">km</option><option value="mi">mi</option></select>
      </span>
    </label>

    <label>Time
      <span class="row">
        <input type="number" id="c-time" value="60" min="1" max="1440" step="1">
        <span class="suffix">minutes</span>
      </span>
    </label>

    <label>Average incline
      <span class="row">
        <input type="number" id="c-grade" value="0" min="-20" max="30" step="0.5">
        <span class="suffix">% grade</span>
      </span>
    </label>
  </div>

  <div class="calc-out">
    <div class="big"><span id="c-kcal">--</span><small>kcal burned</small></div>
    <div class="sub" id="c-sub"></div>
  </div>

  <div class="calc-rows" id="c-rows"></div>
  <p class="calc-note" id="c-warn"></p>
</div>

<style>
.calc{background:#141926;border:1px solid #232c3f;border-radius:16px;padding:18px;margin:26px 0}
.calc-modes{display:flex;gap:6px;background:#0e121b;border:1px solid #232c3f;
            border-radius:999px;padding:4px;margin-bottom:16px}
.calc-modes button{flex:1;appearance:none;border:0;background:transparent;color:#8793ab;
                   font:inherit;font-size:13px;font-weight:600;padding:8px 10px;
                   border-radius:999px;cursor:pointer}
.calc-modes button.on{background:#37d67a;color:#06210f}
.calc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.calc label{display:flex;flex-direction:column;gap:5px;font-size:11px;
            letter-spacing:.09em;text-transform:uppercase;color:#8793ab;font-weight:600}
.calc .row{display:flex;gap:6px;align-items:center}
.calc input,.calc select{background:#0b0e14;border:1px solid #232c3f;color:#e8ecf5;
                         font:inherit;font-size:15px;padding:9px 10px;border-radius:9px;
                         width:100%;min-width:0}
.calc select{width:auto;flex:0 0 auto}
.calc .suffix{color:#8793ab;font-size:12px;text-transform:none;letter-spacing:0;white-space:nowrap}
.calc-out{margin-top:18px;padding-top:16px;border-top:1px solid #232c3f;text-align:center}
.calc-out .big{font-size:44px;font-weight:700;line-height:1.1;font-variant-numeric:tabular-nums;
               color:#37d67a;display:flex;flex-direction:column;align-items:center;gap:2px}
.calc-out .big small{font-size:11px;letter-spacing:.18em;text-transform:uppercase;
                     color:#8793ab;font-weight:600}
.calc-out .sub{margin-top:8px;font-size:13px;color:#8793ab}
.calc-rows{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));
           gap:8px;margin-top:16px}
.calc-rows div{background:#0e121b;border:1px solid #232c3f;border-radius:11px;
               padding:9px;text-align:center}
.calc-rows b{display:block;font-size:16px;font-variant-numeric:tabular-nums;color:#e8ecf5}
.calc-rows span{font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#8793ab}
.calc-note{font-size:12px;color:#ffb23f;margin:12px 0 0;min-height:16px;text-align:center}
</style>

<script>
(function(){
  var act='walk';
  var $=function(id){return document.getElementById(id);};
  var els=['c-weight','c-dist','c-time','c-grade','c-wunit','c-dunit'].map($);

  function calc(){
    var kg=parseFloat($('c-weight').value)||0;
    if($('c-wunit').value==='lb') kg*=0.45359237;
    var dist=parseFloat($('c-dist').value)||0;
    if($('c-dunit').value==='mi') dist*=1.609344;
    var mins=parseFloat($('c-time').value)||0;
    var gradePct=parseFloat($('c-grade').value)||0;
    var g=gradePct/100;

    if(kg<=0||dist<=0||mins<=0){ $('c-kcal').textContent='--'; return; }

    var kmh=dist/(mins/60);
    var mPerMin=dist*1000/mins;
    var v=mPerMin/60;                    // m/s
    var gross, note='';

    if(act==='bike'){
      // Physics: rolling + gravity + aerodynamic drag, divided by human efficiency.
      var mTot=kg+10;                    // rider plus a typical bike
      var theta=Math.atan(g);
      // CdA 0.40 is a normal riding position on the hoods; 0.32 would be a
      // racing tuck and made low speeds read below walking.
      var Crr=0.006, CdA=0.40, rho=1.225, eff=0.24;
      var F = Crr*mTot*9.81*Math.cos(theta)
            + mTot*9.81*Math.sin(theta)
            + 0.5*rho*CdA*v*v;
      var watts=F*v;
      if(watts<0) watts=0;               // freewheeling downhill costs ~nothing
      // Propulsion cost plus resting metabolism. The ACSM equations used for
      // walking and running include resting via their +3.5 term; without this
      // cycling would be scored on propulsion alone and read far too low.
      gross=(watts/eff)*(mins*60)/4184 + 3.5*kg*mins/1000*5;
      if(watts>400) note='That implies '+Math.round(watts)+' W sustained — near-professional. Check your distance, time and gradient.';
      else if(watts>250) note='That implies '+Math.round(watts)+' W sustained, which is a strong trained effort.';
      else if(kmh>50) note='Above 50 km/h the drag model is stretched; treat as indicative.';
    } else {
      // ACSM metabolic equations, VO2 in ml/kg/min.
      var vo2 = (act==='run')
        ? 0.2*mPerMin + 0.9*mPerMin*g + 3.5
        : 0.1*mPerMin + 1.8*mPerMin*g + 3.5;
      if(vo2<3.5) vo2=3.5;               // never below resting
      gross=vo2*kg*mins/1000*5;
      if(act==='walk'&&kmh>7.5) note='Above about 7.5 km/h most people run. Switch to Running for a better estimate.';
      if(act==='run'&&kmh<7)   note='Below about 7 km/h the running equation overestimates. Switch to Walking.';
    }

    var rest=3.5*kg*mins/1000*5;         // resting metabolism over the same period
    var net=Math.max(0,gross-rest);
    var mets=gross/(mins/60)/kg;

    $('c-kcal').textContent=Math.round(gross);
    $('c-sub').textContent=Math.round(net)+' kcal net of resting metabolism';
    var paceSec=mins*60/dist;
    $('c-rows').innerHTML=
      '<div><b>'+kmh.toFixed(1)+'</b><span>km/h</span></div>'+
      '<div><b>'+Math.floor(paceSec/60)+':'+('0'+Math.round(paceSec%60)).slice(-2)+'</b><span>min/km</span></div>'+
      '<div><b>'+mets.toFixed(1)+'</b><span>MET</span></div>'+
      '<div><b>'+(gross/dist).toFixed(0)+'</b><span>kcal/km</span></div>';
    $('c-warn').textContent=note;
  }

  document.querySelectorAll('.calc-modes button').forEach(function(b){
    b.addEventListener('click',function(){
      document.querySelectorAll('.calc-modes button').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on'); act=b.dataset.act; calc();
    });
  });
  els.forEach(function(e){ e.addEventListener('input',calc); e.addEventListener('change',calc); });
  calc();
})();
</script>
:::

## How this is calculated

Most online calorie calculators multiply a single MET value by your weight and
time. That is fine on flat ground and wrong everywhere else, because it has no
way to account for gradient.

This one uses two different models depending on what you are doing.

### Walking and running

The **ACSM metabolic equations**, which are standard in exercise physiology and
take grade as an explicit input:

> Walking: VO₂ = (0.1 × speed) + (1.8 × speed × grade) + 3.5
> Running: VO₂ = (0.2 × speed) + (0.9 × speed × grade) + 3.5

Speed is in metres per minute, grade is a fraction, and VO₂ comes out in
ml/kg/min. Oxygen consumption converts to energy at roughly 5 kcal per litre.

Note the grade coefficient: **1.8 for walking against 0.9 for running.** Climbing
penalises walkers twice as much per unit of grade, which is why a steep hill
turns a walk into a genuinely hard effort while runners lose comparatively less.

### Cycling

Cycling is not well served by MET tables, because air resistance dominates and
scales with the cube of speed in power terms. So this uses a physical model of
the forces you are actually overcoming:

> Power = (rolling resistance + gravity + aerodynamic drag) × speed

with rolling resistance at 0.006, drag area CdA at 0.40 m² (a normal position
on the hoods, not a racing tuck), air density 1.225 kg/m³, and a 10 kg bike. Mechanical power is divided by **0.24** — human muscular
efficiency — to get metabolic cost.

That efficiency figure is the reason cycling burns so much: roughly three
quarters of the energy you produce leaves as heat rather than propulsion.

## Gross versus net calories

The large number is **gross** — total energy expended.

The smaller figure is **net**, with your resting metabolism subtracted. You would
have burned those calories lying on the sofa, so if you are counting calories
against food intake, net is the honest number.

For an hour of exercise the difference is typically 60–100 kcal. Most fitness
apps report gross, which is one reason app estimates tend to look generous.

## How accurate is any of this?

**Roughly ±10–20% for an individual, at best.** Treat the output as a good
estimate, not a measurement.

Sources of error that no calculator can see:

- **Efficiency varies between people** by 5–10%, and trained athletes are more economical than beginners at the same speed.
- **Terrain and surface.** Sand, mud, snow and rough trail cost far more than the equivalent distance on tarmac.
- **Wind.** For cycling this is enormous — a headwind can double your power output at the same ground speed, and the calculator has no way to know.
- **Body composition.** Muscle and fat have different metabolic costs to carry.
- **Temperature.** Both heat and cold add metabolic load.

The relative numbers are more trustworthy than the absolute ones. If it says
today's hilly walk cost 40% more than yesterday's flat one, believe that — even
if both absolute figures are 15% off.

## Rough reference figures

For a 70 kg person on level ground:

| Activity | Speed | kcal per hour | kcal per km |
|---|---|---|---|
| Walking, easy | 4 km/h | 214 | 53 |
| Walking, brisk | 6 km/h | 284 | 47 |
| Running, steady | 10 km/h | 774 | 77 |
| Running, fast | 14 km/h | 1,054 | 75 |
| Cycling, leisure | 16 km/h | 226 | 14 |
| Cycling, moderate | 25 km/h | 485 | 19 |
| Cycling, fast | 32 km/h | 840 | 26 |

The pattern worth noticing: **running costs roughly the same per kilometre
regardless of speed**, because you are lifting your body weight the same number
of times either way. Cycling is the opposite — cost per kilometre rises steeply
with speed, since drag grows with the square of velocity.

Walking is the most efficient per kilometre. It simply takes longer.

## Measuring the inputs

The calculator is only as good as the distance and time you feed it. Self Speed
records both automatically, along with your average speed — see
[average walking speed](/average-walking-speed/) and
[average cycling speed](/average-cycling-speed/) for what to expect.

Incline is the one figure GPS handles poorly. Vertical accuracy is typically two
to three times worse than horizontal, so for a route with meaningful climbing,
take the gradient from a mapping tool rather than from your phone.
