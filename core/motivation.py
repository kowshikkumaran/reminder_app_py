import json
from pathlib import Path

MESSAGES_FILE = Path("../data/messages.json")


def load_messages():
    if not MESSAGES_FILE.exists():
        return []

    with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_messages(messages):
    with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4)


def add_message(new_message):
    messages = load_messages()
    messages.append(new_message)
    save_messages(messages)
    print("Message added successfully.")


def edit_message(old_message, new_message):
    messages = load_messages()

    if old_message not in messages:
        print("Message not found.")
        return

    index = messages.index(old_message)
    messages[index] = new_message
    save_messages(messages)
    print("Message updated successfully.")


choice = int(input("1. Add  2. Edit: "))

if choice == 1:
    new_message = input("Enter the quote: ")
    add_message(new_message)

elif choice == 2:
    old_message = input("Enter the old quote: ")
    new_message = input("Enter the new quote: ")
    edit_message(old_message, new_message)

else:
    print("Invalid choice.")
