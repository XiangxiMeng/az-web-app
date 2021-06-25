import time
# import gevent

from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return "Hello world"


@app.route('/sleep/<t>')
def sleep(t):
    time.sleep(int(t))
    return f"sleep {t} seconds!"


@app.route('/sleep1/<t>')
def sleep1(t):
    time.sleep(int(t))
    return f"sleep1 {t} seconds!"


@app.route('/sleep2/<t>')
def sleep2(t):
    time.sleep(int(t))
    return f"sleep2 {t} seconds!"


@app.route('/sleep3/<t>')
def sleep3(t):
    time.sleep(int(t))
    return f"sleep3 {t} seconds!"


@app.route('/sleep4/<t>')
def sleep4(t):
    time.sleep(int(t))
    return f"sleep5 {t} seconds!"


@app.route('/asleep/<t>')
def asleep(t):
    gevent.sleep(int(t))
    return f"sleep {t} seconds!"


@app.route('/asleep1/<t>')
def asleep1(t):
    gevent.sleep(int(t))
    return f"sleep1 {t} seconds!"


@app.route('/asleep2/<t>')
def asleep2(t):
    gevent.sleep(int(t))
    return f"sleep2 {t} seconds!"


@app.route('/asleep3/<t>')
def asleep3(t):
    gevent.sleep(int(t))
    return f"sleep3 {t} seconds!"


@app.route('/asleep4/<t>')
def asleep4(t):
    gevent.sleep(int(t))
    return f"sleep4 {t} seconds!"
