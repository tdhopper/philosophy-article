all: deploy

.PHONY: deploy
deploy:
	STATIC_DEPS=true pip3 install -U python-twitter requests -t .
	serverless deploy

.PHONY: clean
clean:
	git clean -fd
