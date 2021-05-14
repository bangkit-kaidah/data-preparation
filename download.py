import os
import requests

def download_file(directory, file_url):
    """ Download file from URL and return downloaded file location. """

    file_binary = requests.get(file_url)
    file_name = file_url.split('/')[-1]
    file_location = os.path.join(directory, file_name)
    
    with open(file_location, 'wb') as f:
        f.write(file_binary.content)
        f.close()
    
    print("{file_name} has been successfully downloaded!".format(file_name=file_name))
    return file_location