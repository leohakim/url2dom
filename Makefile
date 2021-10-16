
build:
	docker build -t url2dom .

run:
	docker run -v $(PWD):/usr/src/app --name url2dom -p 8001:80 url2dom

