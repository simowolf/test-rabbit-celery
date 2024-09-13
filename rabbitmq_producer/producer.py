import pika


def send_message(message: str, queue: str = 'hello'):
    credentials = pika.PlainCredentials('user', 'password')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost', 5672, '/', credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue=queue, durable=True)

    for index in range(50):
        channel.basic_publish(
            exchange='',
            routing_key=queue,
            body= f'{{"task": "tasks.process_message", "args": ["Hi RabbitMQ id {index}"], "kwargs": {{}}}}', # message,
            properties=pika.BasicProperties(
                content_type='application/json',
                delivery_mode=2,
            ))

        print(f" [x] Inviato '{message}' alla coda '{queue}'")

    connection.close()