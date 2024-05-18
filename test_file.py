from zipfile import ZipFile
from pypdf import PdfReader
from openpyxl import load_workbook
import csv


def test_pdf_file():
    with ZipFile("resources/zip.zip", "r") as zip_file:
        page = PdfReader(zip_file.open('pdf.pdf'))
        assert 'Python Testing with pytest' in page.pages[1].extract_text()

def test_xlsx_file():
    with ZipFile("resources/zip.zip", "r") as zip_file:
        page = load_workbook(zip_file.open('xlsx.xlsx')).active
        assert 'Mara' in page.cell(row=3, column=2).value

def test_csv_file():
    with ZipFile("resources/zip.zip", "r") as zip_file:
        page = zip_file.open('csv.csv').read().decode('cp1251')
        csvreader = list(csv.reader(page.splitlines()))
        second_row = csvreader[1]
        assert 'дисплей' in second_row[0]