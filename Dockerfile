# Use Debian bookworm (stable) as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Python and system dependencies for video processing
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and assets
COPY app.py .
COPY assets/ ./assets/

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expose the port Gradio will run on
EXPOSE 7860

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import requests; requests.get('http://localhost:7860/healthz')" || exit 1

# Run the application
CMD ["python3", "app.py"]
