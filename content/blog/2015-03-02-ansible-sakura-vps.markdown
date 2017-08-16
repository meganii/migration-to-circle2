---

title: "AnsibleでさくらVPSの初期設定"
date: 2015-03-02T07:31:00+09:00
comments: true
category: ['Tech']
tags: ['ansible','さくらvps']
published: true
img: "https://images-na.ssl-images-amazon.com/images/I/31u6VLGX2kL._SL160_.jpg"
slug: ansible-sakura-vps
---

行き当たりばったりで、設定を繰り返してきた、<a href="http://px.a8.net/svt/ejp?a8mat=2NDW0A+8S5702+D8Y+BWVTE" target="_blank">さくらのVPS</a>。
いい加減、自動化したいと思い、CentOSを初期化して、Ansibleで初期設定をしていきます。


{{% googleadsense %}}


## 方針

1. rootでの初期設定
2. nginxの設定

rootでの作業と、作業用ユーザでログインして作業をするタスク分けておくことで、初期設定と各アプリケーションのインストールをやりやすいようにしておく。


## 前提 ansible インストール

Homebrewからインストールする。
```
brew install ansible
```

### 実行環境

```
## ローカル環境
$ ansible --version
ansible 1.6.10

$ ruby -v
ruby 2.0.0p353 (2013-11-22 revision 43784) [x86_64-darwin12.5.0]

## さくらVPSの標準インストールで入るCentOS
$ cat /etc/redhat-release
CentOS release 6.6 (Final)
```

## 1. rootでの初期設定(sakura_init.yml)

まっさらな状態のCentOSに対して、最低限のセキュリティの設定を行う。

- SSHのポートを変える
- rootでのsshを禁止する
- パスワードでのsshを禁止する
- iptablesを設定する
- adminユーザを作成して、sudoできるようにする
- 鍵の設定を行う



### hosts

```
[test]
192.168.33.33
[vagrant]
vagrant:10022

[sakura_init]
49.212.XXX.XXX
[sakura]
sakura:10022
```

test, vagrantは、vagrantの設定である。
`vagrant:10022`としているのは、

さらに、この`vagrant`と`sakura`は、下記の通り、`~/.ssh/config`に設定している。

### ~/.ssh/config

```
Host vagrant
  Hostname 192.168.33.33
  Port 10022
  User admin
  IdentityFile ~/.ssh/id_rsa

Host jekyll_vagrant
  Hostname 192.168.33.33
  Port 10022
  User jekyll
  IdentityFile ~/.ssh/id_rsa

Host 192.168.33.33
  User root
  IdentityFile ~/.vagrant.d/insecure_private_key
  IdentitiesOnly yes

Host 49.212.138.148
  User root
  IdentityFile ~/.ssh/id_rsa
  IdentitiesOnly yes

Host sakura
  Hostname 49.212.138.148
  Port 10022
  User admin
  IdentityFile ~/.ssh/id_rsa
```

この設定により、下記ようにポート、ホスト名などを省略して接続できる。

```
ssh vagrant
ssh sakura
```


### sakura_init.yml

```yaml
---
- hosts: sakura_init
  user: root
  vars:
    admin_name: admin
    admin_password: password
    admin_public_key_path: ~/.ssh/id_rsa.pub
    ssh_port: 10022
  tasks:
    - name: change SSH port
      lineinfile: dest=/etc/ssh/sshd_config regexp="^#Port" line="Port {{ ssh_port }}" state=present

    - name: create iptables
      template: src=iptables.j2 dest=/etc/sysconfig/iptables

    - name: disallow root SSH access
      lineinfile: dest=/etc/ssh/sshd_config regexp="^#PermitRootLogin " line="PermitRootLogin no" state=present

    - name: disallow password authentication
      lineinfile: dest=/etc/ssh/sshd_config regexp="^#PasswordAuthentication " line="PasswordAuthentication no" state=present

    - name: Add a new user
      user: name={{admin_name}} password={{ admin_password }} groups=wheel state=present

    - name: allow wheel users to sudo
      lineinfile: dest=/etc/sudoers regexp="^#\s*(%wheel\s+ALL=\(ALL\)\s+NOPASSWD{{':'}}\s+ALL)" line="\1" backrefs=yes state=present

    - name: resister a public key
      authorized_key: user={{ admin_name }} key="{{ item }}"
      with_file:
        - "{{ admin_public_key_path }}"

    - name: restart sshd and restart iptables
      shell: service sshd restart && /etc/init.d/iptables restart

```

### iptables.j2

