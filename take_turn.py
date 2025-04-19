def evaluate_play(played_card, table_cards):
   #Mock Function of micheas evaluate_card function
   return [card for card in table_cards if card['rank'] == played_card['rank']]
    
def take_turn(player, table_cards, deck):
    while player['hand']: #iteration requirment 
        played_card = player['hand'].pop(0)  # sequence: play the first card
        # sequence: evaluate the play
        matched_cards = evaluate_play(played_card, table_cards)  

        if matched_cards:  #conditional branching/sequence: check for matches
            #The player keeps the card they played and the matched cards.
            player['collected'].append(played_card)
            player['collected'].extend(matched_cards)
            #updates the player's score
            player['score'] += len(matched_cards) + 1
            
            # iteration: loop through all cards that matched the played card
            for card in matched_cards:  
                if card in table_cards:
                    #sequence: remove matched cards from the table
                    table_cards.remove(card) 
        else:
            # sequence: If no matches found, add the played card to the table
            table_cards.append(played_card)  
            
    # conditional branching/sequence: refill hand if empty
    if not player['hand']:  
        # sequence: draw cards
        player['hand'] = [deck.pop(0) for _ in range(min(4, len(deck)))] 

            