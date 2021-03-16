import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Cookie': 'htVD_2132_atarget=1; htVD_2132_saltkey=cyUOkKe6; htVD_2132_lastvisit=1597503606; htVD_2132_auth=b60fQ6mRpn62zCtiawsO%2FODtiJ5uG4wN%2FmKJNGzljvT3r7LlkRicZ7joDaPPQkEidt4l8THeEacaUxgjDJ7o7f4HuB8x; htVD_2132_connect_is_bind=1; htVD_2132_nofavfid=1; htVD_2132_smile=1D1; htVD_2132_lastviewtime=1275730%7C1599115803; htVD_2132_sid=0; htVD_2132_viewid=tid_1265704; htVD_2132_st_p=1275730%7C1599995807%7C15105a84da7b50ceeaec16ce44be2da3; htVD_2132_secqaaqS0=662862.13e5b9cad69a2e0abb; htVD_2132_ulastactivity=1600068491%7C0; htVD_2132_noticeTitle=1; htVD_2132_visitedfid=16D66D5D2D8; htVD_2132_checkpm=1; htVD_2132_st_t=1275730%7C1600068862%7C009ec2885e095f9f9e359cd9b1b08c18; htVD_2132_forum_lastvisit=D_66_1599995746D_16_1600068862; htVD_2132_lastcheckfeed=1275730%7C1600068863; htVD_2132_lastact=1600068894%09forum.php%09ajax'
}
r = requests.get('https://www.52pojie.cn/forum-16-1.html', headers=headers)
with open('qwq.html', 'w') as f:
    print(f.write(r.text))