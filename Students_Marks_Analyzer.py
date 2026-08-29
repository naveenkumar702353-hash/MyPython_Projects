import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
students_data=pd.DataFrame({
    "Student_Id":[101,102,103,104,105,106,107,108,109,110],
    "Name":["Naveen","Kumar","Arun","Vijay","Santhosh","Ajith","Sanmugam","Surya","Dhanush","Kathi"],
    "Physics_marks":[78,67,98,67,50,70,88,69,79,75],
    "Chemistry_marks":[80,75,69,90,65,80,69,80,79,90],
    "Maths_marks":[90,80,70,75,78,60,69,84,79,90]
    })
Ph=np.array(students_data["Physics_marks"])
Ch=np.array(students_data["Chemistry_marks"])
M=np.array(students_data["Maths_marks"])
student_average = (Ph + Ch + M) / 3
class Analyzer():
    def marks(self,data):
        total=np.sum(data)
        average=np.mean(data)
        highest=np.max(data)
        lowest=np.min(data)
        return total,average,highest,lowest

analyzer=Analyzer()
p_total,p_avg,p_max,p_min=analyzer.marks(Ph)
c_total,c_avg,c_max,c_min=analyzer.marks(Ch)
m_total,m_avg,m_max,m_min=analyzer.marks(M)
print(f"Physics Total mark:{p_total}")
print(f"Physics Average mark:{p_avg}")
print(f"Physics Highest mark:{p_max}")
print(f"Physics Lowest mark:{p_min}")

print(f"Chemistry Total mark:{c_total}")
print(f"Chemistry Average mark:{c_avg}")
print(f"Chemistry Highest mark:{c_max}")
print(f"Chemistry Lowest mark:{c_min}")

print(f"Maths Total mark:{m_total}")
print(f"Maths Average mark:{m_avg}")
print(f"Maths Highest mark:{m_max}")
print(f"Maths Lowest mark:{m_min}")

print(students_data["Name"][student_average>80])
plt.plot(students_data["Name"],student_average,marker="o",markerfacecolor="grey",color="black",markersize=7)
plt.xlabel("Students Name")
plt.ylabel("Average")
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.3)
plt.figure()
subject=["Physics","Chemistry","Maths"]
Average=[p_avg,c_avg,m_avg]
plt.bar(subject,Average)
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()
