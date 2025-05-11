import random as r 
from argparse import ArgumentParser
import sys

#Colette's class - text me if you guys have any questions
class Deck:
    """"Represents the deck of cards in the game.
    
    Attributes: 
        deck_cards (list): A list of cards in the deck.
        player1_hand (list): Cards dealt to player 1.
        player2_hand (list): Cards dealt to player 2.
        table_hand (list): Cards on the table.
    Raises:
        ValueError: If the number of players is not 1.
    """
    def __init__(self):
        """Initializes the deck with 52 cards and empty hands for players.
        Args:
            self (Deck): The Deck instance.
        """
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
        """Shuffles the deck of cards.
        Args:
            self (Deck): The Deck instance.
        """
        r.shuffle(self.deck_cards)

        
    def deal_cards(self, num_players): 
        """Deals cards to players and the table.

        Args:
            num_players (int): The number of players in the game.
        Raises:
            ValueError: If the number of players is not 1.

        Returns:
            tuple: A tuple containing the hands of player 1, player 2, and the 
            table.
        """
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
    """Finds matching cards in hand and table.

    Args:
        cards_hand (list): The player's hand.
        cards_table (list): The cards on the table.
    Raises:
        ValueError: If the number of players is not 1.
    Returns:
        dict: A dictionary with the card from hand as the key and a list of 
        matching cards from the table as the value.
    Side effects:
        Modifies the matched_dict dictionary.
    """
    matched_dict = {}
    for card1 in cards_hand:
        if (card1 != "7D" and card1[:-1] != "J" and card1[:-1] != "K" and 
            card1[:-1] != "Q"):
            temp_value = int(card1[:-1])
            for card2 in cards_table:
                if (card2 != "7D" and card2[:-1] != "J" and card2[:-1] != "K" 
                    and card2[:-1] != "Q"):
                    other_cards = list(cards_table)
                    other_cards.remove(card2)
                    if card1[:-1] == card2[:-1]: 
                        matched_dict[card1] = [card2]
                    for other in other_cards:
                        if (other != "7D" and other[:-1] != "J" and 
                            other[:-1] != "K" and other[:-1] != "Q"):
                            otherother_cards = list(other_cards)
                            otherother_cards.remove(other)
                            if int(card2[:-1]) + int(other[:-1]) == temp_value:
                                matched_dict[card1] = [card2, other]
                            for otherother in otherother_cards:
                                if (otherother != "7D" and 
                                    otherother[:-1] != "J" and 
                                    otherother[:-1] != "K" and 
                                    otherother[:-1] != "Q"):
                                    if (int(card2[:-1]) + int(other[:-1]) + 
                                        int(otherother[:-1]) == temp_value):
                                        matched_dict[card1] = [
                                            card2, other, otherother
                                        ]
    return matched_dict

def evaluate_play(player, played_card, table_cards):
    """Evaluates the played card and updates the player's hand and table cards.

    Args:
        player(Player): The player who played the card.
        played_card (str): The card played by the player.
        table_cards (list): The cards on the table.
        
        Raises:
            ValueError: If the played card is not in the player's hand.

    Returns:
        tuple: A tuple containing the updated player's hand and table cards.
        
    Side effects:
        Modifies the player's hand and the table cards.
    """
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
    """Represents the current state of the game.
    
    Attributes:
        players (list): A list of players in the game.
        table_cards (list): The cards on the table.
        current_turn (int): The index of the player whose turn it is.
    
    """
    def __init__(self, players, table_cards, current_turn=0):
        """Initializes the game state with players, table cards, and current 
        turn.
        
        Args:
            players (list): A list of players in the game.
            table_cards (list): The cards on the table.
            current_turn (int): The index of the player whose turn it is.
            
        Side effects:
            Modifies the players, table_cards, and current_turn attributes.
       
        """
        self.players = players
        self.table_cards = table_cards  
        self.current_turn = current_turn
    
    def __str__(self):
        """ Returns a string representation of the current game state.
        Returns:
            str: A string representation of the current game state.
        """
        return (
            f"Current turn: {self.players[self.current_turn].name}, "
            f"Table cards: {self.table_cards}, "
            f"{self.players[self.current_turn].name}'s score: "
            f"{self.players[self.current_turn].score}"
        )

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)
        
    def update(self, table_cards):
        self.table_cards = table_cards   

