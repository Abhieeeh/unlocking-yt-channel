# YouTube Growth Analysis Project

This project explores metadata of YouTube videos to identify factors contributing to high engagement and virality. The analysis focuses on understanding the relationship between various features of videos and their performance metrics.

## Folder Structure
- `data/`: CSV files containing video metadata
- `notebooks/`: Jupyter Notebooks for EDA and modeling
- `src/`: Python scripts for reusable functions
- `output/`: Graphs and predictions

## What's Inside
- Sample dataset of video metadata
- Plot: Title length vs Views
- Feature: Is video viral (views > 1M)

## Next Steps
- Build EDA notebook to analyze features
- Train a classifier to predict virality
- Optimize model performance and validate results

## Installation
To set up the project, install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Usage
1. Load the dataset using the functions in `src/data_loader.py`.
2. Perform exploratory data analysis in `notebooks/01_eda.ipynb`.
3. Build and evaluate models in `notebooks/02_modeling.ipynb`.
4. Check the output folder for generated plots and predictions.