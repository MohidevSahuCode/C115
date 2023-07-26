import os
import time
import random
import sys
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "C:/Users/mohid/Downloads"
destination = "C:/Users/mohid/OneDrive/Desktop/New folder"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,ext = os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value :
                file = os.path.basename(event.src_path)
                path1 = source + "/" + file
                path2 = destination + "/" + key
                path3 = destination + "/" + key + "/" + file

                if os.path.exists (path2) :
                    print("Directory Exist !")
                    time.sleep(1)

                    if os.path.exists(path3):
                        print("File alredy exist")
                        print("Renaming file")
                        new_file_name = os.path.splitext(file)[0] + str(random.randint(0, 999)) + os.path.splitext(file)[1]
                        path4 = destination + "/" + key + "/" + new_file_name
                        print("Moving " + new_file_name + "...")
                        shutil.move(path1,path4)
                        time.sleep(1)
                    else :
                        print("Moving " + file + "...")
                        shutil.move(path1,path3)
                        time.sleep(1)
                else :
                    print("Making Directory .")
                    os.makedirs(path2)
                    print("Moving " + file + "...")
                    shutil.move(path1,path3)
                    time.sleep(1)

event_handler = FileSystemEventHandler()
observer = Observer()

observer.schedule(event_handler,source,recursive=True)
observer.start()

try :
    while True :
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt :
    print("Stopped.")
    observer.stop()