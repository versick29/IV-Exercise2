import pandas as pd
from sklearn.preprocessing import StandardScaler


def get_data_as_json(data_folder, file_name):
    return pd.read_csv(data_folder + file_name)


def get_pca_columns(all_team_columns):
    column_to_skip = ['id', 'player_id', 'season', 'name', 'full_name',
                      'position', 'birth_date', 'birth_place',
                      'height', 'player_url', 'text', 'teams', 'team_name']
    pca_team_columns = []
    for c in list(all_team_columns):
        if c not in column_to_skip:
            pca_team_columns.append(c)

    return pca_team_columns


def scale_numeric_values(data):
    # create two DataFrames, one for each data type
    removed_columns_data = data[get_pca_columns(data.columns)]

    scaler = StandardScaler().set_output(transform='pandas')

    # imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    return scaler.fit_transform(removed_columns_data)
