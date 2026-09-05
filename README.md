A backend project that demonstrates centralized API routing, authentication, request handling, and cloud-oriented deployment using Python and FastAPI.

## Overview

An API gateway can provide a single entry point for client applications and handle common concerns such as authentication, routing, validation, and monitoring.

This project implements these concepts using FastAPI and supporting infrastructure.

## Features

- API gateway architecture
- REST API routing
- JWT authentication
- Request validation
- Rate limiting
- Redis caching
- NGINX reverse proxy
- Health checks
- Centralized logging
- Docker containerization
- Kubernetes deployment configuration
- GitHub Actions CI/CD

## Tech Stack

### Backend
- Python
- FastAPI

### Authentication
- JWT
- Authentication middleware

### Database & Cache
- PostgreSQL
- Redis

### Infrastructure
- NGINX
- Docker
- Kubernetes

### DevOps
- GitHub Actions
- CI/CD

### Monitoring
- Prometheus
- Grafana

## Architecture

Client
   ↓
NGINX Reverse Proxy
   ↓
FastAPI API Gateway
   ↓
Authentication & Validation
   ↓
Backend Services
   ↓
PostgreSQL / Redis
   ↓
Monitoring
API Endpoints
Login
POST /api/v1/auth/login
Validate Token
GET /api/v1/auth/validate
Health Check
GET /health
Authentication Flow
Client
  ↓
Login
  ↓
JWT Token
  ↓
API Request
  ↓
Token Validation
  ↓
Authorized Request
Running Locally
Clone the repository
git clone https://github.com/Sreejaatte/cloud-native-api-gateway.git
cd cloud-native-api-gateway
Install dependencies
pip install -r requirements.txt
Run with Docker Compose
docker compose up --build

The API can then be accessed through the configured local port.

Project Structure
app/
kubernetes/
nginx/
Dockerfile
docker-compose.yml
requirements.txt

Future Improvements

Add more backend services
Improve authentication flows
Add distributed tracing
Improve rate limiting
Expand monitoring
Add additional API gateway features
License

MIT
