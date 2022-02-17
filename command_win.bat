docker-compose down -v
docker image rm postgres:13-alpine
docker image rm webappstudent_web
docker-compose up -d