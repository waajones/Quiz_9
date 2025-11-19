FROM python:3.12-slim

WORKDIR /app

# Copy and install requirements
COPY req/requirements.txt ./req/requirements.txt
RUN pip install --no-cache-dir -r req/requirements.txt

COPY analyzer.py ./analyzer.py
COPY test_analyzer.py ./tests/test_analyzer.py

# Make sure python imports modules from /app
ENV PYTHONPATH=/app

# Run tests by default
CMD ["pytest", "-q"]
