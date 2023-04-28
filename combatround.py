import random


class CombatRound:
    def __init__(self, board1, board2):
        self.board1 = board1
        self.board2 = board2
        self.current_attacker_board = None
        self.current_defender_board = None
        self.first_attacker = self.determine_first_attacker()

    def set_current_attacker(self, board_id):
        self.current_attacker_board = board_id

    def set_current_defender(self, board_id):
        self.current_defender_board = board_id

    def determine_first_attacker(self):
        # For now, we disregard any forced first attacks, and determine this only based on minion count and RNG
        board1_cards = self.board1.cards
        board2_cards = self.board2.cards

        if len(board1_cards) == len(board2_cards):
            attacking_board = random.choice([self.board1, self.board2])
            self.set_current_attacker(attacking_board.player)
            # self.set_current_defender(<Set this to the not chosen board>)
            if attacking_board == self.board1:
                self.set_current_defender(self.board2.player)
            else:
                self.set_current_defender(self.board1.player)
            return attacking_board.cards[0]
        elif len(board1_cards) > len(board2_cards):
            self.set_current_attacker(self.board1.player)
            self.set_current_defender(self.board2.player)
            return board1_cards[0]
        else:
            self.set_current_attacker(self.board2.player)
            self.set_current_defender(self.board1.player)
            return board2_cards[0]

    def determine_attack_target(self):
        # For now, this is by default a random target, unless there is a Taunt card. If there are multiple Taunt cards,
        # randomly choose from those.
        if attacker.board_membership == 1:
            defender_board = self.board2.cards
        else:
            defender_board = self.board1.cards

        # Check for Taunts
        taunt_cards_defender = [card for card in defender_board if card.taunt]

        if taunt_cards_defender:
            defender_card = random.choice(taunt_cards_defender)
        else:
            defender_card = random.choice(defender_board)

        return defender_card
