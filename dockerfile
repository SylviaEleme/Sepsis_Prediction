FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the application and supporting directories
COPY app/ .            
COPY Models/ /app/Models
COPY Data/ /app/Data

# Expose the port for FastAPI
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "finalapi:app", "--host", "0.0.0.0", "--port", "8000"]