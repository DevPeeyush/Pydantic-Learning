# Pydantic

## Workflow of Pydantic

### 1. Define a Pydantic Model

Define a Pydantic model that represents the **ideal schema** of the data.

- This includes the expected fields, their types, and any validation constraints (e.g., `gt=0` for positive numbers).

### 2. Instantiate the Model with Raw Input Data

Instantiate the model with raw input data (usually a dictionary or JSON-like structure).

- Pydantic will automatically **validate the data** and **coerce it into the correct Python types** (if possible).
- If the data doesn't meet the model's requirements, Pydantic raises a `ValidationError`.

### 3. Pass the Validated Model Object

Pass the validated model object to functions or use it throughout your codebase.

- This ensures that every part of your program works with **clean, type-safe, and logically valid data**.
