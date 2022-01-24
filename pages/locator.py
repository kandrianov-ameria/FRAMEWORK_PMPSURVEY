from collections import namedtuple

Locator = namedtuple("Locator", ["by", "value"])

def assert_success(*args):
    if args == None:
        print("Assert success!")
    if args != None:
        print(f"Assert success! {args}")
    return True

