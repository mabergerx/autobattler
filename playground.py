from board import Board
from api_interactions import get_card_by_name
from card import parse_card_json_item
from card_interactions import attack

# Let's try en example with attacking

attacker_card_data = get_card_by_name("Pupbot")
defender_card_data = get_card_by_name("Sellemental")

attacker_card = parse_card_json_item(attacker_card_data)

defender_card = parse_card_json_item(defender_card_data)

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
board1 = Board(player=1, cards=[attacker_card])
board2 = Board(player=2, cards=[defender_card])
print(board1)
# print(board2)

for c in board1.cards:
    print(c)
    print("----")

