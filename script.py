import sys
import os
from pandas import read_csv
from download import download_file
from convert import save_convert_pdf_to_txt

DIRECTORY = 'downloads/'

if __name__ == "__main__":
    csv_df = read_csv(sys.argv[1])
    file_url_df = csv_df['file_url']
    file_size_df = csv_df['file_size']

    if not os.path.exists(DIRECTORY):
        os.mkdir(DIRECTORY)

    for index, (file_url, file_size) in enumerate(zip(file_url_df, file_size_df)):
        if index == 20: break
        if file_size == 0:
            continue
        file_location = download_file(DIRECTORY, file_url)
        save_convert_pdf_to_txt(file_location)