from run import conn
class UserModel():
    def __init__(self, username, password):
        self.cur = None
        self.result = None
        self.username=username
        self.password=password
    #def create_usertable(self):
        self.cur=conn.cursor()
        #self.result = self.cur.execute("CREATE TABLE USERS(USERID INT PRIMARY KEY NOT NULL, USERNAME  VARCHAR(255) NOT NULL,PASSWORD  VARCHAR(255)  NOT NULL);")
    def save(self):
        self.cur.execute('''INSERT INTO Users(username, password) VALUES(self.username, self.password)''')
        
        
    def db_commit(self):
        conn.commit()

    def db_termination(self):
        self.cur.close()
        conn.close()        
