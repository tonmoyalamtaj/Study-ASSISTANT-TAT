from project import *
from pyfiglet import Figlet
import os
import json
import pytest


ttf = 'templorary_testing_file.json'


def test_vidio_link_cheker():

    
    r1 = Figlet(font='standard')
    is_ok_is_valid = r1.renderText('Ok')
    r2 = Figlet(font='standard')
    is_No_is_valid = r2.renderText('No')

    valid_link_1 = 'https://www.youtube.com/watch?v=JP7ITIXGpHk'
    valid_link_2 = 'https://youtu.be/JP7ITIXGpHk?si=yc1-cjIpZp3U5D2D'
    invalid_link_1='https://youtu.b/JP7ITIXGpHk?si=yc1-cjIpZp3U5D2D'
    invalid_link_2='https://www.yutube.com/watch?v=JP7ITIXGpHk'
    
    assert vidio_link_cheker(valid_link_1) ==(is_ok_is_valid,' :) Your Program is running. :) ',True)
    assert vidio_link_cheker(valid_link_2) == (is_ok_is_valid,' :) Your Program is running. :) ',True)
    assert vidio_link_cheker(invalid_link_1) == (is_No_is_valid,' :( The link is invalid :( ',False)
    assert vidio_link_cheker(invalid_link_2) == (is_No_is_valid,' :( The link is invalid :( ',False)


def test_file_handiling():
    if os.path.exists(ttf):
        os.remove(ttf)
    file_handiling(ttf)
    assert os.path.exists(ttf) == True
    os.remove(ttf)
    assert os.path.exists(ttf) == False


def test_link_injecter():
    if os.path.exists(ttf):
        os.remove(ttf)
    file_handiling(ttf)
    link_injecter(title= 'Et Cetera',link='https://www.youtube.com/watch?v=6pgodt1mezg',file=ttf)
    link_injecter(title= 'CS50P - Introduction',link='https://www.youtube.com/watch?v=OvKCESUCWII&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=1',file=ttf)
    with open(ttf,'r') as x:
        c = json.load(x)["youtube_links"]
        first_block = c[0]
        last_block =  c[-1]

    assert first_block == {'Index': 1, 'title': 'Et Cetera', 'link': 'https://www.youtube.com/watch?v=6pgodt1mezg'}
    assert last_block == {'Index': 2, 'title': 'CS50P - Introduction', 'link': 'https://www.youtube.com/watch?v=OvKCESUCWII&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=1'}

    os.remove(ttf)


def test_checking_is_user_gave_input_properly():
    assert checking_is_user_gave_input_properly('Taj') == None
    assert checking_is_user_gave_input_properly('r') == 'You should write more.'
    with pytest.raises(TypeError):
        checking_is_user_gave_input_properly(23)
    test_list=['fdsajj@','hjfhd#','^jdj','hjdfjd&','hf:fd','jjhfd>fd',
               'kjfdh<kd','jfjhf{','jefif()','khjf}e','kjfe|','jkjfej!j',
               'jkfe.j','jhjeff;f','kfee?f','jijf,f']
    for i in test_list:
        with pytest.raises(SystemExit):
            checking_is_user_gave_input_properly(i)


def test_desplaying_save_title(capsys):
    if os.path.exists(ttf):
        os.remove(ttf)
    file_handiling(ttf)
    link_injecter(title= 'Et Cetera',link='https://www.youtube.com/watch?v=6pgodt1mezg',file=ttf)
    link_injecter(title= 'CS50P - Introduction',link='https://www.youtube.com/watch?v=OvKCESUCWII&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=1',file=ttf)

    displaying_save_title(fileName=ttf)

    captured = capsys.readouterr()

    expected = 'OK\nOK\n1.Et Cetera\n2.CS50P - Introduction\n'

    assert captured.out == expected
    os.remove(ttf)


def test_giving_save_link():
    if os.path.exists(ttf):
        os.remove(ttf)
    file_handiling(ttf)
    link_injecter(title= 'Et Cetera',link='https://www.youtube.com/watch?v=6pgodt1mezg',file=ttf)
    link_injecter(title= 'CS50P - Introduction',link='https://www.youtube.com/watch?v=OvKCESUCWII&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=1',file=ttf)

    assert giving_save_link(user_inputed_index=1,fileName=ttf) == 'https://www.youtube.com/watch?v=6pgodt1mezg'
    assert giving_save_link(user_inputed_index=2,fileName=ttf) == 'https://www.youtube.com/watch?v=OvKCESUCWII&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=1'    
    os.remove(ttf)

    