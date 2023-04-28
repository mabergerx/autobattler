def attack(attacker, defender):
    attacker_attack_stat = attacker.attack
    attacker_health_stat = attacker.health

    defender_attack_stat = defender.attack
    defender_health_stat = defender.health

    attacker_ds = attacker.divine_shield
    defender_ds = defender.divine_shield

    def determine_single_attack_dmg():
        damage_to_defender = 

    # For now we disregard windfury as it doesn't appear in our card set
    if defender_ds:
        if attacker_ds:
            # Nothing happens, as divine shields cancel each other out
            attacker.adjust_health(0)
            defender.adjust_health(0)
        else:
            # Attacker takes damage, while the defender does not

