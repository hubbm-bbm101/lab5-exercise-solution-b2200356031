valid_email = False
while valid_email == False:
  email = input("Please enter your email:")
  if "@" in email and "." in email:
        valid_email = True
        print ("Thank you.")
  else:
        print("Please enter a valid email.")