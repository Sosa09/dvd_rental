# importing the necessary classes/libraries
from connectie_db import SQL_connectie
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, func, desc, select

class Query(SQL_connectie):

    def __init__(self):
        super().__init__()
        
    
    def select_from_table(self, tablename, table = None):

        # check if connection is alive before excecuting
        # if self.connection_alive == False:
        
                    
        table_query = Table(tablename,self.meta_data,autoload_with=self.connection.engine)
        if(table != None):
            table_query = table
        
        s = table_query.select()
        rp = self.connection.execute(s)
        results = rp.fetchall()
        return results

    #function created for refactoring Customer and country or for single searches 
    def count_from_table():
        pass
    
    def select_from_table_by_id():
        pass
    
    def select_from_table_by_name():
        pass


    