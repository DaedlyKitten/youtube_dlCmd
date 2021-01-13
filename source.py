import time
import win32clipboard
from youtube_dl import YoutubeDL

filepath='./'
format1='best' #'bestaudio'
recordfilepath='./videoDLrecord.txt'

ydl_opts = {
    'format': format1,
    #'proxy' : proxy1,
    'outtmpl' : filepath+'%(title)s.%(ext)s', 
    'retries': 5,
    'no_warnings': False,   
    'noplaylist':True,
    # 'nooverwrites': True,
    # 'ignoreerrors': True,
}


[print(x,': ',y) for x,y in ydl_opts.items()]
print(recordfilepath)

def download(url):
    print('\n'+str(time.strftime("%y%m.%d%H%M"))+'\n'+url,file=open(recordfilepath,'a'))

    try:
        YoutubeDL(ydl_opts).download([url])
    except Exception as e: print(e)

    print('\n------Done!-------\n')
    checkit(input('\nAnother ?'))


def checkit(x):
    if 'http' in x:
        a=input(f'\n------------------\nFrom this url?\n\n{x}\n-------------------\nOr input another:')    
        if a.lower()=='': 
            download(x)
        else: checkit(a)
    else: 
        print('Invalid url!')
        checkit(input(f'\nInput another url:'))
# def inputUrl():
#     inputed=input('Input url:')
#     if inputed!='': checkit(inputed)
    


clip=''
try: 
    win32clipboard.OpenClipboard()
    clip = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()      
except Exception as e: print('Failed to read clipboard: ', e)
checkit(clip)

