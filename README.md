# ThioP phylogenetic distribution in Saccharibacteria

Analysis code and data accompanying *[CITATION TO BE ADDED]*. This repository contains the inputs, intermediates, and outputs of the structure-derived HMM search and architectural-orthology pipeline used to assess ThioP distribution across *Candidatus* Saccharimonadia (Saccharibacteria) in GTDB R10-RS226.

## Repository layout

### Inputs
- `foldmason_aa.fa` — FoldMason multiple sequence alignment of 95 AlphaFoldDB structural homologs of the ThioP catalytic domain (input for HMM construction).
- `myprotein.hmm` — profile HMM built from the FoldMason alignment with `hmmbuild` (148 match states).
- `saccharimonadia_reps.tsv` — list of 1977 GTDB R10-RS226 representative genomes in class *Saccharimonadia* with full taxonomy strings.
- `annotation.tsv` — manually curated presence/absence calls for the 12 named-species tree.

### Output tables and lists
- `saccharibacteria_hits_annotated.xlsx` — per-protein and per-species architectural annotation for the 13 UniProt-registered named Saccharibacteria proteomes (Table S1).
- `gtdb_sacchari_hits.xlsx` — per-genome and per-protein annotation for all 1820 HMM hits across the 1977 GTDB representatives (Tables S2, S3).
- `genomes_with_hit.txt` — all GTDB genomes with any HMM hit (1192 genomes, 60.3%).
- `genomes_with_true_ortholog.txt` — refined set of genomes encoding a high-confidence architectural ortholog (1098 genomes, 55.5%; this is the publication number).

### Trees and visualization
- `named_species_tree.nwk` — multi-marker species phylogeny of 12 named Saccharibacteria built with GToTree using the Hug et al. 2016 universal ribosomal marker set.
- `sacchari_subtree.nwk` — GTDB bac120 reference tree pruned to the 1977 *Saccharimonadia* representative tips.
- `itol_presence_refined.txt` — iTOL DATASET_COLORSTRIP annotation: ortholog presence (green) / possible-truncated (orange) / absent (red).
- `itol_order.txt` — iTOL DATASET_COLORSTRIP annotation: GTDB order assignment per genome.

### Scripts
All analysis scripts are in `scripts/`. See `scripts/README.md` for the order of execution.

## Reproducing the analysis from scratch

External data not bundled here (too large; available from public sources):
- **UniRef50** (release 2026_02): `https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref50/uniref50.fasta.gz`
- **GTDB R10-RS226 protein archive**: `https://data.gtdb.ecogenomic.org/releases/latest/genomic_files_reps/gtdb_proteins_aa_reps.tar.gz`
- **GTDB R10-RS226 metadata**: `https://data.gtdb.ecogenomic.org/releases/latest/bac120_metadata.tsv.gz`
- **GTDB R10-RS226 bac120 tree**: `https://data.gtdb.ecogenomic.org/releases/latest/bac120.tree`
- **AlphaFold Protein Structure Database** v6: `https://alphafold.ebi.ac.uk/files/`

## Software

- HMMER 3.4 (`hmmbuild`, `hmmsearch`, `phmmer`)
- Foldseek 10.941cd33 (`easy-search`)
- FoldMason 4.dd3c235 (`easy-msa`, `refinemsa`)
- GToTree v1.8.10
- SignalP 6.0h (slow-sequential mode)
- iTOL v6 (web)
- Python 3.9 with ete3 3.1.3, pandas, openpyxl, scipy 1.15.2

## Citation
*[paper citation to be added on acceptance]*
