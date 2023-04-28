class Board:
    def __init__(self, player, cards):
        self.player = player
        self.cards = cards
        self.num_cards = len(self.cards)

    def add_card_to_board(self, card):
        self.cards.append(card)

    def remove_card_from_board(self, card):
        # TODO: how? do we wanna keep internal card ids per board?
        pass

    def __str__(self):
        board_str = f"Player: {self.player}\n"

        for card in self.cards:
            card_repr = f"{card.name} ({card.attack}/{card.health}) [DS:{card.divine_shield} / Taunt:{card.taunt}]"
            border_len = len(card_repr) + 4  # Adding 2 extra dashes on both sides
            board_str += "|{0:-^{border_len}}|\n".format("", border_len=border_len)
            board_str += "|  {0:{content_len}}|\n".format(card_repr, content_len=border_len - 2)
            board_str += "|{0:-^{border_len}}|\n".format("", border_len=border_len)

        return board_str
