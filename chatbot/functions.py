import possible_incomming

professions_dict = {
    "1": "House Help",
    "2" : "Car Wash",
    "3" : "Electrician"
}

def initial_state():
    response_body = "Hello! Welcome to the Kaamdey Whatsapp service! We help you find and connect to your nearest professionals. \n\nHow can we help you? \n1. Search for help \n2. Become a Sponsor \n3. Request for profession inclusion \n\nReply either with 1,2,3 or reset to restart your session \n\nLanguages:\n*हिंदी के लिए 4 दबाएं* \n*ಕನ್ನಡಕ್ಕಾಗಿ 5 ಒತ್ತಿರಿ*\nYou may also use our web portal for additional information:\n http://86feca20bbc7.ngrok.io"
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
    response_body = "Here are a few individuals you may contact:\n"
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
    response_body = "You want to sponsor:\n{}, \nPlease select their profession: \n1. House Help \n2. Car Wash \n3. Electrician \nReply either with appropriate number.".format(individualname)
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
    response_body = "The individual's number is:\n{}, \nPlease enter any hourly or monthly wage requirements".format(individualnumber)
    return response_body

def sponsor_individualwages(individualwages):
    response_body = "Thank you for the wage details,\nPlease enter a short review of the professional."
    return response_body

def sponsor_individualreview(individualreview):
    response_body = "Thank you for the review,\nPlease take a picture of theirs and send it."
    return response_body

def sponsor_individualpicture(individualpicture):
    response_body = "Thank you for registering the individual." + "\n\nHow can we help you further? \n1. Search for help \n2. Become a Sponsor \n3. Request for profession inclusion \n\nReply either with 1,2,3 or reset to restart your session"
    return response_body


############################################################################################################
#profession inclusion
def profession_inclusion():
    response_body = "Please enter the profession you would like to include."
    return response_body


# #profession inclusion pt 2
def profession_acception(profession):
    print("HERE!")
    listOfProfessions = ["house help","car wash","electrician"]
    if(profession not in listOfProfessions):
        response_body = "Thank you for requesting a new profession inclusion."
        return response_body,True
    else:
        response_body = "The profession already exists, please try again." + "\n\nHow can we help you further? \n1. Search for help \n2. Become a Sponsor \n3. Request for profession inclusion \n\nReply either with 1,2,3 or reset to restart your session"
        return response_body,False

