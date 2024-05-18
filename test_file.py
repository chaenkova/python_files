from pypdf import PdfReader
from openpyxl import load_workbook
import csv
import zipfile


def test_pdf_file():
    with zipfile.ZipFile("resources/zip.zip", "r") as zip_file:
        page = PdfReader(zip_file.open('pdf.pdf'))
        assert 'Python Testing with pytest' in page.pages[1].extract_text()
        zip_file.close()


def test_xlsx_file():
    with zipfile.ZipFile("resources/zip.zip", "r") as zip_file:
        page = load_workbook(zip_file.open('xlsx.xlsx')).active
        assert 'Mara' in page.cell(row=3, column=2).value
        zip_file.close()


def test_csv_file():
    with zipfile.ZipFile("resources/zip.zip", "r") as zip_file:
        page = zip_file.open('csv.csv').read().decode('cp1251')
        csvreader = list(csv.reader(page.splitlines()))
        second_row = csvreader[1]
        assert 'дисплей' in second_row[0]
        zip_file.close()