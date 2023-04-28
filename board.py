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

        # Find the longest card representation
        max_card_repr_len = 0
        card_reprs = []

        for card in self.cards:
            card_repr = f"{card.name} ({card.attack}/{card.health}) [DS:{card.divine_shield} / Taunt:{card.taunt}]"
            max_card_repr_len = max(max_card_repr_len, len(card_repr))
            card_reprs.append(card_repr)

        border_len = max_card_repr_len + 4  # Adding 2 extra dashes on both sides

        # Construct the board representation
        for card_repr in card_reprs:
            board_str += "|{0:-^{border_len}}|\n".format("", border_len=border_len)
            board_str += "| {0:^{content_len}} |\n".format(card_repr, content_len=border_len - 2)
            board_str += "|{0:-^{border_len}}|\n".format("", border_len=border_len)

        return board_str
