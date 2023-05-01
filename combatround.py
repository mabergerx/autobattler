import random


class CombatEvent:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

        self.attacker_attack = attacker.attack
        self.attacker_health = attacker.health
        self.defender_attack = defender.attack
        self.defender_health = defender.health

        self.attacker_ds = attacker.divine_shield
        self.defender_ds = defender.divine_shield

        self.attacker_poisonous = attacker.poisonous
        self.defender_poisonous = defender.poisonous

        self.attacker_windfury = attacker.windfury

    def simulate_attack(self):

        if self.attacker_attack > 0:
            if self.defender_ds:
                defender_health_delta = 0
                self.defender.update_divine_shield()
            else:
                if self.attacker_poisonous:
                    defender_health_delta = (
                        self.defender_health
                    )  # Or maybe better -9999?
                else:
                    defender_health_delta = self.attacker_attack

            if self.attacker_ds:
                attacker_health_delta = 0
                if self.defender_attack > 0:
                    self.attacker.update_divine_shield()
            else:
                if self.defender_poisonous:
                    attacker_health_delta = self.attacker_health
                else:
                    attacker_health_delta = self.defender_attack

            self.attacker.adjust_health(-attacker_health_delta)
            self.defender.adjust_health(-defender_health_delta)
        else:
            pass


"""
What can happen during one confrontation between opposing minions:
- Divine Shield can be triggered
- Windfury can be triggered
- Poisonous can be triggered
- Reborn can be triggered
- Deathrattle can be triggered
- Minion deals damage
- Minion takes damage
- Minions dies
- Minion survives

"""


class CombatRound:
    def __init__(self, board1, board2):
        self.board1 = board1
        self.board2 = board2
        self.current_attacker_board = None
        self.current_defender_board = None
        self.first_attacker = self.determine_first_attacker()
        self.combatevent_flow = []

    def set_current_attacker_board(self, board_id):
        self.current_attacker_board = board_id

    def set_current_defender_board(self, board_id):
        self.current_defender_board = board_id

    def get_board_by_id(self, board_id):
        for board in [self.board1, self.board2]:
            if board.player == board_id:
                return board

    def add_to_combat_flow(self):
        pass

    def determine_first_attacker(self):
        # For now, we disregard any forced first attacks, and determine this only based on minion count and RNG
        board1_cards = self.board1.cards
        board2_cards = self.board2.cards

        if len(board1_cards) == len(board2_cards):
            attacking_board = random.choice([self.board1, self.board2])
            self.set_current_attacker_board(attacking_board.player)
            # self.set_current_defender(<Set this to the not chosen board>)
            if attacking_board == self.board1:
                self.set_current_defender_board(self.board2.player)
            else:
                self.set_current_defender_board(self.board1.player)
            return attacking_board.cards[0]
        elif len(board1_cards) > len(board2_cards):
            self.set_current_attacker_board(self.board1.player)
            self.set_current_defender_board(self.board2.player)
            return board1_cards[0]
        else:
            self.set_current_attacker_board(self.board2.player)
            self.set_current_defender_board(self.board1.player)
            return board2_cards[0]

    def determine_attack_target(self):
        # For now, this is by default a random target, unless there is a Taunt card. If there are multiple Taunt cards,
        # randomly choose from those.
        defender_board = self.get_board_by_id(self.current_defender_board)

        # Check for Taunts
        taunt_cards_defender = [card for card in defender_board.cards if card.taunt]

        if taunt_cards_defender:
            defender_card = random.choice(taunt_cards_defender)
        else:
            defender_card = random.choice(defender_board.cards)

        return defender_card
