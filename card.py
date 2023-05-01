class Card:
    def __init__(self, health, attack, mana_cost, name, text):
        self.health = health
        self.attack = attack
        self.mana_cost = mana_cost
        self.name = name
        self.text = text
        self.taunt = self.has_taunt()
        self.divine_shield = self.has_ds()
        self.windfury = self.has_windfury()
        self.poisonous = self.has_poisonous()
        self.reborn = self.has_reborn()
        self.deathrattle = self.has_deathrattle()
        self.board_membership = None

    def adjust_health(self, health_delta):
        # Health delta should always be a number which we add to health, either negative or positive
        self.health = self.health + health_delta

    def adjust_attack(self, attack_delta):
        # Attack delta should always be a number which we add to attack, either negative or positive
        self.attack = self.attack + attack_delta

    # Ideally, we want to deduce the keywords of the cards based on the metadata from the API. But for the sake of
    # simplicity, now we just parse the card text, as we are only dealing with tier 1 minions anyway.
    def has_taunt(self):
        return "Taunt" in self.text

    # This is maybe too simplistic in terms of texts like "Give your DS minions X" but for now it's ok
    def has_ds(self):
        return "Divine Shield" in self.text

    # Tier 1 minions have no windfury so this is for later
    def has_windfury(self):
        return "Windfury" in self.text

    # Tier 1 minions have no poisonous so this is for later
    def has_poisonous(self):
        return "Poisonous" in self.text

    # This is maybe too simplistic in terms of texts like "Give your Reborn minions X" but for now it's ok
    def has_reborn(self):
        return "Reborn" in self.text

    # This is maybe too simplistic in terms of texts like "Give your Deathrattle minions X" but for now it's ok
    def has_deathrattle(self):
        return "Deathrattle" in self.text

    def assign_board_membership(self, board_id):
        self.board_membership = board_id

    def __str__(self):
        return (
            f"Card: {self.name}\nAttack: {self.attack}\nHealth: {self.health}\nDivine Shield: {self.divine_shield}"
            f"\nTaunt: {self.taunt}\nBoard: {self.board_membership}"
        )


def parse_card_json_item(json_item):
    """
    Convert one card attribute JSON list into a Card object.

    :param json_item:
    :return:
    """
    return Card(
        health=json_item["health"],
        attack=json_item["attack"],
        mana_cost=json_item["manaCost"],
        name=json_item["name"],
        text=json_item["text"],
    )
