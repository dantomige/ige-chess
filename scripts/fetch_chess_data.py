import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_player_color(username, game):
    if game["white"]["username"] == username:
        return "white"
    elif game["black"]["username"] == username:
        return "black"
    else:
        raise ValueError(f"{username} was not in the game.")

def fetch_chess_data_by_user(username):
    """Fetches live chess game data for {username}.

    Args:
        username (str): player username

    Returns:
        pgn, player color of all games
    """

    headers = {
        "User-Agent": os.getenv("IGE_CHESS_USER_AGENT")
    }

    url = f"https://api.chess.com/pub/player/{username}/games/archives"

    response = requests.get(url, headers=headers)
    response_json = response.json()
    archive_urls = response_json["archives"]

    game_pgns = []
    for archive_url in archive_urls:
        response = requests.get(archive_url, headers=headers)
        response_json = response.json()
        games = response_json["games"]
        game_pgns.extend([{"pgn": game["pgn"], "player-color": get_player_color(username, game)} for game in games])

    return game_pgns

if __name__ == "__main__":
    game_pgns = fetch_chess_data_by_user("IgeChess")
    print(len(game_pgns))