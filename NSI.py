import streamlit as st
import math

# Title and instructions
st.title("Scientific Calculator")
st.write("Select an operation and enter the required values.")

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        return "Logarithm undefined for non-positive values"
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# User selects an operation
operation = st.selectbox("Choose an operation", [
    "Addition", "Subtraction", "Multiplication", "Division", 
    "Power", "Square Root", "Logarithm", "Sine", "Cosine", "Tangent"
])

# Depending on the operation, display the necessary input fields
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    x = st.number_input("Enter the first number", value=0.0)
    y = st.number_input("Enter the second number", value=0.0)

    if st.button("Calculate"):
        if operation == "Addition":
            result = add(x, y)
        elif operation == "Subtraction":
            result = subtract(x, y)
        elif operation == "Multiplication":
            result = multiply(x, y)
        elif operation == "Division":
            result = divide(x, y)
        elif operation == "Power":
            result = power(x, y)
        
        st.write("Result:", result)

elif operation == "Square Root":
    x = st.number_input("Enter a number", value=0.0)

    if st.button("Calculate"):
        result = sqrt(x)
        st.write("Result:", result)

elif operation == "Logarithm":
    x = st.number_input("Enter the number", value=1.0)
    base = st.number_input("Enter the base (default is 10)", value=10.0)

    if st.button("Calculate"):
        result = logarithm(x, base)
        st.write("Result:", result)

elif operation in ["Sine", "Cosine", "Tangent"]:
    x = st.number_input("Enter the angle in degrees", value=0.0)

    if st.button("Calculate"):
        if operation == "Sine":
            result = sine(x)
        elif operation == "Cosine":
            result = cosine(x)
        elif operation == "Tangent":
            result = tangent(x)
        
        st.write("Result:", result)
