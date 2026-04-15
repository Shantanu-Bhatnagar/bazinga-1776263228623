from fastapi import FastAPI, HTTPException
from typing import Union

app = FastAPI(
    title="MyProject Calculator API",
    description="A simple calculator API built with FastAPI.",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
async def read_root():
    """
    Welcome message for the Calculator API.
    """
    return {"message": "Welcome to MyProject Calculator API! Use /docs for API documentation."}

@app.get("/add", tags=["Operations"])
async def add_numbers(num1: Union[float, int], num2: Union[float, int]):
    """
    Adds two numbers.
    - **num1**: The first number.
    - **num2**: The second number.
    """
    result = num1 + num2
    return {"operation": "add", "num1": num1, "num2": num2, "result": result}

@app.get("/subtract", tags=["Operations"])
async def subtract_numbers(num1: Union[float, int], num2: Union[float, int]):
    """
    Subtracts the second number from the first.
    - **num1**: The number to subtract from.
    - **num2**: The number to subtract.
    """
    result = num1 - num2
    return {"operation": "subtract", "num1": num1, "num2": num2, "result": result}

@app.get("/multiply", tags=["Operations"])
async def multiply_numbers(num1: Union[float, int], num2: Union[float, int]):
    """
    Multiplies two numbers.
    - **num1**: The first number.
    - **num2**: The second number.
    """
    result = num1 * num2
    return {"operation": "multiply", "num1": num1, "num2": num2, "result": result}

@app.get("/divide", tags=["Operations"])
async def divide_numbers(num1: Union[float, int], num2: Union[float, int]):
    """
    Divides the first number by the second.
    Handles division by zero.
    - **num1**: The dividend.
    - **num2**: The divisor.
    """
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    result = num1 / num2
    return {"operation": "divide", "num1": num1, "num2": num2, "result": result}
