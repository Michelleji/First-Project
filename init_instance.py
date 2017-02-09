import MySQLdb,getpass

class init_db_setup:
        def __init__(self):
                try:
                        origin_user = raw_input('Please input the username to login the database(Use current system user by default): ')
                        origin_passwd = getpass.getpass('Please input the mysql root password(Press Enter if not set): ')
                        self.conn = MySQLdb.connect(host='localhost',user=origin_user,passwd=origin_passwd,port=3306)
                        self.cur = self.conn.cursor()
                        self.password = ''
                        self.databases = set([])
                        self.user_host = []
                except MySQLdb.Error,e:
                        print "MySQL error %d: %s" %(e.args[0],e.args[1])
                        quit()
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        quit()

        def init_databases(self):
                try:
                        print('\nDropping database test...')
                        self.cur.execute('DROP DATABASE test')
                        print('Database test dropped\n')
                except MySQLdb.OperationalError:
                        print("Database test doesn't exit, no need to drop\n")
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        self.conn.close()
                        quit()

                try:
                        print('Removing unsafe users...')
                        self.conn.select_db('mysql')
                        self.cur.execute("DELETE FROM user WHERE user = '' OR host NOT IN ('127.0.0.1','localhost')")
                        print('Unsafe users dropped\n')
                except MySQLdb.OperationalError:
                        print("No unsafe users found, no need to drop\n")
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        self.conn.close()
                        quit()

                try:
                        while not self.password:
                                password_once = getpass.getpass('Please set up the new root password: ')
                                if len(password_once) < 6:
                                        print('The password not safe, shorter than 6 charactors')
                                else:
                                        password_twice = getpass.getpass('Please repeat the new root password again: ')
                                        if password_twice != password_once:
                                                print ('Sorry, passwords do not match, please try again later\nPassword not changed')
                                                quit()
                                        self.password = password_twice
                                        self.conn.select_db('mysql')
                                        pwd_change_sql = "UPDATE user SET password=PASSWORD('"+ self.password +"') WHERE user='root'"
                                        self.cur.execute(pwd_change_sql)
                                        self.cur.execute('FLUSH PRIVILEGES')
                                        print('\nPassword changed sucessfully\n')

                except MySQLdb.Error,e:
                        print "MySQL error %d: %s" %(e.args[0],e.args[1])       
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        self.conn.close()
                        quit()


        def create_databases(self):
                try:
                        while True:
                                dbnames = raw_input('Please input the database names you wanna create(Can be one or more, type the space between the names): ')
                                db_to_create = set(dbnames.split()) - self.databases
                                db_to_ignore = set(dbnames.split()) & self.databases
                                for db in db_to_ignore:
                                        print db,'already exit, ignored'
                                for db in db_to_create:
                                        print 'Creating database',db
                                        self.cur.execute('CREATE DATABASE '+ db)
                                        print db,'CREATED\n'
                                is_continue = raw_input('Continue adding more databases? (Y/N) ')
                                self.databases = self.databases | db_to_create
                                if is_continue.lower() == 'n':
                                        break

                except MySQLdb.Error,e:
                        print "MySQL error %d: %s" %(e.args[0],e.args[1])
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        self.conn.close()
                        quit()

        def create_user(self):
                try:
                        is_conntinue = raw_input("Create the replication user repl@'%' using the same root password, can customize the password using root account later. Create? (Y/N)")
                        if is_conntinue.lower() == 'n':
                                self.conn.close()
                                quit()
                        else:
                                create_repl = "GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO repl@'%' IDENTIFIED BY '"+self.password+"'"
                                self.cur.execute(create_repl)
                                print 'Created'

                except MySQLdb.Error,e:
                        print "MySQL error %d: %s" %(e.args[0],e.args[1])
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        self.conn.close()
                        quit()

                        

#Can customize here
test = init_db_setup()
test.init_databases()
test.create_databases()
test.create_user()
test.conn.close()