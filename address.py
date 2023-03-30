# importing the necessary classes/libraries
from query import Query

class Address:
    #declaring variables outside default init to avoid that these variables reinstantiate on each loop (see get_countr())

    list_addresses = list()
    filtered_result = list()
    query = Query()
 
    
    def __init__(self):
        self.table_name = "address"
        self.id = int()
        self.address = str()
        self.postal_code = int()
        
        
    def get_addresses(self):
        result = self.query.select_from_table(self.table_name)
        for address in result:
            c = Address()
            c.id = address[0]
            c.address = address[1]
            c.postal_code = address[5]
            self.list_addresses.append(c)

    def count_addresses(self):
        print(len(self.list_addresses))
        

    def find_by_id(self, id):
        for address in self.list_addresses:
            if id == address.id:
                print(address.__str__())
                return address.address
                
    def __str__(self):
        print(f"Address Id:\t{self.id}")
        print(f"Address:\t{self.address}")
        print(f"Postal code:\t{self.postal_code}")
        

