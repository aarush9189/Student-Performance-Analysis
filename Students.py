import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Dataset
df = pd.read_csv("students.csv")
print("Student Data:", df)

# Add Total and Percentage
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Percentage"] = df["Total"] / 3

# Highest marks
topper = df.loc[df["Total"].idxmax()]
print("\nTopper:", topper)

# Lowest marks
low = df.loc[df["Total"].idxmin()]
print("\nLowest Scorer:", low)

# Average marks
avg = df[["Maths", "Science", "English"]].mean()
print("\nAverage Marks:", avg)

# Pass/Fail
df["Result"] = df[["Maths", "Science", "English"]].apply(
    lambda x: "Pass" if all(x >= 40) else "Fail", axis=1
)

print("\nFinal Result:\n", df)

# - VISUALIZATION -

# Bar Chart.
plt.figure(figsize=(8,5))
sns.barplot(x="Name", y="Total", data=df)
plt.title("Total Marks of Students")
plt.show()

# here we are finding subject-wise Average
avg.plot(kind="bar", color=["red","green","blue"])
plt.title("Average Marks per Subject")
plt.show()

# Pie Chart - Pass/Fail
df["Result"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()