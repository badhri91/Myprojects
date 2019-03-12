#!/usr/bin/env python3
import paramiko
import os
import sys

log = open("myprog.log", "a")


def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

sshsession=paramiko.SSHClient()

mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa_github")
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def get_connect_details():
    uinputlist = []
    while True:
        connectinfo = input("Enter the hostname and username:")
        if connectinfo == "done":
            break
        else:
            uinputlist.append(connectinfo.split(','))
            print (uinputlist)
    return uinputlist



def user_input():
    usercommands = input("Enter the commands to run:").split(',')
    #print (usercommands)
    return usercommands

uinputlist = get_connect_details()
our_commands = user_input()

sys.stdout = log
for _ in uinputlist:
    print(_[1] + " @ " + _[0])
    sshsession.connect(hostname=_[0], username=_[1], password="alta3")
    for x in our_commands:
        print (commandissue(x).decode('utf-8'))
