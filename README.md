# Microservice App

## Services
### Frontend Service

The frontend service is responsible for building and running the frontend application. It has the following configuration:

* Build: Specifies the build context as ./front and the Dockerfile as frontend.Dockerfile. This means the frontend service will be built using the files present in the ./front directory.
* Ports: Maps port 3000 of the container to port 3000 of the host machine. This allows accessing the frontend application from http://localhost:3000.
* Depends On: Declares a dependency on the backend service. This ensures that the backend service is started before the frontend service.

### Backend Service

The backend service is responsible for building and running the backend application. It has the following configuration:

* Build: Specifies the build context as ./api and the Dockerfile as backend.Dockerfile. This means the backend service will be built using the files present in the ./api directory.
* Ports: Maps port 8000 of the container to port 8000 of the host machine. This allows accessing the backend application from http://localhost:8000.

## Running the Application

To run the application, make sure you have Docker and Docker Compose installed on your system. Navigate to the directory where the docker-compose.yml file is located.

In the terminal, run the following command:

```bash
docker-compose up --build
```

This command will build the Docker images for the frontend and backend services and start the containers. You can access the frontend application in your web browser at http://localhost:3000, and the backend application at http://localhost:8000.

To stop the containers, use Ctrl+C in the terminal, and then run the following command:

```bash
docker-compose stop
```

