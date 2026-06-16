# Todo app

FastAPI web server that reads the port from the `PORT` environment variable and prints the used port on startup.

## Setup

```bash
# build
cd the_project
docker build -t the_project:1.5 .

# testing
docker run -p 3000:3000 the_project:1.5
docker run -p 3000:4000 -e PORT=4000 the_project:1.5

# cluster is already created and configured

# deploy local image
k3d image import the_project:1.5

# create deployment
kubectl apply -f manifests/deployment.yaml
```

## Access

```bash
kubectl get po  # search for the todo pod
kubectl port-forward todo-app-57685974-gk2dm 3003:3000 # for example
```

Open http://localhost:3003 in a browser.
