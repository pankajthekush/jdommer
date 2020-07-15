
try:
    from jdommer.jdommer import jsdom
except ModuleNotFoundError:
    from jdommer import jsdom

from flask import Flask
from flask import abort,request
from waitress import serve
import logging
import sys

app = Flask(__name__)



@app.route('/jsdom',methods=['get'])
def snoopthis():
    url = request.args['url']
    uniqueid = request.args.get('uid',1)
    user_agent = request.args.get('user_agent',None)
    hardata = jsdom(url=url,t_serail=int(uniqueid),user_agent=user_agent)
    return hardata


def runsnooper():
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.DEBUG)
    serve(app, host="0.0.0.0", port=5000,threads=8)


if __name__ == "__main__":
    
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.DEBUG)
    serve(app, host="0.0.0.0", port=5000,threads=8)