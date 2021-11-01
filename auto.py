# importing observer and file system handling from python watchdog lib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self,events):
        i=1
        for filename in os.listdir(folder_to_track):
            print(filename)
            a,b = filename.split(".")
            print(b)
            if b in ["jpg","jpeg","gif","png","raw"]:
                src =  folder_to_track + "/" + filename
                new_dest = folder_of_destination + "/Pictures/" + filename
                os.rename(src, new_dest)
            elif b in ["mp3","mp4"]:
                src =  folder_to_track + "/" + filename
                new_dest = folder_of_destination + "/Music/" + filename
                os.rename(src, new_dest)
            else:
                src =  folder_to_track + "/" + filename
                new_dest = folder_of_destination + "Templates/" + filename
                os.rename(src, new_dest)
                

            
                
     



folder_to_track = "/home/av/Downloads/"
folder_of_destination = "/home/av/Documents/"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt():
    observer.stop()
    
observer.join()