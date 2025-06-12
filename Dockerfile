# Use Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
