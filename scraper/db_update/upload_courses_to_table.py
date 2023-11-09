import keys
from supabase import create_client, Client
import json

url: str = keys.get_url()
key: str = keys.get_key()

supabase: Client = create_client(url, key)

import os

src_dir = "scraper/courses"

# Get a list of the files in the folder
files = os.listdir(src_dir)

# Iterate over the files and read their contents
for file in files:
    with open(f"{src_dir}/{file}", "r") as f:
        
        course_data = json.load(f)
        name = course_data["name"]
        

        data, count = supabase.table('all_courses').upsert({'name': name, 'data' :  course_data}).execute()


    # Do something with the contents of the file

