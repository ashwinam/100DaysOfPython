import art
from replit import clear

print(art.logo) #logo

bidders_information = {}

def biggest_bidder():
  max_bidder = 0
  for each_item in bidders_information:
    if max_bidder < bidders_information[each_item]:
      max_bidder = bidders_information[each_item]

  for each_item in bidders_information:
    if max_bidder == bidders_information[each_item]:
      print(f"The winner is {each_item} with a bid of ${max_bidder} ")
  
# main execution
should_continue = True
while should_continue:
  name = input("What is your name?: ")
  bid = int(input("What is your bid? $"))
  
  bidders_information .update({name:bid})
  result = input("Are there any bidders? type 'yes' or 'no'. ")
  
  if result == "no":
    should_continue = False
  else:
    clear()

biggest_bidder()
