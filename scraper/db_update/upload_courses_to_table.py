import keys
from supabase import create_client, Client
import json
import re
url: str = keys.get_url()
key: str = keys.get_key()

supabase: Client = create_client(url, key)

import os

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
    print(i)


# Iterate over the files and read their contents
for file in sorted_files:
    with open(f"{src_dir}/{file}", "r") as f:
        
        course_data = json.load(f)
        name = course_data["name"]
        print(name)
        data, count = supabase.table('all_courses').upsert({'name': name, 'info' :  course_data}).execute()



