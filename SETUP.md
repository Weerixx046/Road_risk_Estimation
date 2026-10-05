# Contributing to UMA Road Risk Estimation

## Getting Started

Clone the repository to your local machine:

```bash
git clone https://github.com/Weerixx046/Road_risk_Estimation.git
cd Road_risk_Estimation
```

## Development Setup

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Download the Model

Before running the application, download the required model files and place them in the `models` directory.

The project structure should look like:

```text
Road_risk_Estimation/
├── backEnd/
├── models/
│   └── <model-file>
├── requirements.txt
└── ...
```

> **Note:** The application requires the model files in the `models` directory to run correctly.

## Running the Application

Navigate to the `backEnd` directory:

```bash
cd backEnd
```

Start the application using Uvicorn:

```bash
uvicorn main:app --reload
```

After the server starts, the application will be available at:

* **Web API:** http://127.0.0.1:8000
* **Swagger UI:** http://127.0.0.1:8000/docs

The Swagger UI can be used to view and test the available API endpoints.

## Code Style

The project follows standard Python coding conventions based on **PEP 8**.

Please keep the code clean, readable, and properly commented where necessary.
