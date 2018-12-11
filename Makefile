ORG=mbatchkarov
PROJ=k8s-sqs-autoscaler
VERSION=1.0.1

.PHONY=release
build:
	docker build -t ${ORG}/${PROJ}:${VERSION} -f Dockerfile .

push:
	docker push ${ORG}/${PROJ}:${VERSION}

all: build push