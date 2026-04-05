FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "unittest", "discover", "-s", "./Student_system", "-p", "test_Student.py"]