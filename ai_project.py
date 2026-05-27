import pandas as pd
import matplotlib.pyplot as plt

from reportlab.platypus import (
SimpleDocTemplate,
Paragraph,
Spacer,
Image,
Table,
TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter


dfA = pd.read_excel(
"supplier_products.xlsx",
sheet_name="Supplier A"
)

dfB = pd.read_excel(
"supplier_products.xlsx",
sheet_name="Supplier B"
)

dfA.columns = dfA.columns.str.strip()
dfB.columns = dfB.columns.str.strip()


priceA = pd.to_numeric(
dfA.iloc[:, 3],
errors="coerce"
)

priceB = pd.to_numeric(
dfB.iloc[:, 3],
errors="coerce"
)

avgA = priceA.mean()
maxA = priceA.max()
minA = priceA.min()

avgB = priceB.mean()
maxB = priceB.max()
minB = priceB.min()


print("\n=== SUPPLIER A ===")
print(f"Average Price: {avgA:.2f}")
print(f"Highest Price: {maxA}")
print(f"Lowest Price: {minA}")

print("\n=== SUPPLIER B ===")
print(f"Average Price: {avgB:.2f}")
print(f"Highest Price: {maxB}")
print(f"Lowest Price: {minB}")

if avgA < avgB:
    print("\nSupplier A is cheaper on average.")
else:
    print("\nSupplier B is cheaper on average.")



productsA = range(len(priceA))
productsB = range(len(priceB))

fig, ax = plt.subplots(figsize=(10, 6))


fig.patch.set_facecolor("#050816")
ax.set_facecolor("#0b1020")


ax.plot(
productsA,
priceA,
color="#00d9ff",
linewidth=3,
marker="o",
markersize=8,
label="Supplier A"
)

ax.plot(
productsB,
priceB,
color="#ffae00",
linewidth=3,
marker="o",
markersize=8,
label="Supplier B"
)


ax.set_title(
"SUPPLIER PRICE COMPARISON",
fontsize=22,
color="white",
weight="bold"
)


ax.set_xlabel(
"Products",
fontsize=14,
color="white"
)

ax.set_ylabel(
"Price (USD)",
fontsize=14,
color="white"
)


ax.grid(
color="white",
alpha=0.08,
linestyle="--"
)


ax.tick_params(colors="white")

legend = ax.legend()

for t in legend.get_texts():
    t.set_color("white")

chart_path = "comparison_chart.png"

plt.tight_layout()

plt.savefig(
chart_path,
dpi=300,
facecolor=fig.get_facecolor()
)

plt.close()


doc = SimpleDocTemplate(
"AI_Product_Matching_Report.pdf",
pagesize=letter,
rightMargin=30,
leftMargin=30,
topMargin=30,
bottomMargin=30
)

styles = getSampleStyleSheet()

elements = []


def dark_background(canvas, doc):

    canvas.setFillColor(
colors.HexColor("#050816")
)

    canvas.rect(
0,
0,
1000,
1000,
fill=1
)


title_style = styles["Heading1"]

title_style.textColor = colors.HexColor("#00ffcc")
title_style.fontSize = 28

title = Paragraph(
"AI PRODUCT MATCHING REPORT",
title_style
)

elements.append(title)

elements.append(
Spacer(1, 25)
)



data = [
["Metric", "Supplier A", "Supplier B"],

[
"Average Price",
f"{avgA:.2f}",
f"{avgB:.2f}"
],

[
"Highest Price",
f"{maxA}",
f"{maxB}"
],

[
"Lowest Price",
f"{minA}",
f"{minB}"
]
]

table = Table(
data,
colWidths=[180, 120, 120]
)

table.setStyle(TableStyle([

(
"BACKGROUND",
(0, 0),
(-1, 0),
colors.HexColor("#111827")
),

(
"TEXTCOLOR",
(0, 0),
(-1, 0),
colors.white
),

(
"BACKGROUND",
(0, 1),
(-1, -1),
colors.HexColor("#0b1020")
),

(
"TEXTCOLOR",
(0, 1),
(-1, -1),
colors.HexColor("#00ffcc")
),

(
"GRID",
(0, 0),
(-1, -1),
1,
colors.HexColor("#00ffff")
),

(
"FONTNAME",
(0, 0),
(-1, 0),
"Helvetica-Bold"
),

(
"FONTNAME",
(0, 1),
(-1, -1),
"Helvetica"
),

(
"FONTSIZE",
(0, 0),
(-1, -1),
14
),

(
"BOTTOMPADDING",
(0, 0),
(-1, 0),
12
)
]))

elements.append(table)

elements.append(
Spacer(1, 30)
)


img = Image(chart_path)

img.drawHeight = 320
img.drawWidth = 500

elements.append(img)

elements.append(
Spacer(1, 20)
)



message_style = styles["BodyText"]

message_style.textColor = colors.white
message_style.fontSize = 14

if avgA < avgB:

    message = Paragraph(
"Supplier A is cheaper on average.",
message_style
)

else:

    message = Paragraph(
"Supplier B is cheaper on average.",
message_style
)

elements.append(message)


doc.build(
elements,
onFirstPage=dark_background,
onLaterPages=dark_background
)

print("\nProfessional PDF generated successfully!")
