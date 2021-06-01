from os import listdir, getcwd, path, walk
from csv import DictReader, DictWriter, reader
from collections import defaultdict

ORIG_CODES = "8182	8365	5961	0400	0410	0411	0413	0417	0445	0450	0455	0460	0470	0475	0478	0500	0510	0518	0520	0523	0530	0547	0610	0620	0625	0653	0654	0408	9699/SY	8685	9479/S	9479/B	9481/S	9481/B	9607/SY	9607/BY	9608/BY	9618/SY	9626/SY	9708/SY	9708/BY	1JA0	1MU0	4MA1	4PM1	9CN0	9DR0	9DT0	9ET0	9FR0	9PE0	9686	9687	7993	DBPT6	DMGN5	DLGT7	WBI11	WBI12	WBI13	WBI14	WBI15	WBI16	WCH11	WCH12	WCH13	WCH14	WCH15	WCH16	WPH11	WPH12	WPH13	WPH14	WPH15	WPH16	WBS11	WBS12	WBS13	WBS14	WGE01	WGE02	WGE03	WGE04	WHI01	WHI02	WHI03	WHI04	WMA11	WMA12	WST01	WME01	WME02	WDM11	WFM01	WMA13	WMA14	WFM02	WST02	WST03"
FN_CODES = ORIG_CODES.replace("/BY", "").replace("/SY", " AS").replace("/B", "").replace("/S", " AS").split("\t")
ORIG_CODES = ORIG_CODES.split("\t")
GRADE_DATA = defaultdict(dict)
MIN_CANDIDATE = 600
MAX_CANDIDATE = 9999

traversed = []

def source_grade_data():
     """Parse the .tsv file master grade sheet"""
     global GRADE_DATA
     
     with open("export.tsv") as f:
          
          lines = [line.strip() for line in f.readlines()]
          codes = lines[0].split("\t")[1:]
          
          for row in lines[4:]:
               row = row.split("\t")
               
               candidate_number = row[0]               
               if candidate_number.isdigit() and MIN_CANDIDATE <= int(candidate_number) <= MAX_CANDIDATE:               
                    for i, grade in enumerate(row[2:]):                         
                         if grade.strip():                              
                              this_course = codes[i]     
                              GRADE_DATA[this_course][candidate_number] = grade
               

def get_course_code(filename):
     """Find the course code from the .csv's filename"""
     for orig_c, fn_c in zip(ORIG_CODES, FN_CODES):
          if fn_c in filename:
               
               return orig_c

     raise Exception(f"I can't find course code in {filename}")

def get_grade(course_code, can_num):
     """Look in the grade dictionary to find the candidate's grade"""     
     if course_code in GRADE_DATA:
          course = GRADE_DATA[course_code]
     else:
          raise Exception(f"I can't find course code {course_code} in grade data")

     for c in [can_num, str(int(can_num))]:     
          if c in course:
               return course[c]     
     raise Exception(f"{can_num} does not have a grade for course {course_code}")
         

def insert_grades(full_path, course_code):
     """Open the .csv file and add the candidates' grades"""
     
     with open(full_path, newline='') as file:
          csv_read = DictReader(file)
          candidates = [row for row in csv_read]

     

     for candidate in candidates:          
          try:               
               grade = get_grade(course_code, candidate['Candidate Number'])
          except Exception as e:
               print(e)
               grade = input("Enter 'X' to withdraw, input grade, or blank to abandon:\n")
               if grade == "":
                    raise Exception(f"Missing data - CSV write abandoned for {full_path}")

          candidate['Grade'] = grade

     fn = full_path.split("/")[-1]
     

     with open(getcwd()+"/"+"grades_final/"+fn, 'w', newline='') as file:
          
          fieldnames = list(candidates[0].keys())
          csv_write = DictWriter(file, fieldnames=fieldnames)
          csv_write.writeheader()          
          csv_write.writerows(candidates)
               

def walk_folders(folder=None):
     """Walk the directory and find the .csv files to populate"""
     if folder is None:
          folder = getcwd()

     for dirpath, dirnames, filenames in walk(folder):


          for fn in filenames:
               if "grades_final" not in dirpath and fn.endswith(".csv") and "BTEC" not in fn:          
                    course_code = get_course_code(fn)
                    insert_grades(dirpath+"/"+fn, course_code)



if __name__ == "__main__":

     source_grade_data()
     walk_folders()
