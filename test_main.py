from main import *

def test_domain_name_1():
    assert domain_name("http://github.com/carbonfive/raygun") == "github"

def test_domain_name_2():
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"

def test_domain_name_3():
    assert domain_name("https://www.cnet.com") == "cnet"

def test_domain_name_4():
    assert domain_name("http://google.co.jp") == "google"

def test_domain_name_5():
    assert domain_name("www.xakep.ru") == "xakep"

