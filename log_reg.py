"""Simulate a classification (logistic regression) step."""
import pickle

import numpy as np
import yaml

# Get parameter value
with open("params.yaml") as params_file:
    all_params = yaml.safe_load(params_file)
b = all_params["bias"]

print(f"Building model based on data in reduced.csv")
coeffs = np.loadtxt("reduced.csv", delimiter=",")

# For now, consider only the coefficients to represent the "model"
my_model = np.hstack((coeffs, [b]))

# Serialize model for distribution
with open("classifier.pkl", "wb") as output_file:
    pickle.dump(my_model, output_file)
