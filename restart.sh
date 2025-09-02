#!/bin/bash
# This script wipes docker volumes and restart detached
# do not forget to "chmod +x restart.sh" before running
sudo docker compose down -v
sudo docker compose up --build -d