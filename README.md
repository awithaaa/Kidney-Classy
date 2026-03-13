# Kidney-Classy

## Project Description

**Kidney-Classy** is an AI-based system designed to classify kidney diseases from medical images using deep learning. The project implements a complete machine learning workflow including data ingestion, model training, evaluation, and deployment through a web application.

The system leverages **TensorFlow/Keras** for building the deep learning model, **MLflow** for experiment tracking, and **DVC (Data Version Control)** for managing datasets and pipeline stages. A **Flask API** is used to provide endpoints for training and prediction, making it easy to interact with the model.

---

## Key Features

- Deep learning model for kidney disease image classification
- End-to-end machine learning pipeline
- Experiment tracking using MLflow
- Data and pipeline versioning with DVC
- REST API built with Flask
- Simple web interface for interaction

---

## Technology Stack

- **Python**
- **TensorFlow / Keras**
- **Flask**
- **MLflow**
- **DVC**
- **NumPy / Pandas**
- **OpenCV**

---

## Project Setup

### 1. Clone the Repository

```bash
https://github.com/awithaaa/Kidney-Classy
cd Kidney-Classy
```

### 2. Create a Conda Environment

```bash
conda create -n kidney python=3.13 -y
conda activate kidney
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Running the Project

Before using the prediction endpoint, the model must be trained.

### Train the Model

Trigger the training pipeline through the API:

```bash
curl -X POST http://localhost:8080/train
```

This command runs the training pipeline configured with DVC and logs experiments using MLflow.

---

### Start the Application

```bash
python app.py
```

Once the server starts, open the following address in your browser:

```
http://localhost:8080
```

---

## API Endpoints

| Endpoint   | Method | Description                            |
| ---------- | ------ | -------------------------------------- |
| `/`        | GET    | Loads the web interface                |
| `/train`   | POST   | Runs the training pipeline             |
| `/predict` | POST   | Upload an image and receive prediction |

---

## Machine Learning Pipeline

The Kidney-Classy project follows a structured ML pipeline consisting of several stages:

1. **Data Ingestion**
   Collects and prepares the dataset required for training.

2. **Base Model Preparation**
   Defines the deep learning architecture used for classification.

3. **Model Training**
   Trains the neural network using the processed dataset.

4. **Model Evaluation**
   Evaluates model performance and records metrics using MLflow.

---

## Experiment Tracking

All training experiments are logged using **MLflow**, allowing you to track:

- Training parameters
- Model metrics
- Model versions
- Experiment history

---

## Data Version Control

This project uses **DVC** to manage datasets and pipeline stages. It helps maintain reproducibility and version control for machine learning workflows.

---
