import random
import requests
import json

def random_character_request():
    character_id = random.randint(1, 826)
    response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
    return response.json()

def response_output(response):
    print(json.dumps(response, indent=4))
    print("Keys in the JSON structure:")
    for key in response.keys():
        print(key)

def save_to_file(response, character_id):
    with open(f"info_character_{character_id}.json", "w") as file:
        json.dump(response, file, indent=4)

def episode_list(response):
    episode_urls = response["episode"]
    episode_ids = [int(url.split("/")[-1]) for url in episode_urls]
    return episode_ids

def all_episodes_with_character(episode_ids, character_id):
    with open(f"all_episodes_with_character_{character_id}", "a") as file:
        for episode_id in episode_ids:
            file.write(f"https://rickandmortyapi.com/api/episode/{episode_id}\n")

def character_exploration():
    response = random_character_request()
    response_output(response)
    save_to_file(response, response["id"])
    episode_ids = episode_list(response)
    all_episodes_with_character(episode_ids, response["id"])

character_exploration()

