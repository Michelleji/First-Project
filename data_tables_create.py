import MySQLdb,getpass

class data_tables_create():
        def __init__(self):
                try:
                        mysql_user= raw_input('Please input the username to login the database(Use current system user by default): ')
                        mysql_passwd=getpass.getpass('Please input the mysql password(Press Enter if not set): ')
                        self.conn = MySQLdb.connect(host='localhost',user=mysql_user,passwd=mysql_passwd,port=3306)
                        print 'Connecting to Mysql...'
                        self.cur = self.conn.cursor()
                except MySQLdb.Error,e:
                        print 'Cannot connect to Mysql T^T...'
                        print "MySQL error %d: %s" %(e.args[0],e.args[1])
                        quit()
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        quit()
        def db_creat(self):
                try:
                        DB_NAME=raw_input('Please input database name which you want to create:')

                        self.cur.execute("create database " + DB_NAME + "")
                        print "database created..."
                except MySQLdb.Error,e:
                        print "MySQL error %d: %s" %(e.args[0],e.args[1])
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        self.conn.close()
                        quit()
        def tables_create(self):
                try:
                        db_NAME=raw_input('Please input the database you wanna to use:')
                        TABLE_NAME=raw_input('Please input the tables name which you want to create:')
                        MYSQL_ENGINE=raw_input('Please choose your tables engine(InnoDB/MyISAM/others):')
                        self.cur.execute("use "+db_NAME+";create table "+TABLE_NAME+"(id int primary key auto_increment,name char(20)) engine="+MYSQL_ENGINE+";insert into "+TABLE_NAME+"(name) values('michelle test')")
                        
                except MySQLdb.Error,e:
                        print "MySQL error %d: %s" %(e.args[0],e.args[1])      
                except KeyboardInterrupt:
                        print '\nInterrupted by user'
                        self.conn.close()
                        quit()
                print "Table %s created successfully \o/ "%(TABLE_NAME)

test=data_tables_create()
test.db_creat() 
test.tables_create()