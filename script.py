import json
import argparse
from datetime import datetime
from pathlib import Path
import sys

f = Path("notes.json")

def load():
    if f.exists():
        with open(f, "r") as file:
            return json.load(file)
    return []

def save(notes):
    with open(f, "w") as file:
        json.dump(notes, file, indent=4)

def add(topic, message):#adds note with topic and message
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes = load()
    notes.append({"topic": topic, "message": message, "timestamp": timestamp})
    save(notes)
    print("Note added successfully!")

def list_notes(filter_topic=None):#Lists all notes, with option to filter by topic
    notes = load()
    if filter_topic:
        notes = [i for i in notes if i["topic"].lower() == filter_topic.lower()]
    
    if not notes:
        print("No notes found.")
        return
    
    for note in notes:
        print(f"[{note['timestamp']}] {note['topic']}: {note['message']}")

def exit_program():#Exits the program
    sys.exit()

def main():
    parser = argparse.ArgumentParser(description="Daily Discovery Tracker.")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("topic", type=str, help="Topic of the note")
    add_parser.add_argument("message", type=str, help="Message of the note")

    list_parser = subparsers.add_parser("list", help="List all notes")
    list_parser.add_argument("--topic", type=str, help="Filter notes by topic")
    
    exit_parser = subparsers.add_parser("exit", help="Exit the program")
    
    args = parser.parse_args()

    if args.command == "add":
        add(args.topic, args.message)
    elif args.command == "list":
        list_notes(args.topic)
    elif args.command == "exit":
        exit_program()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
