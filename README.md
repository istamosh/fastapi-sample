PS: make sure you are on this directory first.

### Dockerfile
Build the image (make sure to uncomment the line starting with CMD):
`sudo docker build -t fastapi-app .`

View the image:
`sudo docker images fastapi-app`

Run the image:
`sudo docker run -p 8000:8000 fastapi-app`

Run the image detached:
`sudo docker run -d -p 8000:8000 fastapi-app`

Stop the image:
`sudo docker stop image_name`

### Docker Compose
Build and compose the container detached:
`sudo docker compose up --build -d`

Stop the container:
`sudo docker compose down`

Check the log of the container:
`sudo docker logs container_name`

Wipe the postgres database clean:
`sudo docker stop database-service`
`sudo docker compose down`
`sudo docker volume list`
`sudo docker volume rm volume-name`