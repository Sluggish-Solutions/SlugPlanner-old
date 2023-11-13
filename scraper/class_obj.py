import json
import re


class Class_holder:
    # Initialize the class with relevant attributes
    def __init__(
        self,
        name: str,
        title: str,
        class_details: list,
        description: str,
        pre_reqs: str,
        class_notes: str,
        quarter,
    ):
        self.name = name  # Department number
        self.title = title  # Class name
        self.class_details = class_details  # List of class details
        self.description = description  # Class description
        self.pre_reqs = pre_reqs  # Class prerequisites
        self.class_notes = class_notes
        self.quarter = quarter
        self.pre_req_text = pre_reqs
        # Path for the JSON output file (unused in the provided code)
        #

        self.format_properties()

        # *individual path
        # self.json_file_path = f"main/classes/{dept_num}.json"

    @staticmethod
    def re_filter(text):
        pattern = re.compile(r"[^A-Z0-9 ]+|MPE")
        return pattern.sub("", text).strip()

    # Format and separate the department number and class name
    def format_name_and_dept_num(self):
        # Extract the department number and class name from the 'name' attribute
        temp_dept_num = self.title[: self.title.index("-")].strip()
        try:
            temp_title = self.title[self.title.index("\u00a0\u00a0") + 2 :].strip()
        except:
            temp_title = "NULL"

        # Update the class attributes
        self.name = temp_dept_num
        self.title = temp_title

    # Format the class details as a dictionary
    def format_class_details(self):
        # Convert the list of class details into a dictionary
        self.class_details = {param: value for param, value in self.class_details}

    # TODO Really need to fix all of these, with specific examples.
    # Format the class prerequisites
    def format_pre_reqs(self):
        temp_conditions = {}
        
        temp_courses = []

        # these variables must be defined
        temp_conditions[
            "restricted_to_majors"
            ] = ""  # Information about class restrictions (if any)
        temp_conditions["erlw"] = False
        temp_conditions["lower_credits_limit"] = 0
        temp_conditions["upper_credits_limit"] = 500

        # Prerequisite(s): two courses from ART 10D, ART 10E, ART 10F. Enrollment is restricted to proposed art and art majors.
        # Check if there are any restrictions on enrollment

        #TODO get accurate data from here        
        if "Enrollment is restricted to" in self.pre_reqs:
            # Extract and store the restriction information
            val = 0

            if "senior" in self.pre_reqs:
                val = 135
            if "junior" in self.pre_reqs:
                val = 90
            if "sophomore " in self.pre_reqs:
                val = 45
            if "first-year" in self.pre_reqs:
                val = -1

            if "graduate" in self.pre_reqs:
                val = -2

            if "major" in self.pre_reqs:
                temp_conditions["restricted_to_majors"] = self.pre_reqs[
                    self.pre_reqs.index("nrollment is restricted to ")
                    + len("nrollment is restricted to ") :
                ]
                val = -3
            if val > 0:
                temp_conditions["lower_credits_limit"] = val
                # arbitrary value
            if val == -1:
                temp_conditions["upper_credits_limit"] = 45

            if val == -2:
                temp_conditions["lower_credits_limit"] = 180

            if val == 0:
                temp_conditions["upper_credits_limit"] = 5
                temp_conditions["lower_credits_limit"] = 200

            # Remove the restriction information from the prerequisites
            self.pre_reqs = re.sub(
                r".*?Enrollment is restricted to.*?\.", "", self.pre_reqs
            )

        # Check if it required Entry Level Reading and writing
        if (
            "satisfaction of the Entry Level Writing and Composition requirements."
            in self.pre_reqs
        ):
            temp_conditions["erlw"] = True
            self.pre_reqs = self.pre_reqs[
                : self.pre_reqs.index(
                    "satisfaction of the Entry Level Writing and Composition requirements."
                )
            ]

        # Initialize a temporary variable to store the formatted prerequisites
        if self.pre_reqs == "NULL":
            pass

        # Check if prerequisites are separated by semicolon or "or"
        elif "; or" not in self.pre_reqs:
            # Split prerequisites by "and" or semicolon
            split_by_and = re.split(r"[; ]+and[; ]+|;", self.pre_reqs)

            for i, req in enumerate(split_by_and):
                # Split by "or" within each requirement
                split_by_or = req.split(" or ")

                for i, thing in enumerate(split_by_or):
                    # Remove non-alphanumeric characters and leading/trailing spaces
                    split_by_or[i] = self.re_filter(split_by_or[i])

                temp_courses.append(split_by_or)

            for item in temp_courses:
                for item_item in item:
                    if item_item == "":
                        item.remove(item_item)

            # for i, req in enumerate(temp_courses):
            #     temp_courses[i] = req

        elif "; or" in self.pre_reqs:
            # Split prerequisites by "or" or ":"
            split_by_or = re.split(r": | or ", self.pre_reqs)

            for i, thing in enumerate(split_by_or):
                if "and" in split_by_or[i]:
                    # Split by "and" and remove non-alphanumeric characters
                    lol = split_by_or[i].split("and")
                    split_by_or[i] = [self.re_filter(lol[0]), self.re_filter(lol[1])]
                else:
                    # Remove non-alphanumeric characters and leading/trailing spaces
                    split_by_or[i] = self.re_filter(split_by_or[i])

            temp_courses.append(split_by_or)

        else:
            raise Exception("need to figure this one out chief")

        # Update the prerequisites with the formatted data
        self.pre_reqs ={"conditions" : temp_conditions, "text" : self.pre_req_text, 'courses': temp_courses}
        

    # Convert the class information to JSON format and write it to a file
    def format_properties(self):
        self.format_name_and_dept_num()
        self.format_class_details()
        self.format_pre_reqs()

    def toJson(self):
        # Format the class information
        self.format_properties()

        # Create a dictionary to represent the class information
        data_dict = {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "class-details": self.class_details,
            "prerequisites": self.pre_reqs,
            "classnotes": self.class_notes,
            "quarter": self.quarter,
        }

        # Serialize the dictionary to a JSON string
        json_object = json.dumps(data_dict, indent=4)

        # Write the JSON data to a file (in append mode)
        with open(self.json_file_path, "a") as outfile:
            outfile.write(json_object)
