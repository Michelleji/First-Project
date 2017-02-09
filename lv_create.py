#! /usr/bin/env python
#coding=utf-8
import sys
import os
def vg_check(vg_dir):   
        if not os.path.exists(vg_dir):
                print 'No vg found'
                sys.exit()
        ret=os.system("if [ $(vgs|grep domuvg|awk '{print $NF}'|awk -F '.' '{print $1}') -gt 10 ];then echo 'okay' > /dev/null;else cat /efraeerfe &> /dev/null;fi")
        if ret != 0:
                print 'No vg found'
                sys.exit()
def lv_creat(mysql):
        os.system("lvcreate -L 10G -n mysql domuvg &>/dev/null")
        os.system("mkfs.ext4 /dev/domuvg/mysql")
        os.system("mount /dev/domuvg/mysql /var/lib/mysql")
def lv_check(lv_file):
        if os.path.exists(lv_file):
                while True:
                        Choise=raw_input('The mysql lv already exist do you want remove it[Y|N]:')
                        if Choise.upper() == 'Y':
                                os.system('umount /dev/domuvg/mysql &> /dev/null')
                                os.system('lvremove /dev/domuvg/mysql > /dev/null')
                                lv_creat('mysql')
                                break
                        elif Choise.upper() == 'N':
                        
                                while True:
                                        Choise=raw_input('Do you want use the old data[Y] or exit the scripts[N]:')
                                        if Choise.upper() == 'Y':
                                                print 'will use the old data'
                                                break
                                        elif Choise.upper() == 'N':
                                                sys.exit()
                                        else:
                                                pass
        else:
                lv_creat('mysql')
def mount_job():
        ret=os.system("grep '/dev/domuvg/mysql' /etc/fstab")
        if ret == 0:
                pass
        else:
                try:
                        f=open('/etc/fstab', 'a')
                        f.write('\n/dev/domuvg/mysql       /var/lib/mysql          ext4    defaults        0 0\n')
                        f.close()
                except:
                        print 'OPen /etc/fstab failed'
        

vg_check('/dev/domuvg/')
lv_check('/dev/domuvg/mysql')
mount_job()