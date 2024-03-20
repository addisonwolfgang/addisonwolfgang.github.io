import random
name = "Addison"
question = "Will I continue to get better at coding?"
answer = ""
random_number = random.randint(1, 11)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "There's always a chance"
elif random_number == 11:
  answer = "Never gonna happen"
else:
  answer = "Error"

if question == "":
  print("You need to ask the Magic 8-Ball a question.")
elif name == "":
  print("Question:", question)
  print("Magic 8-Ball's Answer:" , answer)

else:
  print(name + " asks:", question)
  print("Magic 8-Ball's Answer:" , answer)
