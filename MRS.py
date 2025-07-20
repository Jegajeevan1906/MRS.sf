import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Read the CSV file
data = pd.read_csv("MRS.csv")

# 2️⃣ Sort by SalesAmount in descending order
sorted_data = data.sort_values(by="Amt", ascending=False)

# 3️⃣ Print the sorted table
print("📊 Sorted Sales Data (Descending):")
print(sorted_data)

# 4️⃣ Plot the bar chart
plt.figure(figsize=(8,6))
plt.bar(sorted_data["Emp Name"], sorted_data["Amt"], color="orange")
plt.title("Amt by Emp Name (Descending)", fontsize=14)
plt.xlabel("Emp Name", fontsize=12)
plt.ylabel("Amt", fontsize=12)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
