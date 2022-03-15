"""Simulate a dimensionality reduction step."""
import numpy as np
import yaml

# Get parameter value
with open("params.yaml") as params_file:
    all_params = yaml.safe_load(params_file)
p = all_params["total_var"]


print(f"Analysing data in samples.csv with parameter {p}")
data = np.loadtxt("samples.csv", delimiter=",")
results = p * data.sum(axis=1)

# Write results
np.savetxt("reduced.csv", results, delimiter=",")
