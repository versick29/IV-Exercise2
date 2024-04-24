import pandas as pd
from sklearn.preprocessing import StandardScaler


def get_data_as_json(data_folder, file_name):
    return pd.read_csv(data_folder + file_name)


def get_pca_columns(all_team_columns):
    column_to_skip = ['id', 'player_id', 'team_name']
    pca_team_columns = []
    for c in list(all_team_columns):
        if c not in column_to_skip:
            pca_team_columns.append(c)

    return pca_team_columns


def scale_numeric_values(data):

    filtered_columns_data = data[get_pca_columns(data)]

    scaler = StandardScaler().set_output(transform='pandas')
    return scaler.fit_transform(filtered_columns_data)
