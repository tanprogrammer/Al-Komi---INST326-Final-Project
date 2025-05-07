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

def match(cards_hand, cards_table):
    matched_dict = {}
    for card1 in cards_hand:
        #Sequence of Steps: Check one card from the hand
        #Iteration: for each card in hand
        if card1 != "7D" and card1[0] != "J" and card1[0] != "K" and card1[0]\
            != "Q": #Conditional branching: check if the card is a wild card or is Queen or King
            temp_value = int(card1[:-1])
            for card2 in cards_table:
                #Sequence of Steps: Check card on table compared to one in hand
                #Iteration: for each card on table
                if card2 != "7D" and card2[0] != "J" and card2[0] != "K" and\
                    card2[0] != "Q":
                    #Conditional branching: check if the card is a wild card or is Queen or King
                    other_cards = list(cards_table)
                    other_cards.remove(card2)
                    if card1[:-1] == card2[:-1]: #Conditional branching: check if card in hand is card on table
                        matched_dict[card1] = [card2]
                    for other in other_cards:
                        #Sequencing of Steps: checks the sum of two cards on the table to card in hand
                        #Iteration: for each card other than the one being compared
                        if other != "7D" and other[0] != "J" and other[0] !=\
                            "K" and other[0] != "Q": #Conditional branching: check if the card is a wild card or is Queen or King
                            otherother_cards = list(other_cards)
                            otherother_cards.remove(other)
                            if int(card2[:-1]) + int(other[:-1]) == temp_value:
                                #Conditional branching: if sum of two cards equals to card in hand
                                matched_dict[card1] = [card2, other]
                            for otherother in otherother_cards:
                                #Sequencing of Steps: checks the sum of three cards on the table to card in hand
                                #Iteration: for each card other than the one being compared and the other card being added
                                if other != "7D" and other[0] != "J" and\
                                other[0] != "K" and other[0] != "Q": #Conditional branching: check if the card is a wild card or is Queen or King
                                    if int(card2[:-1]) + int(other[:-1]) + int(otherother[:-1]) == temp_value:
                                        #Conditional branching: if sum of three cards equals to card in hand
                                        matched_dict[card1] = [card2, other, otherother]
    return matched_dict
    #returns a dictionary of matched cards with the key as cards from your hand
    #and the values being the combinations of cards on the table.


table_cards = []

class Player():
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []
        self.face_up = 0
        self.face_down = 0
        self.combo_dict = {}
    
    def turn (self):
        raise NotImplementedError
    
    def calc_score(self, opponent):
        score = 0
        score += (self.face_up * 10)
        if self.face_down > opponent.face_down:
            score += 30
        return score
    
    def determine_komi(self, cards, table_cards):
        temp_list = table_cards
        if cards == ["7D"] or cards == ["JH"] or cards == ["JC"]\
        or cards == ["JD"] or cards == ["JS"]:
            self.face_up += 1
        for card in cards:
            temp_list.remove(card)
        if len(temp_list) == 0:
            self.face_up += 1
    
class HumanPlayer(Player):
    def __init__(self, table_cards):
        self.cards_in_hand = []
        
    def turn(self, gamestate, table_cards):
        self.combo_dict = match(self.cards_in_hand, table_cards)
        print(gamestate)
        played = input(f"{self.name}, please input the desired card from your "
                       f"hand to play: ")
        while True:
            if played in self.cards_in_hand:
                self.determine_komi(played, table_cards)
                return played
            else:
                print("This card is not in your hand.")
                played = input(f"{self.name}, please input the desired card from your "
                        f"hand to play: ")
                
class ComputerPlayer(Player):
    def __init__(self, robo_name):
        self.name = robo_name
    
    def turn (self, table_cards):
        self.combo_dict = match(self.cards_in_hand, table_cards)
        if "7D" in self.cards_in_hand:
            self.determine_komi(["7D"], table_cards)
            return "7D"
        elif "JH" in self.cards_in_hand or "JS" in self.cards_in_hand\
        or "JD" in self.cards_in_hand or "JC" in self.cards_in_hand:
            for card1 in self.cards_in_hand:
                if card1 == "JH" or card1 == "JS" or card1 == "JD"\
                or card1 == "JC":
                    self.determine_komi([card1], table_cards)
                    return card1
        else:
            for card2 in self.cards_in_hand:
                if card2[:-1] == "Q" or card2[:-1] == "K":
                    self.determine_komi([card2], table_cards)
                    self.face_down += 2
                    return card2
        if self.combo_dict != {}:
            for combo in self.combo_dict:
                if len(self.combo_dict[combo]) == 3:
                    self.determine_komi(self.combo_dict[combo], table_cards)
                    self.face_down += 4
                    return combo
            for combo in self.combo_dict:
                if len(self.combo_dict[combo]) == 2:
                    self.determine_komi(self.combo_dict[combo], table_cards)
                    self.face_down += 3
                    return combo
            for combo in self.combo_dict:
                if len(self.combo_dict[combo]) == 1:
                    self.determine_komi(self.combo_dict[combo], table_cards)
                    self.face_down += 2
                    return combo
        else:
            placed_card = self.cards_in_hand.pop(0)
            return f"Places {placed_card}"

class Gamestate:
    def __init__(self, ):
        