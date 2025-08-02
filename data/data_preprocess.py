import json
import pandas as pd
import os

def load_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)

def process_abyss(data):
    entries = data.get("data", {}).get("list", [])
    df = pd.DataFrame(entries)
    df.to_csv("data/processed/abyss.csv", index=False)
    return df

def process_arena(data):
    entries = data.get("data", {}).get("list", [])
    df = pd.DataFrame(entries)
    df.to_csv("data/processed/arena.csv", index=False)
    return df

if __name__ == "__main__":
    os.makedirs("data/processed", exist_ok=True)
    
    abyss_data = load_json("data/raw/abyss.json")
    arena_data = load_json("data/raw/arena.json")

    abyss_df = process_abyss(abyss_data)
    arena_df = process_arena(arena_data)

    print("Preprocessing completed!")
