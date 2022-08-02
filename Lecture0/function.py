#Define a main function
def main():
    name = input("What's your name? ").title()
    hello(name)

#Define a function with an input parameter
def hello(to="Visitor"):
    print("Hello!", to)

main()