import pandas as pd


def get_data_as_json(data_folder):
    player_data = pd.read_csv(data_folder + "playerData.csv")
    team_data = pd.read_csv(data_folder + "teamData.csv")
    cleaned_player_data = pd.read_csv(data_folder + "cleanedPlayerData.csv")
    return {"player_data": player_data.to_json(),
            "team_data": team_data.to_json(),
            "player_data_for_36": cleaned_player_data.to_json()
            }
