import cx_Oracle, adodbapi

class DB_Connection():
    def __init__(self,db_name,db_user,db_pw):
        self.db_name = db_name
        self.db_user = db_user
        self.db_pw = db_pw

    def ora_sql(self,sql):
        db = cx_Oracle.connect(self.db_user + "/" + self.db_pw + "@" + self.db_name)
        cursor = db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        db.close()
        return rows

    def ora_updt_sql(self,sql):
        db = cx_Oracle.connect(self.db_user + "/" + self.db_pw + "@" + self.db_name)
        cursor = db.cursor()
        cursor.execute(sql)
        cursor.execute('commit')
        db.close()

    def sqlserver_sql(self,sql):
        
        db = adodbapi.connect('Provider=SQLOLEDB.1;Integrated Security=SSPI;Persist Security Info=True;Initial Catalog='+self.db_user+';Data Source='+self.db_name+';Use Procedure for Prepare=1;Auto Translate=True;Packet Size=4096;User Id = '+self.db_pw,300)
        
        cursor = db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        db.close()
        return rows

    def sqlserver_multi_sql(self,sql):
        
        db = adodbapi.connect('Provider=SQLOLEDB.1;Integrated Security=SSPI;Persist Security Info=True;Initial Catalog='+self.db_user+';Data Source='+self.db_name+';Use Procedure for Prepare=1;Auto Translate=True;Packet Size=4096;User Id = '+self.db_pw,300)
        
        cursor = db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows)>100000:
            rows = []
            return False,rows
        else:
            return True,rows
        db.close()
        


        
