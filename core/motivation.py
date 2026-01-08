import json
from pathlib import Path

new_message = input("Enter the quoute: ")

MESSAGES_FILE = Path("../data/messages.json")


def update_messsage(new_message):
    with open(MESSAGES_FILE, "r+", encoding="utf-8") as f:
        messages = json.load(f)
        messages.append(new_message)
        f.seek(0)
        json.dump(messages, f, indent=4)
    print("Message added successfully.")


update_messsage(new_message)
