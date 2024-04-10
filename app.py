from flask import Flask, render_template
import json
import pandas as pd
import os

from utils import get_data_as_json

app = Flask(__name__)

# ensure that we can reload when we change the HTML / JS for debugging
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
DATA_FOLDER = 'static/data/'




@app.route('/')
def data():

    json_data = get_data_as_json(DATA_FOLDER)

    # return the index file and the data
    return render_template("index.html", data=json.dumps(json_data))


if __name__ == '__main__':
    app.run()
