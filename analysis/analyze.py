import pandas as pd

def analyze_abyss(path):
    df = pd.read_csv(path)
    print("=== Abyss Overview ===")
    print(df.describe())
    return df

def analyze_arena(path):
    df = pd.read_csv(path)
    print("=== Arena Overview ===")
    print(df.describe())
    return df

if __name__ == "__main__":
    abyss_df = analyze_abyss("data/processed/abyss.csv")
    arena_df = analyze_arena("data/processed/arena.csv")
