# base image - this is what I have installed
FROM python:3.10.10-slim-buster

# environmnet
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/

# non-root user to run the application
RUN groupadd -g 1001 appuser && useradd -r -u 1001 -g appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

# expose the port the app runs on
EXPOSE 8080

# run the app
CMD ["python", "app.py"]
