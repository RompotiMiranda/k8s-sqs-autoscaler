ORG=mbatchkarov
PROJ=k8s-sqs-autoscaler

.PHONY=release
build:
	docker build -t ${ORG}/${PROJ}:`git rev-parse HEAD` -f Dockerfile .

push:
	docker push ${ORG}/${PROJ}:`git rev-parse HEAD`

all: build push