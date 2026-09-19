"""Content data for Lab.Works."""

CATEGORIES = [
 dict(slug="water-testing", key="water", icon="💧", name="Water Testing",
  short="Drinking, well, pool, wastewater & process water analysis.",
  intro="Water testing identifies chemical, microbiological and physical contaminants in drinking water, private wells, wastewater, pools, boilers and industrial process water. It is the single most requested test category for homeowners, landlords, food businesses and facilities managers.",
  who="Homeowners with private wells, landlords, schools, restaurants, breweries, farms, municipalities, property buyers and industrial plants.",
  tests=[("Coliform & E. coli","Microbiology","24–48 h"),("Lead & copper","Metals (ICP-MS)","3–7 days"),("Nitrate / nitrite","Inorganics","2–5 days"),("Arsenic","Metals","3–7 days"),("PFAS (EPA 533/537.1)","Emerging contaminants","7–15 days"),("Full potability panel","Multi-parameter","5–10 days"),("Legionella","Microbiology","7–10 days"),("Hardness, pH & TDS","Physical/chemical","1–3 days")],
  standards="EPA 200.8, EPA 524.2, EPA 533/537.1, ISO 9308 (E. coli), ISO 11731 (Legionella), WHO drinking-water guidelines, local drinking-water regulations.",
  price="Basic bacteria test ≈ US$30–80; metals panel ≈ $60–200; PFAS ≈ $250–600; comprehensive potability ≈ $200–600 (indicative).",
  faqs=[("How often should I test private well water?","At minimum once a year for coliform bacteria, nitrate and pH, and after flooding, repairs, or any change in taste, colour or smell. Test for arsenic, lead and PFAS at least once and whenever local advisories suggest."),
        ("Do I need an accredited lab for water testing?","For real-estate transactions, regulatory compliance and legal matters you need a lab accredited or certified for drinking-water analysis (e.g. ISO/IEC 17025 or state/provincial certification). Home test strips are only screening tools."),
        ("How do I collect a water sample correctly?","Use the sterile bottles supplied by the lab, follow the flush time specified for the test (first-draw for lead, flushed for bacteria), keep samples cold and deliver within the holding time — often 24–30 hours for bacteria.")]),
 dict(slug="food-testing", key="food", icon="🍎", name="Food & Beverage Testing",
  short="Nutrition labels, shelf life, allergens, pathogens & contaminants.",
  intro="Food testing labs verify safety, quality and label claims for food and beverage products — from nutrition facts panels and allergen declarations to pathogen screens, shelf-life studies and pesticide residues.",
  who="Food start-ups, co-packers, restaurants, bakeries, beverage and supplement brands, importers and exporters.",
  tests=[("Nutrition facts panel","Proximate analysis","5–10 days"),("Shelf-life study","Micro + sensory","2–12 weeks"),("Salmonella / Listeria","Pathogens","2–5 days"),("Allergen (gluten, peanut, milk)","ELISA / PCR","3–7 days"),("Pesticide residues","LC-MS/MS, GC-MS","5–10 days"),("Heavy metals","ICP-MS","5–7 days"),("Water activity & pH","Physical","1–3 days"),("Mycotoxins (aflatoxin)","LC-MS/MS","5–10 days")],
  standards="AOAC Official Methods, ISO 6579 (Salmonella), ISO 11290 (Listeria), FDA BAM, Codex Alimentarius, FSMA, EU 2073/2005.",
  price="Nutrition panel ≈ US$300–900; pathogen screen ≈ $40–150 per target; shelf-life study ≈ $500–3,000+ (indicative).",
  faqs=[("Can I calculate a nutrition label instead of lab testing?","Many regulators accept database calculations for nutrition labels, but lab analysis is more accurate for novel recipes, processed products and claims like 'high protein' or 'low sugar'."),
        ("What's the difference between a pathogen screen and an indicator test?","Pathogen tests look for specific organisms such as Salmonella or Listeria. Indicator tests (total plate count, coliforms, yeast & mould) measure overall hygiene and spoilage risk."),
        ("How long does a shelf-life study take?","Real-time studies take as long as the intended shelf life. Accelerated studies at elevated temperature can shorten this but must be validated for your product.")]),
 dict(slug="environmental-testing", key="environmental", icon="🌍", name="Environmental Testing",
  short="Soil, air, asbestos, mold, sediment & contaminated-site analysis.",
  intro="Environmental labs analyse soil, air, sediment, building materials and waste to support property transactions, remediation projects, occupational-health programmes and environmental permits.",
  who="Environmental consultants, property developers, contractors, facility managers, insurers and homeowners.",
  tests=[("Asbestos (PLM/TEM)","Building materials","1–5 days"),("Mold (air & swab)","Indoor air quality","2–5 days"),("Radon","Indoor air","3–7 days"),("Soil heavy metals","ICP-OES/MS","5–7 days"),("Petroleum hydrocarbons (TPH)","GC-FID","5–10 days"),("VOCs in air (TO-15)","GC-MS","5–10 days"),("Lead paint & dust","Metals","2–5 days"),("Waste characterization (TCLP)","Leachate","7–14 days")],
  standards="EPA SW-846, EPA TO-15, NIOSH methods, ASTM E1527 (Phase I ESA), ISO 16000 (indoor air), AIHA-LAP accreditation.",
  price="Asbestos PLM ≈ US$25–60 per sample; mold air sample ≈ $75–150; soil metals ≈ $50–200 (indicative).",
  faqs=[("Do I need an asbestos test before renovation?","In most jurisdictions yes — buildings constructed before the 1990s must be surveyed for asbestos-containing materials before demolition or renovation."),
        ("What's a Phase I vs Phase II environmental site assessment?","Phase I is a records review and site inspection. Phase II collects soil, groundwater or vapour samples for laboratory analysis when Phase I identifies potential contamination."),
        ("Which accreditation should an environmental lab hold?","Look for ISO/IEC 17025 with the specific methods on the scope, plus programmes such as AIHA-LAP (industrial hygiene), NVLAP (asbestos) or state/provincial environmental certification.")]),
 dict(slug="materials-testing", key="materials", icon="🧱", name="Materials & Product Testing",
  short="Metals, plastics, composites, failure analysis & product safety.",
  intro="Materials testing labs characterise mechanical, chemical and physical properties of metals, polymers, ceramics, composites and finished products — supporting R&D, quality control, certification and failure investigations.",
  who="Manufacturers, engineers, product designers, importers, construction firms and quality managers.",
  tests=[("Tensile & hardness","Mechanical","3–7 days"),("Failure analysis","Metallography/SEM","1–3 weeks"),("Chemical composition (OES/XRF)","Metals","2–5 days"),("Polymer ID (FTIR, DSC)","Plastics","3–7 days"),("Salt-spray corrosion","ASTM B117","1–6 weeks"),("RoHS / REACH screening","Compliance","5–10 days"),("Fatigue testing","Mechanical","2–6 weeks"),("Concrete & aggregate","Construction","7–28 days")],
  standards="ASTM E8 (tensile), ASTM B117, ISO 6892, IEC 62321 (RoHS), EN/ISO product standards, CPSIA for children's products.",
  price="Tensile test ≈ US$50–250 per specimen; failure analysis ≈ $1,500–10,000; RoHS screen ≈ $100–400 (indicative).",
  faqs=[("What is failure analysis?","A structured investigation — visual inspection, fractography, metallography, SEM/EDS and chemical analysis — to determine why a part broke, corroded or wore out, and how to prevent recurrence."),
        ("Can a lab test to my customer's specification?","Yes. Provide the standard (ASTM, ISO, EN or customer spec). Accredited labs list the methods they are accredited for on their scope of accreditation."),
        ("What is RoHS testing?","RoHS limits hazardous substances such as lead, mercury, cadmium, hexavalent chromium and certain flame retardants/phthalates in electrical and electronic equipment. XRF screening is typically followed by confirmatory wet chemistry.")]),
 dict(slug="pharma-cosmetics-testing", key="pharma", icon="💊", name="Pharma, Supplement & Cosmetics Testing",
  short="Potency, stability, micro limits, heavy metals & claim substantiation.",
  intro="Pharmaceutical, dietary-supplement and cosmetics labs confirm identity, potency, purity, stability and safety to meet GMP requirements and substantiate label claims.",
  who="Supplement brands, cosmetic formulators, contract manufacturers, pharma start-ups and importers.",
  tests=[("Identity & potency (HPLC)","Assay","5–10 days"),("Stability (ICH Q1A)","Real-time / accelerated","1–24 months"),("Microbial limits (USP 61/62)","Microbiology","5–7 days"),("Heavy metals (USP 232/233)","ICP-MS","5–7 days"),("Preservative efficacy (USP 51)","Challenge test","4–5 weeks"),("SPF / patch testing","Claims","2–6 weeks"),("Residual solvents (USP 467)","GC","5–10 days"),("Endotoxin (LAL)","Safety","2–5 days")],
  standards="USP/EP/JP monographs, ICH Q1A–Q2, 21 CFR 111 & 211, ISO 22716 (cosmetics GMP), ISO 11930, GLP/GMP compliance.",
  price="HPLC potency ≈ US$150–500 per analyte; USP 51 challenge ≈ $600–1,500; stability programmes quoted per protocol (indicative).",
  faqs=[("Do supplements need third-party testing?","Manufacturers must verify identity, purity, strength and composition under GMP rules; third-party certificates of analysis build retailer and consumer trust."),
        ("What is a preservative efficacy (challenge) test?","The product is inoculated with specified microorganisms and sampled over 28 days to prove the preservative system prevents microbial growth."),
        ("What's the difference between GLP and GMP labs?","GLP covers non-clinical safety studies; GMP covers manufacturing and QC release testing. Choose a lab certified for the regime your regulator requires.")]),
 dict(slug="clinical-health-testing", key="clinical", icon="🩸", name="Clinical & Health Lab Tests",
  short="Blood panels, hormones, allergy, STD & wellness tests via licensed labs.",
  intro="Clinical laboratory tests support diagnosis and wellness monitoring. Many regions allow direct-to-consumer ordering through licensed labs with physician oversight; results should always be reviewed with a qualified clinician.",
  who="Individuals, clinics, corporate wellness programmes, telehealth providers and insurers.",
  tests=[("Complete blood count (CBC)","Haematology","1–2 days"),("Comprehensive metabolic panel","Chemistry","1–2 days"),("Lipid panel","Cardiovascular","1–2 days"),("HbA1c","Diabetes","1–2 days"),("Thyroid panel (TSH, T3, T4)","Hormones","1–3 days"),("Vitamin D","Nutrition","1–3 days"),("STD panel","Infectious disease","2–5 days"),("Food sensitivity / allergy IgE","Immunology","3–7 days")],
  standards="CLIA certification (US), CAP accreditation, ISO 15189 (medical laboratories), HIPAA / GDPR privacy requirements.",
  price="Individual routine tests ≈ US$20–80 direct-to-consumer; comprehensive wellness panels ≈ $100–400 (indicative).",
  faqs=[("Can I order a lab test without a doctor?","It depends on your jurisdiction. Many US states allow direct-access testing where a network physician authorises the order. Always discuss results with a healthcare professional."),
        ("What accreditation should a clinical lab have?","In the US, CLIA certification is legally required and CAP accreditation is a gold standard; internationally, ISO 15189 accreditation is the benchmark."),
        ("Is Lab.Works a medical provider?","No. Lab.Works provides educational information and connects you with licensed laboratories. We do not diagnose or give medical advice.")]),
 dict(slug="microbiology-testing", key="microbiology", icon="🦠", name="Microbiology Testing",
  short="Pathogens, sterility, environmental monitoring & antimicrobial efficacy.",
  intro="Microbiology labs detect and quantify bacteria, yeasts, moulds and viruses in products, surfaces, water and air, and test the efficacy of disinfectants and antimicrobial products.",
  who="Food and pharma QA teams, hospitals, cleanroom operators, disinfectant and textile brands.",
  tests=[("Total plate count","Indicator","2–5 days"),("Environmental swab monitoring","Surfaces","2–5 days"),("Sterility (USP 71)","Pharma","14+ days"),("Antimicrobial efficacy (ISO 22196)","Surfaces/plastics","1–2 weeks"),("Disinfectant efficacy (EN 1276)","Biocides","1–3 weeks"),("Microbial ID (MALDI-TOF / 16S)","Identification","2–7 days")],
  standards="ISO 4833, USP 61/62/71, ISO 22196, EN 1276/13727, AOAC 955.15, ISO 14698 (cleanrooms).",
  price="Plate count ≈ US$20–60; microbial ID ≈ $80–300; efficacy studies ≈ $800–5,000 (indicative).",
  faqs=[("Why do I need environmental monitoring?","It verifies that cleaning and sanitation keep surfaces and air within limits, preventing product contamination — a core requirement of food safety and GMP programmes."),
        ("Can a lab substantiate an 'antibacterial' claim?","Yes, through standardised efficacy tests (e.g. ISO 22196, EN 1276). Claims are regulated, so check requirements in your target markets.")]),
 dict(slug="soil-agriculture-testing", key="agriculture", icon="🌱", name="Soil, Plant & Agriculture Testing",
  short="Soil fertility, plant tissue, feed, fertiliser & irrigation water.",
  intro="Agricultural labs measure nutrients, contaminants and quality parameters in soil, plant tissue, animal feed, fertilisers and irrigation water to optimise yields and meet quality contracts.",
  who="Farmers, agronomists, gardeners, landscapers, feed mills, fertiliser producers and exporters.",
  tests=[("Soil fertility (N-P-K, pH, OM)","Soil","3–7 days"),("Plant tissue nutrients","Plant","3–7 days"),("Feed / forage analysis","Nutrition","3–7 days"),("Irrigation water suitability","Water","3–7 days"),("Soil biology / microbiome","Biology","1–3 weeks"),("Pesticide residues on produce","Residues","5–10 days")],
  standards="AOAC, Mehlich-3 / Olsen extraction, NAPT proficiency programmes, ISO 11464 soil pretreatment.",
  price="Basic soil fertility ≈ US$15–60; feed analysis ≈ $30–120 (indicative).",
  faqs=[("When is the best time to take soil samples?","Sample at the same time each year — usually after harvest or before planting — taking 15–20 cores per uniform field zone and mixing them into one composite."),
        ("How deep should I sample?","Commonly 0–15 cm (0–6 in) for cropland and gardens; deeper profiles are used for nitrate and subsoil constraints.")]),
 dict(slug="cannabis-hemp-testing", key="cannabis", icon="🌿", name="Cannabis & Hemp Testing",
  short="Potency, terpenes, pesticides, heavy metals & compliance COAs.",
  intro="Where legal, cannabis and hemp products must be tested by licensed labs for cannabinoid potency, contaminants and label accuracy before sale.",
  who="Licensed producers, hemp farmers, CBD brands, processors and dispensaries.",
  tests=[("Cannabinoid potency (THC/CBD)","HPLC","2–5 days"),("Terpene profile","GC-MS","3–7 days"),("Pesticide panel","LC-MS/MS","3–7 days"),("Heavy metals","ICP-MS","3–7 days"),("Residual solvents","GC","3–5 days"),("Microbial & mycotoxins","Safety","3–7 days")],
  standards="State/provincial regulations, AOAC SMPR, ISO/IEC 17025 (usually required for licensing), USDA hemp rules.",
  price="Potency ≈ US$40–120; full compliance panel ≈ $300–800 (indicative).",
  faqs=[("Why is my potency result different from another lab's?","Sampling, homogenisation, moisture correction and method differences all affect results. Use ISO 17025-accredited labs and consistent sampling procedures."),
        ("Is hemp testing mandatory?","In most jurisdictions hemp must be tested pre-harvest for total THC; finished CBD products are subject to local labelling and safety rules.")]),
 dict(slug="dna-genetic-testing", key="dna", icon="🧬", name="DNA & Genetic Testing",
  short="Paternity, ancestry, species ID, GMO, sequencing & genotyping.",
  intro="DNA labs provide paternity and relationship testing, species and authenticity verification, GMO detection, microbial identification and next-generation sequencing services for research and industry.",
  who="Families, legal professionals, researchers, food-fraud investigators, breeders and biotech companies.",
  tests=[("Paternity (legal / peace-of-mind)","Relationship","2–5 days"),("Species / meat authenticity","Food fraud","3–7 days"),("GMO screening (PCR)","Food/agri","3–7 days"),("Sanger sequencing","Research","1–3 days"),("Whole-genome / NGS","Research","1–4 weeks"),("Pet & livestock genotyping","Animal","1–3 weeks")],
  standards="AABB accreditation (relationship testing), ISO/IEC 17025, ISO 21569/21570 (GMO), CAP/CLIA for clinical genetics.",
  price="Peace-of-mind paternity ≈ US$80–200; legal paternity ≈ $300–500; Sanger read ≈ $3–10 per sample (indicative).",
  faqs=[("What's the difference between legal and peace-of-mind paternity tests?","Legal tests use a documented chain of custody with identity verification so results are admissible in court; peace-of-mind tests use home-collected samples."),
        ("Can a lab verify that my product is the species on the label?","Yes — DNA barcoding and species-specific PCR can identify fish, meat, herbs and other ingredients, and detect substitution.")]),
]

