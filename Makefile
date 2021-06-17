build-flask:
	cd flask_app &&\
	docker build -t flask-app:latest -f ./flask-service.dockerfile . &&\
	cd ..

build-jina:
	cd jina_app &&\
	docker build -t jina-app:latest -f ./jina.dockerfile . &&\
	cd ..

deploy-all:
	kubectl apply -f k8s/deployment_flask.yaml &&\
	kubectl apply -f k8s/service_flask.yaml &&\
	kubectl apply -f k8s/configmap.yaml &&\
	kubectl apply -f k8s/deployment_gateway.yaml &&\
	kubectl apply -f k8s/deployment_pod0.yaml &&\
	kubectl apply -f k8s/deployment_pod1.yaml &&\
	kubectl apply -f k8s/service_gateway.yaml &&\
	kubectl apply -f k8s/service_pod0.yaml &&\
	kubectl apply -f k8s/service_pod1.yaml

run-kube:
	kubectl apply -f deployment.yaml

minikube-run:
	minikube start --vm-driver=hyperkit --memory 5000 &&\
	minikube mount ./:/workdir

