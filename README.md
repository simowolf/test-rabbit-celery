# test-rabbit-celery


# Steps to Set Up RabbitMQ and Celery Workers with Podman

This guide outlines the steps to set up RabbitMQ, build Celery worker and Flower images, and run them using Podman. These steps were used to run a test environment for message processing using Celery and RabbitMQ.

## Step 1: Run RabbitMQ with Management Plugin

RabbitMQ is a messaging broker that enables your Celery workers to communicate. The following command starts a RabbitMQ container with management plugins enabled.

```bash
podman run --rm -d --name rabbitmq --network rabbitmq-celery-network -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3.13-management
```

- `--rm`: Removes the container when it stops.
- `-d`: Runs the container in detached mode.
- `--network rabbitmq-celery-network`: Connects the container to the specified network for communication between services.
- `-p 5672:5672`: Exposes RabbitMQ's default messaging port.
- `-p 15672:15672`: Exposes the RabbitMQ management console.
- `-e RABBITMQ_DEFAULT_USER=user`: Sets the default RabbitMQ user.
- `-e RABBITMQ_DEFAULT_PASS=password`: Sets the default RabbitMQ password.

## Step 2: Build the Celery Worker Image

Next, we build the Celery worker Docker image using the Dockerfile located in the `celery_consumer` directory.

```bash
podman build -t celery-worker -f celery_consumer/Dockerfile .
```

- `-t celery-worker`: Tags the image as `celery-worker`.
- `-f celery_consumer/Dockerfile`: Specifies the Dockerfile location.

## Step 3: Run the Celery Worker

Run the Celery worker container, ensuring it's connected to the RabbitMQ instance you set up earlier. The worker will be responsible for processing tasks from the RabbitMQ queue.

```bash
podman run --rm -d --network rabbitmq-celery-network --name celery-worker-x localhost/celery-worker --hostname=workerx@%h -Q hello
```

- `--rm`: Removes the container after it stops.
- `--network rabbitmq-celery-network`: Connects to the RabbitMQ-Celery network.
- `--name celery-worker-x`: Names the container (`x` is the worker number, e.g., `celery-worker-1`).
- `--hostname=workerx@%h`: Sets the worker hostname dynamically based on the worker number.
- `-Q hello`: Specifies the queue name the worker listens to.

## Step 4: Build the Celery Flower Image

Celery Flower is a web-based tool for monitoring Celery workers. Build its Docker image:

```bash
podman build -t celery-flower -f celery_consumer/flower/Dockerfile .
```

- `-t celery-flower`: Tags the image as `celery-flower`.
- `-f celery_consumer/flower/Dockerfile`: Specifies the Dockerfile for building the Flower image.

## Step 5: Run the Celery Flower Monitoring Tool

Run the Celery Flower container to monitor your Celery workers via a web interface.

```bash
podman run --rm -d --network rabbitmq-celery-network -p 5555:5555 --name celery-flower localhost/celery-flower
```

- `--rm`: Removes the container after it stops.
- `--network rabbitmq-celery-network`: Connects to the RabbitMQ-Celery network.
- `-p 5555:5555`: Exposes the Flower monitoring tool on port 5555.

## Step 6: Start the Python Producer Script

Finally, run the Python producer script to start sending tasks to the RabbitMQ queue.

```bash
python rabbitmq_producer/main.py
```

This script pushes tasks to the `hello` queue, which the Celery workers will consume.

