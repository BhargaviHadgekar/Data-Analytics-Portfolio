# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy all project files into container
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

# Default command: run unit tests
CMD ["python", "-m", "unittest", "discover", "-s", "./Student_Database_System", "-p", "test_student_grade.py"]