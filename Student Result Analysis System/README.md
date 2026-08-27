# Student Result Analysis System

A simple Python project built with **NumPy** to analyze student marks and generate a complete class result.

## Features

* Read student marks from a CSV file using NumPy.
* Extract student names and subject marks.
* Calculate total marks for every student.
* Calculate average marks for every student.
* Calculate the overall class average.
* Find the highest total marks.
* Identify the class topper.
* Determine whether a student has **Pass** or **Fail** status.
* Display a formatted final result.

## Technologies Used

* Python
* NumPy
* CSV

## Project Structure

```text
Student-Result-Analysis-System/
│
├── student_result.py
├── Student Marks.csv
└── README.md
```

## How It Works

The program loads student data from a CSV file using NumPy:

```python
data = np.loadtxt('Student Marks', delimiter=",", dtype=str)
print(data)
```

Student names and marks are then separated from the dataset:

```python
names = data[:, 0]
marks = data[1:, 1:].astype(int)
```

### Total Marks

The total marks of every student are calculated using `np.sum()`:

```python
total_marks = np.sum(marks, axis=1)
```

### Average Marks

The average marks of every student are calculated using `np.mean()`:

```python
avg_marks = np.mean(marks, axis=1)
```

### Class Average

The overall average of all students' marks is calculated using:

```python
class_average = np.mean(marks)
```

### Finding the Topper

The highest total marks are found using `np.max()`, and `np.argmax()` is used to identify the topper:

```python
highest_numbers = np.max(total_marks)
topper_index = np.argmax(total_marks)
topper_name = names[topper_index]
```

### Pass / Fail Status

Students are classified based on their average marks:

```python
status = np.where(avg_marks > 40, "Pass", "Fail")
```

Students with an average greater than 40 are marked as **Pass**, while others are marked as **Fail**.

## Example Output

```text
____Result____

Ali: Total=350, Average=70.0, Pass
Ahmed: Total=280, Average=56.0, Pass
Usman: Total=190, Average=38.0, Fail
```

## Learning Outcomes

Through this project, I practiced:

* NumPy arrays
* Array slicing
* Data type conversion
* `np.sum()`
* `np.mean()`
* `np.max()`
* `np.argmax()`
* `np.where()`
* Reading CSV data with NumPy
* Calculating student performance
* Basic class result analysis

## Future Improvements

* Add percentage calculation.
* Add grades such as A, B, C and D.
* Find highest and lowest marks in each subject.
* Display subject-wise performance.
* Save the generated result to a CSV file.
* Add graphical representation of student performance.
