import requests
import os
import json


# Card collection

file_path_cards = "tier1_cards.json"
file_path_metadata = "metadata.json"


def reduce_card_info(single_card):
    relevant_keys = ["health", "attack", "manaCost", "name", "text"]
    return {k: v for k, v in single_card.items() if k in relevant_keys}


if os.path.isfile(file_path_cards):
    with open("tier1_cards.json", "r") as outfile:
        cards = json.load(outfile)
        filtered_cards = [reduce_card_info(card) for card in cards]
else:
    print("The file does not exist.")
    # To retrieve fresh BG cards

    client_id = "<>"
    client_secret = "<>"

    def get_access_token(client_id, client_secret):
        token_url = "https://us.battle.net/oauth/token"
        payload = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }
        response = requests.post(token_url, data=payload)
        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            print(f"Error {response.status_code}: Failed to get access token")
            return None

    def get_card_data(access_token, search_params):
        api_url = "https://us.api.blizzard.com/hearthstone/cards"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(api_url, headers=headers, params=search_params)

        if response.status_code == 200:
            return response.json()["cards"]
        else:
            print(f"Error {response.status_code}: Failed to get card data")
            return None

    access_token = get_access_token(client_id, client_secret)

    if access_token:
        search_params = {
            "gameMode": "battlegrounds",
            "pageSize": 100,
            "locale": "en_US",
            "tier": 1,
        }
        cards = get_card_data(access_token, search_params)
        with open("tier1_cards.json", "w") as outfile:
            json.dump(cards, outfile)
        # check
        # print("---")
        # with open("tier1_cards.json", "r") as outfile:
        #     loaded = json.load(outfile)
        #     print(loaded[0])


def get_card_by_name(card_name):
    # Probably a much better way to do it later
    return [card for card in cards if card["name"] == card_name][0]

# Metadata TODO

# if os.path.isfile(file_path_metadata):
#     with open("metadata.json", "r") as outfile:
#         metadata = json.load(outfile)
# else:
#     print("The file does not exist.")
#     # To retrieve fresh BG cards
#
#     client_id = "<>"
#     client_secret = "<>"
#
#     def get_access_token(client_id, client_secret):
#         token_url = "https://us.battle.net/oauth/token"
#         payload = {
#             "grant_type": "client_credentials",
#             "client_id": client_id,
#             "client_secret": client_secret,
#         }
#         response = requests.post(token_url, data=payload)
#         if response.status_code == 200:
#             return response.json()["access_token"]
#         else:
#             print(f"Error {response.status_code}: Failed to get access token")
#             return None
#
#     def get_card_data(access_token, search_params):
#         api_url = "https://us.api.blizzard.com/hearthstone/cards"
#         headers = {"Authorization": f"Bearer {access_token}"}
#         response = requests.get(api_url, headers=headers, params=search_params)
#
#         if response.status_code == 200:
#             return response.json()["cards"]
#         else:
#             print(f"Error {response.status_code}: Failed to get card data")
#             return None
#
#     access_token = get_access_token(client_id, client_secret)
#
#     if access_token:
#         search_params = {
#             "gameMode": "battlegrounds",
#             "pageSize": 100,
#             "locale": "en_US",
#             "tier": 1,
#         }
#         cards = get_card_data(access_token, search_params)
#         with open("tier1_cards.json", "w") as outfile:
#             json.dump(cards, outfile)
