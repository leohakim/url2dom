#!/bin/sh
gunicorn --chdir app app:app -w 2 --threads 2 --timeout 120 -b 0.0.0.0:80 --reload