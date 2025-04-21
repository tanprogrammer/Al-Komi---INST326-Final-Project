#extra lines needed for deliverable function to work. Please note that these attributes were taken
#out of a draft of a class for the final submission. 

#imports
import random as r 

#attributes
deck_cards = [
            '1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 
            'QH', 'KH', '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 
            '10S', 'JS', 'QS', 'KS','1C', '2C', '3C', '4C', '5C', '6C', '7C', 
            '8C', '9C', '10C', 'JC', 'QC', 'KC', '1D', '2D', '3D', '4D', '5D', 
            '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD'
            ]
            
table_hand = []
#num cards per player/hand    
hand_size = 4
#now deal with wild cards in table hand (put as a set)
wildcards = {'7D', 'JD', 'JH', 'JC', 'JS'}


def deal_cards(): 
# dealing to table hand function  
  while len(table_hand) < hand_size: #iteration requirement 
      card = deck_cards.pop()
      #return to deck if wild card
      if card in wildcards: #conditional branching requirement 
          deck_cards.insert(0, card) #back to bottom of deck 
          #self.shuffle_deck() #use shuffle method established earlier - for final not deliverable 
          r.shuffle(deck_cards)
          continue 
      #if not a wildcard, deal to table #sequence of steps requirement 
      elif card not in wildcards:
          table_hand.append(card)
          print(f"Table hand is: {table_hand}.")
      else:
          print("Error.")