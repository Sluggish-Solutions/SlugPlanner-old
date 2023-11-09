import json
import os
import string
class Course:
    
    #todo fix the perms / variables
    
    def __init__(self, classes:list()):
        head = classes[0]
        
        self.classes = classes
        self.name = head.name
        self.title = head.title
        self.class_details = head.class_details
        self.description = head.description
        self.pre_reqs = head.pre_reqs
        self.class_notes = head.class_notes
        

        #todo make class details get rid of ('Enrollment Capacity', 'Enrolled', 'Wait List Capacity', 'Wait List Total'])


        self.total_seats = None
        self.filled_seats = None 
        
        #todo figure out how to format these
        self.priority = None #Should be on a scale of like 1-3
        
        #todo figure out how to format these
        self.quarters_offered = set()
        
        
        self.folder_path = "main/courses"
        
        
    def organize_class_details(self):
        ...

    
    def calculate_priority(self):
        try:
            percentage_filled = (self.filled_seats / float(self.total_seats))*100
            
        except:
            self.priority = "unavailible"
            return
        
        if percentage_filled <=50:
            self.priority="very low"
        elif 50 < percentage_filled <= 75:
            self.priority = "low"
        elif 75 < percentage_filled <= 85:
            self.priority = "moderate"
        elif percentage_filled > 85:
            self.priority = "high"

        

    def calculate_seat_data(self):
        total = 0
        filled = 0
        for class_obj in self.classes:

            try:
                total+= int(class_obj.class_details['Enrollment Capacity'])
            except:
                total+= int(class_obj.class_details['Combined Section Capacity'])
                
            filled += int(class_obj.class_details["Enrolled"])
        
        
        
        self.total_seats = total
        self.filled_seats = filled
        
    
    #todo
    def calculate_quarters_offered(self):
        self.quarters_offered = "no wtf"
        ...
    
    
    def toJson(self):
        


        #! must be in this order
        self.calculate_seat_data()
        self.calculate_priority()
        self.calculate_quarters_offered()
        
        
        data_dict = {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "details": self.class_details,
            "prerequisites": self.pre_reqs,
            "classnotes": self.class_notes,
            "total-seats": self.total_seats,
            "filled_seats":self.filled_seats,
            "quarters_offered": self.quarters_offered,
            "priority":self.priority
        }
        
        json_object = json.dumps(data_dict, indent=4)
        
        os.makedirs(self.folder_path, exist_ok=True)
        
         # Check for any special characters or spaces in self.name
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        cleaned_name = ''.join(c if c in valid_chars else '_' for c in self.name)

        with open(f"{self.folder_path}/{cleaned_name}.json", 'w') as outfile:
            outfile.write(json_object)



