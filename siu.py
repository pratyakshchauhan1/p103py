import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/praty/Downloads"

# intialize event handler class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey,{event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")
event_handler = FileEventHandler()
# intialize observer 
observer = Observer()
# schedule the observer 
observer.schedule(event_handler, from_dir, recursive=True)
#start the observer
observer.start()

while True:
    time.sleep(2)
    print("running...")

