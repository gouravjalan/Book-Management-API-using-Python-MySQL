# Base image (Python installed)
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first (for caching)
COPY required_library.txt .

# Install dependencies
RUN pip install --no-cache-dir -r required_library.txt

# Copy remaining project files
COPY . .

# Expose API port
EXPOSE 8000

# Command to run your application
CMD ["python", "main.py"]