# main.py
import time
from logic import search_room, list_rooms, get_highlights, get_ascii_map

# ANSI colors
YELLOW = "\033[33m"
GREEN = "\033[32m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[0m"

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def loading_effect(text="Searching"):
    print(BLUE + text, end="", flush=True)
    for _ in range(5):
        time.sleep(0.1)
        print(".", end="", flush=True)
    print(RESET + "\n")
    time.sleep(0.3)

def main():
    greeted = False

    while True:
        print(f"{CYAN}\n===============================")
        print(" 🏫  KCMSC CAMPUS TOUR GUIDE")
        print("===============================\n" + RESET)

        if not greeted:
            print(f"{YELLOW}Welcome, student! 🏫  Let’s help you find your class or explore the campus.{RESET}\n")
            greeted = True

        print(MAGENTA + "--------------------------------------------------")
        print("🔍  Search for a room or class (e.g. 201, Principal)")
        print("Or just press Enter to browse all floors.")
        print("--------------------------------------------------" + RESET)
        query = input(GREEN + "> " + RESET).strip()

        if query:
            loading_effect("🔍 Searching")
            result = search_room(query)

            if not result:
                print(RED + "❌ Room not found. Try again.\n" + RESET)
            elif "multiple" in result:
                print(YELLOW + "⚠️  Multiple matches found:\n" + RESET)
                for r in result["multiple"]:
                    print(f" - Room {r['room']}: Class {r['class']} (Section: {r['section']})")
                print()
            else:
                print(GREEN + "✅ Found!" + RESET)
                print(f"{CYAN}Room:{RESET} {result['room']}")
                print(f"{CYAN}Class:{RESET} {result['class']}")
                print(f"{CYAN}Section:{RESET} {result['section']}")
                print(f"{CYAN}Floo203r:{RESET} {result['floor']}\n")

        else:
            print(f"{CYAN}\nList of available floors:\n{RESET}")
            print("1. Floor 1\n2. Exit")
            choice = input(GREEN + "\nEnter your choice: " + RESET).strip()

            if choice == "1":
                print(f"{YELLOW}\n--------------------------------")
                print("📍 You are now viewing: Floor 1")
                print("--------------------------------\n" + RESET)

                for room_info in list_rooms():
                    print(CYAN + " - " + RESET + room_info)

                print(f"\n{YELLOW}✨ Highlights:{RESET}")
                for h in get_highlights():
                    print(f"{MAGENTA} - {h}{RESET}")

                print("\nOptions:")
                print("1. View ASCII map")
                print("2. Go back to main menu")
                print("3. Exit")

                opt = input(GREEN + "\n> " + RESET).strip()
                if opt == "1":
                    print(BLUE + get_ascii_map() + RESET)
                elif opt == "3":
                    break
                else:
                    continue

            elif choice == "2":
                break
            else:
                print(RED + "❌ Invalid choice, try again." + RESET)

        again = input(YELLOW + "\nWould you like to continue? (y/n): " + RESET).lower().strip()
        if again != "y":
            break

    print(CYAN + "\nThank you for using KCMSC Campus Tour Guide! 🎓  Have a great day!\n" + RESET)

if __name__ == "__main__":
    main()
1
