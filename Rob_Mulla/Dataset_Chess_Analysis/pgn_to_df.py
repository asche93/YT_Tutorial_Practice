import argparse
import pandas as pd
from tqdm.auto import trange
from glob import glob
import os
import chess
import chess.pgn

def pgn_to_df(pgn_file):
    """Pull metadata from pgn file and puts in dataframe format.

    Args:
        

    Returns:
    """
    headers = []
    games = []
    mainline_moves = []
    with open(pgn_file, mode="r", encoding="utf-8") as pgn:
        while True:
            header = chess.pgn.read_headers(pgn)
            if header is None:
                break
            headers.append(header)

    with open(pgn_file, mode="r", encoding="utf-8") as pgn:
        for _ in trange(len(headers)):
            game = chess.pgn.read_game(pgn)
            games.append(game)
            moves = str(game.mainline_moves())
            mainline_moves.append(moves)
    games_df = pd.DataFrame(headers)
    games_df["mainline_moves"] = mainline_moves
    games_df["Date_clean"] = pd.to_datetime(games_df["Date"], format="%Y.%m.%d", errors="coerce")
    games_df["Online"] = games_df["Site"].str.endswith("INT")
    return games_df

def run(pgn_files):
    for pgn in pgn_files:
        print(f"Running for pgn file {pgn}")
        fn = pgn.split("/")[-1].replace(".pgn", "")
        if os.path.exists(f"games/{fn}.parquet"):
            print("File already exists")
            continue
        try:
            games_df = pgn_to_df(pgn)
            os.makedirs("games", exist_ok=True)
            games_df.to_parquet(f"games/{fn}.parquet")
        except Exception as e:
            print(f"Failed for {pgn} with exception {e}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process PGN files and extract games.")
    parser.add_argument(
        "--gm",
        type=str,
        help="Comma-separated list of player names to filter PGN files by. If not provided, all PGN files will be processed."
    )
    args = parser.parse_args()

    # Parse the player list and get relevant files
    if args.gm:
        pgn_files = []
        for gm in args.gm.split(","):
            pgn_path = f"pgns/{gm}.pgn"
            if os.path.exists(pgn_path):
                pgn_files.append(pgn_path)
    else:
        pgn_files = glob("pgns/*.pgn")

    # Run the processing
    run(pgn_files)