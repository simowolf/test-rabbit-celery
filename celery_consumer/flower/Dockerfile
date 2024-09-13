FROM python:3.11

WORKDIR /app

# Copy dependencies
COPY requirements.txt /app/requirements.txt

# Install Flower
RUN pip install -r requirements.txt
RUN pip install flower

COPY . /app/

# Run Flower, connecting to RabbitMQ broker
ENTRYPOINT ["celery", "-A", "tasks",  "flower", "--broker=amqp://user:password@rabbitmq:5672//", "--port=5555", "--broker-api=\"http://user:password@rabbitmq:15672/api/\""]
