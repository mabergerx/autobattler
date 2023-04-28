def attack(attacker, defender):
    attacker_attack_stat = attacker.attack
    attacker_health_stat = attacker.health

    defender_attack_stat = defender.attack
    defender_health_stat = defender.health

    attacker_ds = attacker.divine_shield
    defender_ds = defender.divine_shield

    def determine_health_delta_after_attack(attacker_divine_shield, defender_divine_shield):

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
    if defender_ds:
        if attacker_ds:
            # Nothing happens, as divine shields cancel each other out
            defender_delta, attacker_delta = determine_health_delta_after_attack(attacker_ds, defender_ds)
            attacker.adjust_health(attacker_delta)
            defender.adjust_health(defender_delta)
        else:
            # Attacker takes damage, while the defender does not