```
*filter
:INPUT   ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT  ACCEPT [0:0]
:RH-Firewall-1-INPUT - [0:0]

-A INPUT -j RH-Firewall-1-INPUT
-A FORWARD -j RH-Firewall-1-INPUT
-A RH-Firewall-1-INPUT -i lo -j ACCEPT
-A RH-Firewall-1-INPUT -p icmp --icmp-type any -j ACCEPT
-A RH-Firewall-1-INPUT -p 50 -j ACCEPT
-A RH-Firewall-1-INPUT -p 51 -j ACCEPT
-A RH-Firewall-1-INPUT -p udp --dport 5353 -d 224.0.0.251 -j ACCEPT
-A RH-Firewall-1-INPUT -p udp -m udp --dport 631 -j ACCEPT
-A RH-Firewall-1-INPUT -p tcp -m tcp --dport 631 -j ACCEPT
-A RH-Firewall-1-INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# add start
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport {{ ssh_port }} -j ACCEPT
# add end

-A RH-Firewall-1-INPUT -j REJECT --reject-with icmp-host-prohibited

COMMIT
```

### ansible実行

```
$ ansible-playbook -i hosts sakura_init.yml -k -c paramiko
# さくらVPSで設定したrootパスワード
```

## 2. nginxの設定

`playbook.yml`で、jekyllのフォルダ、nginxのインストール、設定を行う。

### playbook.yml

```yaml
---
- hosts: sakura
  sudo: yes
  user: admin
  vars:
    user_name: jekyll
    user_password: password
    user_public_key_path: ~/.ssh/id_rsa.pub
    httpd_port: 80
  tasks:
    - name: Add a new user
      user: name={{user_name}} password={{ user_password }} state=present

    - name: register a public key
      authorized_key: user={{ user_name }} key="{{ item }}"
      with_file:
        - "{{user_public_key_path}}"

    - name: Create Jekyll directory
      file: path=/home/jekyll/www/meganii.com/ state=directory owner=jekyll group=jekyll mode=0755

    - name:  Add 755
      file: path=/home/jekyll

    - name: Copy the EPEL repository definition
      copy: src=epel.repo dest=/etc/yum.repos.d/epel.repo

    - name: Create the GPG key for EPEL
      copy: src=RPM-GPG-KEY-EPEL-6 dest=/etc/pki/rpm-gpg

    - name: Install nginx
      yum: name=nginx state=present

    - name: add iptables rule for httpd
      lineinfile: dest=/etc/sysconfig/iptables regexp="{{ httpd_port }}" line="-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport {{ httpd_port }} -j ACCEPT" insertbefore="^# add end" state=present
    - name: Copy nginx congiguration for jekyll
      template: src=default.conf dest=/etc/nginx/conf.d/default.conf

    - name: iptables restart
      command: /etc/init.d/iptables restart

    - name: restart nginx
      command: service nginx restart
```

### epel.repo

```
[epel]
name=Extra Packages for Enterprise Linux 6 - $basearch
#baseurl=http://download.fedoraproject.org/pub/epel/6/$basearch
mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-6&arch=$basearch
failovermethod=priority
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6

[epel-debuginfo]
name=Extra Packages for Enterprise Linux 6 - $basearch - Debug
#baseurl=http://download.fedoraproject.org/pub/epel/6/$basearch/debug
mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-debug-6&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux 6 - $basearch - Source
#baseurl=http://download.fedoraproject.org/pub/epel/6/SRPMS
mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-source-6&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
gpgcheck=1
```

### RPM-GPG-KEY-EPEL-6

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.5 (GNU/Linux)

