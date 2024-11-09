# BDI-Assignment

# 3-Tier Web Application Kubernetes Deployment

I have created Docker images for a simple 3-tier web application using Dockerfiles for each component and pushed these images to Docker Hub for easy access and deployment.

# 3-Tier Web Application Docker Images

Nginx Web Server - evilvampire/bdiui:v1,
Flask Application Server - evilvampire/bdiapi:v1,
PostgreSQL Database - evilvampire/bdidb:v1,

# kubernetes folder contains the Kubernetes deployment configuration for a 3-tier web application.

## Prerequisites

* Kubernetes cluster (e.g., Minikube, )
* Docker images for Nginx, Flask, and Postgres

## Deployment

1. Apply the deployment configuration: `kubectl apply -f deployment.yaml`
2. Apply the service configuration: `kubectl apply -f service.yaml`
3. Apply the ingress configuration: `kubectl apply -f ingress.yaml`
4. Apply the configmap configuration: `kubectl apply -f configmap.yaml`
5. Apply the secrets configuration: `kubectl apply -f secrets.yaml`

## Verification

1. Check the deployment status: `kubectl get deployments`
2. Check the pod status: `kubectl get pods`
3. Check the service status: `kubectl get svc`
4. Access the application: `curl http://hello-world.example.com`
5. Access the application through clusterip or Nodeport also.
