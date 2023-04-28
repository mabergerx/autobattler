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

    def has_ds(self):
        return "Divine Shield" in self.text

    # Tier 1 minions have no windfury so this is for later
    def has_windfury(self):
        return "Windfury" in self.text
