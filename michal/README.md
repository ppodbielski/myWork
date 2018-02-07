docker build -f Django_Server -t django/score_app:01 .
docker build -f Celery_Worker -t django/celery_worker:01 .
docker build -f Celery_Beat -t django/celery_beat:01 .

docker network create django_network
docker run -d --hostname my-rabbit --name rabbit-server -p 15672:15672 --network django_network rabbitmq:3.7-management
docker run -d  -p 8000:8000 --name=web --network django_network -t django/score_app:02
docker run -d --name=celery_w --network django_network -t django/celery_worker:01
docker run -d --name=celery_b --network django_network -t django/celery_beat:01



