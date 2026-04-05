FROM python:3.11-slim

WORKDIR /app

COPY . /app

CMD ["python", "-m", "unittest", "discover", "-s", "./Student_system", "-p", "test_Student.py"]