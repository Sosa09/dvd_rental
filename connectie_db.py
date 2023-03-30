import sqlalchemy
class SQL_connectie:
    def __init__(self, db="dvdrental", host="localhost:5432"):
        # //open connection
        self.engine = None
        self.db = db
        self.host = host
        self.meta_data = None
        self.connection = None
        self.connection_succes = False
        self.open_db_connection() 
        
                    
    def open_db_connection(self):
        # TODO add precheck like do you want tu use self.db as db if yes continue no ask user to put the db name he wants to use
        #print the db and host that will be used in this program
        print(f"using db = {self.db}\n using host = {self.host}")
        
        # asking the end user to enter his username/password in order to auth to the db local server
        username = input("enter your username:\n")
        pwd = input("Enter your password\n")    
        
         
        self.engine = sqlalchemy.create_engine(f'postgresql+psycopg2://{username}:{pwd}@{self.host}/{self.db}')
        #try to open 
        try:   

            self.connection = self.engine.connect()            
            self.meta_data = sqlalchemy.MetaData()
            self.connection_succes = True
        except Exception as e:
            print(e);
            print("connection failed try again");
            self.open_db_connection()
            
    def close_db_connection(self):
        #Dispose the connection after you finished with your program
        self.connection = self.engine.dispose()
        pass
    def connection_alive(self):
        if(self.connection_succes == False or self.connection.closed or self.connection):
            print("connection is not open, check your network settings or try to re enter your password")
            q = input("do you want to try to put connect ? (Y/n)\n")
            if(q.lower() == 'y'):
                self.open_db_connection()              
            else:
                print("Connection is closed")
                return False
        else:          
            print("Connection is open let's begin") 
            return True

    