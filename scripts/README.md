# Analysis scripts

Run in the order indicated. Each script is self-contained and uses inputs from the parent directory.

1. `01_build_hmm.sh` — build the profile HMM from the FoldMason alignment
2. `02_hmmsearch_uniref50.sh` — broad search across UniRef50
3. `03_extract_saccharimonadia_proteomes.sh` — filter GTDB metadata to *Saccharimonadia* and extract per-genome protein FASTAs from the GTDB bulk archive
4. `04_hmmsearch_gtdb.sh` — HMM search against the concatenated Saccharimonadia proteomes
5. `05_run_signalp.sh` — SignalP 6.0 on hit sequences
6. `06_architecture_classify.py` — classify each hit by architectural features (CxN motif + signal peptide and/or sortase site) and aggregate per-genome
7. `07_qc_stats.py` — Mann–Whitney comparisons of completeness, contamination, and genome size between present/absent groups
8. `08_build_named_species_tree.sh` — GToTree multi-marker tree for the 12 named species
9. `09_prune_gtdb_tree.py` — prune the GTDB bac120 reference tree to *Saccharimonadia*
10. `10_make_itol_annotations.py` — generate iTOL annotation files
11. `11_build_excel_tables.py` — build Table S1 (named species) and Tables S2/S3 (GTDB-wide)
