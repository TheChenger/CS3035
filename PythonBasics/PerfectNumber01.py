num = int(input('Enter a number: '))
def perfNum(n):
    divisor = 2
    sum = 1

    while divisor * divisor < n:
        if n % divisor == 0:
            sum = sum + divisor + n/divisor
            divisor += 1
        else:
            divisor += 1

    if n == sum:
        print(n)

while num >= 6:
    perfNum(num)
    num -= 1