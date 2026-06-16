# Todo app

FastAPI web server that reads the port from the `PORT` environment variable and prints the used port on startup.

## Setup

```bash
# build
cd the_project
docker build -t the_project:1.2 .

# testing
docker run -p 3000:3000 the_project:1.2
docker run -p 3000:4000 -e PORT=4000 the_project:1.2

# cluster is already created and configured

# deploy local image
k3d image import the_project:1.2

# create deployment
kubectl apply -f manifests/deployment.yaml