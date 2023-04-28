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
