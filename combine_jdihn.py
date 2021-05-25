import os
import re
import pandas as pd

def combine_jdihn_csv_files(files):
    """ Combine JDIHN pages CSV file into one CSV file. """

    pattern = 'jdihn_page_'
    df_list = []
    for file_name in files:
        if re.search(pattern, file_name):
            csv_df = pd.read_csv(os.path.join(directory, file_name))
            df_list.append(csv_df)
    
    return pd.concat(df_list)

if __name__ == '__main__':
    directory = 'data/'
    try:
        files = os.listdir(directory)
        combined_df = combine_jdihn_csv_files(files)    
    except FileNotFoundError:
        print("Directory doesn't exist.")
    except ValueError:
        print("JDIHN CSV file doesn't exist.")
    else:
        saved_name = 'jdihn_regulations.csv'
        combined_df.to_csv(os.path.join(directory, saved_name), index=False)
        print("{} has been successfully saved!".format(saved_name))