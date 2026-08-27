import numpy as np

data = np.loadtxt('Student Marks',delimiter=",",dtype=str)
print(data)

names = data[:,0]
print(names)
marks = data[1:,1:].astype(int)
print(marks)

"""Total and Average of Every Student"""
total_marks = np.sum(marks,axis=1)
print("Total Marks Of Every Subject Is: ",total_marks)

avg_marks = np.mean(marks,axis=1)
print("Average Marks Is: ",avg_marks)

"""Class Result"""
class_average = np.mean(marks)
highest_numbers = np.max(total_marks)
topper_index = np.argmax(total_marks)
topper_name = names[topper_index]

"""Fail/Pass Students"""
status = np.where(avg_marks>40,"Pass","Fail")
print(status)

"""Final Output"""
print("____Result____")
for i in range(len(names)):
    print(f"{names[i]}: Total={total_marks[i]},Average={avg_marks[i]},{status[i]}")


#select users.name,user.email,addresses.state from users inner join addresses on users.id = addresses.user_id;a