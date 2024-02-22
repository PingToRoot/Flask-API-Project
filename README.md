# REST API Project

A Flask application implementing JWT authentication and rate limiting, containerized with Docker for easy deployment in a Kubernetes environment. This project is designed to serve as a secure and scalable backend API.

I did this project to gain a deeper understanding of Python libraries as well as get exposure to Kubernetes and Docker.

## Installation

Before installation, ensure you have Docker installed on your machine. If you're planning to deploy using Kubernetes, make sure you have `kubectl` configured for your Kubernetes cluster.

Clone the repository to your local machine:

```bash
git clone https://github.com/pingtoroot/flask-api-project.git
cd flask-api-project
```

Build the Docker image:

```bash
docker build -t your_project_name .
```

## Usage

To run the application locally using Docker:

```bash
docker run -p 5000:5000 your_project_name
```

The API can be accessed at http://localhost:5000.

## Endpoints

- **GET /** - Welcome message (public).
- **POST /login** - Authenticates user and returns a JWT (public).
- **GET /protected** - A protected route that requires a valid JWT to access (protected).

## Example Requests

### Logging In:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"test", "password":"test"}' http://localhost:5000/login
```

### Acessing Protected Route:

Use the token received from **'/login'** in the Authorisathion header:

```bash
curl -H "Authorization: Bearer <TOKEN_HERE>" http://localhost:5000/protected
```

## Deploying to Kubernetes

Ensure your Kubernetes cluster is running and kubectl is configured correctly. Apply the Kubernetes configurations:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## License

This project is licensed under the MIT License.
