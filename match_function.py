##Jeffrey's algorithm:
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
                        matched_dict[card1] = card2
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
                        
            