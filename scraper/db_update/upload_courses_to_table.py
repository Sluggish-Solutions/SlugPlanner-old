import keys
from supabase import create_client, Client
import json
import re
url: str = keys.get_url()
key: str = keys.get_key()

supabase: Client = create_client(url, key)

import os
import time

src_dir = "scraper/courses"

def custom_alphanumeric_sort_key(class_name):
    # Regular expression to match segments of letters and numbers
    # segment_regex = re.compile(r'([a-zA-Z]+)|(\d+)')

    # # Get a list of segments for the course name
    # segments = segment_regex.findall(name)

    # # Create a key tuple for sorting
    # key_tuple = tuple((int(num) if num else part.lower()) for part, num in segments)

    # return (len(key_tuple), key_tuple)
    
    match = re.match(r"([a-zA-Z]+) (\d+)([a-zA-Z]*)\.json", class_name)
    if match:
        prefix, number, letter = match.groups()
        return (prefix, int(number), letter)
    else:
        return (class_name, 0, "")  # Handle cases where the pattern doesn't match
    


# Get a list of the files in the folder
files = os.listdir(src_dir)
sorted_files = sorted(files, key=custom_alphanumeric_sort_key)

for i in sorted_files:
    with open('scraper/db_update/file.txt', 'a') as f:
        f.write(i)
        f.write("\n")


# Iterate over the files and read their contents
for i, file in enumerate(sorted_files):
    with open(f"{src_dir}/{file}", "r") as f:
        
        course_data = json.load(f)
        name = course_data["name"]
        order = i
        print(name)
        print(order)
        data, count = supabase.table('new_all_courses').upsert({'name': name,'order':order, 'info' :  course_data}).execute()




