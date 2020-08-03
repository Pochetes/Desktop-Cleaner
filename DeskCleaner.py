#! python3

import sys
import time, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from extension import extension_paths

def rename(path, destination_path):
    # adds a number incremented to duplicate files
    if Path(destination_path / path.name).exists():
        i = 0

        while True:
            i += 1
            # ex. file.py ---> duplicate ---> file1.py, file2.py, etc.
            new_name = destination_path / f'{path.stem}_{i}{path.suffix}'

            if not new_name.exists():
                # if no duplicates, return original name
                return new_name

    else:
        # if no file in Roberto, return folder path
        return destination_path / path.name 

class MyHandler(FileSystemEventHandler):
    def __init__(self, path, dest):
        self.path = path.resolve()
        self.dest = dest.resolve()

    def on_modified(self, event):
        for child in self.path.iterdir():
            # skips non-specified locations and directories      
            if child.is_file() and (child.suffix.lower() in extension_paths):
                # changes file location to path/to/file/Roberto/file.ext
                destination_path = self.dest / extension_paths[child.suffix.lower()]
                # renames the file for duplicates
                destination_path = rename(path=child, destination_path=destination_path)
                shutil.move(child, destination_path)
        
        
if __name__ == "__main__":
    path = Path.home() / 'Desktop'
    destination_path = path / 'Roberto'
    event_handler = MyHandler(path=path, dest=destination_path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


