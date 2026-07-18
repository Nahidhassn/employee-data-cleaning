import numpy as np
import pandas as pd


def main():

    # =====================
    # Create Employee DataFrame
    # =====================
    employees = {
        "Employee_ID": ["E101", "E102", "E103", "E104", "E105", "E106"],
        "Name": [" nahid ", "gOOnJon", "ABIR", "rafi", "mim ", "hasan"],
        "Department": ["IT", "HR", "Finance", "IT", np.nan, "Marketing"],
        "Salary": [35000, 42000, 38000, 45000, np.nan, 50000],
        "Experience": [2, 5, 3, 8, 4, 10],
        "Joining_Date": [
            "2023-01-15",
            "2022-08-20",
            "2024-03-10",
            "2021-11-05",
            "2025-06-25",
            "2020-02-18",
        ],
    }

    df = pd.DataFrame(employees)

    # =====================
    # Data Cleaning
    # =====================
    print("\n--- Data Cleaning ---")

    df["Name"] = df["Name"].str.strip().str.title()

    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum())

    df["Department"] = df["Department"].fillna("Unknown")
    df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())

    # =====================
    # Data Transformation
    # =====================
    print("\n--- Data Transformation ---")

    df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

    df["Bonus"] = df["Salary"] * 0.10

    df["Salary_Status"] = np.where(
        df["Salary"] > 40000,
        "High",
        "Normal"
    )

    df["Experience_Level"] = np.where(
        df["Experience"] >= 5,
        "Senior",
        "Junior"
    )

    print(df)

    # =====================
    # Salary Analysis
    # =====================
    print("\n--- Salary Analysis ---")

    salary_summary = df["Salary"].agg(
        Total_Salary="sum",
        Average_Salary="mean",
        Highest_Salary="max",
        Lowest_Salary="min"
    )

    print(salary_summary)

    # =====================
    # Department-wise Analysis
    # =====================
    print("\n--- Department-wise Salary Summary ---")

    department_salary_summary = (
        df.groupby("Department")["Salary"]
        .agg(
            Total_Salary="sum",
            Average_Salary="mean",
            Highest_Salary="max",
            Lowest_Salary="min"
        )
        .reset_index()
    )

    print(department_salary_summary)

    # =====================
    # Filtering
    # =====================
    print("\n--- High Paid IT Employees ---")

    high_paid_it_employees = df.query(
        "Department == 'IT' and Salary > 40000"
    )

    print(high_paid_it_employees)

    # =====================
    # Date Analysis
    # =====================
    print("\n--- Date Analysis ---")

    df["Days_Worked"] = (
        pd.Timestamp.now() - df["Joining_Date"]
    ).dt.days

    employees_joined_2024 = df[
        df["Joining_Date"].dt.year == 2024
    ]

    print("\nEmployees Joined in 2024:")
    print(employees_joined_2024)

    # =====================
    # Reports
    # =====================
    print("\n--- Employee Reports ---")

    best_paid_employee = df.loc[df["Salary"].idxmax()]
    most_experienced_employee = df.loc[df["Experience"].idxmax()]
    least_experienced_employee = df.loc[df["Experience"].idxmin()]

    print("\nBest Paid Employee:")
    print(best_paid_employee)

    print("\nMost Experienced Employee:")
    print(most_experienced_employee)

    print("\nLeast Experienced Employee:")
    print(least_experienced_employee)

    # =====================
    # Performance Evaluation
    # =====================
    print("\n--- Performance Evaluation ---")

    df["Performance"] = np.where(
        (df["Salary"] > 45000) &
        (df["Experience"] >= 5),
        "Excellent",
        "Good"
    )

    print(df[["Name", "Performance"]])

    # =====================
    # Sort by Salary
    # =====================
    print("\n--- Employees Sorted by Salary ---")

    salary_sorted_df = df.sort_values(
        by="Salary",
        ascending=False
    )

    print(salary_sorted_df)


if __name__ == "__main__":
    main()