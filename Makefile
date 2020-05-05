#!make
include .env
export $(bash sed 's/=.*//' env)

start:
	export SSH_USR=$(SSH_USR) \
	SSH_PWD=$(SSH_PWD) \
	SSH_HOST=$(SSH_HOST) \
	&& python3 app.py

install:
	pip3 install -r requirements.txt