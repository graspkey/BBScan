# Global Variables share among modules
from fake_useragent import UserAgent

stop_me = False

ua = UserAgent()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
#user_agent = ua.random

default_headers = {'User-Agent': user_agent, 'Connection': 'Keep-Alive', 'Range': 'bytes=0-102400'}

ports_saved_to_file = False