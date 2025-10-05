# Dockerfile for NASA Space Apps Project

# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Environment variable placeholder for OpenAI API key
# Actual key will be injected at runtime
ENV OPENAI_API_KEY=""

# Default command to run your Python script
CMD ["python", "main.py"]
