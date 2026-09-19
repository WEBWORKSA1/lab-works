"""Calculator widget markup."""

def sel(name, opts, default=None):
    o = "".join(f'<option{" selected" if x == default else ""}>{x}</option>' for x in opts)
    return f'<select name="{name}" aria-label="{name} unit">{o}</select>'

V = ["L", "mL", "µL"]
C = ["M", "mM", "µM", "nM"]
M = ["g", "mg", "µg", "kg"]

CALC_FORMS = {
"molarity": f"""<div><label>What do you want to find?</label><select name="mode"><option value="mass">Mass of solute needed</option><option value="molarity">Molarity from a known mass</option></select></div>
<div data-mode="mass"><label>Desired concentration</label><div class="unit"><input name="conc" inputmode="decimal" value="0.1">{sel("concU", C, "M")}</div></div>
<div data-mode="molarity"><label>Mass weighed</label><div class="unit"><input name="mass" inputmode="decimal" value="2.922">{sel("massU", M, "g")}</div></div>
<div><label>Final volume</label><div class="unit"><input name="vol" inputmode="decimal" value="500">{sel("volU", V, "mL")}</div></div>
<div><label>Molecular weight (g/mol) <button type="button" class="chip" data-mw-lookup>Look up from formula</button></label><input name="mw" inputmode="decimal" value="58.44"></div>""",
"dilution": """<p class="form-note">Fill any three values. Leave the unknown blank.</p>
<div class="form-row"><div><label>Stock concentration C₁</label><input name="c1" inputmode="decimal" value="10"></div><div><label>Volume of stock V₁</label><input name="v1" inputmode="decimal" placeholder="unknown"></div></div>
<div class="form-row"><div><label>Final concentration C₂</label><input name="c2" inputmode="decimal" value="1"></div><div><label>Final volume V₂</label><input name="v2" inputmode="decimal" value="50"></div></div>
<div class="form-row"><div><label>Concentration unit</label><select name="cu"><option>M</option><option>mM</option><option>µM</option><option>×</option><option>% w/v</option><option>mg/mL</option><option>µg/mL</option></select></div><div><label>Volume unit</label><select name="vu"><option>mL</option><option>µL</option><option>L</option></select></div></div>""",
"serial": """<div class="form-row"><div><label>Starting concentration</label><input name="c0" inputmode="decimal" value="1000"></div><div><label>Concentration unit</label><select name="cu"><option>µg/mL</option><option>ng/mL</option><option>mM</option><option>µM</option><option>cells/mL</option><option>CFU/mL</option></select></div></div>
<div class="form-row"><div><label>Dilution factor (fold)</label><input name="factor" inputmode="decimal" value="10"></div><div><label>Number of tubes</label><input name="steps" inputmode="numeric" value="6"></div></div>
<div><label>Diluent volume per tube (µL)</label><input name="vfinal" inputmode="decimal" value="900"></div>""",
"molarmass": """<div><label>Chemical formula</label><input name="formula" value="CuSO4·5H2O" autocomplete="off" spellcheck="false"></div>
<div class="chips"><button type="button" class="chip" onclick="this.form.formula.value='NaCl';this.form.dispatchEvent(new Event('input'))">NaCl</button><button type="button" class="chip" onclick="this.form.formula.value='C6H12O6';this.form.dispatchEvent(new Event('input'))">Glucose</button><button type="button" class="chip" onclick="this.form.formula.value='C4H11NO3';this.form.dispatchEvent(new Event('input'))">Tris</button><button type="button" class="chip" onclick="this.form.formula.value='Na2HPO4';this.form.dispatchEvent(new Event('input'))">Na₂HPO₄</button><button type="button" class="chip" onclick="this.form.formula.value='C10H16N2O8';this.form.dispatchEvent(new Event('input'))">EDTA</button></div>""",
"buffer": f"""<div><label>Buffer preset</label><select data-preset><option value="">Custom…</option><option value="4.76|60.05|82.03">Acetate (acetic acid / sodium acetate)</option><option value="6.15|195.24|217.22">MES</option><option value="7.20|119.98|141.96" selected>Phosphate (NaH₂PO₄ / Na₂HPO₄)</option><option value="7.48|238.30|260.29">HEPES (free acid / Na salt)</option><option value="8.07|157.60|121.14">Tris (Tris-HCl / Tris base)</option><option value="10.33|84.01|105.99">Carbonate (NaHCO₃ / Na₂CO₃)</option></select></div>
<div class="form-row"><div><label>pKa</label><input name="pka" inputmode="decimal" value="7.20"></div><div><label>Target pH</label><input name="ph" inputmode="decimal" value="7.4"></div></div>
<div class="form-row"><div><label>Total buffer concentration</label><div class="unit"><input name="total" inputmode="decimal" value="100">{sel("totalU", C, "mM")}</div></div><div><label>Final volume</label><div class="unit"><input name="vol" inputmode="decimal" value="1">{sel("volU", V, "L")}</div></div></div>
<div class="form-row"><div><label>MW weak acid (g/mol, optional)</label><input name="mwa" inputmode="decimal" value="119.98"></div><div><label>MW conjugate base (g/mol, optional)</label><input name="mwb" inputmode="decimal" value="141.96"></div></div>""",
"rcf": """<div><label>Rotor radius</label><div class="unit"><input name="radius" inputmode="decimal" value="8.5"><select name="radiusU"><option>cm</option><option>mm</option></select></div></div>
<div class="form-row"><div><label>Speed (RPM)</label><input name="rpm" inputmode="decimal" value="13000"></div><div><label>…or g-force (× g)</label><input name="g" inputmode="decimal" placeholder="leave blank to calculate"></div></div>""",
"pcr": """<div class="form-row"><div><label>Number of reactions</label><input name="n" inputmode="numeric" value="24"></div><div><label>Overage (%)</label><input name="overage" inputmode="decimal" value="10"></div></div>
<div class="form-row"><div><label>Reaction volume (µL)</label><input name="rxn" inputmode="decimal" value="25"></div><div><label>Template per reaction (µL)</label><input name="template" inputmode="decimal" value="1"></div></div>
<label class="check"><input type="checkbox" name="mg" value="1"> Add separate MgCl₂ (buffer without Mg²⁺)</label>""",
"cells": """<div class="form-row"><div><label>Live (unstained) cells counted</label><input name="live" inputmode="numeric" value="180"></div><div><label>Dead (blue) cells counted</label><input name="dead" inputmode="numeric" value="12"></div></div>
<div class="form-row"><div><label>Large squares counted</label><input name="squares" inputmode="numeric" value="4"></div><div><label>Dilution factor (trypan 1:1 = 2)</label><input name="dilution" inputmode="decimal" value="2"></div></div>
<p class="form-note">Optional — seeding plan</p>
<div class="form-row"><div><label>Cells per well</label><input name="target" inputmode="numeric" placeholder="e.g. 50000"></div><div><label>Number of wells</label><input name="wells" inputmode="numeric" placeholder="e.g. 24"></div></div>
<div><label>Medium volume per well (mL)</label><input name="perwell" inputmode="decimal" placeholder="e.g. 0.5"></div>""",
"stats": """<div><label>Replicate values</label><textarea name="data" spellcheck="false">10.2, 10.5, 9.9, 10.1, 10.4, 11.6</textarea></div>""",
"nucleic": """<div class="form-row"><div><label>Sample type</label><select name="type"><option value="50">dsDNA (50)</option><option value="40">RNA (40)</option><option value="33">ssDNA (33)</option><option value="custom">Custom factor</option></select></div><div><label>Custom factor</label><input name="custom" inputmode="decimal" placeholder="e.g. oligo"></div></div>
<div class="form-row"><div><label>A260</label><input name="a260" inputmode="decimal" value="0.75"></div><div><label>A280</label><input name="a280" inputmode="decimal" value="0.40"></div></div>
<div class="form-row"><div><label>A230 (optional)</label><input name="a230" inputmode="decimal" value="0.36"></div><div><label>Dilution factor</label><input name="dil" inputmode="decimal" value="1"></div></div>
<div><label>Path length (cm)</label><input name="path" inputmode="decimal" value="1"></div>""",
"beer": """<p class="form-note">Fill any three values. Leave the unknown blank.</p>
<div class="form-row"><div><label>Absorbance A</label><input name="A" inputmode="decimal" value="0.5"></div><div><label>Molar absorptivity ε (L·mol⁻¹·cm⁻¹)</label><input name="eps" inputmode="decimal" value="6220"></div></div>
<div class="form-row"><div><label>Path length l (cm)</label><input name="l" inputmode="decimal" value="1"></div><div><label>Concentration c (mol/L)</label><input name="c" inputmode="decimal" placeholder="unknown"></div></div>""",
"ppm": """<div class="form-row"><div><label>Value</label><input name="value" inputmode="decimal" value="250"></div><div><label>From unit</label><select name="from"><option value="ppm">ppm</option><option value="mgL">mg/L</option><option value="ppb">ppb</option><option value="ugL">µg/L</option><option value="gL">g/L</option><option value="pct">% w/v</option><option value="M">M (mol/L)</option><option value="mM">mM</option></select></div></div>
<div class="form-row"><div><label>Molecular weight (g/mol, for molarity)</label><input name="mw" inputmode="decimal" value="58.44"></div><div><label>Solution density (g/mL)</label><input name="density" inputmode="decimal" value="1"></div></div>""",
}
