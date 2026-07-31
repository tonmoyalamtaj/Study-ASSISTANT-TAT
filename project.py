import re
from pyfiglet import Figlet
import sys
import json
import os
import yt_dlp
import ffmpeg
import webbrowser


file_name = "link_data_base.json"
puntuation_list = [',', '.', '/', '?', '!', '#',
                   '(', ')', '{', '}', ':', ";", '"', "'", '-', '<', ">",
                   '@', "/", '$', "%", '^', '&', '*', ']', '[', '|']


def main():
    user_choice = input('''    1.Inject any link
    2.open any link
    Please Enter your choice: ''')

    if user_choice == '1':
        Inject_any_link()

    elif user_choice == '2':
        try:
            Open_any_link()
        except FileNotFoundError:
            f = Figlet(font='standard')
            print(f"{f.renderText('Sorry')}\n :( this file is empty at first inject some link :(")
    else:
        f = Figlet(font='standard')
        print(f"{f.renderText('Sorry')}\n :( Your Input should be 1 or 2. :(")


def Open_any_link():
    displaying_save_title(fileName=file_name)
    try:
        user_choice = int(input('Please Enter Your choice: '))
        link = giving_save_link(fileName=file_name, user_inputed_index=user_choice)
        webbrowser.open_new_tab(link)
    except ValueError:
        font = Figlet(font='standard')
        print(font.renderText('sorry'), ':( you should you the index number of the title :(')
    except IndexError:
        font = Figlet(font='standard')
        print(font.renderText(
            'sorry'), ':( Your Index is Not found\n Please Insert that Index in fron of the title. :(')


def Inject_any_link():
    user_link = input('Enter your youtube vidio link: ')
    if vidio_link_cheker(user_link)[2]:
        print(f"{vidio_link_cheker(user_link)[0]}\n{vidio_link_cheker(user_link)[1]}")
    else:
        sys.exit(f"{vidio_link_cheker(user_link)[0]}\n{vidio_link_cheker(user_link)[1]}")

    user_title = input('Enter your youtube vidio title: ')
    checking_is_user_gave_input_properly(user_title)

    file_handiling(file=file_name)

    link_injecter(title=user_title, link=user_link, file=file_name)
    # want to download

    want_to_download(title=user_title, link=user_link)


def vidio_link_cheker(link):
    pattern_checker = re.search(
        pattern=r"^https?://(www\.)?(youtube\.com|youtu\.be)/.+$", string=link)
    if pattern_checker:
        runining = Figlet(font='standard')
        return (runining.renderText('Ok'), " :) Your Program is running. :) ", True)

    else:
        runining = Figlet(font='standard')
        return (runining.renderText('No'), " :( The link is invalid :( ", False)


def want_to_download(title, link):
    user_is_download_wanted = input('Are you want to download this link[y/n|'']: ')
    if user_is_download_wanted.lower() == 'y':
        file_downloader(fileName=title, link=link)
    else:
        font = Figlet(font='standard')
        print(f"{font.renderText('Ok')}\n :) Your yt vidio link is saved :)")


def file_handiling(file):
    if os.path.exists(file):
        print("OK")
    else:
        with open(file, 'w') as file:
            must_be_code = {
                "youtube_links": [
                ]}
            json.dump(must_be_code, file, indent=2)


def link_injecter(link, title, file):
    with open(file, 'r') as files:
        info = json.load(files)
        # for indexing
        lenth = len(info["youtube_links"]) + 1

    inputting_info = {
        "Index": lenth,
        "title": title,
        "link": link
    }

    info["youtube_links"].append(inputting_info)

    with open(file, 'w') as files:
        json.dump(info, files, indent=2)

    print('OK')


def checking_is_user_gave_input_properly(x):
    for i in puntuation_list:
        if i in list(x):
            runining = Figlet(font='standard')
            sys.exit(f"{runining.renderText('Sorry')}\n :( There have a special charecter :( ")
        else:
            pass

    if isinstance(x, str):
        if len(x) > 1:
            pass
        else:
            return 'You should write more.'
    else:
        runining = Figlet(font='standard')
        sys.exit(f'{runining.renderText('Sorry')}\n :( Please Give the Title in string :( ')


def displaying_save_title(fileName):
    with open(fileName, 'r') as x:
        y = json.load(x)['youtube_links']
        for i in range(len(y)):
            indexs = y[i]['Index']
            title = y[i]['title']
            print(f'{indexs}.{title}')


def file_downloader(link, fileName):
    templorary_vidio = 't.mp4'
    templorary_audio = 't.m4a'

    fileName = fileName.replace(' ', '_')
    for i in puntuation_list:
        fileName = fileName.replace(i, '')
    fileName = f"{fileName}.mp4"

    # main command

    for_vidio_command = {
        'format': 'bestvideo',
        'outtmpl':  templorary_vidio
    }

    for_audio_command = {
        'format': 'bestaudio',
        'outtmpl': templorary_audio
    }

    try:
        with yt_dlp.YoutubeDL(for_vidio_command) as vidio:
            vidio.download([link])
        with yt_dlp.YoutubeDL(for_audio_command) as Audio:
            Audio.download([link])

        vd = ffmpeg.input(templorary_vidio)
        ao = ffmpeg.input(templorary_audio)
        ffmpeg.output(
            vd,
            ao,
            fileName,
            vcodec='copy',
            acodec='aac'
        ).run(overwrite_output=True)

    except Exception as Error:
        run = Figlet(font='standard')
        print(run.renderText('Sorry'), f" :( {Error} :( ")

    finally:
        if os.path.exists(templorary_audio):
            os.remove(templorary_audio)

        if os.path.exists(templorary_vidio):
            os.remove(templorary_vidio)


def giving_save_link(user_inputed_index, fileName):
    with open(fileName, 'r') as x:
        y = json.load(x)['youtube_links'][user_inputed_index-1]
        return y['link']


if __name__ == "__main__":
    main()
