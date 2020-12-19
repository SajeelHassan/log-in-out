import pymysql
class DBHandler:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user = user
        self.password=password
        self.database=database
    def isUserExist(self,uname):
            mydb = None
            status=False
            try:
                mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                mydbCursor = mydb.cursor()
                sql = "Select username from users WHERE username =%s"
                mydbCursor.execute(sql,uname)
                myresult = mydbCursor.fetchone()
                if myresult != None:
                    if myresult[0] == uname:
                        status = True
            except Exception as e:
                print(str(e))
            finally:
                if mydb != None:
                    mydb.close()
                return status
    def isEmailExist(self,email):
            mydb = None
            status=False
            try:
                mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                mydbCursor = mydb.cursor()
                sql = "Select email from users WHERE email =%s"
                mydbCursor.execute(sql,email)
                myresult = mydbCursor.fetchone()
                if myresult != None:
                    if myresult[0] == email:
                        status = True
            except Exception as e:
                print(str(e))
            finally:
                if mydb != None:
                    mydb.close()
                return status
    def signUp(self,fname,email,uname,pwd):
        mydb = None
        status = False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "INSERT INTO users (fullname,email,username,password) VALUES (%s,%s,%s,%s)"
            args=(fname,email,uname,pwd)
            mydbCursor.execute(sql, args)
            mydb.commit()
            status = True
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            return status
    def login(self,uname,pwd):
        mydb = None
        status = False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "Select username,password from users WHERE username =%s AND password =%s"
            args=(uname,pwd)
            mydbCursor.execute(sql, args)
            myresult = mydbCursor.fetchone()
            if myresult != None:
                if myresult[0] == uname and myresult[1]==pwd:
                    status = True
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()
            return status

    def getEmail(self,uname):
        mydb = None
        status=False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "Select email,username from users WHERE username = %s"
            mydbCursor.execute(sql,uname)
            myresult = mydbCursor.fetchone()

            if myresult != None:
                if myresult[1]==uname:
                    status = True
        except Exception as e:
            print(str(e))
        finally:
            if mydb != None:
                mydb.close()

            if status is True:
                return myresult[0]
            else:
                return 'not found'
