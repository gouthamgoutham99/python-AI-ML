numbers = list(map(int, input("Enter six numbers separated by space: ").split()))

product = 1
for n in numbers:
  product*= n
print("the product of the numbers is :", product)
