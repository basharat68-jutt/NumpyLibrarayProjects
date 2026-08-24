# Data Cleaning

This project demonstrates a basic data cleaning technique using **NumPy**. It focuses on identifying and handling missing values (`NaN`) in salary data.

## Features

* Detects missing values in the dataset.
* Counts the total number of missing values.
* Calculates the average salary while ignoring missing values.
* Replaces missing salary values with the average salary.
* Calculates the final mean and standard deviation.

## Technologies Used

* Python
* NumPy

## How It Works

The project uses a NumPy array containing salary values, including some missing values represented by `NaN`.

First, `np.isnan()` is used to identify the missing values and count them.

Then, `np.nanmean()` calculates the average salary while ignoring the missing values.

The missing values are replaced with the calculated average salary.

Finally, the program calculates the mean and standard deviation of the cleaned data.

## Example

Original data:

```text
[50000, 60000, NaN, 45000, 70000, NaN, 55000, NaN, 65000]
```

The missing values are replaced with the average salary calculated from the available values.

## Purpose

The purpose of this project is to understand how missing values can be detected and handled during the **data cleaning** process using NumPy.
