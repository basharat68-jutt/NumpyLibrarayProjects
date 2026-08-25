import numpy as np

marks = np.array([
    [85,78,92],
    [45,52,60],
    [67,54,86],
    [54,76,56],
    [56,45,87]
])

subjects = ["Math","English","Stat"]
students = ["Ali","Awais","Arslan","Anas","Hassan"]

passing_marks = 40

print("="*40)
print("STUDENT MARKS ANALYZER")
print("="*40)

"""Total of every Students"""
total_marks = np.sum(marks, axis=1)
print(f"Total marks of every student is: {total_marks}")
"""AVERAGE MARKS OF EVERY STUDENT"""
avg_marks = np.average(marks, axis=1)
print(f"Average marks of every student is: {avg_marks}")

print("\n Student Wise Result")
for i in range(len(students)):
    status = "Pass" if np.all(marks[i] >= passing_marks) else "Fail" #np.all agr all values true hoe to he condition true hogi verna nhii
    print(f"{students[i]} Total={total_marks[i]},Avg={avg_marks[i]:.2f}->{status}")

"""Toper and Fail Student Index"""
topper_index = np.argmax(total_marks)
fail_indexes = np.where(np.any(marks < passing_marks, axis=1))[0]
print(f"Toper {students[topper_index]} with {total_marks[topper_index]} Marks")
print(f"Failed Students: {[students[i] for i in fail_indexes]}")
    
"""Subject Wise Analysis"""
subject_avg = np.average(marks, axis=0)
subject_highest = np.max(marks, axis=0)
subject_lowest = np.min(marks, axis=0)

for i in range(len(subjects)):
    print(f"{subjects[i]}: Avg={subject_avg[i]:.2f},High={subject_highest[i]}, Lowest={subject_lowest[i]}")

"""Overall Stats of Class"""
print("\n CLASS STATS")
print(f"Class Average = {np.mean(marks):.2f}")
print(f"Highest Score in Class: {np.max(marks)}")
print(f"Lowest Score in Class: {np.min(marks)}")
print(f"Stranderd Deviation: {np.std(marks):.2f}")