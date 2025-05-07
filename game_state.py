class Gamestate:
    """Game state class."""
    def __init__(self, players, deck, table_cards, current_turn=0, round_number=1):
        self.players = players 
        self.deck = deck      
        self.table_cards = table_cards  
        self.current_turn = current_turn  
        self.round_number = round_number
        self.komi_triggered = False 
    
    def __str__(self):
        return (
            f"Round: {self.round_number}, "
            f"Current turn: {self.players[self.current_turn]}, "
            f"Table cards: {self.table_cards}, "
            f"Deck size: {len(self.deck)}, "
        )

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)
