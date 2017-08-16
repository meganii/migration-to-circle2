---
title: "Installing Oracle Database Express Edition11g on Vagrant(CentOS 6.4)"
date: 2015-02-08T15:11:00+09:00
lastmod: 2017-01-02T08:58:00+09:00
comments: true
category: ['Tech']
tags: ['Oracle','database']
published: true
img: "https://farm9.staticflickr.com/8640/16468400201_39ccfefbac_s.jpg"
slug: oracle-express-edition-11g-install
---

I'd like to learn about Oracle, so I installed Oracle 11g Express Edition on Vagrant(CentOS).

## Environment

- VirtualBox version 4.3.14
- Vagrant 1.6.3
- Oracle Database Express Edition 11g R2
- Host OS: Mac OS X Mavericks
- Guest OS: CentOS 6.4 x86_64 Minimal(20140116)

[Release CentOS 6.4 x86_64 Minimal (2014-01-16) · 2creatives/vagrant-centos](https://github.com/2creatives/vagrant-centos/releases/tag/v6.4.2)


## Installing Oracle11g

1. Setting Vagrant(Host OS)
2. Downloading Oracle Database Express Edition 11g(Host OS)
3. Installing package for installing Oracle(Guest OS)
4. Installing Oracle(Guest OS)
5. Status Check

{{% googleadsense %}}

## 1. Setting Vagrant(Host OS)

### Installing VirtualBox and Vagrant

I'll omit installing VirtualBox and Vagrant.

### Setting for network

Adding IP address in Vagrantfile.

```
# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos64-x86_64-20140116"

  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"
end

```

### Setting share folder

Creating share folder to access by Guest OS.

<p><a href="https://www.flickr.com/photos/35571855@N06/16444231326" title="Vagrant share folderby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7423/16444231326_e7bed11e94_z.jpg" alt="Vagrant share folder"></a></p>



### Boot OS

```
vagrant up
```


## 2. Downloading Oracle Database Express Edition 11g(Host OS)

Downloading Oracle Database Express Edition 11g below url.(You need to sign up oracle.)

http://www.oracle.com/technetwork/jp/database/database-technologies/express-edition/downloads/index.html

After downloading, put downloaded files into share folder.


## 3. Installing package for installing Oracle(Guest OS)


[Database Express Edition Installation Guide \- Contents](http://docs.oracle.com/cd/E17781_01/install.112/e18802/toc.htm#XEINL102)

Software requirements are the following package.

- glibc should be greater than or equal to 2.3.4-2.41
- make should be greater than or equal to 3.80
- binutils should be greater than or equal to 2.16.91.0.5
- gcc should be greater than or equal to 4.1.2
- libaio should be greater than or equal to 0.3.104


### Installing libaio and bc

In my enviroment, I only need to install `libaio` and 'bc'.

```
yum install libaio bc
```


### Adding computer name in hosts file

```
vi /etc/hosts
```

```diff
- 127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
+ 127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4 vagrant-centos64.vagrantup.com
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
```

You can get computer name by `hostname` command.


## 4. Installing Oracle(Guest OS)

### Installing by rpm

```
rpm -ivh oracle-xe-11.2.0-1.0.x86_64.rpm
```

```
$ rpm -ivh oracle-xe-11.2.0-1.0.x86_64.rpm
Preparing...                ########################################### [100%]
   1:oracle-xe              ########################################### [100%]
Executing post-install steps...
You must run '/etc/init.d/oracle-xe configure' as the root user to configure the database.
```

### Creating database

Creating database by the following command.

```
/etc/init.d/oracle-xe configure
```


```
Oracle Database 11g Express Edition Configuration
-------------------------------------------------
This will configure on-boot properties of Oracle Database 11g Express
Edition.  The following questions will determine whether the database should
be starting upon system boot, the ports it will use, and the passwords that
will be used for database accounts.  Press <Enter> to accept the defaults.
Ctrl-C will abort.

Specify the HTTP port that will be used for Oracle Application Express [8080]:

Specify a port that will be used for the database listener [1521]:

Specify a password to be used for database accounts.  Note that the same
password will be used for SYS and SYSTEM.  Oracle recommends the use of
different passwords for each database account.  This can be done after
initial configuration:
Confirm the password:

Do you want Oracle Database 11g Express Edition to be started on boot (y/n) [y]:y

Starting Oracle Net Listener...Done
Configuring database...Done
Starting Oracle Database 11g Express Edition instance...Done
Installation completed successfully.
```



## 5. Status Check

I accessed `http://192.168.33.10:8080` after setting iptables disable.

Username and password are the following.

- username： system
- password： setup when installing oracle

You can access and check oracle work well.

<p><a href="https://www.flickr.com/photos/35571855@N06/16468400201" title="oracle xe installby meganii, on Flickr"><img class="img-responsive" src="https://farm9.staticflickr.com/8640/16468400201_39ccfefbac_z.jpg" alt="oracle xe install"></a></p>

## Ref
- [ swapon /swapfile](https://gist.github.com/koudaiii/0ed6a8558aa297af463e)
- [linux スワップ（swap）領域の作成](http://kazmax.zpp.jp/linux_beginner/mkswap.html)
- [http://docs.oracle.com/cd/E11882_01/install.112/e24326/toc.htm#BHCGJCEA](http://docs.oracle.com/cd/E11882_01/install.112/e24326/toc.htm#BHCGJCEA)
