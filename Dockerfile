FROM python:3.12-slim

# Work in /app
WORKDIR /app

# Copy and install requirements
COPY req/requirements.txt ./req/requirements.txt
RUN pip install --no-cache-dir -r req/requirements.txt

# Copy your code and tests into the image
COPY analyzer.py ./analyzer.py
COPY test_analyzer.py ./tests/test_analyzer.py

# Make sure Python can import modules from /app
ENV PYTHONPATH=/app

# Run tests by default
CMD ["pytest", "-q"]
