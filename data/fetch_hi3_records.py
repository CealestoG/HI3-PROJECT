import requests
import json
import os

# === Configuration ===
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Cookie": "ltoken_v2=YOUR_TOKEN_HERE; ltuid_v2=YOUR_UID_HERE",  # Replace placeholders
    "User-Agent": "Mozilla/5.0"
}
BASE_URL = "https://bbs-api-os.hoyolab.com/game_record/bh3/api/"

# === Function to Fetch Abyss Records ===
def fetch_abyss_records():
    url = BASE_URL + "abyss/battle"
    response = requests.get(url, headers=HEADERS)
    if response.ok:
        return response.json()
    else:
        print("Failed to fetch abyss records.")
        return None

# === Function to Fetch Arena Records ===
def fetch_arena_records():
    url = BASE_URL + "challenge/battle"
    response = requests.get(url, headers=HEADERS)
    if response.ok:
        return response.json()
    else:
        print("Failed to fetch arena records.")
        return None

# === Save Fetched Data ===
def save_json(data, filename):
    os.makedirs("data/raw", exist_ok=True)
    with open(f"data/raw/{filename}", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    abyss_data = fetch_abyss_records()
    arena_data = fetch_arena_records()

    if abyss_data:
        save_json(abyss_data, "abyss.json")
    if arena_data:
        save_json(arena_data, "arena.json")
