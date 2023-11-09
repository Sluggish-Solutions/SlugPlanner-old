from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from course import Course
import os
from class_obj import Class_holder

start_time = time.time()


def get_courses(quarter):
        
    # URL of the page we want to scrape
    url = "https://pisa.ucsc.edu/class_search/index.php"

    driver = webdriver.Firefox()
    driver.get(url)

    time.sleep(2)
    
    term = Select(driver.find_element(By.ID, 'term_dropdown'))
    
    if quarter == "fall":
        term.select_by_visible_text("2023 Fall Quarter")
    elif quarter == "winter":
        term.select_by_visible_text("2023 Winter Quarter")
    elif quarter == "spring":
        term.select_by_visible_text("2023 Spring Quarter")
    else:
        raise Exception("select proper quarter")

    # Selecting "All Classes" from the dropdown menu on the webpage
    inputClassType = Select(driver.find_element(By.ID, 'reg_status'))
    inputClassType.select_by_visible_text("All Classes")

    # Finding and clicking the "Submit" button
    sub_butt = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-lg.btn-primary.btn-block")
    sub_butt.click()
    
    shown_per_page = Select(driver.find_element(By.ID, "rec_dur"))
    shown_per_page.select_by_visible_text("100")
    
    class_id_links = []
    
    while True:
    # for i in range(1):
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Assuming class_id_xxx is present in the 'id' attribute of the 'a' tags
        for link in soup.find_all('a', id=lambda x: x and x.startswith('class_id_')):
            href = link.get('href')
            class_id_links.append(href)

        try:
            button = driver.find_element(By.LINK_TEXT, "next")
            button.click()
        except:
            break
        
    # Print the total number of class links extracted
    print(f"scraped_classes length = {len(class_id_links)}")
            
    classes = []
    
    #getting course data
    for i, link in enumerate(class_id_links):
        
        print(f"working on {quarter} class {i+1}")
        
        url = f"https://pisa.ucsc.edu/class_search/{link}"
        driver.get(url)

        dept_num = None
        name = None
        class_details = []
        description = None
        pre_reqs = None

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # Class Name
        className = soup.find("h2").text.strip()
        name = className

        # Class info
    
        class_infos = soup.find_all('dl')

        for class_info in class_infos:
            params = class_info.find_all('dt')
            values = class_info.find_all('dd')

            for param, value in zip(params, values):
                class_details.append((param.text, value.text))

        # Description
        # Find the <div> element with the class "panel-body"
        descrip_head = soup.find("div", string="Description")
        descrip_text = descrip_head.find_next_sibling("div")
        description = descrip_text.get_text(strip=True) if descrip_text else ''

        # Pre-requisites
        try:
            pre_req_head = soup.find("div", string="Enrollment Requirements")
            pre_req_text = pre_req_head.find_next_sibling("div")
            pre_reqs = pre_req_text.get_text(strip=True) if pre_req_text else ''
            pre_reqs = pre_reqs[pre_reqs.index(":") + 1:].strip()
        except:
            pre_reqs = 'NULL'

        #TODO add class notes scraper
        
        try:
            class_notes_head = soup.find("div", string="Class Notes")
            class_notes_text = class_notes_head.find_next_sibling("div")
            class_notes = class_notes_text.get_text(strip=True) if class_notes_text else ''
        except:
            class_notes = "NULL"
        # Create a Class_holder object and add it to the list of classes
        classes.append(Class_holder(name=dept_num, title=name, class_details=class_details, description=description, pre_reqs=pre_reqs, class_notes=class_notes, quarter=quarter))

    driver.close()
    return classes
    

def combine_classes(fall, winter, spring):
    all_classes = fall + winter + spring

    print(f'classes pre grouping:{len(all_classes)}')
    
    sorted_classes = sorted(all_classes, key=lambda x: x.name)
    
    grouped_classes = []
    temp = []

    while len(sorted_classes) != 0:
        head = sorted_classes[0]
        temp.append(head)
        
        # if len(classes) != 1:
        for i in range(len(sorted_classes)):
            
            try:
                next_obj = sorted_classes[i+1]
            except IndexError:
                print()
                if len(temp) > 0:
                    grouped_classes.append(temp)
    
                    temp = []

                else:
                    if grouped_classes[-1][0].name != head.name:
                        grouped_classes.append([head])

                sorted_classes.remove(head)
                break
                
                
            if head.name == next_obj.name:
                temp.append(next_obj)
            else:
                grouped_classes.append(temp)
                
                for i in temp:
                    sorted_classes.remove(i)
                
                temp = []                
                break

    if grouped_classes[-1][0].name == grouped_classes[-2][0].name:
        grouped_classes.remove(grouped_classes[-1])

    count = 0
    for i in grouped_classes:
        print("-"*20)
        for j in i:
            print(j.name)
            count+=1
            
    print(f"total amount of classes = {count}")
                
    print(f"classes size: {len(sorted_classes)}")
    print(f"grouped_classes size: {len(grouped_classes)}")
        
    
    return grouped_classes



def construct_courses(groups):
    courses = []
    
    for group in groups:
        courses.append(Course(group))
        
    #return course object
    return courses

if __name__ == "__main__":
    
    fall_courses = get_courses("fall")
    winter_courses = get_courses("winter")
    spring_courses = get_courses("spring")


    
    all_classes = combine_classes(fall_courses, winter_courses, spring_courses)
    
    all_courses = construct_courses(all_classes)
    
    for course in all_courses:
        course.toJson()

    end_time = time.time()
    print(f"Elapsed time: {end_time-start_time} seconds")

    
    
    