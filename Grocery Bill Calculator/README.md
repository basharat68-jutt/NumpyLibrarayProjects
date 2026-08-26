# Shopping Bill Calculator

A simple Python project using **NumPy** to calculate the total bill, find the most expensive item, and calculate the average price of purchased items.

## Features

* Calculates the **total bill** of all purchased items.
* Finds the **most expensive item** using `np.argmax()`.
* Calculates the **average price** using `np.average()`.
* Uses NumPy arrays for price calculations.

## Technologies Used

* Python
* NumPy

## Example Data

The project contains the following items and prices:

| Item   | Price |
| ------ | ----: |
| Water  |    50 |
| Potato |    60 |
| Soap   |   110 |
| Lemon  |    60 |
| Sugar  |   180 |

## Output

```text
Total Bill of Things Bought: 460
suger is most expensive with price of 180
92.0
```

## NumPy Functions Used

* `np.sum()` — Calculates the total of all prices.
* `np.argmax()` — Finds the index of the item with the highest price.
* `np.average()` — Calculates the average price.

## How to Run

1. Install NumPy:

```bash
pip install numpy
```

2. Run the Python file:

```bash
python main.py
```

## Purpose

This project is a beginner-level NumPy practice project designed to understand **arrays, aggregation functions, indexing, and basic calculations** in Python.
