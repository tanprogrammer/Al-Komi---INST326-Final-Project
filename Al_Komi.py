import random as r 


#Colette's class - text me if you guys have any questions 
class Deck:
    '''docstring
    '''
    def __init__(self, deck_cards, player1_hand, player2_hand, table_hand):
        '''Initializes class attributes. 
        '''
        self.deck_cards = [
            '1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 
            'QH', 'KH', '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 
            '10S', 'JS', 'QS', 'KS','1C', '2C', '3C', '4C', '5C', '6C', '7C', 
            '8C', '9C', '10C', 'JC', 'QC', 'KC', '1D', '2D', '3D', '4D', '5D', 
            '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD'
            ]
        self.player1_hand = []
        self.player2_hand = []
        self.table_hand = []
        
    def shuffle_deck(self):
        '''Shuffles deck for the game. 
        '''
        r.shuffle(self.deck_cards)

        
    def deal_cards(self, num_players): 
        '''Deals cards to players and table. 
        '''
        #value error lines 
        if num_players !=2:
            raise ValueError("You have inputted an invalid number of players.")
        else:
            self.num_players = num_players 
        
        #num cards per player/hand    
        hand_size = 4
        #now deal with wild cards in table hand (put as a set)
        wildcards = {'7D', 'JD', 'JH', 'JC', 'JS'}
        
        #table hand 
        while len(self.table_hand) < hand_size: #iteration requirement 
            card = self.deck_cards.pop()
            #return to deck if wild card
            if card in wildcards: #conditional branching requirement 
                self.deck_cards.insert(0, card) #back to bottom of deck 
                self.shuffle_deck() #use shuffle method established earlier 
                continue 
            #if not a wildcard, deal to table 
            elif card not in wildcards:
                self.table_hand.append(card)
                print(f"Table hand is: {self.table_hand}.")
            else:
                print("Error.")
        
        #player hands   
        self.player1_hand = [self.deck_cards.pop() for _ in range(hand_size)]  
        print(f"Player 1 hand is: {self.player1_hand}.") #check  
        self.player2_hand = [self.deck_cards.pop() for _ in range(hand_size)] 
        print(f"Player 2 hand is: {self.player2_hand}.") #check 
        
        #returns tuple of hands
        return self.player1_hand, self.player2_hand, self.table_hand  
           
  
  
