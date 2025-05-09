import random as r 
from argparse import ArgumentParser
import sys

#Colette's class - text me if you guys have any questions
class Deck:
    '''docstring
    '''
    def __init__(self):
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
        if num_players != 1:
            raise ValueError("You have inputted an invalid number of players.")
        else:
            self.num_players = num_players
        
        #num cards per player/hand    
        hand_size = 4
        #now deal with wild cards in table hand (put as a set)
        wildcards = {'7D', 'JD', 'JH', 'JC', 'JS'}
        self.shuffle_deck()
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
            else:
                print("Error.")
        
        #player hands   
        self.player1_hand = [self.deck_cards.pop() for _ in range(hand_size)]  
        self.player2_hand = [self.deck_cards.pop() for _ in range(hand_size)] 
        
        #returns tuple of hands
        return self.player1_hand, self.player2_hand, self.table_hand 

def match(cards_hand, cards_table):
    matched_dict = {}
    for card1 in cards_hand:
        if card1 != "7D" and card1[:-1] != "J" and card1[:-1] != "K" and card1[:-1]\
            != "Q":
            temp_value = int(card1[:-1])
            for card2 in cards_table:
                if card2 != "7D" and card2[:-1] != "J" and card2[:-1] != "K" and\
                    card2[:-1] != "Q":
                    other_cards = list(cards_table)
                    other_cards.remove(card2)
                    if card1[:-1] == card2[:-1]: 
                        matched_dict[card1] = [card2]
                    for other in other_cards:
                        if other != "7D" and other[:-1] != "J" and other[:-1] !=\
                            "K" and other[:-1] != "Q":
                            otherother_cards = list(other_cards)
                            otherother_cards.remove(other)
                            if int(card2[:-1]) + int(other[:-1]) == temp_value:
                                matched_dict[card1] = [card2, other]
                            for otherother in otherother_cards:
                                if otherother != "7D" and otherother[:-1] != "J" and\
                                otherother[:-1] != "K" and otherother[:-1] != "Q":
                                    if int(card2[:-1]) + int(other[:-1]) + int(otherother[:-1]) == temp_value:
                                        matched_dict[card1] = [card2, other, otherother]
    return matched_dict

def evaluate_play(player, played_card, table_cards):
    table_cards_num = []
    for card in table_cards:
        table_cards_num.append(card[:-1])
    if played_card in player.combo_dict:
        player.cards_in_hand.remove(played_card)
        for card in player.combo_dict[played_card]:
            table_cards.remove(card)
        return player.cards_in_hand, table_cards
    elif played_card == "7D" or played_card == "JC" or played_card == "JD"\
    or played_card == "JS" or played_card == "JH":
        player.cards_in_hand.remove(played_card)
        table_cards = []
        return player.cards_in_hand, table_cards
    else:
        if played_card[:-1] in table_cards_num:
            player.cards_in_hand.remove(played_card)
            for card in table_cards:
                if card[:-1] == played_card[:-1]:
                    table_cards.remove(card)
            return player.cards_in_hand, table_cards
        else:
            player.cards_in_hand.remove(played_card)
            table_cards.append(played_card)
            return player.cards_in_hand, table_cards
            
class Gamestate:
    """Game state class."""
    def __init__(self, players, table_cards, current_turn=0):
        self.players = players
        self.table_cards = table_cards  
        self.current_turn = current_turn
    
    def __str__(self):
        return (
            f"Current turn: {self.players[self.current_turn].name}, "
            f"Table cards: {self.table_cards}, "
            f"{self.players[self.current_turn].name}'s score: {self.players[self.current_turn].score}"
        )

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)
        
    def update(self, table_cards):
        self.table_cards = table_cards   

class Player():
    def __init__(self, name, player_hand):
        self.name = name
        self.cards_in_hand = list(player_hand)
        self.face_up = 0
        self.face_down = 0
        self.combo_dict = {}
        self.score = 0
    
    def turn (self):
        raise NotImplementedError
    
    def calc_score(self, opponent):
        if self.face_up != 0:
            self.score += (self.face_up * 10)
            self.face_up -= (1 * self.face_up)
        if self.face_down > opponent.face_down and self.score >= 40:
            self.score += 30

    def determine_komi(self, cards, table_cards):
        if len(cards) == 1:
            temp_list = []
            for card in table_cards:
                temp_list.append(card[:-1])
            if cards == ["7D"]:
                self.face_up += 1
            elif cards[0][:-1] in temp_list:
                for value in temp_list:
                    if str(value) == str(cards[0][:-1]):
                        temp_list.remove(cards[0][:-1])
            if len(temp_list) == 0:
                self.face_up += 1
        else:
            temp_list = table_cards.copy()
            for card in cards:
                temp_list.remove(card)
            if len(temp_list) == 0:
                self.face_up += 1 
    
    def add_face_down(self, played_card, table_cards):
        if played_card in self.combo_dict:
            self.face_down += (1 + len(self.combo_dict[played_card]))
        if played_card == "JS" or played_card == "JD"\
        or played_card == "JH" or played_card == "JC":
            self.face_down += len(table_cards)
        elif played_card[:-1] == "K" or played_card[:-1] == "Q":
            for card in table_cards:
                if played_card == card:
                    self.face_down += 2
    
class HumanPlayer(Player):   
    def turn(self, gamestate, table_cards):
        self.combo_dict = match(self.cards_in_hand, table_cards)
        print(gamestate)
        print(f"Your hand: {self.cards_in_hand}")
        played = input(f"{self.name}, please input the desired card from your "
                       f"hand to play: ")
        if played == "exit":
            raise ValueError
        while True:
            if played in self.cards_in_hand:
                self.determine_komi([played], table_cards)
                self.add_face_down(played, table_cards)
                return played
            else:
                print("This card is not in your hand.")
                played = input(f"{self.name}, please input the desired card from your "
                        f"hand to play: ")
                
