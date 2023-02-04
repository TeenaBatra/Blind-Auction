from replit import clear

from art import logo

print(logo)
end_of_game=False
print("Welcome to the secret auction game.")
list_of_bids=[]
def add_to_list(name,bid):
  bids_dictionary={}
  bids_dictionary["name"]=name
  bids_dictionary["bid"]=bid
  list_of_bids.append(bids_dictionary)
def max_bid():
  for i in range(0,len(list_of_bids)):
    temp_dict=list_of_bids[i]
    temp_dict["bid"]
    if i==0:
      max=temp_dict["bid"]
    if temp_dict["bid"]>max:
      max=temp_dict["bid"]
  print(f"The max bid for this auction is: {max}")
  
while end_of_game!=True:
  name=input("What's your name? ")
  bid=input("What's your bid? ")
  add_to_list(name,bid)
  new_bid=input("Anyone else to place bid? Yes or No\n").lower()

  if new_bid=="yes":
    clear()
  else:
    end_of_game=True
    max_bid()
  


