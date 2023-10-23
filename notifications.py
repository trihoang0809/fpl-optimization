import requests
import datetime
import os

FPL_API_URL = "https://api.fpl.com/data"

def fetch_current_gameweek():
    response = requests.get(f"{FPL_API_URL}/events")
    for event in response.json():
        if event["is_current"]:
            return event
    return None

def notify(deadline):
    message = f"Remember to set your FPL lineup by {deadline}"
    os.system(f'notify-send "{message}"')

if __name__ == "__main__":
    current_gameweek = fetch_current_gameweek()
    if current_gameweek:
        deadline_datetime = datetime.datetime.strptime(current_gameweek["deadline_time"], "%Y-%m-%dT%H:%M:%SZ")
        current_datetime = datetime.datetime.utcnow()
        one_day_before = deadline_datetime - datetime.timedelta(days=1)

        if current_datetime >= one_day_before:
            notify(deadline_datetime.strftime("%Y-%m-%d %H:%M:%S"))
