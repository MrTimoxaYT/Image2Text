# Image2Text
Image2Text is a program for recognizing text from images, which has a CLI and a WebUI 

### WebUI preview
![image](webui_preview.png?raw=true)


## Update Image2Text to latest version

Install and pull any new requirements and changes by opening a command line window in the `Image2Text` directory and running the following commands.

```
pip install -r requirements.txt
git pull
```

## Setup

### Install Git and Python

Follow the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install Git on your computer. Also follow this [guide](https://realpython.com/installing-python/) to install Python if you haven't already. 


### Clone Image2Text repository

Open a command line window and run these commands to clone this entire repository and install the additional dependencies required.

```
git clone https://github.com/MrTimoxaYT/Image2Text
cd Image2Text
pip install -r requirements.txt
```



## Usage with WebUI

To run the Image2Text WebUI, run the following command.

```
python src/webui_app.py
```

| Flag                                       | Description |
|--------------------------------------------|-------------|
| `-h`, `--help`                             | Show this help message and exit. |
| `--share`                                  | Create a public URL. This is useful for running the web UI on Google Colab. |
| `--listen`                                 | Make the web UI reachable from your local network. |
| `--listen-host LISTEN_HOST`                | The hostname that the server will use. |
| `--listen-port LISTEN_PORT`                | The listening port that the server will use. |

Once the following output message `Running on local URL:  http://127.0.0.1:7860` appears, you can click on the link to open a tab with the WebUI.



## Disclaimer

I am not liable for any direct, indirect, consequential, incidental, or special damages arising out of or in any way connected with the use/misuse or inability to use this software.
