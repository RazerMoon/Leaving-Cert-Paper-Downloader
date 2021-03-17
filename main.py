# DO NOT USE THIS TO SPAM EXAMINATIONS.IE WITH REQUESTS; USE RESPONSIBLY.

from PyPDF2 import PdfFileMerger, PdfFileReader
from pathlib import Path
import requests

lang = "EV"
subjects = {"Physics": 21, "Chemistry": 22}
max_year = 2010
min_year = 2007 # 2007 is lowest

def createDirectories():
  for subject in subjects.keys():
    Path(f"./Papers/{subject}").mkdir(parents=True, exist_ok=True)

def downloadPapers():
  for subject, ident in subjects.items():
    for year in range(min_year, max_year+1):
      file = Path(f"./Papers/{subject}/{year}.pdf")

      # Don't redownload files
      if not file.exists():
        print(f"Downloading {year} {subject} Paper")
        response = requests.get(f"https://www.examinations.ie/archive/exampapers/{year}/LC0{ident}ALP000{lang}.pdf")

        print(f"Writing to ./Papers/{subject}/{year}.pdf")
        file.write_bytes(response.content)
      else:
        print(f"./Papers/{subject}/{year}.pdf already exists!")

def mergePapers(): # Assumes papers were downloaded successfully
  for subject in subjects.keys():
    merger = PdfFileMerger()

    for year in range(min_year, max_year+1):
      merger.append(PdfFileReader(f"./Papers/{subject}/{year}.pdf"))

    merger.write(f"./Papers/{subject}/collection.pdf")

if __name__ == '__main__':
    createDirectories()
    downloadPapers()
    mergePapers()