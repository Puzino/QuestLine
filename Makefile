SHELL := /bin/bash

cli:
	python3 client/cli.py

serv:
	python3 server/run_server.py