#!/usr/bin/env python
# coding: utf-8

"""
Restraint Score Calculator for Protein–Peptide Docking

This script calculates a composite restraint score based on:
- Evolutionary weights (wi, wj)
- Distance between atoms (dij)
- Spatial dispersion of protein atoms
- Sequence dispersion of peptide contacts

Author: Miriam Gulman
Date: *
"""

import pandas as pd
import numpy as np
import argparse
import os


def compute_restraint_score(excel_path):
    """
    Compute the restraint score from an Excel file containing restraint information.

    Parameters:
        excel_path (str): Path to the Excel file.

    Returns:
        pd.DataFrame: DataFrame with all computed columns.
        float: Final restraint score.
    """

    # --- Read Excel and extract Ls value ---
    sheet = pd.read_excel(excel_path, header=None)
    Ls_value = float(sheet.iloc[1, 1])  # Assumes Ls is stored in B2

    # --- Read data starting from row with headers ---
    df = pd.read_excel(excel_path, skiprows=2)

    # --- Constants ---
    Lx = 23.41
    Ly = 18.69
    Lz = 14.50
    d0 = 1.8
    N = len(df)

    # --- Step 1: wij ---
    df['wij'] = (df['wi'] + df['wj']) / 2

    # --- Step 2: f(dij) ---
    df['fdij'] = np.exp(-(df['dij'] - d0))

    # --- Step 3: Ω_ij ---
    df['omega_ij'] = df['wij'] * df['fdij']

    # --- Step 4: Protein centroid ---
    mu_x = df['prot x coor'].mean()
    mu_y = df['prot y coor'].mean()
    mu_z = df['prot z coor'].mean()

    # --- Step 5: σ_P^i ---
    df['sigma_P'] = (
        ((df['prot x coor'] - mu_x) / Lx) ** 2 +
        ((df['prot y coor'] - mu_y) / Ly) ** 2 +
        ((df['prot z coor'] - mu_z) / Lz) ** 2
    ) / N

    # --- Step 6: μ_s ---
    mu_s = df['sl'].mean()

    # --- Step 7: σ_L^j ---
    df['sigma_L'] = ((df['sl'] - mu_s) / Ls_value) ** 2 / N

    # --- Step 8: Final restraint score ---
    restraint_score = np.sum(df['omega_ij'] * (df['sigma_P'] + df['sigma_L'])) * N

    # --- Print Result ---
    print(f"\nFile: {excel_path}")
    print(f"Restraint Score (σ): {restraint_score:.6f}")

    # --- Save Output ---
    output_path = os.path.splitext(excel_path)[0] + "_output.xlsx"
    df.to_excel(output_path, index=False)
    print(f"Output written to: {output_path}")

    return df, restraint_score


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute restraint score from an Excel file.")
    parser.add_argument("excel_file", help="Path to the input .xlsx file")
    args = parser.parse_args()

    compute_restraint_score(args.excel_file)