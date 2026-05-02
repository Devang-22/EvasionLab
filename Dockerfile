# Use a lightweight python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the API port
EXPOSE 5000

# Run with Gunicorn for better performance than the default Flask dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]