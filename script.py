import sys
import os
from pandas import read_csv
from download import download_file
from convert import save_convert_pdf_to_txt

DIRECTORY = 'downloads/'

if __name__ == "__main__":
    file_csv = read_csv(sys.argv[1])
    url_df = file_csv['url']

    if not os.path.exists(DIRECTORY) and url_df.count+1 > 0:
        os.mkdir(DIRECTORY)

    for url in url_df:
        file_location = download_file(DIRECTORY, url)
        save_convert_pdf_to_txt(file_location)