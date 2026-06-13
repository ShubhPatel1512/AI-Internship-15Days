"""
Day 4 - Data Handling with Pandas
Tasks:
1. DataFrame basics: read_csv, head(), info(), describe()
2. Analyze: average, highest, lowest marks per subject
3. Generate bar and pie charts using Matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------
# 1. DATAFRAME BASICS
# -----------------------------------------------------

# Read the CSV file into a DataFrame
df = pd.read_csv("student_marks.csv")

print("=" * 50)
print("1. FIRST 5 ROWS - head()")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("2. DATAFRAME INFO - info()")
print("=" * 50)
print(df.info())

print("\n" + "=" * 50)
print("3. STATISTICAL SUMMARY - describe()")
print("=" * 50)
print(df.describe())

# -----------------------------------------------------
# 2. ANALYSIS: AVERAGE, HIGHEST, LOWEST MARKS PER SUBJECT
# -----------------------------------------------------

print("\n" + "=" * 50)
print("4. ANALYSIS PER SUBJECT")
print("=" * 50)

# Group data by Subject
grouped = df.groupby("Subject")["Marks"]

avg_marks = grouped.mean().round(2)
max_marks = grouped.max()
min_marks = grouped.min()

# Combine into a single summary table
summary = pd.DataFrame({
    "Average Marks": avg_marks,
    "Highest Marks": max_marks,
    "Lowest Marks": min_marks
})

print(summary)

# Find which student got the highest/lowest marks per subject
print("\n--- Top Scorer per Subject ---")
for subject in df["Subject"].unique():
    subject_df = df[df["Subject"] == subject]
    top_student = subject_df.loc[subject_df["Marks"].idxmax()]
    low_student = subject_df.loc[subject_df["Marks"].idxmin()]
    print(f"{subject}: Highest -> {top_student['Name']} ({top_student['Marks']}) | "
          f"Lowest -> {low_student['Name']} ({low_student['Marks']})")

# -----------------------------------------------------
# 3. CHARTS USING MATPLOTLIB
# -----------------------------------------------------

# --- BAR CHART: Average Marks per Subject ---
plt.figure(figsize=(8, 5))
avg_marks.plot(kind="bar", color=["#4C72B0", "#55A868", "#C44E52"])
plt.title("Average Marks per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.xticks(rotation=0)
for i, val in enumerate(avg_marks):
    plt.text(i, val + 1, str(val), ha="center", fontweight="bold")
plt.tight_layout()
plt.savefig("average_marks_bar_chart.png")
print("\nSaved: average_marks_bar_chart.png")

# --- BAR CHART: Highest vs Lowest Marks per Subject ---
plt.figure(figsize=(8, 5))
x = range(len(summary.index))
width = 0.35
plt.bar([i - width/2 for i in x], summary["Highest Marks"], width, label="Highest", color="#2ca02c")
plt.bar([i + width/2 for i in x], summary["Lowest Marks"], width, label="Lowest", color="#d62728")
plt.xticks(x, summary.index)
plt.title("Highest vs Lowest Marks per Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.legend()
plt.tight_layout()
plt.savefig("highest_lowest_bar_chart.png")
print("Saved: highest_lowest_bar_chart.png")

# --- PIE CHART: Overall Marks Distribution by Subject ---
total_marks_by_subject = df.groupby("Subject")["Marks"].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    total_marks_by_subject,
    labels=total_marks_by_subject.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#66b3ff", "#99ff99", "#ffcc99"],
    explode=[0.03] * len(total_marks_by_subject)
)
plt.title("Total Marks Distribution by Subject (All Students)")
plt.tight_layout()
plt.savefig("marks_distribution_pie_chart.png")
print("Saved: marks_distribution_pie_chart.png")

# --- PIE CHART: Individual Student Average Marks Share ---
student_avg = df.groupby("Name")["Marks"].mean().round(2)

plt.figure(figsize=(8, 8))
plt.pie(
    student_avg,
    labels=student_avg.index,
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Each Student's Share of Average Marks")
plt.tight_layout()
plt.savefig("student_avg_pie_chart.png")
print("Saved: student_avg_pie_chart.png")

print("\nAll charts generated successfully!")
