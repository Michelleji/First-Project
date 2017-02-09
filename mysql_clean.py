#!/bin/python
import os
import sys
import shutil
class clean:
        def __init__(self,dir,lv,pac_list):
                self.Work_dir = dir
                self.Work_lv = lv
                self.pac_list=pac_list
        def clean_mysql(self):
                while True:
                        Answer=raw_input('Do you want remove mysql [Y\N]:')
                        if Answer.upper() == 'Y':
                                for i in self.pac_list:
                                        print i
                                        Return=os.system("rpm -qa|grep -i %s" % i)
                                        if Return != 0:
                                                print 'No package found'
                                        else:
                                                os.system("yum remove -y %s" % i)
                                break
                        elif Answer.upper() == 'N':
                                sys.exit()
                        else:
                                pass
        def clean_data(self):
                while True:
                        Answer=raw_input('Do you want clean mysql data [Y\N]:')
                        if Answer.upper()=='Y':
                                if os.path.exists(self.Work_dir):
                                        pass
                                else:
                                        print 'No dir found'
                                        sys.exit()
                                filelist=os.listdir(self.Work_dir)
                                for i in filelist:
                                        filepath = os.path.join(self.Work_dir,i)
                                        if os.path.isfile(filepath):
                                                os.remove(filepath)
                                        elif os.path.isdir(filepath):
                                                shutil.rmtree(filepath,True)
                                break
                        
                        elif Answer.upper()=='N':
                                sys.exit()
                        else:
                                pass
        def clean_lv(self):
                while True:
                        Answer=raw_input('Do you want remove the lv [Y\N]:')
                        if Answer.upper()=='Y':
                                os.system("umount %s" % self.Work_dir)
                                os.system("lvremove %s" % self.Work_lv)
                                break
                        elif Answer.upper()=='N':
                                sys.exit()
                        else:
                                pass
work=clean('/var/lib/mysql','/dev/domuvg/mysql',['mysql*','Percona*'])
work.clean_mysql()
work.clean_data()
work.clean_lv()