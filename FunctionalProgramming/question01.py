#Cameron Cheng
#CS3035-01


def add(x,y):
    return x+y
def mult(x,y):
    return x*y

def process_digits(n, operation1):
    if n > 0:
        x = n % 10
        xx = n // 10
        y = xx % 10
        z = xx // 10
        op = operation1(x,y)
        return operation1(process_digits(z, operation1), op)
    else:
        return 0
def main():

    int1 = int(input("Enter a number: "))
    print(process_digits(int1,add))
    print(process_digits(int1,mult))

main()