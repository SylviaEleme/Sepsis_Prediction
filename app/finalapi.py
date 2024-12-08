from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
import joblib
import uvicorn
import io

# Initialize FastAPI app
app = FastAPI(
    title="Sepsis Prediction API",
    description="This API predicts Sepsis using trained models.",
)

# Define paths to the models
MODEL_PATHS = {
    "RandomForest": "Models/RandomForest_Sepssis_Model.pkl"
}

# Load the models
models = {}
for model_name, path in MODEL_PATHS.items():
    try:
        models[model_name] = joblib.load(path)
    except Exception as e:
        raise RuntimeError(f"Failed to load model '{model_name}' from '{path}'. Error: {e}")

# Define required features for each model
REQUIRED_COLUMNS = {
    "RandomForest": ["PRG", "PL", "PR", "SK", "TS", "M11", "BD2", "Age", "Insurance"]
}

@app.get("/")
async def root_endpoint():
    return {"Message": "Welcome to the Sepsis Prediction API"}

@app.post("/predict")
async def predictor(model: str, file: UploadFile = File(...)):
    """
    Accepts a model name and a file with input data.
    Returns predictions for each row in the file.
    """
    # Check if the specified model exists
    if model not in models:
        raise HTTPException(
            status_code=400,
            detail=f"Model '{model}' not found. Available models: {list(models.keys())}",
        )

    # Load the uploaded CSV file
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading the file: {e}")

    # Retrieve required columns
    required_columns = REQUIRED_COLUMNS.get(model, None)
    if required_columns is None:
        raise HTTPException(
            status_code=500,
            detail=f"Required columns for model '{model}' are not defined.",
        )

    # Ensure the uploaded file has the required columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise HTTPException(
            status_code=400,
            detail=f"The uploaded file is missing required columns: {missing_columns}",
        )

    # Filter the data to only required columns
    df = df[required_columns]

    # Retrieve the model
    model_used = models[model]

    # Make predictions
    try:
        predictions = model_used.predict(df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during prediction: {e}")

    # Return the results
    return {
        "model_used": model,
        "predictions": predictions.tolist(),
    }

if __name__ == "__main__":
    uvicorn.run("finalapi:app", host="0.0.0.0", port=8000)

