from flask import Flask, render_template
import json
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from utils import get_data_as_json, get_pca_columns, scale_numeric_values

app = Flask(__name__)

# ensure that we can reload when we change the HTML / JS for debugging
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
DATA_FOLDER = 'static/data/'


@app.route('/')
def data():
    # 1. Get data from the csv files and pass them to the client
    player_data = get_data_as_json(DATA_FOLDER, "playerData.csv")
    team_data = get_data_as_json(DATA_FOLDER, "teamData.csv")
    cleaned_player_data = get_data_as_json(DATA_FOLDER, "cleanedPlayerData.csv")

    #2. Calculate PCA
    scaled_team_data = scale_numeric_values(team_data)
    scaled_pca_team = PCA(n_components=2).fit_transform(scaled_team_data)

    json_data = {"playerData": player_data.to_json(),
                 "teamData": team_data.to_json(),
                 "playerDataFor36": cleaned_player_data.to_json(),
                 "scaledPcaTeam": repr(scaled_pca_team)
                 }

    # return the index file and the data
    return render_template("index.html", data=json.dumps(json_data))


if __name__ == '__main__':
    app.run()
