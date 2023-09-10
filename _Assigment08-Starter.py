# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# GPabla,9.8.2023,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
lstOfFileData = []
choice_str = ''


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        GPabla,9.8.2023,Modified code to complete assignment 8
    """

    # Constructor
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    # Properties
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, name):
        if not str(name).isnumeric():
            self.__product_name = name
        else:
            raise Exception("Please do not include numbers in the product name.")

    @property
    def product_price(self):
        return str(self.__product_price).title()

    @product_price.setter
    def product_price(self, price):
        if str(price).isnumeric():
            self.__product_price = price
        else:
            raise Exception("Please do not include alpha characters for the product value.")

    # Methods
    def __str__(self):
        """  Returns object data in a comma separated string of values

        :return: (string) CSV data
        """
        object_data_csv = self.product_name + ',' + self.product_price
        return object_data_csv

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #


class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        GPabla,9.8.2023,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """ Saves data from a list of product objects to a File

                :param file_name: (string) with name of file:
                :param list_of_product_objects: (list) you want filled with file data:
                :return: (list) of product objects
                """

        try:
            obj_file = open(file_name, 'w')
            for row in list_of_product_objects:
                obj_file.write(row.__str__() + '\n')
            obj_file.close()
            print("Save was successful!")

        except Exception as e:
            print("Save was not successful, please try again.")
            print(e, e.__doc__, type(e), sep='\n')
        return lstOfProductObjects

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of product objects

                :param file_name: (string) with name of file:
                :return: (list) of product objects
                """

        list_of_rows = []
        try:
            obj_file = open(file_name, 'r')
            for line in obj_file:
                row = line.split(',')
                list_of_rows.append(row)
            obj_file.close()

        except Exception as e:
            print("There was a general error, please try again.")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """  A class for performing Input and Output

    methods:
        print_menu_items():

        input_menu_choice():

        print_current_list_items(list_of_rows):

        input_product_data():

        remove_product_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        GPabla,9.8.2023,Modified code to complete assignment 8
    """

    # Add code to show menu to user (Done for you as an example)
    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user

        :return: nothing
        """

        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Remove an existing item
        4) Save Data to File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

                :return: string
                """

        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Shows the current product names and prices in the list of product objects

                :param list_of_rows: (list) of rows you want to display
                :return: nothing
                """

        print("The current products defined are:")
        for row in list_of_rows:
            print(row.__str__())
        print()  # Add an extra line for looks

    @staticmethod
    def input_product_data():
        """  Gets data for a product object

                :return: (product) object with input data
                """
        prod = None
        try:
            product_name = str(input("Please enter a product: ")).strip()
            product_price = str(input("Please assign a price to the product: ")).strip()
            print()
            prod = Product(product_name, product_price)
        except Exception as e:
            print(e)
        return prod

    @staticmethod
    def remove_product_data():
        """  Gets the product name to be removed from the list

                :return: (string) with product
                """
        remove_product_name = str(input("Which product would you like to remove:"))
        return remove_product_name

# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfFileData = FileProcessor.read_data_from_file(strFileName)

for row in lstOfFileData:
    lstOfProductObjects.append(Product(row[0], row[1].strip()))

IO.print_current_list_items(lstOfProductObjects)

# Show user a menu of options
while True:
    IO.print_menu_items()

# Get user's menu option choice
    choice_str = IO.input_menu_choice()

# Show user current data in the list of product objects
    if choice_str.strip() == '1':
        if (None in lstOfProductObjects):
            lstOfProductObjects.remove(None)
        IO.print_current_list_items(lstOfProductObjects)
        continue

# Let user add data to the list of product objects
    elif choice_str.strip() == '2':
        lstOfProductObjects.append(IO.input_product_data())
        continue

# Let user remove data from the list of product objects
    elif choice_str.strip() == '3':
        str_remove = IO.remove_product_data()
        for row in lstOfProductObjects:
            if str(row.product_name.lower() == str_remove.lower()):
                lstOfProductObjects.remove(row)
        continue

# let user save current data to file and exit program
    elif choice_str.strip() == '4':
        lstOfProductObjects = FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        continue

    elif choice_str.strip() == '5':
        break
# Main Body of Script  ---------------------------------------------------- #
