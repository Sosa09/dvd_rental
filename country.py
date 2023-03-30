# importing the necessary classes/libraries
from query import Query

class Country:
    #declaring variables outside default init to avoid that these variables reinstantiate on each loop (see get_countr())

    list_countries = list()
    filtered_result = list()
    
    
    def __init__(self):
        self.table_name = "country"
        self.name = str()
        self.id = int()
        self.query = Query()
    
    def get_countries(self):
        result = self.query.select_from_table(self.table_name)
        for country in result:
            c = Country()
            c.id = country[0]
            c.name = country[1]
            self.list_countries.append(c)
            
    def count_countries(self):
        print(len(self.list_countries))
            
    def count_special(self):
        # will inculde a loop to let the end user choose the type of filter he wants
        # beginswith, last, name like xxx
        pass
    
    def search_by_name(self, name):
        self.filtered_result = list(filter(lambda c: name in c.name, self.list_countries))
        for country in self.filtered_result:
            print(country.__str__());
            
    def __str__(self):
        print(f"Country Name:{self.name}")
        print(f"Country Id:  {self.id}")
   
        