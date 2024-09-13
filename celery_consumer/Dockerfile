FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/

# Default entrypoint for Celery worker
ENTRYPOINT ["celery", "-A", "tasks", "worker", "--loglevel=info"]

# Default arguments, if none are passed during container execution
CMD ["--hostname=worker-default", "-Q", "default"]