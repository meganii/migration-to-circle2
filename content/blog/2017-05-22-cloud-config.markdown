---
title: "cloud-config"
date: 2017-05-22T22:35:05+09:00
lastmod: 2017-05-22T22:35:05+09:00
comments: true
category: ['']
tags: ['']
published: false
slug: cloud-config
img:
---

<!--more-->
{{% googleadsense %}}

```zsh
#cloud-config

ssh_authorized_keys:
  - "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwqqaRVk+nSwyzrUBiNSxNb9OF0+viqEhkGYGothhRizt4Ouve1Yrmc7Db2S8jxNCr4wcczp07E1AZm9f8aAywN8dooROy5B5Fq3PXuxVQmu4ZloNeH9v3TgF6Dol/d8wqtu7QInupZbx1Tfm615KtAeWh37ref6T16yLH5/5zPsp0mGMDcKqpu5pXxlxR9Uli3XNetYGRsBFskME4McdOpiY3FRJyMUprAloKFnJRYSI1wCYMqvdP7/cf108LdLizJemSEbaWQHe5Kj/7DMgvzQh6RogdmcuN2JBfFr0vZplHoJO3VTomQJNW/UtdRQ14+izUZOLOeEpzLVq+v49v yuhei24@gmail.com"

coreos:
  update:
    reboot-strategy: best-effort
  units:
    - name: docker.service
      command: start

    - name: timezone.service
      command: start
      content: |
        [Unit]
        Description=timezone
        [Service]
        Type=oneshot
        RemainAfterExit=yes
        ExecStart=/usr/bin/ln -sf ../usr/share/zoneinfo/Japan /etc/localtime

    - name: swap-file.service
      command: start
      content: |
        [Unit]
        Description=Swap file
        [Service]
        Type=oneshot
        RemainAfterExit=true
        Environment="SWAP_FILE=/swap" "SWAP_SIZE=4G"
        ExecStart=/usr/bin/sh -c "[ -e ${SWAP_FILE} ] || (touch ${SWAP_FILE} && chattr +C ${SWAP_FILE} && fallocate -l ${SWAP_SIZE} ${SWAP_FILE} && chmod 600 ${SWAP_FILE} && mkswap ${SWAP_FILE})"
        ExecStart=/usr/bin/sh -c "losetup -f ${SWAP_FILE}"
        ExecStart=/usr/bin/sh -c "swapon $(losetup -j ${SWAP_FILE} | cut -d : -f 1)"
        ExecStop=/usr/bin/sh -c "swapoff $(losetup -j ${SWAP_FILE} | cut -d : -f 1)"
        ExecStop=/usr/bin/sh -c "losetup -d $(losetup -j ${SWAP_FILE} | cut -d : -f 1)"
        [Install]
        WantedBy=multi-user.target

    - name: kenchan-bot.service
      command: start
        content: |
        [Unit]
        Description=KenchanBot
        After=docker.service
        Requires=docker.service
        [Service]
        TimeoutStartSec=0
        ExecStartPre=-/usr/bin/docker kill busybox1
        ExecStartPre=-/usr/bin/docker rm busybox1
        ExecStartPre=/usr/bin/docker pull busybox
        ExecStart=/usr/bin/docker run --name busybox1 busybox /bin/sh -c "trap 'exit 0' INT TERM; while true; do echo Hello World; sleep 1; done"
        [Install]
        WantedBy=multi-user.target
users:
  - name: "admin"
    groups:
      - "sudo"
      - "docker"
    ssh-authorized-keys:
      - "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwqqaRVk+nSwyzrUBiNSxNb9OF0+viqEhkGYGothhRizt4Ouve1Yrmc7Db2S8jxNCr4wcczp07E1AZm9f8aAywN8dooROy5B5Fq3PXuxVQmu4ZloNeH9v3TgF6Dol/d8wqtu7QInupZbx1Tfm615KtAeWh37ref6T16yLH5/5zPsp0mGMDcKqpu5pXxlxR9Uli3XNetYGRsBFskME4McdOpiY3FRJyMUprAloKFnJRYSI1wCYMqvdP7/cf108LdLizJemSEbaWQHe5Kj/7DMgvzQh6RogdmcuN2JBfFr0vZplHoJO3VTomQJNW/UtdRQ14+izUZOLOeEpzLVq+v49v yuhei24@gmail.com"

write_files:
  - path: /etc/ssh/sshd_config
    permissions: 0600
    owner: root:root
    content: |
      # Use most fefaults for sshd configulation.
      UsePrivilegeSeparation sandbox
      Subsystem sftp internal-sftp
      ClientAliveInterval 180

      PermitRootLogin no
      PasswordAuthentication no
      ChallengeResponseAuthentication no
      AllowUsers core

  - path: /etc/sysctl.d/swap.conf
    permissions: 0644
    owner: root
    content: |
      vm.swappiness=10
      vm.vfs_cache_pressure=50

```
