
"""
NumPy Student Marks Analysis

Description:
Calculate mean, median, maximum, minimum, and standard
deviation from a NumPy array of student marks.
"""

import numpy as np


def analyze_marks(marks):
    """Calculate descriptive statistics for student marks."""

    if marks.size == 0:
        raise ValueError("The marks array cannot be empty.")

    if not np.all(np.isfinite(marks)):
        raise ValueError("Marks must contain valid numeric values.")

    if np.any((marks < 0) | (marks > 100)):
        raise ValueError("Marks must be between 0 and 100.")

    results = {
        "Mean": np.mean(marks),
        "Median": np.median(marks),
        "Maximum": np.max(marks),
        "Minimum": np.min(marks),
        "Standard Deviation": np.std(marks),
    }

    return results


def display_results(marks, results):
    """Display the marks and calculated statistics."""

    print("\n" + "=" * 52)
    print("          NUMPY STUDENT MARKS ANALYSIS")
    print("=" * 52)

    print("\nStudent Marks:")
    print(marks)

    print("\nSTATISTICAL RESULTS")
    print("-" * 52)

    for statistic, value in results.items():
        print(f"{statistic:<25}: {value:.2f}")

    print("-" * 52)

    print("\nINTERPRETATION")
    print(f"Average mark: {results['Mean']:.2f}")
    print(f"Highest mark: {results['Maximum']:.2f}")
    print(f"Lowest mark : {results['Minimum']:.2f}")

    print(
        f"Standard deviation: "
        f"{results['Standard Deviation']:.2f}"
    )

    if results["Standard Deviation"] < 10:
        print("Interpretation: Marks are relatively consistent.")
    elif results["Standard Deviation"] < 20:
        print("Interpretation: Marks show moderate variation.")
    else:
        print("Interpretation: Marks show high variation.")

    print("\nAnalysis completed successfully.")


def main():
    # Sample marks for ten students, out of 100.
    marks = np.array(
        [78, 85, 92, 67, 88, 76, 95, 81, 72, 86],
        dtype=float
    )

    results = analyze_marks(marks)
    display_results(marks, results)


if __name__ == "__main__":
    main()
