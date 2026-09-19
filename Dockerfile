FROM python:3.12-slim

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

EXPOSE 8080

# Use gunicorn in production, not the Flask dev server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
