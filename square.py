def main():
    x = int(input("What's x? "))
    print(f"{x} squared is", square(x))

def square(n):
#    return n ** 2
    return pow(n, 2)

main()