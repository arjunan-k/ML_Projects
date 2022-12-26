# ------------------------------------Process Started------------------------------------- #

# Importing the two classes.
from zillow import Zillow
from google_forms import GoogleForms

# Calling the classes.
form = GoogleForms()
zillow = Zillow()

# Getting the list of address/price/link by calling methods in Zillow class.
address = zillow.address_list()
price = zillow.price_list()
link = zillow.link_list()

# Adding the details to google forms by method in GoogleForms class.
for n in range(len(address)):
    form.fill_form(address[n], price[n], link[n])

# ------------------------------------Process Finished------------------------------------ #