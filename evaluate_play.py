def evaluate_play(played_card,table_cards): # micheas kidane
    # Sequence of steps.
    if played_card == "J": # checking if card is jack
        return {"jack, cleared cards": table_cards}
    if played_card == '7D': # checking if card is 7 of Diamonds
        return {"wildcard, cleared cards": table_cards}
 
    # Conditional Branching
    if played_card in ['Q', 'K']: # checking if card is Queen or King
        for card in table_cards: # iteration over cards on table
            if card == played_card:
                return {"matched_card": card}
     
    # checking if komi is present.       
    if len(table_cards) == 1 and all(card not in ["J", "Q", "K"]
                                        for card in table_cards):
        return {"Komi, cleared cards": table_cards}
