IMAGE_NAME=animal-identification-app:latest
DEPLOYMENT_FILES=k8s/deployment.yaml k8s/service.yaml
NAMESPACE_FILE=k8s/namespace.yaml
NAMESPACE=default


all: build load apply

build:
	./build.sh

load:
	./deploy.sh

apply:	
	kubectl apply -f $(NAMESPACE_FILE)
	kubectl apply -f $(DEPLOYMENT_FILES) --namespace=$(NAMESPACE)

delete:
	kubectl delete -f $(DEPLOYMENT_FILES) --namespace=$(NAMESPACE)

restart:
	kubectl rollout restart deployment/animal-identification-app --namespace=$(NAMESPACE)

status:
	kubectl get pods,svc --namespace=$(NAMESPACE)

rollback:
	./scripts/rollback.sh

.PHONY: all build load deploy delete restart status
