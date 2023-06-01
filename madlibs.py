# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____"

# youtuber = "Fajorin Damilola"

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

verb1 = input("input verb " )
verb2 = input("input verb " )
adj = input("input adjective ")
famous_person = input("input famous person ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \ I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)