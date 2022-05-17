from main import *

def test_domain_name():
    assert domain_name("http://github.com/carbonfive/raygun") == "github"

