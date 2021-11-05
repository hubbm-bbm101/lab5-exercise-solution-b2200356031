import random
n = random.randint(0,80)
while True:
  guess = input("Plase make your guess.")
  if int(guess) > n :
      print ("Decrease your number.")
  elif int(guess) < n :
      print ("Increase your number.")
  else:
      print ("Your guess is corect.")
      break

