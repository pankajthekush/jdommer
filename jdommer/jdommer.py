from subprocess import Popen,PIPE,check_output,STDOUT
import subprocess
import sys
import os
from time import sleep
import threading
from pathlib import Path
from itertools import cycle
import signal


latest_ua_list =  ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (X11; Linux i686; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/27.0 Mobile/15E148 Safari/605.1.15',
        'Mozilla/5.0 (iPad; CPU OS 10_15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/27.0 Mobile/15E148 Safari/605.1.15',
        'Mozilla/5.0 (iPod touch; CPU iPhone OS 10_15_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/27.0 Mobile/15E148 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Mozilla/5.0 (Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36']



all_ua = cycle(latest_ua_list)



def html_exists(filename):
    sleep(5)    
    if os.path.exists(filename):
        pg_status =  True
    else:
        pg_status = False
 
    return pg_status
 
def jsdom(url,t_serail,user_agent = None):
    

    if user_agent is None:
        user_agent = next(all_ua)

    status = None
    file_name = f'{t_serail}.html'
    if os.path.exists(file_name):
        os.remove(file_name)

    s_command = f'single-file "{url}" {file_name}  --back-end=jsdom --save-raw-html --user-agent="{user_agent}"'

    res = Popen(s_command, shell=True,preexec_fn=os.setsid,stdin=PIPE, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

    try:
        res.wait(timeout=600)
    except subprocess.TimeoutExpired:
        print(f'{url} returned timeout error ,exiting')
        os.killpg(os.getpgid(res.pid), signal.SIGTERM)  
        status = False
    
    is_success = html_exists(file_name)
    status = is_success

    return_text = None
    if status:
        with open(file_name,'r',encoding='utf-8') as f:
            return_text = f.read()
    else:
        return_text =  'error while getting url'

    if os.path.exists(file_name):
        os.remove(file_name)


    dict_data = dict()
    dict_data['status'] = status
    dict_data['page_source'] = return_text
    return dict_data
 
        

if __name__ == "__main__":
    # run_threaded_jsdom()
    # run_single_file_prcess()
    # p_killer()
    # run_threaded_chdriver()
    # process_single_file(engine='chdriver')
    # p_killer()
    # threaded_sngle_file()
    # run_threaded_jsdom()

    print(jsdom(url='https://www.google.com',user_agent='python',t_serail=1))




