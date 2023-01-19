from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

app.autodiscover_tasks()

@app.task
def add(x, y):
    return x + y