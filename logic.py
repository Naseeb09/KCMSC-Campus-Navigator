from data import campus_data
from data import ascii_maps

def search_room(query):
    query = query.lower().strip()
    matches = []
    similar = []

    for floor, floor_data in campus_data.items():
        if not floor.startswith("Floor"):
            continue

        rooms = floor_data.get("rooms", [])
        for room in rooms:
            if not isinstance(room, dict):
                continue

            room_num = str(room.get("room", "")).lower()
            room_class = str(room.get("class", "")).lower()
            section = str(room.get("section", "")).lower()

            # FULL MATCH
            if query in room_num or query in room_class or query in section:
                matches.append({
                    "room": room.get("room"),
                    "class": room.get("class"),
                    "section": room.get("section"),
                    "floor": floor
                })
            # SIMILAR MATCH (partial/fuzzy)
            elif query and (
                room_class.startswith(query) or
                room_num.startswith(query) or
                section.startswith(query)
            ):
                similar.append({
                    "room": room.get("room"),
                    "class": room.get("class"),
                    "section": room.get("section"),
                    "floor": floor
                })

    # Return exact matches first
    if matches:
        return matches

    # Return similar suggestions if no exact match
    return {"similar": similar}


def list_rooms(floor="Floor 1"):
    floor_data = campus_data.get(floor, {})
    rooms = floor_data.get("rooms", [])
    return [f"Room {r['room']}: Class {r['class']} (Section: {r['section']})" for r in rooms]


def get_highlights(floor="Floor 1"):
    floor_data = campus_data.get(floor, {})
    return floor_data.get("highlights", [])



def get_ascii_map(floor="Floor 1"):
    floor_map = ascii_maps.get(floor)
    
    if floor_map:
        return f"""
🗺️  ASCII Map of {floor}:
{floor_map}
"""
    else:
        # Fallback box if map is not available
        return f"""
🗺️  ASCII Map of {floor}:
  +------------------------------------------------+
  |                ASCII map not found            |
  |         (No visual representation yet)        |
  +------------------------------------------------+
"""

