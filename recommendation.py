import requests

FPL_API_URL = "https://api.fpl.com/data"

def fetch_current_form():
    response = requests.get(f"{FPL_API_URL}/players-form")
    return response.json()

def recommend_players_based_on_form(players_form):
    # A simplified recommendation logic based on players' form
    top_players = sorted(players_form, key=lambda x: x['form'], reverse=True)[:10]
    return top_players

if __name__ == "__main__":
    players_form = fetch_current_form()
    top_recommendations = recommend_players_based_on_form(players_form)
    print("Top recommended players:", top_recommendations)
