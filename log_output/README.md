# Log-output

Prints a timestamp and UUID to stdout every 5 seconds.

## Setup

```bash
# build
cd log_output
docker build -t log-output:1.3 .

# deploy
k3d image import log-output:1.3
kubectl apply -f manifests/deployment.yaml
```


## Logs

```bash
# follow
kubectl logs -f deployment/log-output
```