class ComputerPlayer(Player):
    def turn (self, table_cards):
        self.combo_dict = match(self.cards_in_hand, table_cards)
        if "7D" in self.cards_in_hand:
            self.determine_komi(["7D"], table_cards)
            print(f"{self.name} just played the 7D")
            return "7D"
        elif "JH" in self.cards_in_hand or "JS" in self.cards_in_hand\
        or "JD" in self.cards_in_hand or "JC" in self.cards_in_hand:
            for card1 in self.cards_in_hand:
                if card1 == "JH" or card1 == "JS" or card1 == "JD"\
                or card1 == "JC":
                    print(f"{self.name} just played the {card1}")
                    return card1
        else:
            for card2 in self.cards_in_hand:
                if card2[:-1] == "Q" or card2[:-1] == "K":
                    self.determine_komi([card2], table_cards)
                    self.face_down += 2
                    print(f"{self.name} just played the {card2}")
                    return card2
        if self.combo_dict != {}:
            for combo in self.combo_dict:
                if len(self.combo_dict[combo]) == 3:
                    self.determine_komi(self.combo_dict[combo], table_cards)
                    self.face_down += 4
                    print(f"{self.name} just played the {combo}")
                    return combo
            for combo in self.combo_dict:
                if len(self.combo_dict[combo]) == 2:
                    self.determine_komi(self.combo_dict[combo], table_cards)
                    self.face_down += 3
                    print(f"{self.name} just played the {combo}")
                    return combo
            for combo in self.combo_dict:
                if len(self.combo_dict[combo]) == 1:
                    self.determine_komi(self.combo_dict[combo], table_cards)
                    self.face_down += 2
                    print(f"{self.name} just played the {combo}")
                    return combo
        else:
            placed_card = self.cards_in_hand[0]
            print(f"{self.name} just played the {placed_card}")
            return placed_card
        
class Game:
    def __init__(self, players, table_cards, deck):
        self.players = players
        self.player1 = players[0]
        self.player2 = players[1]
        self.table_cards = table_cards
        self.deck = deck
        
    def restart(self, gamestate):
        if len(self.table_cards) == 0:
            wildcards = {'7D', 'JD', 'JH', 'JC', 'JS'}
            while len(self.table_cards) < 4:
                card = self.deck.deck_cards.pop()
                if card in wildcards:
                    self.deck.deck_cards.insert(0, card)
                    self.deck.shuffle_deck()
                    continue
                elif card not in wildcards:
                    self.table_cards.append(card)
                else:
                    print("Error.")
            gamestate.update(self.table_cards)
    def refill(self, player):
        player.cards_in_hand = [self.deck.deck_cards.pop() for _ in range(4)]  
        
    def start(self):
        gamestate = Gamestate(self.players, self.table_cards)
        while self.player1.score < 70 and self.player2.score < 70 and len(self.deck.deck_cards) >= 5:
            if self.players[gamestate.current_turn] == self.player1:
                played_card = self.player1.turn(gamestate, self.table_cards)
                self.player1.cards_in_hand, self.table_cards = evaluate_play(self.player1, played_card, self.table_cards)
                if len(self.table_cards) == 0:
                    self.restart(gamestate)
                if len(self.player1.cards_in_hand) == 0:
                    self.refill(self.player1)
                self.player1.calc_score(self.player2)
                gamestate.update(self.table_cards)
                gamestate.next_turn()
            elif self.players[gamestate.current_turn] == self.player2:
                played_card = self.player2.turn(self.table_cards)
                self.player2.cards_in_hand, self.table_cards = evaluate_play(self.player2, played_card, self.table_cards)
                if len(self.table_cards) == 0:
                    self.restart(gamestate)
                if len(self.player2.cards_in_hand) == 0:
                    self.refill(self.player2)
                self.player2.calc_score(self.player1)
                print(f"{self.player2.name}'s score: {self.player2.score}")
                gamestate.update(self.table_cards)
                gamestate.next_turn()
        if self.player1.score >= 70:
            print(f"{self.player1.name} IS THE WINNER!")
            print(f"{self.player1.name}'s score: {self.player1.score}")
            print(f"{self.player2.name}'s score: {self.player2.score}")
        elif self.player2.score >= 70:
            print(f"{self.player2.name} IS THE WINNER!")
            print(f"{self.player1.name}'s score: {self.player1.score}")
            print(f"{self.player2.name}'s score: {self.player2.score}")
        else:
            if self.player1.face_down > self.player2.face_down:
                self.player1.score += 30
            else:
                self.player2.score += 30
            if self.player1.score > self.player2.score:
                print(f"{self.player1.name} IS THE WINNER!")
                print(f"{self.player1.name}'s score: {self.player1.score}")
                print(f"{self.player2.name}'s score: {self.player2.score}")
            elif self.player2.score > self.player1.score:
                print(f"{self.player2.name} IS THE WINNER!")
                print(f"{self.player1.name}'s score: {self.player1.score}")
                print(f"{self.player2.name}'s score: {self.player2.score}")
            else:
                print("IT'S A TIE!")

                
def main(name):
    players = []
    deck = Deck()
    num_players = len([name])
    player1_hand, player2_hand, table_cards = deck.deal_cards(num_players)
    if num_players == 1:
        player = HumanPlayer(name, player1_hand)
        com_player = ComputerPlayer("Robot Bob", player2_hand)
        players.append(player)
        players.append(com_player)
    else:
        ValueError ("Too many players.")
    game = Game(players, table_cards, deck)
    game.start()
        
def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file where
    each line consists of a name, a tab character, and a phone number.
    
    Args:
        name(str): player's name.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("name", help="player name")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name)