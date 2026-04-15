# MyProject Calculator API

A simple calculator API built with FastAPI.

## Description

This project provides a basic set of arithmetic operations (addition, subtraction, multiplication, division) exposed via a RESTful API.

## Features

-   Addition of two numbers
-   Subtraction of two numbers
-   Multiplication of two numbers
-   Division of two numbers (with zero division handling)
-   Interactive API documentation (Swagger UI)

## Getting Started

### Prerequisites

-   Python 3.8+
-   pip (Python package installer)
-   (Optional) Docker and Docker Compose

### Local Development

1.  **Clone the repository:**
    bash
    git clone <repository-url>
    cd MyProject
    

2.  **Create a virtual environment (recommended):**
    bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    

3.  **Install dependencies:**
    bash
    pip install -r requirements.txt
    

4.  **Run the application:**
    bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    

    The API will be available at `http://127.0.0.1:8000`.
    Access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

### Running with Docker

1.  **Build the Docker image:**
    bash
    docker build -t myproject-calculator .
    

2.  **Run the Docker container:**
    bash
    docker run -p 8000:8000 myproject-calculator
    

    The API will be available at `http://localhost:8000`.

### Running with Docker Compose

1.  **Build and run the services:**
    bash
    docker-compose up --build
    

    The API will be available at `http://localhost:8000`.
    To stop the services:
    bash
    docker-compose down
    

## API Endpoints

-   **GET /**: Welcome message.
-   **GET /add?num1={float}&num2={float}**: Adds two numbers.
    -   Example: `/add?num1=5&num2=3`
-   **GET /subtract?num1={float}&num2={float}**: Subtracts `num2` from `num1`.
    -   Example: `/subtract?num1=10&num2=4`
-   **GET /multiply?num1={float}&num2={float}**: Multiplies two numbers.
    -   Example: `/multiply?num1=6&num2=7`
-   **GET /divide?num1={float}&num2={float}**: Divides `num1` by `num2`.
    -   Example: `/divide?num1=20&num2=5`
    -   Handles division by zero with a 400 error.

## Technologies Used

-   [FastAPI](https://fastapi.tiangolo.com/)
-   [Uvicorn](https://www.uvicorn.org/)
-   Python 3

## License

This project is open source and available under the MIT License.
