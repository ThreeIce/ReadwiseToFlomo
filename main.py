import datetime
import requests
import yaml
import os

data_path = "./data.yml"
config_path = "./config.yml"
config = None
data = None
fetched_notes = None
def fetch_from_export_api(updated_after=None):
    full_data = []
    next_page_cursor = None
    while True:
        params = {}
        if next_page_cursor:
            params['pageCursor'] = next_page_cursor
        if updated_after:
            params['updatedAfter'] = updated_after
        print("Making export api request with params " + str(params) + "...")
        response = requests.get(
            url="https://readwise.io/api/v2/export/",
            params=params,
            headers={"Authorization": f"Token {config["readwise_token"]}"}, verify=False
        )
        full_data.extend(response.json()['results'])
        next_page_cursor = response.json().get('nextPageCursor')
        if not next_page_cursor:
            break
    return full_data
# read config
with open(config_path,"r") as f:
    config = yaml.safe_load(f)

if os.path.exists(data_path) and (os.path.getsize(data_path) != 0):
    with open(data_path,"r") as f:
        data = yaml.safe_load(f)
    fetched_notes = fetch_from_export_api(data["last_fetch_time"])
else:
    data = {"last_fetch_time":"","cached_notes":[]}
    fetched_notes = fetch_from_export_api()
data["last_fetch_time"] = datetime.datetime.now().isoformat()

for book in fetched_notes:
    for highlight in book["highlights"]:
        memo = highlight["text"] + "\n"
        if highlight["note"]:
            memo += "**Note:**\n" + highlight["note"] + "\n"
        memo += "[Source](" + highlight["readwise_url"] + ")\n"
        memo += highlight["title"]
        data["cached_notes"].append(memo)



with open(data_path,"w") as f:
    yaml.safe_dump(data,f)

