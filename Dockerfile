FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application into the container
COPY . /app

# Default command (can be overridden by compose)
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]