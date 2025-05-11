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