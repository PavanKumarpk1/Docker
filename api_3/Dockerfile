# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
# Create a requirements.txt with: fastapi, uvicorn
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API script
COPY main.py .

# Expose the port the API runs on
EXPOSE 8003

# Command to run the application
CMD ["python", "main.py"]