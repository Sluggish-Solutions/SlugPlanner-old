import json
import os
import string
class Course:
    
    #todo fix the perms / variables
    
    def __init__(self, classes:list()):
        head = classes[0]
        self.name = head.name
        self.title = head.title
        self.description = head.description
        self.pre_reqs = head.pre_reqs
        self.class_notes = head.class_notes
    
        try:
            self.career = head.class_details["Career"]
        except:
            self.career = "error"

        try:
            if head.class_details["General Education"] == "\u00a0":
                self.gen_ed_code = "NULL"
            else:
                self.gen_ed_code = head.class_details["General Education"]
        except:
            self.gen_ed_code = "error"
            
        try:
            self.type = head.class_details["Type"]
        except:
            self.type = "error"
            
        try:
            self.credits = head.class_details["Credits"]
            self.credits = self.credits[:self.credits.index(" ")]
        except:
            self.credits = "error"
        
        self.classes = classes
        
        self.quarters_offered = self.get_quarters_offered()
        self.quarterly_info = self.get_quarterly_info()
        
        self.folder_path = "scraper/courses/test"
        
    def get_quarters_offered(self):
        quarters = set()
        
        for i in self.classes:
            quarters.add(i.quarter)
        
        quarters = list(quarters)
        return sorted(quarters)
        

    def get_quarterly_info(self):
        
        all_info = {}
        
        for quarter in self.quarters_offered:
            quarter_info = {}
            quarters_classes = [i for i in self.classes if quarter == i.quarter]

            #* Seat Data
            total_seats = 0
            filled_seats = 0
            
            for class_obj in quarters_classes:

                try:
                    total_seats+= int(class_obj.class_details['Enrollment Capacity'])
                except:
                    try:
                        total_seats+= int(class_obj.class_details['Combined Section Capacity'])
                    except:
                        total_seats = -1
                   
                try:
                    filled_seats += int(class_obj.class_details["Enrolled"])
                except:
                    filled_seats = 1

            
            quarter_info["total_seats"] = total_seats
            quarter_info["filled seats"] = filled_seats        
            
            #* priority data
            priority = "none"
            try:
                percentage_filled = (filled_seats / float(total_seats))*100
                
            except:
                priority = "unavailible"
                percentage_filled = -1
            
            if 0 <= percentage_filled <=50:
                priority="very low"
            elif 50 < percentage_filled <= 75:
                priority = "low"
            elif 75 < percentage_filled <= 85:
                priority = "moderate"
            elif percentage_filled > 85:
                priority = "high"
            
            
            quarter_info["priority"] = priority
            
            all_info[quarter] = quarter_info
        
        return all_info

    def toJson(self):
        
        #! must be in this order  
        data_dict = {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "pre_req_data": self.pre_reqs,
            "class_notes": self.class_notes,
            "career": self.career,
            "gen_ed_code": self.gen_ed_code,
            "type": self.type,
            "credits": self.credits,
            # "classes": self.classes,
            "quarters_offered": self.quarters_offered,
            "quarterly_info":self.quarterly_info,
        }
        
        json_object = json.dumps(data_dict, indent=4)
        
        os.makedirs(self.folder_path, exist_ok=True)
        
         # Check for any special characters or spaces in self.name
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        cleaned_name = ''.join(c if c in valid_chars else '_' for c in self.name)

        with open(f"{self.folder_path}/{cleaned_name}.json", 'w') as outfile:
            outfile.write(json_object)



