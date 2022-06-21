# alphavantage-demo
Alphavantage-demo on how to display NDAYS of information from a certain stock symbol. This is currently set to work locally.

## Pre-requisites
You will need the following installed:
- helm
- kubernetes cluster
- docker

## Getting started
The first step is to build the image.
```
cd alphavantage-demo
docker build -t [tag] .
```

## NGINX
Minikube: use the following command to enable ingress
```
minikube addons enable ingress
```
Using Docker Destop: For us to have an ingress to work locally, you will need NGINX running. This can be simply installed with Helm by running the following command:
```
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```

## Alphavantage-app
```
cd charts/alphavantage
helm upgrade --install [chart-name] -f values.yaml . --namespace=[namespace] --create-namespace --set image=[image_name_tag]
```
`image_name_tag` can be found from the docker build tag you placed.  
Once this has been setup, you should be able to navigate to `http://alphavantage.local` and see the results for NDAYS and the average close value for all those days.  
NOTE: for `https://alphavantage.local` to work as well, you will need to add this to your /etc/hosts file, so `127.0.0.1 alphavantage.local`

## Monitoring
A simple prometheus scraping can be found under http://alphavantage.local/metrics 

### About alphavantage-demo chart
Templates containes all the definitions, including ConfigMap and Secrets. Currently the secret value is set in base64, but this could be changed to use a secret provider like Vault. The values for ConfigMap and name of the ingress can be changed in the values.yaml file. Image name can also be set in values.yaml file