TOOLS = [
 dict(slug="molarity-calculator", calc="molarity", icon="🧪", name="Molarity Calculator",
  short="Mass needed for a molar solution — or molarity from mass.",
  kw="molarity molar solution mass grams mol/L preparation",
  body="""<h2>How to use the molarity calculator</h2><p>Choose <em>Find mass</em> to calculate how many grams of solute you need for a target concentration and volume, or <em>Find molarity</em> if you already weighed your compound. Use the formula-lookup button to compute molecular weight automatically.</p>
<h2>Molarity formula</h2><div class="formula">mass (g) = concentration (mol/L) × volume (L) × molecular weight (g/mol)</div>
<h2>Worked example</h2><p>To prepare 500 mL of 0.1 M NaCl (MW 58.44 g/mol): 0.1 × 0.5 × 58.44 = <strong>2.922 g</strong>. Dissolve in ~400 mL water, then bring to exactly 500 mL in a volumetric flask.</p>
<div class="callout"><strong>Pro tip:</strong> For hydrated salts (e.g. CuSO₄·5H₂O) use the MW of the hydrate you actually weigh, not the anhydrous form.</div>""",
  faqs=[("What is the difference between molarity and molality?","Molarity is moles of solute per litre of solution (mol/L); molality is moles per kilogram of solvent (mol/kg). Molality does not change with temperature."),
        ("Why bring to volume instead of adding a fixed volume of water?","The solute occupies volume. Dissolving then filling to the mark in a volumetric flask gives an exact final volume and therefore an accurate concentration."),
        ("How do I convert mM to M?","Divide by 1,000. 250 mM = 0.25 M.")]),
 dict(slug="dilution-calculator", calc="dilution", icon="💧", name="Dilution Calculator (C1V1 = C2V2)",
  short="Solve any dilution: stock volume, final concentration or volume.",
  kw="dilution c1v1 c2v2 stock solution dilute",
  body="""<h2>The dilution equation</h2><div class="formula">C₁ × V₁ = C₂ × V₂</div><p>C₁ is stock concentration, V₁ the volume of stock you take, C₂ the final concentration and V₂ the final total volume. Leave the unknown blank and the calculator solves it.</p>
<h2>Worked example</h2><p>You need 50 mL of 1× buffer from a 10× stock: V₁ = (1 × 50) / 10 = <strong>5 mL</strong> of stock + 45 mL water.</p>
<div class="callout">Units of C₁ and C₂ must match, and units of V₁ and V₂ must match.</div>""",
  faqs=[("Can I use C1V1 = C2V2 for percentages?","Yes, as long as both concentrations use the same unit (% w/v, mg/mL, M, ×, etc.)."),
        ("What is a dilution factor?","The ratio of final volume to aliquot volume (V₂/V₁) — equivalently C₁/C₂. A 1:10 dilution has a dilution factor of 10.")]),
 dict(slug="serial-dilution-calculator", calc="serial", icon="🧫", name="Serial Dilution Calculator",
  short="Tube-by-tube plan and concentrations for any fold dilution series.",
  kw="serial dilution series fold 1:10 standard curve plating",
  body="""<h2>How serial dilutions work</h2><p>Each tube is diluted by the same factor from the previous tube, so concentration falls geometrically. Serial dilutions are used for standard curves, bacterial plate counts (CFU), ELISAs and MIC assays.</p>
<div class="formula">Cₙ = C₀ / Fⁿ &nbsp;&nbsp; transfer = V_final / (F − 1)</div>
<h2>Example</h2><p>10-fold series with 900 µL diluent per tube: transfer 100 µL each step. Tube 3 is at 1:1,000 of the stock.</p>""",
  faqs=[("Why change tips between every transfer?","Carry-over on the tip adds error that compounds across the series. Fresh tips and thorough mixing keep each step accurate."),
        ("How many dilutions do I need for plate counts?","Enough to get 30–300 colonies on a plate. For dense cultures that often means 10⁻⁵ to 10⁻⁸.")]),
 dict(slug="molar-mass-calculator", calc="molarmass", icon="⚛️", name="Molar Mass Calculator",
  short="Molecular weight and % composition from any chemical formula.",
  kw="molar mass molecular weight formula mw g/mol composition",
  body="""<h2>How it works</h2><p>Type a formula using standard notation. Parentheses, square brackets and hydrates (· or .) are supported — e.g. <code>Ca(OH)2</code>, <code>K4[Fe(CN)6]</code>, <code>CuSO4·5H2O</code>. Atomic weights follow IUPAC standard values.</p>
<div class="formula">M = Σ (nᵢ × Aᵢ)</div><h2>Example</h2><p>Glucose C₆H₁₂O₆ = 6(12.011) + 12(1.008) + 6(15.999) = <strong>180.156 g/mol</strong>.</p>""",
  faqs=[("Is molar mass the same as molecular weight?","Numerically yes. Molar mass has units of g/mol; molecular weight is often quoted as a unitless relative mass or in daltons."),
        ("Why does my value differ slightly from the supplier's?","Suppliers may use older atomic-weight tables or round differently. Always use the formula weight printed on your specific bottle for hydrates and salts.")]),
 dict(slug="buffer-calculator", calc="buffer", icon="⚖️", name="Buffer Calculator (Henderson–Hasselbalch)",
  short="Acid/base amounts for phosphate, Tris, acetate, HEPES and more.",
  kw="buffer henderson hasselbalch pka ph phosphate tris acetate hepes",
  body="""<h2>Henderson–Hasselbalch equation</h2><div class="formula">pH = pKa + log₁₀([A⁻]/[HA])</div><p>Pick a preset buffer or enter your own pKa, choose a target pH and total concentration, and the calculator splits the total into conjugate base and weak acid amounts.</p>
<h2>Choosing a buffer</h2><table><tr><th>Buffer</th><th>pKa (25 °C)</th><th>Useful range</th></tr><tr><td>Acetate</td><td>4.76</td><td>3.8–5.8</td></tr><tr><td>MES</td><td>6.15</td><td>5.5–6.7</td></tr><tr><td>Phosphate (pKa₂)</td><td>7.20</td><td>6.2–8.2</td></tr><tr><td>HEPES</td><td>7.48</td><td>6.8–8.2</td></tr><tr><td>Tris</td><td>8.07</td><td>7.0–9.0</td></tr><tr><td>Carbonate (pKa₂)</td><td>10.33</td><td>9.2–10.8</td></tr></table>
<div class="callout">pKa shifts with temperature and ionic strength (Tris ≈ −0.028 per °C). Always finish by adjusting with a calibrated pH meter.</div>""",
  faqs=[("Why is my buffer pH off from the calculation?","Activity effects, temperature, ionic strength and reagent hydration all shift real pH. Calculations get you close; the pH meter gets you exact."),
        ("What concentration should my buffer be?","Most biochemical buffers are 10–100 mM. Higher concentrations give more buffering capacity but may affect enzymes or cells.")]),
 dict(slug="centrifuge-rpm-rcf-calculator", calc="rcf", icon="🌀", name="Centrifuge RPM ↔ RCF (g-force) Calculator",
  short="Convert rotor speed to g-force and back using rotor radius.",
  kw="centrifuge rpm rcf g force convert rotor radius",
  body="""<h2>Formula</h2><div class="formula">RCF = 1.118 × 10⁻⁵ × r(cm) × RPM²</div><p>Protocols should specify g-force because RPM alone depends on rotor size. Use the maximum radius (r<sub>max</sub>) from the rotor manual.</p>
<h2>Example</h2><p>A rotor with r = 8.5 cm at 13,000 RPM gives 1.118e-5 × 8.5 × 13,000² ≈ <strong>16,060 × g</strong>.</p>""",
  faqs=[("Where do I find the rotor radius?","In the rotor or centrifuge manual — usually listed as r_max. You can also measure from the centre of the spindle to the bottom of the tube in its spinning position."),
        ("Is 'xg' the same as RCF?","Yes. Relative centrifugal force is expressed as multiples of Earth's gravity (× g).")]),
 dict(slug="pcr-master-mix-calculator", calc="pcr", icon="🧬", name="PCR Master Mix Calculator",
  short="Scale buffer, dNTPs, primers, polymerase and water for n reactions.",
  kw="pcr master mix calculator primers dntp polymerase reactions",
  body="""<h2>How it works</h2><p>Enter the number of reactions, reaction volume and overage. The calculator uses common final concentrations — 1× buffer, 0.2 mM each dNTP, 0.5 µM each primer, 1.25 U polymerase per 50 µL — and fills the rest with water. Always follow your enzyme supplier's recommendations.</p>
<div class="callout">Add 5–10% overage to cover pipetting loss. Keep the mix on ice and add the polymerase last.</div>""",
  faqs=[("Why prepare a master mix?","It reduces pipetting steps, improves consistency between reactions and saves reagents."),
        ("Should template go in the master mix?","No — add template separately to each tube so you can include different samples and a no-template control.")]),
 dict(slug="cell-count-calculator", calc="cells", icon="🔬", name="Hemocytometer Cell Count & Seeding Calculator",
  short="Cells/mL, viability and seeding volumes from hemocytometer counts.",
  kw="cell count hemocytometer viability trypan blue seeding density",
  body="""<h2>Formula</h2><div class="formula">cells/mL = (cells counted ÷ squares counted) × dilution factor × 10⁴</div><p>Each large square of a Neubauer hemocytometer holds 0.1 µL (10⁻⁴ mL). With trypan blue mixed 1:1, the dilution factor is 2.</p>
<h2>Viability</h2><div class="formula">viability % = live ÷ (live + dead) × 100</div>""",
  faqs=[("How many cells should I count?","Aim for 100–300 cells total across the squares for statistical reliability; dilute or concentrate if needed."),
        ("Which cells on the border do I count?","Use a consistent rule — typically count cells touching the top and left lines but not the bottom and right.")]),
 dict(slug="statistics-calculator", calc="stats", icon="📊", name="Lab Statistics Calculator",
  short="Mean, SD, SEM, CV%, 95% CI and Grubbs outlier score from replicates.",
  kw="statistics standard deviation mean sem cv confidence interval outlier grubbs replicates",
  body="""<h2>What you get</h2><p>Paste replicate values to get descriptive statistics used in QC and method validation: mean, median, sample standard deviation, standard error, coefficient of variation, a t-based 95% confidence interval and the Grubbs G statistic for the most extreme point.</p>
<div class="formula">SD = √(Σ(x − x̄)² / (n − 1)) &nbsp; SEM = SD/√n &nbsp; CV% = SD/x̄ × 100</div>
<div class="callout">Compare Grubbs G to the critical value for your n (e.g. 1.887 for n = 5 at α = 0.05) before rejecting any outlier — and document the reason.</div>""",
  faqs=[("SD or SEM — which should I report?","SD describes the spread of your data; SEM describes the precision of the mean. Report SD for variability and SEM or CI when comparing means."),
        ("What is an acceptable CV%?","It depends on the assay: many analytical methods target < 2–5%, while biological assays often accept 10–20%.")]),
 dict(slug="dna-concentration-calculator", calc="nucleic", icon="🧾", name="DNA/RNA Concentration & Purity (A260)",
  short="ng/µL from A260 plus 260/280 and 260/230 purity checks.",
  kw="dna rna concentration a260 nanodrop 260 280 purity",
  body="""<h2>Formula</h2><div class="formula">concentration (ng/µL) = A₂₆₀ × factor × dilution ÷ path length (cm)</div><p>Factors: dsDNA 50, RNA 40, ssDNA 33 (oligos vary by sequence).</p>
<h2>Purity ratios</h2><ul><li><strong>A260/A280</strong> ≈ 1.8 for pure DNA and ≈ 2.0 for RNA. Lower values suggest protein or phenol.</li><li><strong>A260/A230</strong> 2.0–2.2 is ideal. Lower values suggest guanidine salts, EDTA or carbohydrates.</li></ul>""",
  faqs=[("Why is my 260/280 ratio above 2.0 for DNA?","Often RNA contamination. Consider RNase treatment or a fluorometric dsDNA assay."),
        ("Is UV absorbance accurate for low concentrations?","Below ~10 ng/µL, fluorometric dyes (e.g. PicoGreen/Qubit-type assays) are more accurate and specific.")]),
 dict(slug="beer-lambert-calculator", calc="beer", icon="🌈", name="Beer–Lambert Law Calculator",
  short="Solve absorbance, molar absorptivity, path length or concentration.",
  kw="beer lambert law absorbance extinction coefficient concentration spectrophotometer",
  body="""<h2>Beer–Lambert law</h2><div class="formula">A = ε × l × c</div><p>A is absorbance (unitless), ε molar absorptivity (L·mol⁻¹·cm⁻¹), l path length (cm) and c concentration (mol/L). Fill three values to solve for the fourth.</p>
<div class="callout">Linearity usually holds for A ≈ 0.1–1.0. Dilute samples that read above your instrument's linear range.</div>""",
  faqs=[("Why does Beer–Lambert fail at high absorbance?","Stray light, molecular interactions and refractive-index changes cause deviations; dilute into the linear range."),
        ("Where do I find ε?","Literature, supplier datasheets or by measuring a standard curve of known concentrations.")]),
 dict(slug="ppm-concentration-converter", calc="ppm", icon="🔁", name="Concentration Converter (ppm, mg/L, %, M)",
  short="Convert between ppm, ppb, mg/L, g/L, % w/v and molarity.",
  kw="ppm ppb mg/l convert concentration percent molarity converter",
  body="""<h2>Key relationships</h2><div class="formula">1 ppm ≈ 1 mg/L (dilute aqueous) &nbsp; 1 % w/v = 10 g/L = 10,000 mg/L &nbsp; M = (mg/L) ÷ (1000 × MW)</div><p>Enter a value, choose its unit and — for molar conversions — the molecular weight.</p>""",
  faqs=[("Is ppm always equal to mg/L?","Only for dilute water-based solutions with density ≈ 1 g/mL. For other matrices, ppm is mass/mass (mg/kg)."),
        ("How do I convert ppm to molarity?","Divide mg/L by the molecular weight (g/mol) to get mmol/L, then divide by 1,000 for mol/L.")]),
]

