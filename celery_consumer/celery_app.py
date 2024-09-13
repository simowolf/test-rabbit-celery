from celery import Celery

app = Celery('rabbitmq_celery_app', broker='pyamqp://user:password@rabbitmq:5672//')

app.conf.task_acks_late = True
app.conf.broker_transport_options = {'confirm_publish': True}
app.conf.result_backend = None
