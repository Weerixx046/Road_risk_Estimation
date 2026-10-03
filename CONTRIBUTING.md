# Contributing to UMA Road Risk Estimation

## Getting Started

Clone the repository to your local machine:

```bash
git clone https://github.com/Weerixx046/Road_risk_Estimation.git
cd Road_risk_Estimation
```

## Development Setup

Create and activate a Python virtual environment:

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

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