GUIDES = [
 dict(slug="how-to-choose-an-accredited-testing-lab", icon="🏅", cat="Lab testing", title="How to Choose an Accredited Testing Laboratory (ISO/IEC 17025 Explained)",
  desc="A practical checklist for selecting a testing lab: accreditation scope, methods, turnaround, sampling, pricing and red flags.",
  body="""<p>Choosing the wrong lab costs more than the invoice: rejected certificates, re-sampling, missed launches and — in regulated industries — compliance failures. This checklist is what experienced QA managers use.</p>
<h2 id="accreditation">1. Check accreditation — and the scope</h2><p><strong>ISO/IEC 17025</strong> is the international standard for testing and calibration laboratories. It certifies that a lab has a working quality system <em>and</em> is technically competent for specific methods. The key word is <em>specific</em>: accreditation applies only to methods listed on the lab's <strong>scope of accreditation</strong>. Always download the scope from the accreditation body (A2LA, ANAB, UKAS, CALA, NABL, DAkkS, etc.) and confirm your test method and matrix are listed.</p>
<p>Clinical labs have their own frameworks: <strong>CLIA</strong> and <strong>CAP</strong> in the US and <strong>ISO 15189</strong> internationally. Pharmaceutical QC labs work under <strong>GMP</strong>, and non-clinical safety studies under <strong>GLP</strong>.</p>
<h2 id="method">2. Confirm the exact method and detection limits</h2><p>Ask for the method reference (EPA, ASTM, ISO, AOAC, USP), the <strong>limit of quantitation (LOQ)</strong> and measurement uncertainty. An LOQ above your regulatory limit makes the result useless.</p>
<h2 id="sampling">3. Understand sampling and holding times</h2><p>Many analyses fail before the sample reaches the lab. Request the lab's containers, preservatives and chain-of-custody forms, and ask about holding times — bacteria in water typically must be analysed within 24–30 hours.</p>
<h2 id="turnaround">4. Compare turnaround and rush options</h2><p>Standard turnaround ranges from 24 hours (simple micro) to several weeks (stability, failure analysis). Rush fees often add 50–200%.</p>
<h2 id="price">5. Compare total cost, not unit price</h2><p>Include sampling kits, shipping (often cold-chain), sample prep, rush surcharges, report formats and re-test policies.</p>
<h2 id="redflags">Red flags</h2><ul><li>Cannot show a current certificate or scope</li><li>No method references on the report</li><li>Prices far below market with no explanation</li><li>No quality-control data (blanks, spikes, duplicates) available on request</li></ul>
<div class="callout"><strong>Shortcut:</strong> Send one request through our <a href="../quote.html">free quote form</a> and we'll match you with labs whose scope fits your test.</div>"""),
 dict(slug="home-water-testing-guide", icon="💧", cat="Water", title="Home & Well Water Testing: What to Test, When and How",
  desc="Which contaminants to test in tap and private well water, how often, how to sample, and how to read your results.",
  body="""<p>Public water systems are monitored by utilities, but <strong>private wells are the owner's responsibility</strong>, and household plumbing can add lead and copper to even treated water.</p>
<h2>What to test</h2><table><tr><th>Parameter</th><th>Why</th><th>How often</th></tr><tr><td>Total coliform & E. coli</td><td>Sewage/animal contamination</td><td>Yearly + after floods</td></tr><tr><td>Nitrate</td><td>Fertiliser, septic; dangerous for infants</td><td>Yearly</td></tr><tr><td>Lead & copper</td><td>Old pipes, solder, fixtures</td><td>Once, then if plumbing changes</td></tr><tr><td>Arsenic, uranium, manganese</td><td>Natural geology</td><td>Once, then every 3–5 years</td></tr><tr><td>PFAS</td><td>Firefighting foam, industry, landfills</td><td>If near known sources</td></tr><tr><td>pH, hardness, iron</td><td>Corrosion, scale, staining</td><td>Every few years</td></tr></table>
<h2>How to sample</h2><ol><li>Order sterile bottles from an accredited or certified lab.</li><li>For <strong>bacteria</strong>, remove aerators, disinfect the tap, run water 2–3 minutes and fill without touching the inside of the cap.</li><li>For <strong>lead</strong>, collect a first-draw sample after water has sat 6+ hours.</li><li>Keep samples cold and deliver within the stated holding time.</li></ol>
<h2>Reading results</h2><p>Compare each result with the maximum contaminant level (MCL) or guideline value in your jurisdiction. Any E. coli detection means the water is unsafe to drink until disinfected and re-tested.</p>
<div class="callout">Use our <a href="../tools/ppm-concentration-converter.html">ppm ↔ mg/L converter</a> to compare results reported in different units.</div>"""),
 dict(slug="how-to-prepare-molar-solutions", icon="🧪", cat="Protocols", title="How to Prepare Molar Solutions Accurately (Step-by-Step)",
  desc="From calculation to volumetric flask: the correct way to prepare molar solutions, with common mistakes to avoid.",
  body="""<p>Accurate solutions are the foundation of reproducible experiments. Here's the professional workflow.</p>
<h2>1. Calculate the mass</h2><div class="formula">mass (g) = M (mol/L) × V (L) × MW (g/mol)</div><p>Use our <a href="../tools/molarity-calculator.html">molarity calculator</a> and the MW printed on your reagent bottle (hydrates matter!).</p>
<h2>2. Weigh precisely</h2><p>Use an analytical balance for masses under ~1 g. Tare a clean weigh boat, add solute with a clean spatula, and record the actual mass.</p>
<h2>3. Dissolve in less than final volume</h2><p>Dissolve in about 70–80% of the final volume with stirring. Some salts are endothermic or exothermic — let the solution return to room temperature.</p>
<h2>4. Adjust pH if needed</h2><p>For buffers, adjust pH <em>before</em> bringing to final volume.</p>
<h2>5. Bring to volume</h2><p>Transfer quantitatively to a volumetric flask, rinse the beaker into the flask, fill to the calibration mark at eye level, stopper and invert 10–15 times.</p>
<h2>Common mistakes</h2><ul><li>Adding solute to a fixed volume of water (final volume is then wrong)</li><li>Using anhydrous MW for a hydrate</li><li>Filling to the mark while the solution is warm</li><li>Not labelling with name, concentration, date and initials</li></ul>"""),
 dict(slug="serial-dilution-guide", icon="🧫", cat="Protocols", title="Serial Dilutions Made Simple: Plate Counts, Standard Curves & ELISAs",
  desc="Understand serial dilution math, choose the right fold, and avoid the pipetting errors that ruin standard curves.",
  body="""<p>A serial dilution repeatedly dilutes a sample by a fixed factor, producing a geometric series of concentrations.</p>
<h2>The math</h2><div class="formula">Cₙ = C₀ / Fⁿ</div><p>With a 10-fold series, tube 1 is 1:10, tube 2 1:100, tube 3 1:1,000. With 2-fold, concentrations halve each step — ideal for standard curves and MIC assays.</p>
<h2>Choosing a fold</h2><ul><li><strong>10-fold</strong>: bacterial and viral titres spanning many logs.</li><li><strong>2- or 3-fold</strong>: standard curves, ELISAs, antibody titrations.</li></ul>
<h2>Technique checklist</h2><ol><li>Pre-fill all tubes with diluent.</li><li>Mix each tube thoroughly (vortex or pipette up and down 5–10×).</li><li>Change tips between every transfer.</li><li>Label everything before starting.</li></ol>
<p>Generate a complete tube-by-tube plan with our <a href="../tools/serial-dilution-calculator.html">serial dilution calculator</a>.</p>"""),
 dict(slug="centrifuge-rpm-vs-rcf", icon="🌀", cat="Equipment", title="RPM vs RCF: Why Your Protocol Says ×g (and How to Convert)",
  desc="Why g-force matters more than RPM, how to find rotor radius, and a quick conversion reference.",
  body="""<p>Two centrifuges spinning at the same RPM can apply very different forces. That's why good protocols specify <strong>relative centrifugal force (RCF, × g)</strong>.</p>
<div class="formula">RCF = 1.118 × 10⁻⁵ × r × RPM²</div>
<h2>Quick reference (r = 10 cm)</h2><table><tr><th>RPM</th><th>≈ × g</th></tr><tr><td>1,000</td><td>112</td></tr><tr><td>3,000</td><td>1,006</td></tr><tr><td>5,000</td><td>2,795</td></tr><tr><td>10,000</td><td>11,180</td></tr><tr><td>15,000</td><td>25,155</td></tr></table>
<h2>Safety</h2><ul><li>Always balance tubes by mass, not just volume.</li><li>Never exceed the rotor's rated speed; derate for dense solutions.</li><li>Use sealed buckets for biohazards and wait for the rotor to stop completely.</li></ul>
<p>Convert instantly with the <a href="../tools/centrifuge-rpm-rcf-calculator.html">RPM ↔ RCF calculator</a>.</p>"""),
 dict(slug="nanodrop-260-280-ratio-explained", icon="🧾", cat="Molecular biology", title="A260/A280 & A260/A230 Ratios Explained: Is Your DNA Pure?",
  desc="What spectrophotometer purity ratios mean, what causes bad ratios, and how to fix them.",
  body="""<p>UV spectrophotometry is the quickest way to estimate nucleic-acid concentration and purity.</p>
<h2>Concentration</h2><div class="formula">ng/µL = A260 × 50 (dsDNA) | × 40 (RNA) | × 33 (ssDNA)</div>
<h2>Purity ratios</h2><table><tr><th>Ratio</th><th>Target</th><th>Low value suggests</th></tr><tr><td>A260/A280</td><td>~1.8 DNA, ~2.0 RNA</td><td>Protein, phenol</td></tr><tr><td>A260/A230</td><td>2.0–2.2</td><td>Guanidine, EDTA, carbohydrates, phenol</td></tr></table>
<h2>Fixes</h2><ul><li>Extra wash steps on silica columns to remove guanidine</li><li>Ethanol precipitation to remove salts</li><li>RNase treatment if the 260/280 of DNA is &gt; 2.0</li><li>Blank with the same buffer your sample is in</li></ul>
<p>Calculate concentration and purity with the <a href="../tools/dna-concentration-calculator.html">DNA/RNA calculator</a>.</p>"""),
 dict(slug="food-shelf-life-testing-guide", icon="🍎", cat="Food", title="Food Shelf-Life Testing: Methods, Costs & How to Set a Best-Before Date",
  desc="Real-time vs accelerated shelf-life studies, what's tested, costs and a step-by-step plan for food brands.",
  body="""<p>A defensible shelf life protects consumers and your brand. It must be based on evidence — microbiological, chemical and sensory.</p>
<h2>Real-time vs accelerated</h2><ul><li><strong>Real-time</strong>: store under intended conditions and test at intervals until the product fails. Most reliable.</li><li><strong>Accelerated (ASLT)</strong>: elevated temperature/humidity speed up degradation; useful for shelf-stable products when the degradation mechanism is understood.</li></ul>
<h2>What's measured</h2><ul><li>Microbiology: total plate count, yeast & mould, relevant pathogens</li><li>Chemistry: pH, water activity, rancidity (peroxide value), vitamin loss</li><li>Sensory: appearance, odour, flavour, texture</li></ul>
<h2>Planning your study</h2><ol><li>Define failure criteria before you start.</li><li>Choose time points (e.g. 0, 25%, 50%, 75%, 100%, 125% of target life).</li><li>Test samples from production — not kitchen prototypes.</li><li>Add a safety margin to the final date.</li></ol>
<div class="callout">Studies commonly cost from about US$500 to several thousand. <a href="../quote.html?category=food">Get quotes from food labs</a>.</div>"""),
 dict(slug="lab-safety-essentials", icon="🦺", cat="Safety", title="Lab Safety Essentials: The Rules Every Lab Should Enforce",
  desc="PPE, chemical storage, SDS, waste, biosafety levels and emergency procedures in one practical checklist.",
  body="""<p>Most lab incidents are preventable with consistent basics.</p>
<h2>Personal protective equipment</h2><ul><li>Lab coat, safety glasses/goggles and closed-toe shoes at all times</li><li>Gloves matched to the chemical (nitrile is not universal — check compatibility charts)</li><li>Face shields for splash hazards; cryo-gloves for liquid nitrogen</li></ul>
<h2>Chemical management</h2><ul><li>Keep a current Safety Data Sheet (SDS) for every chemical</li><li>Segregate incompatibles: acids from bases, oxidisers from flammables</li><li>Label secondary containers with name, hazard and date</li></ul>
<h2>Biosafety levels</h2><table><tr><th>BSL</th><th>Examples</th><th>Key controls</th></tr><tr><td>1</td><td>Non-pathogenic E. coli</td><td>Standard practices</td></tr><tr><td>2</td><td>Staphylococcus aureus, human cell lines</td><td>BSC for aerosols, restricted access</td></tr><tr><td>3</td><td>M. tuberculosis</td><td>Negative pressure, respirators</td></tr><tr><td>4</td><td>Ebola virus</td><td>Positive-pressure suits, isolated facility</td></tr></table>
<h2>Emergencies</h2><p>Know the location of eyewash stations, safety showers, spill kits, fire extinguishers and exits. Report every incident and near-miss.</p>"""),
]

