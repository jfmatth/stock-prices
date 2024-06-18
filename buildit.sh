#! /bin/bash
repository="jfmatth/stockprices"
export tag_version=$(awk -F'\"' '/appVersion/{print $2}' kubernetes/helm/Chart.yaml)
docker build . -t $repository:$tag_version
docker push $repository:$tag_version
