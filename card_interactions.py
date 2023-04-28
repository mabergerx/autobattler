from api_interactions import get_card_by_name
from card import Card


def attack(attacker, defender):
    attacker_attack_stat = attacker.attack

    defender_attack_stat = defender.attack

    attacker_ds = attacker.divine_shield
    defender_ds = defender.divine_shield

    def determine_health_delta_after_attack(
        attacker_divine_shield, defender_divine_shield
    ):

        # TODO: Remember to update divine shield status after this resolves!

        if defender_divine_shield:
            defender_health_delta = 0
        else:
            defender_health_delta = attacker_attack_stat

        if attacker_divine_shield:
            attacker_health_delta = 0
        else:
            attacker_health_delta = defender_attack_stat

        return defender_health_delta, attacker_health_delta

    # For now we disregard windfury as it doesn't appear in our card set
    defender_delta, attacker_delta = determine_health_delta_after_attack(
        attacker_ds, defender_ds
    )
    attacker.adjust_health(-attacker_delta)
    defender.adjust_health(-defender_delta)


# Let's try en example!

attacker_card_data = get_card_by_name("Pupbot")
defender_card_data = get_card_by_name("Sellemental")

attacker_card = Card(
    health=attacker_card_data["health"],
    attack=attacker_card_data["attack"],
    mana_cost=attacker_card_data["manaCost"],
    name=attacker_card_data["name"],
    text=attacker_card_data["text"],
)

defender_card = Card(
    health=defender_card_data["health"],
    attack=defender_card_data["attack"],
    mana_cost=defender_card_data["manaCost"],
    name=defender_card_data["name"],
    text=defender_card_data["text"],
)

print(attacker_card)
print("---")
print(defender_card)
print("---")

# Perform attack
print(f"Now performing an attack by {attacker_card.name} on {defender_card.name}!")
attack(attacker_card, defender_card)
print(attacker_card)
print("---")
print(defender_card)
print("---")