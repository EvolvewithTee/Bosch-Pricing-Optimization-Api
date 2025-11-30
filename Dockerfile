
# Use a small official Python image
FROM python:3.10-slim

# Make Python print logs immediately
ENV PYTHONUNBUFFERED=1

# All files will live in /app inside the container
WORKDIR /app

# (Optional) helps compile some Python packages
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Install Python packages first (faster builds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your API code and model files
COPY app.py .
COPY pricing_model.pkl .
COPY scaler.pkl .

# App Runner will connect to this port
EXPOSE 8080

# Start the Flask app with Gunicorn on port 8080
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]
