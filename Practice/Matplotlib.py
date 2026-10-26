
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. LINE CHART
# ============================================================

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 200]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()


# ============================================================
# 2. LINE CHART - MARKERS AND LINE STYLES
# ============================================================

plt.plot(
    months,
    sales,
    marker="o",
    linestyle="--"
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()


# ============================================================
# 3. BAR CHART
# ============================================================

departments = ["IT", "HR", "Finance", "Sales"]
employees = [8, 5, 6, 10]

plt.bar(departments, employees)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.show()


# ============================================================
# 4. HORIZONTAL BAR CHART
# ============================================================

plt.barh(departments, employees)

plt.title("Employees by Department")
plt.xlabel("Number of Employees")
plt.ylabel("Department")

plt.show()


# ============================================================
# 5. BAR LABELS
# ============================================================

bars = plt.bar(departments, employees)

plt.bar_label(bars)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")

plt.show()


# ============================================================
# 6. SORTED BAR CHART
# ============================================================

import pandas as pd

df = pd.DataFrame({
    "department": departments,
    "employees": employees
})

df = df.sort_values("employees", ascending=False)

bars = plt.bar(df["department"], df["employees"])

plt.bar_label(bars)
plt.title("Employees by Department - Highest to Lowest")
plt.xlabel("Department")
plt.ylabel("Employees")

plt.show()


# ============================================================
# 7. GROUPED BAR CHART
# Compare 2025 vs 2026
# ============================================================

departments = ["IT", "HR", "Finance"]

employees_2025 = [8, 5, 6]
employees_2026 = [10, 7, 9]

x = np.arange(len(departments))
width = 0.35

plt.bar(
    x - width / 2,
    employees_2025,
    width,
    label="2025"
)

plt.bar(
    x + width / 2,
    employees_2026,
    width,
    label="2026"
)

plt.xticks(x, departments)

plt.title("Employees by Department: 2025 vs 2026")
plt.xlabel("Department")
plt.ylabel("Employees")

plt.legend()

plt.show()


# ============================================================
# 8. PIE CHART
# ============================================================

departments = ["IT", "HR", "Finance"]
employees = [10, 5, 8]

plt.pie(
    employees,
    labels=departments
)

plt.title("Company Summary")

plt.show()


# ============================================================
# 9. PIE CHART WITH PERCENTAGES
# ============================================================

plt.pie(
    employees,
    labels=departments,
    autopct="%1.1f%%"
)

plt.title("Employees by Department")

plt.show()


# ============================================================
# 10. PIE CHART WITH EXPLODE
# Highlight IT
# ============================================================

plt.pie(
    employees,
    labels=departments,
    autopct="%1.1f%%",
    explode=[0.1, 0, 0]
)

plt.title("Employees by Department")

plt.show()


# ============================================================
# 11. PIE CHART WITH START ANGLE
# ============================================================

plt.pie(
    employees,
    labels=departments,
    autopct="%1.1f%%",
    explode=[0.1, 0, 0],
    startangle=90
)

plt.title("Employees by Department")

plt.show()


# ============================================================
# 12. HISTOGRAM
# ============================================================

ages = [
    21, 22, 22, 23, 24,
    25, 25, 25, 26, 27,
    28, 30, 31, 35, 40
]

plt.hist(ages)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show()


# ============================================================
# 13. HISTOGRAM WITH BINS
# ============================================================

plt.hist(
    ages,
    bins=5
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show()


# ============================================================
# 14. HISTOGRAM WITH EDGE COLOR
# ============================================================

plt.hist(
    ages,
    bins=5,
    edgecolor="black"
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show()


# ============================================================
# 15. SCATTER PLOT
# Experience vs Salary
# ============================================================

experience = [1, 2, 3, 5, 7, 10]
salary = [30000, 35000, 40000, 50000, 65000, 90000]

plt.scatter(
    experience,
    salary
)

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.show()


# ============================================================
# 16. SCATTER PLOT - MARKER
# ============================================================

plt.scatter(
    experience,
    salary,
    marker="s"
)

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.show()


# ============================================================
# 17. SCATTER PLOT - SIZE AND TRANSPARENCY
# ============================================================

plt.scatter(
    experience,
    salary,
    s=100,
    alpha=0.5
)

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.show()


# ============================================================
# 18. SUBPLOTS
# ============================================================

months = ["Jan", "Feb", "Mar"]
sales = [100, 150, 130]
profit = [40, 70, 60]

plt.subplot(1, 2, 1)

plt.plot(months, sales)
plt.title("Sales")


plt.subplot(1, 2, 2)

plt.plot(months, profit)
plt.title("Profit")


plt.tight_layout()
plt.show()


# ============================================================
# 19. SUBPLOT - 2 x 2 LAYOUT
# ============================================================

plt.subplot(2, 2, 1)
plt.plot(months, sales)
plt.title("Sales")


plt.subplot(2, 2, 2)
plt.bar(months, sales)
plt.title("Bar Chart")


plt.subplot(2, 2, 3)
plt.scatter([1, 2, 3], sales)
plt.title("Scatter")


plt.subplot(2, 2, 4)
plt.hist(sales)
plt.title("Histogram")


plt.tight_layout()
plt.show()


# ============================================================
# 20. FIGURE SIZE
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


# ============================================================
# 21. FINAL COMBINED EXAMPLE
# ============================================================

plt.figure(figsize=(10, 5))

plt.scatter(
    experience,
    salary,
    s=100,
    alpha=0.5,
    marker="o"
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.grid()
plt.tight_layout()

plt.show()


# ============================================================
# MATPLOTLIB COMPLETE
# ============================================================