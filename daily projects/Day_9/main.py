import art
from replit import clear

print(art.logo) #logo

bidders_information = {}

def biggest_bidder(bid):
  max_bidder = 0
  biggest_bidder = ""
  for each_item in bid:
    if max_bidder < bid[each_item]:
      max_bidder = bid[each_item]
      biggest_bidder = each_item # from angela code
      
  print(f"The winner is {biggest_bidder} with a bid of ${max_bidder} ")

  # mine execution
  # for each_item in bidders_information:
  #   if max_bidder == bidders_information[each_item]:
  
# main execution
should_continue = True
while should_continue:
  name = input("What is your name?: ")
  bid = int(input("What is your bid? $"))
  
  # bidders_information .update({name:bid}) # my execution
  bidders_information[name] = bid #angela execution
  result = input("Are there any bidders? type 'yes' or 'no'. ")
  
  if result == "no":
    should_continue = False
    biggest_bidder(bidders_information)
  else:
    clear()

