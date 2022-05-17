import re


# This function parses out just the domain name
def domain_name(URL_string):
    return re.sub(r"http.*://|www.|\..*", "", URL_string)