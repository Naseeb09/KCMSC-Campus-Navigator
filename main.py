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
        time.sleep(0.07)
        print(".", end="", flush=True)
    print(RESET + "\n")
    time.sleep(0.2)

def main():
    greeted = False

    floors = [key for key in sorted(campus_data.keys()) if key.startswith("Floor")]

    while True:
        print(f"{CYAN}\n===============================")
        print(" 🏫  KCMSC CAMPUS TOUR GUIDE")
        print("===============================\n" + RESET)

        if not greeted:
            print(f"{YELLOW}Welcome, student! 🏫  Let’s help you find your class or explore the campus.{RESET}\n")
            greeted = True

        print(MAGENTA + "--------------------------------------------------")
        print("🔍  Search for a room or class (e.g. 201, One, Nursery)")
        print("Or just press Enter to browse all floors.")
        print("--------------------------------------------------" + RESET)
        query = input(GREEN + "> " + RESET).strip()

        # --------------------------------------
        # SEARCH MODE
        # --------------------------------------
        if query:
            loading_effect("🔍 Searching")

            result = search_room(query)
            
            # ---------- NO RESULT ----------
            if not result:
                print(RED + "❌ No results found.\n" + RESET)

            # ---------- SIMILAR ----------
            elif isinstance(result, dict) and "similar" in result:
                print(RED + "❌ No exact match found." + RESET)
                print(YELLOW + "\n🔎 Showing similar matches:\n" + RESET)

                for r in result["similar"]:
                    print(f"{CYAN}Room:{RESET} {r['room']}")
                    print(f"{CYAN}Class:{RESET} {r['class']}")
                    print(f"{CYAN}Section:{RESET} {r['section']}")
                    print(f"{CYAN}Floor:{RESET} {r['floor']}")
                    print(MAGENTA + "-" * 45 + RESET)

            # ---------- EXACT RESULTS ----------
            elif isinstance(result, list):

                # Only ONE match → show single format
                if len(result) == 1:
                    r = result[0]
                    print(GREEN + "✅ Found!\n" + RESET)
                    print(f"{CYAN}Room:{RESET} {r['room']}")
                    print(f"{CYAN}Class:{RESET} {r['class']}")
                    print(f"{CYAN}Section:{RESET} {r['section']}")
                    print(f"{CYAN}Floor:{RESET} {r['floor']}\n")

                # Multiple exact matches
                else:
                    print(GREEN + "🎯 Multiple matches found:\n" + RESET)
                    for r in result:
                        print(f"{CYAN}Room:{RESET} {r['room']}")
                        print(f"{CYAN}Class:{RESET} {r['class']}")
                        print(f"{CYAN}Section:{RESET} {r['section']}")
                        print(f"{CYAN}Floor:{RESET} {r['floor']}")
                        print(MAGENTA + "-" * 45 + RESET)

        # --------------------------------------
        # BROWSE MODE
        # --------------------------------------
        else:
            print(f"{CYAN}\nList of available floors:\n{RESET}")

            for i, f in enumerate(floors, 1):
                print(f"{i}. {f}")

            print(f"{len(floors) + 1}. Exit")

            choice = input(GREEN + "\nEnter your choice: " + RESET).strip()

            if not choice.isdigit():
                print(RED + "❌ Invalid choice, try again." + RESET)
                continue

            choice = int(choice)

            if 1 <= choice <= len(floors):
                selected_floor = floors[choice - 1]

                print(f"{YELLOW}\n--------------------------------")
                print(f"📍 You are now viewing: {selected_floor}")
                print("--------------------------------\n" + RESET)

                # Rooms list
                for room_info in list_rooms(selected_floor):
                    print(CYAN + " - " + RESET + room_info)

                # Highlights
                highlights = get_highlights(selected_floor)
                if highlights:
                    print(f"\n{YELLOW}✨ Highlights:{RESET}")
                    for h in highlights:
                        print(f"{MAGENTA} - {h}{RESET}")

                # Options
                print("\nOptions:")
                print("1. View ASCII map")
                print("2. Go back to main menu")
                print("3. Exit")

                opt = input(GREEN + "\n> " + RESET).strip()
                if opt == "1":
                    print(BLUE + get_ascii_map(selected_floor) + RESET)
                elif opt == "3":
                    break
                else:
                    continue

            elif choice == len(floors) + 1:
                break
            else:
                print(RED + "❌ Invalid choice." + RESET)

        again = input(YELLOW + "\nWould you like to continue? (y/n): " + RESET).lower().strip()
        if again != "y":
            break

    print(CYAN + "\nThank you for using KCMSC Campus Tour Guide! 🎓  Have a great day!\n" + RESET)

if __name__ == "__main__":
    from data import campus_data
    main()
