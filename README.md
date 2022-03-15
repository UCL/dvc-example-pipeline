# Example pipeline for DVC
This repository is a very naive simulation of a machine learning pipeline.
Its purpose is to show how a pipeline can be automated and tracked using
[dvc](https://dvc.org/).

## Requirements
- Python 3
- `numpy`
- `pyyaml`

You also need a CSV file named `samples.csv` (the values don't actually matter,
but the code must be able to read it).

## Running
```bash
dvc run -n pca \
        -d reduce_dim.py -d samples.csv \
        -p total_var \
        -o reduced.csv \
        python reduce_dim.py

dvc run -n classification \
        -d log_reg.py -d reduced.csv \
        -o classifier.pkl \
        python log_reg.py

dvc run -n evaluation \
        -d evaluate.py -d classifier.pkl \
        -m scores.json \
        python evaluate.py
```

This should produce a file named `dvc.yaml` describing the pipeline.