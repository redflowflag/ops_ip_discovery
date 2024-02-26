#!/usr/bin/env python
#coding:utf-8

import paramiko

pwd = input("please enter your ssh pwd:")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bastion.yanfeng.com', 22, 'uwuxl040/10.195.132.199/root', pwd)
stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())
stdin, stdout, stderr = ssh.exec_command('ifconfig')
print(stdout.read() + stderr.read())
ssh.close()