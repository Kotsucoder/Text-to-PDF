import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("text/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem.capitalize()
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename}")

pdf.output("output.pdf")