import os
import csv
import sys
import requests


def write_csv_header(file_path, header):
    """ Create a CSV file and write a header. """

    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
    
    head_tail = os.path.split(file_path)
    print("CSV file {} has been created in {}!".format(head_tail[1], head_tail[0]))


def write_csv_rows(file_path, data):
    """ Write several rows in CSV file from a list. """

    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def jdih_kemenkeu_crawl(regulation_start, regulation_end, file_path):
    """ Get title and subjects of regulations from JDIH Kemenkeu. """

    if regulation_start > regulation_end:
        print("Error: Starting regulation number can't be larger than ending regulation number!")
        return
    print("Starting JDIH Kemenkeu crawling!")

    total_new_rows = 0
    for page in range(regulation_start-1, regulation_end, 10):
        page_url = 'https://jdih.kemenkeu.go.id/api/AppPeraturans?offset={}'.format(page)
        page_res = requests.get(page_url)

        page_dict = page_res.json()
        regulations = page_dict['Data']

        regulations_list = []
        for regulation in regulations:
            regulation_id = regulation['PeraturanId']

            regulation_url = 'https://jdih.kemenkeu.go.id/api/AppPeraturans/ByUrl/{}'.format(regulation_id)
            regulation_res = requests.get(regulation_url)

            try:
                regulation_dict = regulation_res.json()
                subjects = regulation_dict['Subyek']
            except:
                print("Warning: Found an empty regulation!")
                continue

            if len(subjects) > 0:
                subject_list = [subject['RefSubjectNames'].strip().title() for subject in subjects]
                subject_str = ', '.join(subject_list)

                regulation_title = regulation['Judul'].strip()
                regulations_list.append([regulation_title, subject_str])
        
        write_csv_rows(file_path, regulations_list)
        total_new_rows += len(regulations_list)
        print("Crawled page: {} | New rows: {} | Total new rows: {}".format(1+page//10, len(regulations_list), total_new_rows))
    
    print("JDIH Kemenkeu crawling has been completed!")


if __name__ == '__main__':
    directory = 'data/'
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Folder {} has been created!".format(directory))
    
    file_name = 'jdih_kemenkeu_regulations.csv'
    file_path = os.path.join(directory, file_name)
    header = ['title', 'label']
    write_csv_header(file_path, header)

    try:
        regulation_start = int(sys.argv[1])
        regulation_end = int(sys.argv[2])
    except:
        print("Error: Please input starting regulation number and ending regulation number!")
    else:
        jdih_kemenkeu_crawl(regulation_start, regulation_end, file_path)