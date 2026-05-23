import hashlib 
import time 
import os 
import requests

files_to_monitor = ["/etc/passwd", "/etc/shadow"] # Input the path
hash_dict = {} 

WEBHOOK_URL = "" # Input your Webhook URL

def get_file_hash(file_path): 
    with open(file_path, 'rb') as f: 
        return hashlib.sha256(f.read()).hexdigest() 

def initialize_hashes(): 
    for file in files_to_monitor: 
        hash_dict[file] = get_file_hash(file) 

def check_integrity(): 
    for file, initial_hash in hash_dict.items(): 
        if not os.path.exists(file): 
            print(f"{file}not found!") 
            continue 
        current_hash = get_file_hash(file) 
        if current_hash != initial_hash:
            alert_message = f"Alert! A Change has benn detected in {file}!" 
            print(alert_message)
	    send_notification(alert_message)

def send_notification(message): 
    payload = {"content": message}
    print(payload) 
    requests.post(WEBHOOK_URL, json=payload) 

initialize_hashes()
print("File Integrity Monitioring started.")

while True: 
    check_integrity() 
    time.sleep(3600)
