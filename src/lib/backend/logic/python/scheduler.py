import keys
import json
from supabase import create_client, Client

url: str = keys.get_url()
key: str = keys.get_key()

supabase: Client = create_client(url, key)

response = supabase.table("all_courses").select("*").order('order', desc=False).execute()

# Assuming response is a list of dictionaries
weird_shit = response.json()

ordered_classes = json.loads(weird_shit)

print(type(ordered_classes))


ordered_classes = ordered_classes["data"]

list_of_classes = {}
for i in ordered_classes:
    name = i["name"]
    list_of_classes[name] = i


###START OF LOGIC
major = "CS"
prereq = ['AP C BC 3', 'CSE 20', 'WRIT 1']

def prereq_check(prereq, desired_class):
    flag = True
    for i in list_of_classes[desired_class]
if(major == 'CS'):





# ordered classes is now a list of dicts, with each dict being class info