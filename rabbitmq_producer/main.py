from producer import send_message

if __name__ == '__main__':
    # Messaggio da inviare
    message = '{"task": "tasks.process_message", "args": ["Hi RabbitMQ!!"], "kwargs": {}}'

    # Chiama la funzione per inviare il messaggio
    send_message(message)

    # Puoi cambiare il messaggio o la coda qui, ad esempio:
    # send_message("Un altro messaggio", queue="un_altra_coda")
