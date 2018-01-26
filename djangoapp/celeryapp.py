from celery import Celery
import requests
import wget
#app = Celery('tasks', broker='pyamqp://guest@localhost//')
user = 'paszko'
pattern = 'pkt'
url = 'https://rozwal.to/profile/' + user


#@app.task
def get_page_score():
    response = requests.get(url)

    line = [l for l in response.text.split('\n') if pattern in l]
    number = [int(l) for l in str(line).split() if l.isdigit()]
    print(number)


if __name__ == '__main__':
    get_page_score()