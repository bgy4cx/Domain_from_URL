import re


def domain_name(URL_string):
    x = re.sub("http.*://|www.|\..*", "", URL_string)
    return x