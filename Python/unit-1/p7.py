# p7 : To read a card as input and output if the card is lucky or not.

c=input("Enter Any Suit with Card : ")

suit,card=c.split()

if(suit=='diamond' and suit=='spade' or card=='queen' or card=='king'):
  print("Card is Lucky")
else:
  print("Please,try next time")