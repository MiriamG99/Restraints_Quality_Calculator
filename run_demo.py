#!/usr/bin/env python
# coding: utf-8


from Restraints_quality_calculator import compute_restraint_score

# High scoring example
print("=== High Scoring Example ===")
compute_restraint_score("demo/1azg_high_scoring_example.xlsx")

# Low scoring example
print("\n=== Low Scoring Example ===")
compute_restraint_score("demo/1azg_low_scoring_example.xlsx")

