---
title: "gcp docker"
date: 2017-05-01T16:28:13+09:00
lastmod: 2017-05-01T16:28:13+09:00
comments: true
category: ['']
tags: ['']
published: false
slug: gcp-docker
img:
---

<!--more-->
{{% googleadsense %}}


```
sudo apt-get update
```

```
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
```

```
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
```


```
ERROR: Couldn't connect to Docker daemon - you might need to run `docker-machine start default`.
```


以下のコマンドが必要かどうかわからない
```
docker-machine create --driver google --google-project meganii-gcp default
```


##

ubuntu上でbundle install が失敗するのはメモリ不足が原因っぽい
スワップを追加したところ、gem

bundle installが実施されないと怒られる。。。


## tips

`su`でrootになるときのパスワードがわからないと思ったら、以下のコマンドでrootになれるとのこと
```
sudo -i
```



gcloud compute instances create kenchan2 \
    --image-family cos-stable \
    --image-project cos-cloud \
    --zone us-central1-a \
    --machine-type f1-micro


## CoreOS



gcloud compute instances create kenchan_coreos \
    --image-family coreos-stable \
    --image-project coreos-cloud \
    --zone us-central1-a \
    --machine-type f1-micro

gcl


あまり良い方法ではないかもしれないけど、以下の通り、ユーザを変えてダウンロードした
```
sudo mkdir -p /opt/bin
sudo chown -R $(whoami) /opt/bin
curl -L https://github.com/docker/compose/releases/download/1.1.0/docker-compose-`uname -s`-`uname -m` > /opt/bin/docker-compose
chmod +x /opt/bin/docker-compose
sudo chown -R root /opt/bin
```


https://github.com/docker/machine/issues/652



## 参考

[How To Install and Use Docker on Ubuntu 16\.04 \| DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)
