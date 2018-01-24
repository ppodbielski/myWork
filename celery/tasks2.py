from celery import Celery

app = Celery('tasks2', backend='rpc://', broker='pyamqp://')

@app.task
def add2(x,y):
    return x + y