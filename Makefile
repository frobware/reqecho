
REPO ?= frobware/reqecho

build:
	docker build . -t $(REPO)

push:
	docker push $(REPO)
