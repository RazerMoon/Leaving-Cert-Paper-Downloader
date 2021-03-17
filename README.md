# Leaving Cert Paper Downloader

Python script that downloads all the papers for a subject (or subjects) from [Examinations.ie](https://www.examinations.ie/) and merges them into one large PDF.

## Why

Sometimes you might get be given an exam question to do, but you won't be given the year.

By creating one PDF with the papers from each year, it is much easier to find a question.

You can just Ctrl+F in one PDF rather than repeating that for each paper until you find the question you were looking for. This is especially tedious if you have to download each of the papers yourself.

## How to use

Install dependencies

```bash
pip install -r requirements.txt
```

Go into main.py and adjust values to your liking

Run

```bash
py main.py
```

Go to `./Papers/{subject}/collection.pdf` and Ctrl+F

## Why can't you just give me the collections?

It is against the [Terms and Conditions](https://www.examinations.ie/TermsConditions.html) of the SEC.

> "They may not otherwise copy, modify, or distribute the examination material, or publish, broadcast, transmit, or otherwise distribute any portion of this material without the express written authorisation of the State Examinations Commission."

## Notice

Do not use this script to spam the website with requests. Please be aware of the fact that deciding to download all of the papers on the website is bad. At maximum, download all the papers from a subject.
