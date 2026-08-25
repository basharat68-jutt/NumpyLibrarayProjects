# Student Marks Analyzer 📊

A simple **Student Marks Analyzer** project built using **Python and NumPy**.
This project analyzes students' marks and provides student-wise, subject-wise, and overall class statistics.

## 📌 Features

* Calculate **total marks** of every student
* Calculate **average marks** of every student
* Determine whether a student **Passed or Failed**
* Find the **Topper** of the class
* Find all **Failed Students**
* Calculate **subject-wise average marks**
* Find the **highest marks** in each subject
* Find the **lowest marks** in each subject
* Calculate the **class average**
* Find the **highest and lowest score** in the class
* Calculate the **standard deviation** of all marks

## 🛠️ Technologies Used

* **Python**
* **NumPy**

## 📂 Project Structure

```text
Student-Marks-Analyzer/
│
├── student_marks_analyzer.py
└── README.md
```

## 📊 Dataset

The project contains marks of 5 students in 3 subjects:

| Student | Math | English | Stat |
| ------- | ---: | ------: | ---: |
| Ali     |   85 |      78 |   92 |
| Awais   |   45 |      52 |   60 |
| Arslan  |   67 |      54 |   86 |
| Anas    |   54 |      76 |   56 |
| Hassan  |   56 |      45 |   87 |

**Passing Marks:** 40

## 🔍 NumPy Functions Used

This project demonstrates several useful NumPy functions:

* `np.sum()` — Calculate total marks
* `np.average()` — Calculate averages
* `np.all()` — Check whether all subjects meet the passing criteria
* `np.any()` — Check whether any subject is below passing marks
* `np.argmax()` — Find the index of the highest total
* `np.where()` — Find indexes of failed students
* `np.max()` — Find maximum marks
* `np.min()` — Find minimum marks
* `np.mean()` — Calculate overall mean
* `np.std()` — Calculate standard deviation

## 📐 Understanding `axis`

A major concept demonstrated in this project is NumPy's `axis` parameter.

### `axis=1`

Used for calculations **student-wise**, across each student's subjects.

```python
np.sum(marks, axis=1)
```

This calculates the total marks for every student.

### `axis=0`

Used for calculations **subject-wise**, down each column.

```python
np.average(marks, axis=0)
```

This calculates the average marks for each subject.

## ▶️ How to Run

### 1. Install NumPy

```bash
pip install numpy
```

### 2. Run the Python file

```bash
python student_marks_analyzer.py
```

## 🎯 Purpose of the Project

The main purpose of this project is to practice **NumPy arrays, aggregation functions, conditions, indexing, and axis operations** by creating a small real-world data analysis project.

## 🚀 Future Improvements

Possible improvements include:

* Add more students dynamically
* Take student marks as user input
* Save results to a CSV file
* Create charts using Matplotlib
* Add grade calculation (`A`, `B`, `C`, etc.)
* Find the topper in each individual subject
* Create a complete student performance report

## 👨‍💻 Author

**Basharat Jutt**

---

⭐ If you find this project useful, feel free to give it a star!
