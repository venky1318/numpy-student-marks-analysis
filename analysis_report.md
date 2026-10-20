# NumPy Student Marks Analysis

## 1. Project Overview

This project demonstrates the use of NumPy for numerical analysis by calculating statistical measures from a collection of student marks.

The program uses a NumPy array containing marks for ten students and calculates the mean, median, maximum, minimum, and population standard deviation.

## 2. Objective

The objectives are:

- To create a NumPy array of student marks.
- To calculate the mean and median.
- To identify the highest and lowest marks.
- To calculate the standard deviation.
- To interpret the statistical results.

## 3. Dataset

The project uses manually created marks for ten students, with each mark represented on a scale of 0 to 100.

Marks: 78, 85, 92, 67, 88, 76, 95, 81, 72, 86.

No external dataset is required.

## 4. Statistical Methods

**Mean:** The sum of all marks divided by the number of students.

**Median:** The middle value after arranging the marks in ascending order. For an even number of observations, it is the average of the two middle values.

**Maximum:** The highest mark in the dataset.

**Minimum:** The lowest mark in the dataset.

**Standard Deviation:** A measure of how widely the marks vary around the mean. This program uses population standard deviation through `numpy.std()`.

## 5. Results

| Statistic | Result |
|---|---:|
| Number of students | 10 |
| Mean | 82.00 |
| Median | 83.00 |
| Maximum | 95.00 |
| Minimum | 67.00 |
| Population standard deviation | Approximately 8.05 |

## 6. Interpretation

The average mark is 82, indicating a strong overall performance in this sample.

The median is 83, which is close to the mean. The highest mark is 95, while the lowest is 67.

The population standard deviation is approximately 8.05 marks. This indicates that the marks have a relatively limited spread around the average compared with a dataset exhibiting much larger variation.

These conclusions describe only the sample marks used in this project.

## 7. Tools and Technologies

- Python 3
- NumPy
- Visual Studio Code
- GitHub

## 8. Conclusion

The project demonstrates how NumPy simplifies numerical calculations using built-in statistical functions. It provides a basic understanding of descriptive statistics and their use in student performance analysis.

The program can be extended to accept marks from users or read student marks from a CSV file.
