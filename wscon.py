#!/usr/bin/env python
import sys
import websocket
import thread
import time
import signal

def on_open(ws):
    print "\n>>>> OPENED <<<<\n"
    sys.stdout.flush()

def on_message(ws, message):
    print message
    ws.send("hoge hoge hoge hoge", opcode=websocket.ABNF.OPCODE_BINARY)
    sys.stdout.flush()

def on_error(ws, error):
    print ">>>> ERROR <<<< %s" % error
    sys.stdout.flush()

def on_close(ws):
    print ">>>> CLOSED <<<<"
    sys.stdout.flush()

def main():
    url = 'ws://localhost:5555'
    print('connect to %s' % url)
    ws = websocket.WebSocketApp(url,
        on_open=on_open,
        on_message=on_message,
        on_error = on_error)

    signal.signal(signal.SIGINT, lambda signum, frame: ws.close())
    ws.run_forever()
    print("END")

if __name__ == "__main__":
    import multiprocessing
    proc = multiprocessing.Process(target = main)
    signal.signal(signal.SIGINT, lambda signum, frame: proc.terminate())
    proc.start()

