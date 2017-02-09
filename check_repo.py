#! /usr/bin/env python
#coding=utf-8
import os

TEXT='''[cnc]
name=cnc
baseurl=http://61.129.13.40/repo/cnc/
gpgcheck=1
gpgkey=http://61.129.13.40/repo/rpm-gpg/RPM-GPG-KEY-CNC'''

#print TEXT

def create_CNC_repo():
    fp = open('/etc/yum.repos.d/CNC.repo', 'w')
    fp.write(TEXT)


def check_CNC_repo():
    file = "/etc/yum.repos.d/CNC.repo"
    if os.path.isfile(file):
        print "file exist, rename and create another-----------------------"
        os.rename("/etc/yum.repos.d/CNC.repo", "/etc/yum.repos.d/CNCbck.repo")
        create_CNC_repo()
        os.system("rpm -Uhv http://www.percona.com/downloads/percona-release/percona-release-0.0-1.x86_64.rpm")
        os.system("yum makecache")
        
    else:
        print "file not exist, will create it------------------------------"
        create_CNC_repo()
        os.system("rpm -Uhv http://www.percona.com/downloads/percona-release/percona-release-0.0-1.x86_64.rpm")
        os.system("yum makecache")

check_CNC_repo()