mQINBEvSKUIBEADLGnUj24ZVKW7liFN/JA5CgtzlNnKs7sBg7fVbNWryiE3URbn1
JXvrdwHtkKyY96/ifZ1Ld3lE2gOF61bGZ2CWwJNee76Sp9Z+isP8RQXbG5jwj/4B
M9HK7phktqFVJ8VbY2jfTjcfxRvGM8YBwXF8hx0CDZURAjvf1xRSQJ7iAo58qcHn
XtxOAvQmAbR9z6Q/h/D+Y/PhoIJp1OV4VNHCbCs9M7HUVBpgC53PDcTUQuwcgeY6
pQgo9eT1eLNSZVrJ5Bctivl1UcD6P6CIGkkeT2gNhqindRPngUXGXW7Qzoefe+fV
QqJSm7Tq2q9oqVZ46J964waCRItRySpuW5dxZO34WM6wsw2BP2MlACbH4l3luqtp
Xo3Bvfnk+HAFH3HcMuwdaulxv7zYKXCfNoSfgrpEfo2Ex4Im/I3WdtwME/Gbnwdq
3VJzgAxLVFhczDHwNkjmIdPAlNJ9/ixRjip4dgZtW8VcBCrNoL+LhDrIfjvnLdRu
vBHy9P3sCF7FZycaHlMWP6RiLtHnEMGcbZ8QpQHi2dReU1wyr9QgguGU+jqSXYar
1yEcsdRGasppNIZ8+Qawbm/a4doT10TEtPArhSoHlwbvqTDYjtfV92lC/2iwgO6g
YgG9XrO4V8dV39Ffm7oLFfvTbg5mv4Q/E6AWo/gkjmtxkculbyAvjFtYAQARAQAB
tCFFUEVMICg2KSA8ZXBlbEBmZWRvcmFwcm9qZWN0Lm9yZz6JAjYEEwECACAFAkvS
KUICGw8GCwkIBwMCBBUCCAMEFgIDAQIeAQIXgAAKCRA7Sd8qBgi4lR/GD/wLGPv9
qO39eyb9NlrwfKdUEo1tHxKdrhNz+XYrO4yVDTBZRPSuvL2yaoeSIhQOKhNPfEgT
9mdsbsgcfmoHxmGVcn+lbheWsSvcgrXuz0gLt8TGGKGGROAoLXpuUsb1HNtKEOwP
Q4z1uQ2nOz5hLRyDOV0I2LwYV8BjGIjBKUMFEUxFTsL7XOZkrAg/WbTH2PW3hrfS
WtcRA7EYonI3B80d39ffws7SmyKbS5PmZjqOPuTvV2F0tMhKIhncBwoojWZPExft
HpKhzKVh8fdDO/3P1y1Fk3Cin8UbCO9MWMFNR27fVzCANlEPljsHA+3Ez4F7uboF
p0OOEov4Yyi4BEbgqZnthTG4ub9nyiupIZ3ckPHr3nVcDUGcL6lQD/nkmNVIeLYP
x1uHPOSlWfuojAYgzRH6LL7Idg4FHHBA0to7FW8dQXFIOyNiJFAOT2j8P5+tVdq8
wB0PDSH8yRpn4HdJ9RYquau4OkjluxOWf0uRaS//SUcCZh+1/KBEOmcvBHYRZA5J
l/nakCgxGb2paQOzqqpOcHKvlyLuzO5uybMXaipLExTGJXBlXrbbASfXa/yGYSAG
iVrGz9CE6676dMlm8F+s3XXE13QZrXmjloc6jwOljnfAkjTGXjiB7OULESed96MR
XtfLk0W5Ab9pd7tKDR6QHI7rgHXfCopRnZ2VVQ==
=V/6I
-----END PGP PUBLIC KEY BLOCK-----
```

### default.conf

```
#
# The default server
#
server {
    listen 	 80;
    server_name  meganii.com;

    #charset koi8-r;

    #access_log  logs/host.access.log  main;

    location / {
        root   /home/jekyll/www/meganii.com;
        index  index.html index.htm;
    }

    error_page  404              /404.html;
    location = /404.html {
        root   /usr/share/nginx/html;
    }

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}
```

### 実行

```
$ ansible-playbook -i hosts playbook.yml
```


## ハマったポイント

### パスワードは、以下の処理をしなければならない

```
$ openssl passwd -salt hoge -1 fuga
$1$hoge$DP2bw0KOW0ZhAg2ssVHY7.
```

### オプションの指定

-k -c paramiko のオプションを付けないとエラー

```
$ ansible-playbook -i hosts playbook.yml -k -c paramiko
設定した root のパスワードを入力
```


## まとめ

vagrantで、centosを立てて、ansibleのテストを行なった。vagrant上のcentosでは上手くいくが、本番のさくらVPSに対してはエラーになることがあったので、その度再インストールを繰り返した。

問題になったのは、hostsの設定部分であったり、ファイルコピーの部分であったりまだ原因がよくわかっていない。


でも、何度も繰り返し同じことを行えるのは、すごく心強い。秘伝のサーバー設定に陥りがちだけど、いざとなれば、再インストールで元に戻せる安心感を手に出来た。




## 参考
[Ansible でさくらのVPS の環境構築を自動化　～ハマりポイントとともに～ - akiyoko blog](http://akiyoko.hatenablog.jp/entry/2013/12/16/020529)

SSDプランが月々685円から使える！<a href="http://px.a8.net/svt/ejp?a8mat=2NDW0A+8S5702+D8Y+C8O76" target="_blank">さくらのVPS</a>
<img border="0" width="1" height="1" src="http://www19.a8.net/0.gif?a8mat=2NDW0A+8S5702+D8Y+C8O76" alt="">

## 参考(Infrastructure as Code)
<div class="booklink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="booklink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/asin/B00BSPH158/meganii-22/" name="booklink" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/31u6VLGX2kL._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="booklink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/asin/B00BSPH158/meganii-22/" rel="nofollow" name="booklink" target="_blank">入門Chef Solo - Infrastructure as Code[Kindle版]</a><div class="booklink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail" style="margin-bottom:5px;">伊藤直也 伊藤直也 2013-03-11    </div><div class="booklink-link2" style="margin-top:10px;"><div class="shoplinkkindle" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B00BSPH158/meganii-22/" rel="nofollow" target="_blank">Kindle</a></div><div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/gp/search?keywords=%93%FC%96%E5Chef%20Solo%20-%20Infrastructure%20as%20Code&__mk_ja_JP=%83J%83%5E%83J%83i&url=search-alias%3Dstripbooks&tag=meganii-22" rel="nofollow" target="_blank">Amazon[書籍版]</a></div>                              	  	  	  	</div></div><div class="booklink-footer" style="clear: left"></div></div>
