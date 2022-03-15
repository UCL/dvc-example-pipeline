"""Simulate calculation of metrics."""
import json

# Sample values - normally these would depend on the model performance!
metrics = {
    "precision": 0.63,
    "roc_auc": 0.85
}

with open("scores.json", "w") as metrics_file:
    json.dump(metrics, metrics_file)
