import pypdf

reader = pypdf.PdfReader("paper_1.pdf")
page = reader.pages[0]
print(page.extract_text())