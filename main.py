from customer import Customer
from country import Country
from query import Query
# define the main class to execute your program
class main:
    
    def __init__(self):
        pass
    
if __name__ == "__main__":

    # load resources from db "customer" and "country"
    
    table_customer = Customer()
    table_country = Country()
    
    #try customer result
    table_customer.get_customers()
    table_customer.count_customer()
    table_customer.search_by_name("Lind")
    
    #tru country result
    table_country.get_countries()
    table_country.count_countries()
    table_country.search_by_name("Afg")