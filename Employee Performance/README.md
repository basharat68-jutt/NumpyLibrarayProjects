# Employee Performance Management System

A simple **Employee Performance Management System** built with **Python and NumPy**. This project collects employee KPI data, calculates performance scores, assigns grades, determines promotion status, and identifies the best and worst-performing employees.

## 📌 Features

* Enter KPI data for multiple employees
* Store employee data using a NumPy array
* Calculate total score for each employee
* Calculate average score
* Calculate performance percentage
* Assign performance grades
* Determine whether an employee should be promoted
* Find the best-performing employee
* Find the worst-performing employee
* Calculate the average total score
* Round calculated results using NumPy

## 📊 KPIs

The system uses 4 KPIs for each employee:

1. **Sales**
2. **Attendance**
3. **Projects**
4. **Rating**

Each KPI is assumed to have a maximum score of **10**.

## 🛠️ Technologies Used

* Python
* NumPy

## ⚙️ How It Works

The program first creates a NumPy array with rows representing employees and columns representing KPIs.

```python
data = np.zeros((employees, kpis), dtype=int)
```

The user then enters the Sales, Attendance, Projects, and Rating scores for each employee.

The total score is calculated using:

```python
total_score = np.sum(data, axis=1)
```

The performance percentage is then calculated based on the maximum possible score.

The system also uses NumPy functions such as:

* `np.zeros()`
* `np.sum()`
* `np.average()`
* `np.where()`
* `np.argmax()`
* `np.argmin()`
* `np.mean()`
* `np.round()`

## 🎯 Performance Grading

| Performance | Grade |
| ----------- | ----- |
| 7 or above  | A     |
| 6 or above  | B     |
| 5 or above  | C     |
| 4 or above  | D     |
| Below 4     | F     |

> **Note:** The current grading function expects the performance value on a 0–10 scale.

## 📈 Promotion Criteria

An employee is marked as:

* **Promote** → Performance ≥ 7
* **Not Promote** → Performance < 7

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Install NumPy

```bash
pip install numpy
```

### 3. Run the Python file

```bash
python employee_performance.py
```

### 4. Enter Employee Data

The program will ask you to enter the KPI scores for each employee.

## 💡 Example

For 3 employees, the program may store data like:

```text
[[8 9 7 8]
 [6 7 8 6]
 [9 8 9 9]]
```

The program then calculates:

```text
Total Score
Average Score
Performance %
Grade
Promotion Status
Best Employee
Worst Employee
Average Total Score
```

## 📚 Learning Objectives

This project is useful for practicing:

* NumPy arrays
* 2D arrays
* Array indexing
* Nested loops
* `axis=1`
* Aggregation functions
* Conditional logic
* `np.where()`
* `np.argmax()`
* `np.argmin()`
* Basic employee performance analysis

## 👨‍💻 Author

**Basharat Jutt**

This project was created as a practice project to improve Python and NumPy skills.
