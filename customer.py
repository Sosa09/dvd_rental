from sqlalchemy import Table, Column, select
from address import Address
from connectie_db import SQL_connectie
from query import Query

class Customer():
    
    list_customers = list()
    filtered_result = list()
    query = Query()
    def __init__(self):
        self.tablename = "customer"
        self.customer_id = int()
        self.store_id = int()
        self.first_name = str()
        self.last_name = str()
        self.full_name = str()
        self.email = str()
        self.address_id = str()
        self.address_name = str()
                   

    def get_customers(self, adr):
        # get all customers from db
        customers = self.query.select_from_table(self.tablename)
        address = adr
        #iterate the customers from db and store them in the list_customers list
        for customer in customers:
        
            c = Customer()           
            c.customer_id = customer[0]
            c.store_id = customer[1]
            c.first_name = customer[2]
            c.last_name = customer[3]
            c.full_name = c.first_name + " " + c.last_name
            c.email = customer[4]
            c.address_id = customer[5]
            c.address_name = address.find_by_id(c.address_id)
            
            self.list_customers.append(c)
 
    def count_customer(self):
        print(len(self.list_customers))                
   
    def count_special(self):
        # will inculde a loop to let the end user choose the type of filter he wants
        # beginswith, last, name like xxx
        pass    
    
    def search_by_name(self, name):
        #this filter uses select of the given name by the user to search into the db result
        self.filtered_result = list(filter(lambda c: name in c.first_name, self.list_customers))
        for customer in self.filtered_result:
            print(customer.__str__());
    
    def search_by_id():
        pass
    
    def __str__(self):
        print(f"Name:        {self.full_name}")
        print(f"Address:     {self.address_name}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Store ID:    {self.store_id}")
        print(f"email:       {self.email}")
    

        
            
    
