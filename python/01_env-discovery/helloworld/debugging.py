# Program to check Armstrong numbers in a certain interval
# A positive integer is called an Armstrong number of order n if
#  abcd... = a^n + b^n + c^n + d^n + ..

lower = 10
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       errorbyzerp= digit/sum
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)