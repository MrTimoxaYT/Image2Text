import gradio as gr
from app import main
from argparse import ArgumentParser

langs = {
    'English':'en',
    'Russian':'ru',
    'German':'de',
    'French':'fr',
    'Japanese':'ja',
    'Korean': 'ko'
}


def transcribe_webui_func(lang='English',filepath='',save_in_file=False):
    extract_lang = langs[lang]
    extracted_text = main(lang=extract_lang,filepath=filepath,save_in_file=save_in_file)
    return gr.update(value=extracted_text.strip('\n'))
    

if __name__ == '__main__':
    parser = ArgumentParser(description='Image2Text.', add_help=True)
    parser.add_argument("--share", action="store_true", dest="share_enabled", default=False, help="Enable sharing")
    parser.add_argument("--listen", action="store_true", default=False, help="Make the WebUI reachable from your local network.")
    parser.add_argument('--listen-host', type=str, help='The hostname that the server will use.')
    parser.add_argument('--listen-port', type=int, help='The listening port that the server will use.')
    args = parser.parse_args()
    
    with gr.Blocks(title='Image2Text') as img2txt_app:

        with gr.Row():
            # image_input = gr.Text(label='Image input', info='Full path to a local file. For file upload, click the button below.')
            with gr.Column():
               
                
                img = gr.Image(label='Image input', info='Full path to a local file. For file upload, click the button below.', type='filepath',height=640)
                # img.upload(process_file_upload, inputs=img, outputs=img)
                
                with gr.Row():
                    accuracy = gr.Slider(minimum=5, maximum=50,value=20,step=5, label='Paragrafs accuracy (default 20)',interactive=True)            
                    lang_radio_btn = gr.Radio(choices=['English','Russian','German','French','Japanese','Korean'],value='English',label='What language of text in picture?')  
                
                save_in_file_status = gr.Checkbox(value=False, label='Save result?')                     
                transcribe_btn = gr.Button('Extract text from image', variant='primary')
                


            with gr.Column():
                text_output = gr.Text(label='Text from image',info='All extracted text of images in "output" folder when u save it in file')


        # button processing section
        transcribe_btn.click(transcribe_webui_func,inputs=[lang_radio_btn,img,save_in_file_status],outputs=text_output)
            
            

        img2txt_app.launch(
        share=args.share_enabled,
        enable_queue=True,
        server_name=None if not args.listen else (args.listen_host or '0.0.0.0'),
        server_port=args.listen_port,
    )