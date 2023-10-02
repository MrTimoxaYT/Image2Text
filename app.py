import easyocr
from os.path import basename
from datetime import datetime


# text transcribe
def text_transcribe(path, lang):
    reader = easyocr.Reader(lang_list=[lang])

    text = reader.readtext(path,detail=1,paragraph=True)

    return text


    
# paragraph placement
def paragrafs_setter(text):
    final_text = ''
    for word in text:
        final_text+=f'{word[-1:][0]}\n'
    return final_text

# save in fale transcribed text
def write_in_file_transcribed_text(text, file_name):
    with open(f'output/{file_name}.txt', 'w', encoding='UTF-8') as file:
        file.write(text)
    print(f'[+] File {file_name}.txt saved!')
    

def main(lang='en',filepath='',save_in_file=False):
    if bool(len(filepath)):
        text = text_transcribe(filepath,lang)
        transcribed_text = paragrafs_setter(text)
        if save_in_file: # save in fale transcribed text
            write_in_file_transcribed_text(transcribed_text,f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}_"+basename(filepath).split('.')[0]+'_transcribed')
        return transcribed_text
    else:
        print("[!] File doen't exists or filepath is incorrect")
        return "[!] File doen't exists or filepath is incorrect"
if __name__ == '__main__':
    lang = input('Which text lang (example: en): ').lower()
    filepath = input('Image file path: ').strip('"')
    paragrafs_accuracy = input('Paragrafs accuracy (default 20): ') # in px 
    transcribed_text = main(lang, filepath,save_in_file=True)
    print(transcribed_text)