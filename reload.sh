#!/bin/bash


cd /home/saito/Dean-of-Students/
sudo git pull
sudo docker stop dos
sudo docker rm dos
sudo docker build -t dos .
sudo docker run -d --name dos dos
