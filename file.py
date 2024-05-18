
import os
import time
import requests
import zipfile


def download_file(url, filename):
    content = requests.get(url=url).content
    if not os.path.exists("tmp"):
        os.mkdir("tmp")

    with open(os.path.join("./tmp", filename), 'wb') as file:
        file.write(content)


download_file("https://github.com/qa-guru/qa_guru_python_9_7_files/raw/master/tmp/file_example_XLSX_50.xlsx","xlsx.xlsx")
#time.sleep(4)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists("recources"):
    os.mkdir("recources")

RESOURCE_DIR = os.path.join(CURRENT_DIR, "recources")

with zipfile.ZipFile(os.path.join(RESOURCE_DIR, "zip.zip"), 'w') as zf:
    for file in ['xlsx.xlsx', 'pdf.pdf', 'csv.csv']:
        add_file = os.path.join("./tmp",file)
        zf.write(add_file, os.path.basename(add_file))


