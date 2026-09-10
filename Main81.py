# E38.Merge the PDF.
from PyPDF2 import PdfMerger;
import os;
merger = PdfMerger()
files = [file for file in os.listdir() if file.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)
merger.write("Merged-PDF.pdf")
merger.close()