#!/bin/sh

sudo docker-compose -f ./test1/docker-compose1.yaml up --scale worker=3 &
sudo docker-compose -f ./test2/docker-compose2.yaml up --scale worker=3 &
sudo docker-compose -f ./test3/docker-compose3.yaml up --scale worker=3 &
sudo docker-compose -f ./test4/docker-compose4.yaml up --scale worker=3 &
sudo docker-compose -f ./test5/docker-compose5.yaml up --scale worker=3 &
sudo docker-compose -f ./test6/docker-compose6.yaml up --scale worker=3 &
sudo docker-compose -f ./test7/docker-compose7.yaml up --scale worker=3 &