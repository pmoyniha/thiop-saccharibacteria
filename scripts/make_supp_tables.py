import pandas as pd
from collections import defaultdict

with open('genomes_with_true_ortholog.txt') as f:
    ortho_set = {l.strip() for l in f if l.strip()}

tax = {}
with open('saccharimonadia_reps.tsv') as f:
    next(f)
    for line in f:
        acc, t = line.strip().split('\t')
        parts = {p.split('__')[0]: p.split('__')[1] for p in t.split(';') if '__' in p}
        tax[acc] = parts

order_counts = defaultdict(lambda: [0, 0])
for acc, t in tax.items():
    o = t.get('o', 'unknown')
    order_counts[o][0] += 1
    if acc in ortho_set:
        order_counts[o][1] += 1

order_rows = []
for o, (n, h) in sorted(order_counts.items(), key=lambda x: -x[1][0]):
    order_rows.append({
        'GTDB order': o, 'Total genomes (N)': n,
        'With ThioP ortholog': h, 'Without ThioP ortholog': n - h,
        'Prevalence (%)': round(h / n * 100, 1),
        'Notes': 'Formally described; contains all cultured Saccharibacteria' if o == 'Saccharimonadales' else 'Placeholder name (uncultured environmental lineage)'
    })
totals = sum(r['Total genomes (N)'] for r in order_rows)
totals_h = sum(r['With ThioP ortholog'] for r in order_rows)
order_rows.append({'GTDB order':'TOTAL','Total genomes (N)':totals,'With ThioP ortholog':totals_h,'Without ThioP ortholog':totals-totals_h,'Prevalence (%)':round(totals_h/totals*100,1),'Notes':''})
order_df = pd.DataFrame(order_rows)

ARCH_PRIORITY = {
    'High (CxN + sortase + SignalP)': 6,
    'High (CxN + sortase; secretion implied)': 5,
    'High (CxN + SignalP; non-canonical anchor)': 5,
    'Possible (CxN only; no secretion evidence)': 3,
    'Likely paralog (secreted but no CxN)': 2,
    'Likely false positive': 1,
    'False positive (fragment)': 1,
}

hits_xl = pd.read_excel('saccharibacteria_hits_annotated.xlsx', sheet_name='Hits (default E)')
hits_xl['_priority'] = hits_xl['Architecture'].map(lambda a: ARCH_PRIORITY.get(a, 0))
best = (hits_xl.sort_values(['_priority','E-value (full seq)'], ascending=[False, True])
                .drop_duplicates('Species', keep='first'))
best = best.set_index('Species')

named = [
    ('Candidatus Saccharimonas aalborgensis',      'present'),
    ('Candidatus Mycosynbacter amalyticus',        'present'),
    ('Candidatus Chaera renei',                    'present'),
    ('Candidatus Microsaccharimonas sossegonensis','present'),
    ('Candidatus Southlakia epibionticum',         'present'),
    ('Candidatus Nanosynbacter lyticus',           'present'),
    ('Candidatus Nanosynbacter featherlites',      'present'),
    ('Candidatus Nanosynbacter sp. TM7-074',       'present'),
    ('Candidatus Nanosyncoccus alces',             'absent'),
    ('Candidatus Nanosyncoccus nanoralicus',       'absent'),
    ('Candidatus Nanogingivalis gingivitcus',      'absent'),
    ('Candidatus Minimicrobia vallesae',           'absent'),
    ('Candidatus Minimicrobia naudis',             'indeterminate'),
]
species_rows = []
for sp, status in named:
    row = {'Species': sp, 'ThioP status': status}
    if sp in best.index:
        r = best.loc[sp]
        row['Best ortholog UniProt accession'] = r['UniProt accession']
        row['E-value (full seq)'] = f"{r['E-value (full seq)']:.1e}"
        row['Architecture'] = r['Architecture']
    else:
        row['Best ortholog UniProt accession'] = '\u2014'
        row['E-value (full seq)'] = '\u2014'
        row['Architecture'] = '\u2014'
    if sp == 'Candidatus Minimicrobia naudis':
        row['Notes'] = 'Proteome insufficient for phylogenetic placement (4/16 universal ribosomal markers); single hit is a 105-aa fragment'
    elif status == 'absent':
        row['Notes'] = 'No hit at default or permissive (E<=1) HMMER threshold; no structural homolog (Foldseek TM-score <0.3) across all proteins in genome'
    else:
        row['Notes'] = ''
    species_rows.append(row)
species_df = pd.DataFrame(species_rows)

with pd.ExcelWriter('thiop_supplementary_tables.xlsx', engine='openpyxl') as w:
    order_df.to_excel(w, sheet_name='Table S1 GTDB order prevalence', index=False)
    species_df.to_excel(w, sheet_name='Table S2 Named species', index=False)

print("Wrote thiop_supplementary_tables.xlsx\n")
print("Table S2 (corrected):")
print(species_df[['Species','ThioP status','Best ortholog UniProt accession','E-value (full seq)','Architecture']].to_string(index=False))
