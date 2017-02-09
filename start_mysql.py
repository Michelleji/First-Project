#! /usr/bin/env python
#coding=utf-8

import shutil
import os



def configure_mysql():
    file = "/etc/my.cnf"
    if os.path.isfile(file):
#      "file exist, rename and create another-----------------------"
        os.rename("/etc/my.cnf", "/etc/mybck.cnf")
        shutil.copy("/usr/share/mysql/my-small.cnf", "/etc/my.cnf")
    else:
#       "file not exist, will create it------------------------------"    
        shutil.copy("/usr/share/mysql/my-small.cnf", "/etc/my.cnf")
    os.system("mkdir -p /tmp/mysql > /dev/null")
    os.system("chown mysql.mysql /tmp/mysql > /dev/null")
    os.system("chown mysql:mysql /var/lib/mysql -R > /dev/null")
    start = os.system("service mysqld start > /dev/null")
    if start == 0:
        print "MySQL Start Successfully"
    else:
        print "MySQL Start Failed"

configure_mysql()