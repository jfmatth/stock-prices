# Stock-prices

piku + yahooquery + django = Stock-prices


# Kubernetes work

## Docker build
```
docker build . -t jfmatth/stockprices:<tag>
```

current tag = 0.2

## Helm
```
helm install <name> kubernetes/helm 


## Updates

1/7/2024 - YahooQuery was again updated to make it work with API changes on Yahoo side.  A git push piku is all it takes to recreate the environment.

