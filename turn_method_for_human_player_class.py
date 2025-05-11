#turn function for the human player class
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
                played = input(f"{self.name}, please input the desired card"
                        f"from your hand to play: ")
        