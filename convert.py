from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_string(file_path):
    """ Convert PDF file to string. """

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    
    with open(file_path, 'rb') as file:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()
        for page in PDFPage.get_pages(file, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            interpreter.process_page(page)
        file.close()
    
    device.close()
    str = retstr.getvalue()
    retstr.close()
    
    return str

def save_convert_pdf_to_txt(file_path):
    """ Save and convert PDF file to TXT file. """

    content = convert_pdf_to_string(file_path)
    with open(file_path[:-4]+".txt", 'wb') as f:
        f.write(content.encode('utf-8'))
        f.close()
    
    print("{file_path} has been successfully converted!".format(file_path=file_path))