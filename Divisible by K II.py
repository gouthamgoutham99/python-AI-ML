num = int(input("enter a number:"))
k = int(input("enter a k value:"))
sum = 0
for i in range(1, num+1):
  if i % k ==0:
    sum+= i
print(sum)
