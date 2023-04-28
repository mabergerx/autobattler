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

    # def __str__(self):
    #     cards = "\n       ".join(
    #         [
    #             f"{card.name} ({card.attack}/{card.health}) [DS:{card.divine_shield} / Taunt:{card.taunt}]"
    #             for card in self.cards
    #         ]
    #     )
    #     return f"Player: {self.player}\nCards: {cards}"

    def __str__(self):
        board_str = f"Player: {self.player}\n"

        for card in self.cards:
            card_repr = f"{card.name} ({card.attack}/{card.health}) [DS:{card.divine_shield} / Taunt:{card.taunt}]"
            board_str += "|{0:-^48}|\n".format("")
            board_str += "|{0:^48}|\n".format(card_repr)
            board_str += "|{0:-^48}|\n".format("")

        return board_str
