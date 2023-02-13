class Shoe:
    #method to initialise a shoe object
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #method to return cost of a shoe object
    def get_cost(self):
        return self.cost

    #method to return quantity of a shoe object
    def get_quantity(self):
        return self.quantity

    #method to print shoe object in a user friendly format
    def __str__(self):
        return(f"""Country:    {self.country}
Code:       {self.code}
Product:    {self.product}
Cost:       {self.cost}
Quantity:   {self.quantity}
""")

#instantiate list of shoes so we can iterate over it
shoe_list = []

#List of countries to compare against for shoe creation
countries = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']

#Function skips the title line of the text file then separates each individual line into a list item so we can iterate over them
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as f:
            i = 0
            for line in f:
                if i!=0:
                    line_arr = line.split(",")
                    new_shoe = Shoe(line_arr[0],line_arr[1],line_arr[2],int(line_arr[3]),int(line_arr[4].strip("\n")))
                    shoe_list.append(new_shoe)
                i+=1
    except FileNotFoundError:
        print("Oops! Please ensure that the file 'inventory.txt' is in the right place!")

#Function ensures that user-input shoe codes are 5 digits and numerical
def verify_shoe_code():
    while True:
        try:
            shoe_number = int(input("Please enter the 5 digit shoe code following 'SKU' for the item: "))
            if shoe_number/10000 >= 1 and shoe_number/100000 <= 1:
                break
            else:
                print("Oops! Please enter a 5 digit numerical code.")
        except ValueError:
            print("Oops! Please enter a 5 digit numerical code.")

    return(shoe_number)

#Function takes user input to instantiate a new object from the shoe Class and appends it to the shoe list
def capture_shoes():
    is_country = False
    while is_country == False:
        country = input("Where are the items stored? ")
        for i in countries:
            if country.lower() == i.lower():
                is_country = True
                break            
        if is_country == False:
            print("Oops! Please enter the country where these items are stored.")

    shoe_number = verify_shoe_code()            
    code = "SKU" + str(shoe_number) 

    product = input("Enter the style name of the item: ")

    while True:
        try:
            cost = int(input("Enter the individual unit price: "))
            break
        except ValueError:
            print("Oops! Please enter a numerical value.")

    while True:
        try:
            quantity = int(input("How many of the item are in stock? "))
            break
        except ValueError:
            print("Oops! Please enter a numerical value.")

    new_shoe = Shoe(country,code,product,cost,quantity)
    shoe_list.append(new_shoe)

#Function iterates over shoe list and prints each entry
def view_all():
    for shoe in shoe_list:
        print(shoe)

#Function iterates over shoe list to find the item with the lowest quantity, then prompts user to update stock total and rewrite it to text file
def re_stock():
    lowest = shoe_list[0]
    for shoe in shoe_list:
        if lowest.quantity > shoe.quantity:
            lowest = shoe

    restock = input(f"""The item with the lowest stock is the {lowest.product} with {lowest.quantity} items.
Would you like to order more stock and update this total? Y/N """)
    if restock.lower() == "y":
        while True:
            try:
                restock_amount = int(input("How many items would you like to order? "))
                break
            except ValueError:
                print(f"Oops! Please enter the number of item {lowest.product} you would like to order.")
        
        lowest.quantity = int(lowest.quantity) + restock_amount

        with open("inventory.txt", "w") as f:
            f.write("Country,Code,Product,Cost,Quantity")
            for shoe in shoe_list:
                f.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
            
#Function iterates over shoe list to return the item matching user entered shoe code or print a fail message and prompt to try again
def search_shoe():
    search_complete = False
    while search_complete == False:
        shoe_number = verify_shoe_code()             
        shoe_code = "SKU" + str(shoe_number) 

        for shoe in shoe_list:
            if shoe.code == shoe_code:
                print(shoe)
                search_complete = True
        if search_complete == False:
            try_again = input("An item matching that shoe code could not be found. Would you like to try again? Y/N ")
            if try_again.lower() == "n":
                search_complete = True
            
#function calculates and prints the value of each item in shoe list from its product and value characteristics   
def value_per_item():
    for shoe in shoe_list:
        shoe_value = shoe.get_cost() * shoe.get_quantity()
        print(f"Stock of item {shoe.product} has a value of R{shoe_value}.")

#function iterates over shoe list to find the item with the largest quantity property, then prints a message saying it is on sale
def highest_qty():
    highest = shoe_list[0]
    for shoe in shoe_list:
        if highest.quantity < shoe.quantity:
            highest = shoe

    print(f"""The product with the highest quantity of items in stock is the {highest.product} with {highest.quantity} items in stock.
{highest.product} is now on sale!""")


#Populate shoe list
read_shoes_data()

#Menu loops until user chooses the exit option.
menu = ""
while menu != "7":
    menu = input(f"""Welcome to the Nike Warehouse Stock Manager Application.
Please select a number from the options below to continue:
1 - View All
2 - Add New Item Entry
3 - Re-Stock
4 - Search Shoe Using Shoe Code
5 - Individual Item Value
6 - Determine Sale Item
7 - Quit
""")

    if menu == "1":
        view_all()

    elif menu == "2":
        capture_shoes()

    elif menu == "3":
        re_stock()

    elif menu == "4":
        search_shoe()

    elif menu == "5":
        value_per_item()

    elif menu == "6":
        highest_qty()

    elif menu == "7":
        print("Goodbye!")
    
    else:
        print("Oops! Please select a number from 1-7 to continue.")


