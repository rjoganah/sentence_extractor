import sys
from os import listdir
from os.path import join
from unidecode import unidecode
from tika import parser
import nltk

 
def parse_line_space(item, path_output, i):
    """
    Parse the file from item path with Tika
    For each file, write sentences in a file
    """
    file = parser.from_file(item)
    f = open(path_output + '/case_' + str(i) +'.txt','w')
    if file['content']:
        corpus = unidecode(file['content']).split('\n')
    else:
        f.close()
        return False
    paragraphs = []
    new_paragraph = ''
   
    for line in corpus:
        if line == '':
            if len(new_paragraph) > 15:
                paragraphs.append(new_paragraph)
            new_paragraph = ''
        else:
            new_paragraph += line
    for paragraph in paragraphs:
        sents = nltk.sent_tokenize(paragraph)
        for sent in sents:
            f.write(sent + '\n')
    f.close()
    return True
   
if __name__ == '__main__':
    path_to_pdfs = sys.argv[1]
    path_to_write = sys.argv[2]
    print(path_to_pdfs)
    ocr_files = []
    for i,f in enumerate(listdir(path_to_pdfs)):
        if f.endswith('.pdf'):
            if(not parse_line_space(join(path_to_pdfs,f),path_to_write,i)):
                ocr_files.append((i,f))
    #print(str(ocr_files))

