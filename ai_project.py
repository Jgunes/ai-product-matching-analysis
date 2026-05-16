import pandas as pd
import matplotlib.pyplot as plt


dFA = pd.read_excel(
"supplier_products.xlsx",
sheet_name="Supplier A"
)

dFB = pd.read_excel(
"supplier_products.xlsx",
sheet_name="Supplier B"
)

dFA.columns = dFA.columns.str.strip()
dFB.columns = dFB.columns.str.strip()


print("=== SUPPLIER A ===")
print(dFA.head())

print("\n=== SUPPLIER B ===")
print(dFB.head())



priceA = pd.to_numeric(dFA.iloc[:, 3], errors="coerce")
priceB = pd.to_numeric(dFB.iloc[:, 3], errors="coerce")


avgA = priceA.mean()
maxA = priceA.max()
minA = priceA.min()

avgB = priceB.mean()
maxB = priceB.max()
minB = priceB.min()

print("\n=== AI INSIGHTS ===")

print(f"Supplier A Average Price: {avgA:.2f}")
print(f"Supplier B Average Price: {avgB:.2f}")

print(f"Supplier A Highest Price: {maxA}")
print(f"Supplier B Highest Price: {maxB}")

print(f"Supplier A Lowest Price: {minA}")
print(f"Supplier B Lowest Price: {minB}")

if avgA < avgB:
    print("\nSupplier A is cheaper on average.")
else:
    print("\nSupplier B is cheaper on average.")



plt.figure(figsize=(10, 5))

plt.plot(priceA, marker="o", label="Supplier A")
plt.plot(priceB, marker="o", label="Supplier B")

plt.title("Supplier Price Comparison")
plt.xlabel("Products")
plt.ylabel("Price")

plt.legend()

chart_path = "comparison_chart.png"

plt.savefig(chart_path)

print(f"\nChart saved as {chart_path}")


with open("report.txt", "w") as report:

    report.write("AI PRODUCT MATCHING REPORT\n")
    report.write("============================\n\n")

    report.write("SUPPLIER A STATISTICS\n")
    report.write("----------------------\n")
    report.write(f"Average Price: {avgA:.2f}\n")
    report.write(f"Highest Price: {maxA}\n")
    report.write(f"Lowest Price: {minA}\n\n")

    report.write("SUPPLIER B STATISTICS\n")
    report.write("----------------------\n")
    report.write(f"Average Price: {avgB:.2f}\n")
    report.write(f"Highest Price: {maxB}\n")
    report.write(f"Lowest Price: {minB}\n\n")

    if avgA < avgB:
        report.write("Supplier A is cheaper on average.\n")
    else:
        report.write("Supplier B is cheaper on average.\n")

print("\nReport generated successfully")