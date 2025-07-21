# Restraint Score Calculator

This Python project provides a tool to calculate **restraint scores** for protein–peptide docking systems. The method evaluates each restraint's informativeness by integrating:

- Evolutionary conservation  
- Spatial proximity of atoms  
- Dispersion across the protein surface and peptide sequence

It is designed for structure prediction workflows such as HADDOCK and enables efficient modeling with minimal, high-quality restraints.

---

## Repository Structure

```
restraint-score/
├── Restraints_quality_calculator.py             # Core calculator script
├── run_demo.ipynb                               # Script to run both high and low scoring examples
├── demo/
│   ├── 1azg_high_scoring_example.xlsx           # Example input file 1
│   ├── 1azg_low_scoring_example.xlsx            # Example input file 2
│   ├── 1azg_high_scoring_example_output.xlsx    # Output 1 (generated)
│   └── 1azg_low_scoring_example_output.xlsx     # Output 2 (generated)
├── conservation_weights.xlsx                    # Reference scores from 43 PDB complexes
├── README.md                                    
```

---

## How to Use

### 1. Install Dependencies

This project uses:

- `pandas`
- `numpy`
- `openpyxl` (for reading and writing `.xlsx` files)

Install them with:

```bash
conda install pandas numpy openpyxl
```

---

### 2. Run the Demo

Execute the demo script, which processes two example Excel files:

```bash
python run_demo.py
```

This will print results to the terminal and save detailed output files for each input.

---

### 3. Run on Your Own File

To calculate the restraint score for your own Excel input file, use the following command:

```bash
python Restraints_quality_calculator.py path/to/your_file.xlsx
```

Replace `path/to/your_file.xlsx` with the path to your actual `.xlsx` file.

This will:
- Print the final restraint score to the terminal
- Save the detailed output to `your_file_output.xlsx` in the same directory

---

## Input Format

Each input Excel file should contain:

- A constant `Ls` value (number of peptide residues in active site) stored in **row 2, column B**
- A table starting at **row 3** with the following column headers:

| restraints | prot x coor | prot y coor | prot z coor | sl | wi | wj | dij |
|------------|--------------|--------------|--------------|----|-----|-----|------|

Where:
- `sl`: peptide residue index
- `wi`, `wj`: evolutionary conservation scores for the protein and peptide residues
- `dij`: interatomic distance between atoms involved in the restraint

---

## Conservation Weights

Each restraint entry must include conservation scores (`wi`, `wj`). You have two options for assigning them:

### Option 1: Use Your Own Conservation Scores  
If you have performed multiple sequence alignments (MSA) on your own protein and peptide sequences, you can calculate conservation scores using any preferred method and enter them directly into the input Excel file.

### Option 2: Use Our Scores as a Reference  
We provide a file:

```
conservation_weights.xlsx
```

This file includes conservation scores calculated for the **43 PDB complexes** used in our benchmark study. These scores were generated based on:

- Multiple sequence alignments of homologous protein sequences
- Class-specific alignments for **class I** and **class II** peptides

---

## Output

Each output file (e.g. `your_file_output.xlsx`) contains:

- Intermediate values: `w_ij`, `f(dij)`, `Omega_ij`
- Spatial and sequence variance: `sigma_P`, `sigma_L`
- Final restraint score: printed in terminal and saved to Excel

---

## Notes

- You can modify `1azg_high_scoring_example.xlsx` to test different restraint sets.
- To use your own data, follow the same column structure and format.
- For method transparency, see the original dataset used for benchmarking.

---

## Citation

If you use this tool for academic work, please cite the method described in:

*Restraint Quality, Not Quantity, Predicts Peptide–Protein Docking Outcomes.*  
Gulman M., Chill J., Major D.T., 2025.  
Department of Chemistry, Bar-Ilan University.

---
