# Data Preparation


## Description
This repository is to get training data for Machine Learning model and prepare data* for database and prediction. Written using Python.

*Python code for crawling database and prediction data is in [jdihn-crawl](https://github.com/bangkit-kaidah/jdihn-crawl) repository.


## Requirements
- Python 3.8


## Data Sources
- Training data from [JDIH Kemenkeu](https://jdih.kemenkeu.go.id/in/home)
- Database and prediction data from [JDIHN](https://jdihn.go.id/)


## Usage
```
python crawl.py <start_page> <end_page>
python combine_jdihn.py
python clean_jdihn.py
```