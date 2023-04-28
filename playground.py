from board import Board
from api_interactions import get_card_by_name
from card import parse_card_json_item
from card_interactions import attack
from combatround import CombatRound

# Let's try en example with attacking

attacker_card_data = get_card_by_name("Pupbot")
defender_card_data = get_card_by_name("Sellemental")
second_defender_card_data = get_card_by_name("Dozy Whelp")

attacker_card = parse_card_json_item(attacker_card_data)

defender_card = parse_card_json_item(defender_card_data)
second_defender_card = parse_card_json_item(second_defender_card_data)

# print(attacker_card)
# print("---")
# print(defender_card)
# print("---")
#
# # Perform attack
# print(f"Now performing an attack by {attacker_card.name} on {defender_card.name}!")
# attack(attacker_card, defender_card)
# print(attacker_card)
# print("---")
# print(defender_card)
# print("---")


# Boards test
board1 = Board(player=1, cards=[attacker_card, attacker_card])
board2 = Board(player=2, cards=[defender_card, second_defender_card])
print(board1)
print(board2)

# for c in board1.cards:
#     print(c)
#     print("----")

combat_round1 = CombatRound(board1, board2)
print("determining first attacker...")
# print(combat_round1.first_attacker)
print("Current attacker board:", combat_round1.current_attacker_board)
print("Current defender card:", combat_round1.determine_attack_target().name)