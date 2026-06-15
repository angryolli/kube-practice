# Log-output

Prints a timestamp and UUID to stdout every 5 seconds.

## Setup

```bash
# build
cd log_output
docker build -t log-output .

# cluster
k3d cluster create -a 2
kubectl config use-context k3d-k3s-default

# deploy
k3d image import log-output
kubectl create deployment log-output --image=log-output
```

## Image pull policy

Local image only -> edit the deployment:

```bash
kubectl edit deployment log-output
```

Set `imagePullPolicy: IfNotPresent`.

## Logs

```bash
# follow
kubectl logs -f deployment/log-output
```
