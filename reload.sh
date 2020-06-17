#!/bin/bash


cd /home/saito/Dean-of-Students/
sudo git pull
sudo docker stop dosb
sudo docker rm dosb
sudo docker build -t dosb .
sudo docker run -d --name dos dosb