class Player():
    """ Represents a player in the game.
    
    Attributes:
        name (str): The name of the player.
        cards_in_hand (list): The cards in the player's hand.
        face_up (int): The number of face-up cards.
        face_down (int): The number of face-down cards.
        combo_dict (dict): A dictionary of card combinations.
        score (int): The player's score.
        
    """ 
    def __init__(self, name, player_hand):
        """ 
        Initializes the player with a name and a hand of cards.
        Args:
            name (str): The name of the player.
            player_hand (list): The cards in the player's hand.
            
        Side effects:
            Modifies the name, cards_in_hand, face_up, face_down, 
            combo_dict, and score attributes.
        """ 
        self.name = name
        self.cards_in_hand = list(player_hand)
        self.face_up = 0
        self.face_down = 0
        self.combo_dict = {}
        self.score = 0
    
    def turn (self):
        raise NotImplementedError
    
    def calc_score(self, opponent):
        """Calculates the player's score based on the game rules.

        Args:
        opponent (Player): The opponent player.

        Side effects:
            Modifies the player's score based on the game rules.
        """
        if self.face_up != 0:
            self.score += (self.face_up * 10)
            self.face_up -= (1 * self.face_up)
        if self.face_down > opponent.face_down and self.score >= 40:
            self.score += 30

    def determine_komi(self, cards, table_cards):
        """ Determines the komi based on the played cards and table cards.

        Args:
            cards (list): The cards played by the player.
            table_cards (list): The cards on the table.

         Side effects:
            Modifies the player's face_up attribute based on the game rules.
    """
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
        """ Adds face-down cards based on the played card and table cards.

    Args:
        played_card (str): The card played by the player.
        table_cards (list): The cards on the table.

    Side effects:
        Modifies the player's face_down attribute based on the game rules.
    """
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
    """ Represents a human player in the game.
    
    Attributes:
        name (str): The name of the player.
        cards_in_hand (list): The cards in the player's hand.
        face_up (int): The number of face-up cards.
        face_down (int): The number of face-down cards.
        combo_dict (dict): A dictionary of card combinations.
        score (int): The player's score.
    """ 
    def turn(self, gamestate, table_cards):
        """ Handles the player's turn by prompting for input and validating the
        played card.

        Args:
            gamestate (Gamestate): The current game state.
            table_cards (list): The cards on the table.

        Raises:
            ValueError: If the player inputs "exit".

        Side effects:
            Modifies the player's cards_in_hand and face_down attributes.

        Returns:
            str: The card played by the player.
        """
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
                played = input(f"{self.name}, please input the desired card"
                        f"from your hand to play: ")
                
class ComputerPlayer(Player):
    """ Represents a computer player in the game.
    
    Attributes:
        name (str): The name of the player.
        cards_in_hand (list): The cards in the player's hand.
        face_up (int): The number of face-up cards.
        face_down (int): The number of face-down cards.
        combo_dict (dict): A dictionary of card combinations.
        score (int): The player's score.

    Args:
        Player (Player): The base class for the player.
    """
    def turn (self, table_cards):
        """ Handles the computer player's turn by selecting a card to play.

        Args:
            table_cards (list): The cards on the table.

        Side effects:
            Modifies the computer player's cards_in_hand and face_down 
            attributes.

        Returns:
            str: The card played by the computer player.
        """
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
    """ Represents the game of Al-Komi.
    
    Attributes:
        players (list): A list of players in the game.
        player1 (Player): The first player.
        player2 (Player): The second player.
        table_cards (list): The cards on the table.
        deck (Deck): The deck of cards used in the game.
    """
    def __init__(self, players, table_cards, deck):
        """ Initializes the game with players, table cards, and deck.

        Args:
            players (list): A list of players in the game.
            table_cards (list): The cards on the table.
            deck (Deck): The deck of cards used in the game.

        Side effects:
            Modifies the players, player1, player2, table_cards, and deck 
            attributes.
        """
        self.players = players
        self.player1 = players[0]
        self.player2 = players[1]
        self.table_cards = table_cards
        self.deck = deck
        
    def restart(self, gamestate):
        """ Restarts the game by dealing new cards to the table.

        Args:
            gamestate (Gamestate): The current game state.

        Side effects:
            Modifies the table_cards attribute with new cards.
        """
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
        """Refills the player's hand with new cards from the deck.

        Args:
            player (Player): The player whose hand needs to be refilled.

        Side effects:
            Modifies the player's cards_in_hand attribute with new cards.
        """
        player.cards_in_hand = [self.deck.deck_cards.pop() for _ in range(4)]  
        
    def start(self):
        """ Starts the game loop and handles player turns. """
        gamestate = Gamestate(self.players, self.table_cards)
        while (self.player1.score < 70 and self.player2.score < 70 and 
               len(self.deck.deck_cards) >= 5):
            if self.players[gamestate.current_turn] == self.player1:
                played_card = self.player1.turn(gamestate, self.table_cards)
                (self.player1.cards_in_hand, 
                 self.table_cards) = evaluate_play(self.player1, played_card, 
                                                   self.table_cards)
                if len(self.table_cards) == 0:
                    self.restart(gamestate)
                if len(self.player1.cards_in_hand) == 0:
                    self.refill(self.player1)
                self.player1.calc_score(self.player2)
                gamestate.update(self.table_cards)
                gamestate.next_turn()
            elif self.players[gamestate.current_turn] == self.player2:
                played_card = self.player2.turn(self.table_cards)
                (self.player2.cards_in_hand, 
                 self.table_cards) = evaluate_play(self.player2, played_card, 
                                                   self.table_cards)
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
    """ Main function to start the game.
    This function initializes the game with a human player and a computer
    player, deals cards, and starts the game loop.
    It also handles command-line arguments for the player's name.

    Args:
        name (str): The name of the human player.

    Side effects:
        Modifies the players list with the human player and computer player.
        Initializes the game with the players and starts the game loop.
    """
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
    """ Parse command-line arguments.
    This function uses argparse to handle command-line arguments for the
    player's name. It provides help information and allows the user to
    specify the player's name when running the script.

    Args:
        arglist (list): A list of command-line arguments.

    Returns:
        Namespace: A namespace object containing the parsed arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("name", help="player name")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name)