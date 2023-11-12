# Scraper
- Need to work on formatting pre-reqs better
- run multiple instances at once? (multithreading) for faster usage

# Uploading to Database
- Actually use the relational capabilities of the database
- Try learning SQL to do it yourself instead of relying on supabase to do it for you
- Maybe look into hosting a supabase database ourselves?


# Database
- Explore the capabilities of the supabase database
- Figure out how to cache the data from supabase? Make it hosted client side on initial webpage load?


# Selection of classes? 
- initally make it like an empty planner where they can drag/drop? nahhh thats cringeeeee

- just make a checker first. Simple check if any given schedule can be used.
- Drag and drop interface for schedules, and the checker will check against satisfied and virtual pre-reqs, along with when courses can be taken. raise error if a proposed schedule cannot be fixed

- Its like a first step, and then we can implement a generator for these schedules


# Backend

- Right now we dont really have a backend, only running on supabase

- In the future, maybe a golang server with python as a database?
	- Sounds kind of complicated for this small project
- Django server perhaps?
	- could do all logic inside of python while just exporing final thing to server

- Or just try to keep implementing data inside of typescript
- Also depends on if django is even compatible with supabase
- REST-api django server with postgres database could be the key? but supabase makes integration so easyyyyyy
