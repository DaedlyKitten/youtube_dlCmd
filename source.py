
import time
import win32clipboard
import youtube_dl


filepath='./'
# proxy1='http://127.0.0.1:'

ydl_opts = {
    'format': 'best',
    # 'proxy' : proxy1,
    'outtmpl' : filepath+'%(title)s.%(ext)s',  #  adding some random number to avoid overwrite
    'retries': 5,
    'no_warnings': False,   
    'noplaylist':True,
    # 'nooverwrites': True,
    # 'ignoreerrors': True,
}

# print('proxy:', proxy1)
# print('path: ',filepath)
print('youtube_dl wrapper, compiled with Pyinstaller.\n@konporer \n-------------\n\n')


def download(url):
    print('\n'+str(time.strftime("%c"))+'\n'+url,file=open(filepath+'record.txt','a'))

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e: print(e)



def checkit(x):
    if 'http' in x and input(f'From this url?\n\n{x}\n------------------\n"n" to input another.').lower()!='n': 
        download(x)
    else: 
        inputed=input('Input url:')
        if inputed!='': checkit(inputed)


    

win32clipboard.OpenClipboard()
clip = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

while True:
    try: checkit(clip)
    except Exception as e: print(e)


