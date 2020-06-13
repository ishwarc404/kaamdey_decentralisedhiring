import possible_incomming

professions_dict = {
    "1": "House Help",
    "2" : "Car Wash",
    "3" : "Electrician"
}

def initial_state():
    response_body = "Hello! Welcome to the Kaamdev Whatsapp service! We help you find and connect to your nearest professionals. \nHow can we help you? \n1. Search for help \n2. Become a Sponsor \nReply either with 1 or 2"
    return response_body

############################################################################################################
#search

def switchtosearch_state():
    response_body = "What kind of service are you looking for? \n1. House Help \n2. Car Wash \n3. Electrician \nReply either with appropriate number."
    return response_body

def search_servicetype(servicetype):
    try:
        servicetype = professions_dict[servicetype]
    except:
        return "Please select the right profession option."
    response_body = "The individual's profession is:\n{}, \nPlease enter your desired address of service".format(servicetype)
    return response_body


def search_serviceaddress(serviceaddress):
    response_body = "Here are some individuals you can contact:\n"
    return response_body



############################################################################################################
#sponsor

def switchtosponsor_state():
    response_body = "Thank you for applying for sponsorship \nLet's get started \nPlease enter your name"
    return response_body

def sponsor_name(name):
    name = name.title()
    response_body = "Hi! {}, \nPlease enter your address".format(name)
    return response_body

def sponsor_address(address):
    address = address.title()
    response_body = "Your address is:\n{}, \nPlease enter the name of the individual you want to sponsor:".format(address)
    return response_body

def sponsor_individualname(individualname):
    individualname = individualname.title()
    response_body = "You want to sponsor:\n{}, \nPlease select their profession: \n1. House Help \n2. Car Wash \n3. Electricitan \nReply either with appropriate number.".format(individualname)
    return response_body

def sponsor_individualprofession(individualprofession):
    try:
        individualprofession = professions_dict[individualprofession]
    except:
        return "Please select the right profession option."
    response_body = "The individual's profession is:\n{}, \nPlease enter their address.".format(individualprofession)
    return response_body

def sponsor_individualaddress(individualaddress):
    response_body = "The individual's address is:\n{}, \nPlease enter their contact number.".format(individualaddress)
    return response_body

def sponsor_individualnumber(individualnumber):
    individualnumber = individualnumber.title()
    response_body = "The individual's number is:\n{}, \nPlease take a picture of theirs and send it.".format(individualnumber)
    return response_body

def sponsor_individualpicture(individualpicture):
    response_body = "Thank you for registering the individual."
    return response_body