EQUIPMENT = [
 ("🌀","Centrifuges","Max RCF, rotor options (fixed-angle vs swing-bucket), refrigeration, noise, imbalance detection, footprint.","benchtop centrifuge"),
 ("💧","Pipettes","Volume range, single vs multichannel, ergonomics, calibration service, tip compatibility.","laboratory pipette set"),
 ("⚖️","Analytical balances","Readability (0.1 mg vs 0.01 mg), capacity, internal calibration, draft shield, GLP printouts.","analytical balance 0.1mg"),
 ("🔬","Microscopes","Compound vs stereo, optics (plan achromat), LED illumination, camera port, phase contrast/fluorescence.","compound microscope laboratory"),
 ("🧪","pH meters","Accuracy (±0.01), ATC, electrode type for your samples, calibration points, data logging.","benchtop ph meter"),
 ("🧬","PCR / qPCR thermal cyclers","Block format, ramp rate, gradient, number of optical channels, software & data export.","pcr thermal cycler"),
 ("🌈","Spectrophotometers","UV-Vis range, micro-volume capability, cuvette vs plate, bandwidth, software.","uv vis spectrophotometer"),
 ("🔥","Autoclaves & sterilizers","Chamber size, cycle types (liquid, dry, vacuum), validation and documentation.","laboratory autoclave"),
 ("🌡️","Incubators & shakers","Temperature uniformity, CO₂ control, humidity, orbit diameter, capacity.","laboratory incubator"),
 ("🧊","Lab freezers (-20/-80 °C)","Temperature stability, recovery time, alarms/monitoring, energy use, capacity.","ultra low temperature freezer"),
 ("💨","Fume hoods & biosafety cabinets","Ducted vs ductless, face velocity, class (BSC I/II/III), certification.","biosafety cabinet"),
 ("🧫","Water purification systems","Type I/II/III water, flow rate, TOC monitoring, consumable costs.","laboratory water purification system"),
]

