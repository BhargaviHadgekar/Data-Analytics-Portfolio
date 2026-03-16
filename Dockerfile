# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your project
COPY . /app

# Install system dependencies for pyodbc
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    libpq-dev \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

# Default command
CMD ["python", "-m", "unittest", "discover", "-s", "./Student_Database_System", "-p", "test_student_grade.py"]