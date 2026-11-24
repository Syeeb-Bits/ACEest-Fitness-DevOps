# ACEest Fitness & Gym – DevOps Assignment 2

## Project Overview
A Flask-based fitness workout tracker demonstrating DevOps practices.

## Technologies
- Python and Flask
- Pytest
- Git and GitHub
- Jenkins CI/CD
- Docker and Docker Hub
- SonarQube
- Kubernetes and Minikube

## Application Features
- Add workouts
- Record workout duration
- View workout history
- Health endpoint: /health

## Run Locally
pip install -r requirements.txt
python application/app.py

## Run Tests
pytest -v

## Docker
docker build -t aceest-fitness:jenkins .
docker run -p 5000:5000 aceest-fitness:jenkins

## Kubernetes
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/canary.yaml

## Deployment Strategies Demonstrated
- Rolling Update
- Rollback
- Canary deployment (separate canary instance)

## Repository
https://github.com/Syeeb-Bits/ACEest-Fitness-DevOps
