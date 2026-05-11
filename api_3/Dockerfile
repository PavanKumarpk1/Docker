FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Ensure the database file exists and has permissions
RUN touch db.json && chmod 666 db.json

EXPOSE 8003

# Run the app
CMD ["python", "main.py"]
