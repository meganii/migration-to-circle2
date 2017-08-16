---
title: "Conoha VPSにCoreOSをインストールする"
date: 2017-04-16T21:14:51+09:00
lastmod: 2017-04-16T21:14:51+09:00
comments: true
category: ['Tech']
tags: ['Conoha','VPS']
published: true
slug: installing-coreos-with-conoha-vps
img: "/images/2017/04/conoha-api-64x.png"
---

[ConoHaのVPSにCoreOSをインストール \- Qiita](http://qiita.com/miyasakura_/items/4d81dc5fe6f9de0f0dd5)を参考に<a href="https://px.a8.net/svt/ejp?a8mat=2TGARC+63OZ02+50+4YR6O2" target="_blank" rel="nofollow">Conoha VPS</a>
<img border="0" width="1" height="1" src="https://www13.a8.net/0.gif?a8mat=2TGARC+63OZ02+50+4YR6O2" alt="">にCoreOSをインストールしました。



<!--more-->
{{% googleadsense %}}


## 手順

### 1.SSH Keyを作成しておく

pemファイルをダウンロードして、`chmod 400 20170416104656.pem`で権限を変えておき、最終的には以下の通りログインします。

```bash
ssh core@xxx.xxx.xxx.xxx -i 20170416104656.pem
```


### 2.メモリ1GB以上のプランでVPSを作成

ここではCentOSを選択しました。作成するときには「1.」作成した`SSH KEY`を選択します。

ここで初っ端からつまづいたのだが、メモリが512MBだとエラーになり進めませんでした。そういうものなのでしょうか。


### 3.サーバをシャットダウン

ISOをマウントするため、せっかく起動したサーバを停止させます。


### 4.APIユーザを作成

![APIユーザ作成](/images/2017/04/conoha-api.png)

APIユーザを作成しておきます。


### 5.conohaのISOツールをダウンロード

OSXの場合は、以下の通りコマンドを実行します。

```
$ mkdir tmp
$ cd tmp
$ curl -sL https://github.com/hironobu-s/conoha-iso/releases/download/current/conoha-iso-osx.amd64.gz | zcat > conoha-iso && chmod +x ./conoha-iso
```


### 6. ISOをダウンロード

```
./conoha-iso download -i https://stable.release.core-os.net/amd64-usr/current/coreos_production_iso_image.iso -u {userid} -p {password} -n {テナント名} -r tyo1
```

しばらくすると、下記コマンドでダウンロードしたファイルが確認できる。(今見るとやはり2015年のファイルだ・・・)

```
./conoha-iso list -u {userid} -p {password} -n {テナント名} -r tyo1
[Image1]
Name:  coreos_production_iso_image.iso
Url:   https://stable.release.core-os.net/amd64-usr/current/coreos_production_iso_image.iso
Path:  /mnt/isos/repos/tenant_iso_data/f4d7162265934927b4db72d1df18fb15/coreos_production_iso_image.iso
Ctime: Thu May 28 09:07:56 2015
Size:  169869312
```

### 7. ISOファイルをアタッチする

```
./conoha-iso insert -u {userid} -p {password} -n {テナント名} -r tyo1
```

### 8. サーバ起動

しばらくすると、コンソールからログインできるようになります。


### 9. パーティションの削除



```
sudo fdisk /dev/sda
```

- パーティション確認はp
- パーティション削除はd
- wで書き込み


### 10. `coreos-install`でセットアップ

`vim ~/cloud-config.yaml`で設定ファイルを作成します。

```yaml
#cloud-config

ssh_authorized_keys:
  - "ssh-rsa ・・・・"
```


```
sudo coreos-install -d /dev/vda -C stable -c ~/cloud-config.yaml
```

successとなったら、

`sudo reboot`で再起動します。


## 11.Image保存

もう一度同じ作業を繰り返さなくてもよいように、Image保存しておきます。

![Image保存](/images/2017/04/image-save.png)



## 補足

### CoreOSのアップデート

Current versionをダウンロードしたつもりがなぜか古いバージョンが落ちてきたので、以下のコマンドでCodeOSの最新化を行いました。

```
sudo update_engine_client -update
```

### cloud-config.yamlってどうやって更新するのか

2回目以降に以下のエラーとなる。

```
sudo coreos-install -d /dev/vda -C stable -c ~/cloud-config.yaml
(中略)
blockdev: ioctl error on BLKRRPART: Device or resource busy
```

なんでかなと思ったら、原因は下記コマンドは初回のみで、更新するときには、`/var/lib/coreos-install/user_data`のファイルを直接更新するらしい。

config fileのsyntax checkは下記のコマンドを実行して確認する。

```
sudo coreos-cloudinit -validate=true -from-file=/var/lib/coreos-install/user_data
```

syntax checkが問題なければ下記コマンドを叩いて、設定を適用する。
```
$ sudo coreos-cloudinit -from-file=/var/lib/coreos-install/user_data
```


更新した後は、`sudo reboot`で再起動する。


### ライブラリは、`/opt/bin`に入れるみたい

CoreOSでは、システム領域にはファイルの書き込みが出来ないらしいので、`/home/core/`以下か、`/opt/bin`に入れるのが流儀みたい。

そもそも、CoreOSの思想としては「アプリケーションは全てコンテナで動かすべし」というのが大前提にある。

```
curl -L https://github.com/docker/compose/releases/download/1.12.0/docker-compose-`uname -s`-`uname -m` > /opt/bin/docker-compose
chmod +x /opt/bin/docker-compose
```


### ssh周りのデフォルト設定

パスワードログインを禁止するため、ssh周りのデフォルト設定をメモしておく

```
sudo cat /etc/ssh/sshd_config
# Use most defaults for sshd configuration.
UsePrivilegeSeparation sandbox
Subsystem sftp internal-sftp
ClientAliveInterval 180
UseDNS no
```



## CoreOSでswapの設定

```
core@150-95-148-60 ~/kenchan2 $ free
             total       used       free     shared    buffers     cached
Mem:       1020680     697808     322872      66720      22372     299476
-/+ buffers/cache:     375960     644720
Swap:            0          0          0
```

```
core@150-95-148-60 ~ $ free
             total       used       free     shared    buffers     cached
Mem:       1020680     267036     753644        352      15296     154564
-/+ buffers/cache:      97176     923504
Swap:      4194300          0    4194300
```


## CoreOSの設定

https://gist.github.com/dalbani/5d88fef62b76309d0198

```
#cloud-config

coreos:
  units:
    - name: systemd-sysctl.service
      command: restart

    - name: swap-file.service
      command: start
      content: |
        [Unit]
        Description=Swap file
        [Service]
        Type=oneshot
        RemainAfterExit=true
        Environment="SWAP_FILE=/swap" "SWAP_SIZE=512m"
        ExecStart=/usr/bin/sh -c "[ -e ${SWAP_FILE} ] || (touch ${SWAP_FILE} && chattr +C ${SWAP_FILE} && fallocate -l ${SWAP_SIZE} ${SWAP_FILE} && chmod 600 ${SWAP_FILE} && mkswap ${SWAP_FILE})"
        ExecStart=/usr/bin/sh -c "losetup -f ${SWAP_FILE}"
        ExecStart=/usr/bin/sh -c "swapon $(losetup -j ${SWAP_FILE} | cut -d : -f 1)"
        ExecStop=/usr/bin/sh -c "swapoff $(losetup -j ${SWAP_FILE} | cut -d : -f 1)"
        ExecStop=/usr/bin/sh -c "losetup -d $(losetup -j ${SWAP_FILE} | cut -d : -f 1)"

        [Install]
        WantedBy=multi-user.target

write_files:
  - path: /etc/sysctl.d/swap.conf
    permissions: 0644
    owner: root
    content: |
      vm.swappiness=10
      vm.vfs_cache_pressure=50
```


## datadog

```
docker run -d --name dd-agent -v /var/run/docker.sock:/var/run/docker.sock:ro -v /proc/:/host/proc/:ro -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro -e API_KEY={YOUR_API_KEY} -e SD_BACKEND=docker datadog/docker-dd-agent:latest
```


## Conoha VPS
<a href="https://px.a8.net/svt/ejp?a8mat=2TGARC+63OZ02+50+4YSWE9" target="_blank" rel="nofollow">
<img border="0" width="336" height="280" alt="" src="https://www29.a8.net/svt/bgt?aid=170401656369&wid=001&eno=01&mid=s00000000018030032000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www13.a8.net/0.gif?a8mat=2TGARC+63OZ02+50+4YSWE9" alt="">
