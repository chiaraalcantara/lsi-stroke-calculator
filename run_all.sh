#!/bin/bash


# Run all notebooks front to back for reproducibility

mkdir -p output/100_transforms
mkdir -p output/200_models

# Not run as it just transforms data from XPT to parquet
# poetry run papermill src/notebooks/100_transforms/110_merge_datasets.ipynb output/100_transforms/100_sas_to_parquet.ipynb
poetry run papermill --cwd src/notebooks/100_transforms src/notebooks/100_transforms/110_merge_datasets.ipynb output/100_transforms/110_merge_datasets.ipynb
poetry run papermill --cwd src/notebooks/100_transforms src/notebooks/100_transforms/120_data_cleaning.ipynb output/100_transforms/120_data_cleaning.ipynb
poetry run papermill --cwd src/notebooks/200_models src/notebooks/200_models/200_random_forest.ipynb output/200_models/200_random_forest.ipynb
