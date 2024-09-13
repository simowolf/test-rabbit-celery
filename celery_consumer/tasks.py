import time
from celery_app import app
import random

@app.task(bind=True, acks_late=True, max_retries=5, default_retry_delay=10)
def process_message(self, message):
    """
    """
    try:
        test_fail = bool(random.getrandbits(1))
        print(f" [x] Processing message: {message}")
        if test_fail:
            raise Exception('Random Exception')

        time.sleep(20)

        print(f" [x] Task completed for message: {message}")

    except Exception as e:
        print(f" [!] Error processing message: {message}, Error: {e}")

        raise self.retry(exc=e)