# Notebank Scraper

This scraper is being used to populate the schools/courses database for: https://github.com/talham7391/notebank-service

**Last confirmed working:** Saturday, November 30, 2019

# What it does

It scrapes all the courses the University of Waterloo offers and displays them in a list with each course formatted as: 

`COURSE_CODE_SUBJECT COURSE_CODE_NUMBER - COURSE TITLE`

### Random samples from a run

```
MATH 217 - Calculus 3 for Chemical Engineering
HRM 307 - Labour Relations
PHARM 155 - Introduction to Drug Information Fundamentals
GBDA 204 - Working in Teams and Project Management
```

*Note: actual output will be in alphabetical order.*

# Usage

1. `git clone git@github.com:talham7391/notebank-scraper.git`
2. `cd notebank-scraper`
3. `pipenv install`
4. `pipenv shell`
5. `python src/courses.py > courses.txt`

You will see a progress bar letting you how many pages still need to be scraped.