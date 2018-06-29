import psycopg2


class UserModel():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        try:
            self.conn = psycopg2.connect(dbname="postgres", user="postgres", host="localhost", password="XABC", port=5432)
        except:
            print("connection error")
        self.cur=self.conn.cursor()
    
    
    def save(self):
        self.cur.execute(""" INSERT INTO r_users (username, passwd) 
                                VALUES (%s, %s); """
                                , (self.username, self.password))
        self.conn.commit()

    def find_user(self, username):
        self.cur.execute(""" SELECT username, passwd  FROM r_users WHERE username=username """)
        print(self.cur.fetchone())
        return self.cur.fetchone()
        
        
    def db_termination(self):
        self.cur.close()
        self.conn.close() 

class RideModel():
    def __init__(self, ridecreator, destination, departure, fare, d_date, request):
        self.ridecreator = ridecreator
        self.destination = destination
        self.departure = departure
        self.fare = fare
        self.d_date = d_date
        self.request = request

        try:
            self.conn = psycopg2.connect(dbname="postgres", user="postgres", host="localhost", password="XABC", port=5432)
        except:
            print("cant connect")
            
        self.cur=self.conn.cursor()

    def save(self):
        self.cur.execute(""" INSERT INTO ride_offers (ridecreator, destination, departure, fare, d_date, request)
                            VALUES (%s, %s); """
                            , (self.ridecreator, self.destination, self.departure, self.fare, self.d_date, self.request))
        self.conn.commit()

    
        
