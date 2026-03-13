# Kidney-Classy

AI-powered kidney disease classification using deep learning for automated diagnosis. Project integrates MLflow for experiment tracking, DVC for version controlling, providing a robust pipeline to evaluate kidney health and detect potential conditions.

# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/awithaaa/Kidney-Classy
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.13 -y
```

```bash
conda activate kidney
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up you local host and port
```

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd

- mlflow ui

### dagshub

[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI= \
MLFLOW_TRACKING_USERNAME= \
MLFLOW_TRACKING_PASSWORD= \
python script.py

Run this to export as env variables:

```bash

set MLFLOW_TRACKING_URI=your_uri

set MLFLOW_TRACKING_USERNAME=your_username

set MLFLOW_TRACKING_PASSWORD=your_password

```
