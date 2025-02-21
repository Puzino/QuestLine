SHELL := /bin/bash

cli:
	python3 client/run_client.py

serv:
	python3 server/run_server.py