VIDEOS = [
 ("How to use a micropipette correctly","micropipette technique tutorial","Technique"),
 ("Serial dilution step-by-step","serial dilution lab tutorial","Technique"),
 ("Preparing a molar solution","how to prepare molar solution lab","Technique"),
 ("Hemocytometer cell counting","hemocytometer cell counting tutorial","Cell culture"),
 ("Agarose gel electrophoresis","agarose gel electrophoresis tutorial","Molecular biology"),
 ("PCR explained visually","PCR animation explained","Molecular biology"),
 ("How to test your well water","how to collect well water sample for testing","Testing"),
 ("Inside an ISO 17025 lab","ISO 17025 laboratory tour","Testing"),
 ("Centrifuge balancing & safety","centrifuge balancing safety lab","Safety"),
 ("Aseptic technique basics","aseptic technique microbiology","Microbiology"),
 ("Using a UV-Vis spectrophotometer","uv vis spectrophotometer tutorial","Equipment"),
 ("Lab safety: PPE essentials","lab safety PPE training","Safety"),
]

JOB_CATS = [("🧪","Chemistry & analytical"),("🦠","Microbiology"),("🧬","Molecular biology & genomics"),("🩸","Clinical laboratory science"),("💊","Pharma QC / QA"),("🌍","Environmental science"),("🍎","Food science & safety"),("🧱","Materials & engineering"),("📊","Lab data & bioinformatics"),("🎓","Academic research & postdocs"),("🛠️","Lab technicians & service engineers"),("📈","Scientific sales & marketing")]
