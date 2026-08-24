"""Handle Missing Values"""

import numpy as np
salaries = np.array([50000,60000,np.nan,45000,70000,np.nan,55000,np.nan,65000])

print("Original Data: ",salaries)
missing_count = np.sum(np.isnan(salaries))
print("Missing Values In Your Data Is: ",missing_count)
"""Fill Null Values With Average"""
avg_salary = np.nanmean(salaries) #nan ko ignore kr k mean
print(avg_salary)
salaries[np.isnan(salaries)] = avg_salary
print(f"Nan is filled by Avg Salary: {avg_salary:.2f}")
print(salaries)
print(f"\nFinal Mean: {np.mean(salaries):.2f}")
print(f"\nFinal Std Dev: {np.std(salaries)}")
