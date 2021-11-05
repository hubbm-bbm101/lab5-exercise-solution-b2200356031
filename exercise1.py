N = input("Please enter a N value")
evenSum=0
evenNuCou=0
oddSum=0
for i in range(1,int(N)+1):
  if i%2==0 :
    evenSum+=i
    evenNuCou+=1
  else:
    oddSum+=i
print(oddSum)
print(evenSum/evenNuCou)
    