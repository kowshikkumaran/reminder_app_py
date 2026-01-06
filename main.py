import json
from pathlib import Path
from core import reminder

MESSAGES_FILE = Path("data/messages.json")


def load_messages():
    with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    messages = load_messages()
    print(reminder.remind(messages))


if __name__ == "__main__":
    main()
