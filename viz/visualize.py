import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

def plot_abyss_scores(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=range(len(df)), y=df["score"])
    plt.title("Abyss Score Over Time")
    plt.xlabel("Battle Index")
    plt.ylabel("Score")
    plt.savefig("viz/abyss_score_plot.png")
    plt.close()

def plot_arena_ranks(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=df.index, y=df["rank"])
    plt.title("Arena Ranks Over Time")
    plt.xlabel("Battle Index")
    plt.ylabel("Rank")
    plt.savefig("viz/arena_rank_plot.png")
    plt.close()

if __name__ == "__main__":
    os.makedirs("viz", exist_ok=True)

    abyss_df = pd.read_csv("data/processed/abyss.csv")
    arena_df = pd.read_csv("data/processed/arena.csv")

    plot_abyss_scores(abyss_df)
    plot_arena_ranks(arena_df)

    print("Visualizations saved to viz/ folder!")
