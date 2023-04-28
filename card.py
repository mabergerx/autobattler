class Card:
    def __init__(self, health, attack, mana_cost, name, text, taunt, divine_shield):
        self.health = health
        self.attack = attack
        self.mana_cost = mana_cost
        self.name = name
        self.text = text
        self.taunt = taunt
        self.divine_shield = divine_shield

    def adjust_health(self, health_delta):
        # Health delta should always be a number which we add to health, either negative or positive
        self.health = self.health + health_delta

    def adjust_attack(self, attack_delta):
        # Attack delta should always be a number which we add to attack, either negative or positive
        self.attack = self.attack + attack_delta
