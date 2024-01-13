import requests

FPL_API_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"


def fetch_players_data():
    response = requests.get(FPL_API_URL)
    data = response.json()
    return data['elements']

def recommend_players_based_on_form(players_data):
    # A simple recommendation logic based on players' form and points
    top_players = sorted(players_data, key=lambda x: (float(x['form']), x['total_points']), reverse=True)[:10]
    return top_players

def display_recommendations(recommendations):
    print("\nTop recommended players:")
    for player in recommendations:
        print(f"Name: {player['first_name']} {player['second_name']}, Team: {player['team']}, Form: {player['form']}, Total Points: {player['total_points']}")

if __name__ == "__main__":
    players_data = fetch_players_data()
    recommendations = recommend_players_based_on_form(players_data)
    display_recommendations(recommendations)
