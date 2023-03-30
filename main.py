from customer import Customer
from country import Country
from address import Address

# define the main class to execute your program
class main:

    def __init__(self):
        pass

if __name__ == "__main__":

    # load resources from db "customer" and "country"

    table_customer = Customer()
    # table_country = Country()
    table_address = Address()


    #tru country result
    table_address.get_addresses()
    # print(table_address.list_addresses)
    table_address.count_addresses()
    table_address.find_by_id(12)

    # #try customer result
    table_customer.get_customers(table_address)
    table_customer.count_customer()
    table_customer.search_by_name("Lind")

    # #tru country result
    # table_country.get_countries()
    # table_country.count_countries()
    # table_country.search_by_name("Afg")

