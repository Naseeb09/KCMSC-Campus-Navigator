# logic.py
from data import campus_data

def search_room(query):
    query = query.strip().lower()
    floor = "Floor 1"

    # Search by room number (exact match)
    for room in campus_data[floor]:
        if room["room"] == query:
            return {
                "room": room["room"],
                "class": room["class"],
                "section": room["section"],
                "floor": floor
            }

    # Search by section or class keyword (like "principal", "dance", etc.)
    for room in campus_data[floor]:
        if query in room["section"].lower() or query in room["class"].lower():
            return {
                "room": room["room"],
                "class": room["class"],
                "section": room["section"],
                "floor": floor
            }

    return None


def list_rooms(floor="Floor 1"):
    rooms = campus_data.get(floor, [])
    return [f"Room {r['room']}: Class {r['class']} (Section: {r['section']})" for r in rooms]


def get_highlights(floor="Floor 1"):
    return campus_data.get("Highlights", [])


def get_ascii_map():
    return """
🗺️  ASCII Map of Floor 1:
  +-------------------------------------+
  | 201 | 202 | 203 | 204 | 205 | 206  |
  +-------------------------------------+
  | 207 | 208 | 209 | 210 | 211 | 212  |
  +-------------------------------------+
  |          Corridor → Exit            |
  +-------------------------------------+
"""
