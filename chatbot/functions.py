import possible_incomming


def initial_state():
    response_body = "Hello! How can we help you? \n 1. Search for help \n 2. Become a Sponsor \n Reply either with 1 or 2"
    return response_body

def switchtosearch_state():
    response_body = "What kind of service are you looking for? \n 1. House Help \n 2. Car Wash \n 3. Electricitan \n Reply either with appropriate number."
    return response_body


#sponsor

def switchtosponsor_state():
    response_body = "Thank you for applying for sponsorship \n Let's get started \n Please enter your name"
    return response_body

def sponsor_name(name):
    name = name.title()
    response_body = "Hi! {}, \n please enter your address".format(name)
    return response_body

def sponsor_address(address):
    address = address.title()
    response_body = "Your address is:\n {}, \n Please enter the name of the individual you want to sponsor:".format(address)
    return response_body

def sponsor_individualname(individualname):
    individualname = individualname.title()
    response_body = "You want to sponsor:\n {}, \n Please enter their contact number:".format(individualname)
    return response_body


def sponsor_individualnumber(individualnumber):
    individualnumber = individualnumber.title()
    response_body = "The individual's number is:\n {}, \n Please take a picture of theirs and send it.".format(individualnumber)
    return response_body

def sponsor_individualpicture(individualpicture):
    response_body = "The individual's image uploaded is:\n {}, \n Thank you.".format(individualpicture)
    return response_body
