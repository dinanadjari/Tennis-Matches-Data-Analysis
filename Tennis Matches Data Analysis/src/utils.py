def get_winner_id(row):
    if row['winner_code'] == 1:
        return row['home_id']
    elif row['winner_code'] == 2:
        return row['away_id']
    else:
        return None
    
def get_winner_name(row):
    if row['winner_code'] == 1:
        return row['home_name']
    elif row['winner_code'] == 2:
        return row['away_name']
    
def get_winner_country(row):
    if row['winner_code'] == 1:
        return row['country_home']
    elif row['winner_code'] == 2:
        return row['country_away']
    else:
        return None