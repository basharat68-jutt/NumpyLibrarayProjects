import numpy as np
employees = 3
kpis = 4
kpis_total = kpis * 10
data = np.zeros((employees,kpis),dtype=int)
for i in range(employees):
    print(f"Enter Data For {i+1} emplyee")
    for j in range(kpis):
        if j == 0:
            data[i,j] = int(input("Enter Sales of this employee"))
        elif j == 1:
            data[i,j] = int(input("Enter Attendance of this employee"))
        elif j == 2:
            data[i,j] = int(input("Enter Projects of this employee"))
        elif j == 3:
            data[i,j] = int(input("Enter Rating of this employee"))
print(data)
total_score = np.sum(data,axis=1)
print("Total Score Is: ",total_score)
Average_Score = np.average(data)
print("Average Score Is: ",Average_Score)
performance = (total_score / kpis_total) * 100
print("Performance % Is: ",performance,"%")
def gra(per):
    if per >= 7: return "A"
    elif per >=6: return "B"
    elif per>=5:return "C"
    elif per>=4:return "D"
    else: return "F"

grade = gra(performance)
print(grade)
promote_or_not = np.where(performance >=7 , "promote","not promote")
print(promote_or_not)
best_employee = np.argmax(total_score)
print(total_score[best_employee])
worst_employee = np.argmin(total_score)
print(total_score[worst_employee])
kpis_avg = np.mean(total_score)
print(np.round(kpis_avg,2))
