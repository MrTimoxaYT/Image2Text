import easyocr
from os.path import basename
from datetime import datetime


# text transcribe
def text_transcribe(path, lang):
    reader = easyocr.Reader(lang_list=[lang])

    text = reader.readtext(path,detail=1)

    return text

# the accuracy of checking a word whether it is in the same line as the previous one
def in_range_checker(list_to_avg, next_height=0,paragrafs_accuracy=20):
    avg = 0
    for item in list_to_avg[0]:
        avg += item[1]  
    avg = avg / 4
    
    if next_height in range(int(avg-paragrafs_accuracy),int(avg+paragrafs_accuracy)):
        return True,avg
    else:
        return False,avg
    
    
# paragraph placement
def paragrafs_setter(text):
    final_text = ''

    avg_word = 0 
    for word in text:
        
        word_status,new_avg_word = in_range_checker(word,avg_word)
        
        if word_status:
            final_text+=f' {word[1]}'
            avg_word=new_avg_word
        else:
            final_text+=f'\n{word[1]}'
            avg_word=new_avg_word
    
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

if __name__ == '__main__':
    lang = input('Which text lang (example: en): ').lower()
    filepath = input('Image file path: ').strip('"')
    paragrafs_accuracy = input('Paragrafs accuracy (default 20): ') # in px 
    transcribed_text = main(lang, filepath,save_in_file=True)
    print(transcribed_text)