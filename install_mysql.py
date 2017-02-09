import os

class Install_MySQL:
        def __init__(self):
                self.version_list = {'5.5':'Percona-Server-server-55.x86_64 Percona-Server-client-55.x86_64 Percona-Server-shared-55.x86_64','5.6':'Percona-Server-server-56.x86_64 Percona-Server-client-56.x86_64 Percona-Server-shared-56.x86_64'}
                self.version = ''
                self.confirm = ''
                self.mount_point = '/var/lib/mysql/'
        def get_version(self):
                while self.version not in self.version_list:
                        try:
                                self.version = raw_input('Please choose the version you wanna install: (Type 5.5/5.6) ')
                        except KeyboardInterrupt:
                                print '\nInterrupted by user'
                                quit()

                return self.version 
        def install(self):
                try:
                        version = self.version
                        print 'You are going to install the following packages:\n',self.version_list[version]
                        self.confirm = raw_input('Install? (Y/N) ')
                        if self.confirm.lower() in ['y','']:
                                command = 'yum install -y ' + self.version_list[version]
                                os.system(command)
                        else:
                                print 'Ending ...'
                                quit()
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        quit()


#rpm -Uhv http://www.percona.com/downloads/percona-release/percona-release-0.0-1.x86_64.rpm

test = Install_MySQL()
test.get_version()
test.install()