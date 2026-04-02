def factorial(x):
    if(x < 0):
        return -1
    if(x == 1 or x == 0):
        return 1
    sum = x * factorial(x - 1)
    return sum

x = int(input("Enter x: "))
n = int(input(("Enter n: ")))

print("For a singular cycle, the result is: ")
result = lambda x, n: (x**n) / factorial(n)
print(result(x, n))

print("The sum of a proper calc is: ")

def exp_x(x, n):
    tot = 0
    for k in range(n):
        tot = tot + (x**k) / factorial(k)
    return tot

print(exp_x(x, n))


bot = 0.0
def solve(n):
   global bot
   if n <= 0.0 :
       return
   solve(n - 1)
   if n % 2 != 0:
       bot += 1.0/n
   else:
       bot -= 1.0/n

times = int(input("how many timres?"))
solve(times)
print(bot)

