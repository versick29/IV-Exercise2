from flask import Flask, render_template
import json
from utils import data_conversion_to_JSON
import pandas as pd 

app = Flask(__name__)

# ensure that we can reload when we change the HTML / JS for debugging
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route('/')
def data():
    
    #CSV files converted to json
    data_conversion_to_JSON()

    # replace this with the real data
    teamData = pd.read_json("teamData.json")
    playerData = pd.read_json("playerData.json")
    cleanedPlayerData = pd.read_json("cleanedPlayerData.json")

    # return the index file and the data
    return render_template("index.html", teamData , playerData, cleanedPlayerData )


if __name__ == '__main__':
    app.run()
