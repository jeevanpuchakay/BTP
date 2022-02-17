from shutil import copy
import os
from pathlib import Path

def makedir(path):
    try:
        path = Path(path)
        path.mkdir(parents=True)
        print("Directory created")
    except FileExistsError as e:
        print("Output directory already exists.")


if __name__ == "__main__":
    source_folder = "/media/anuj/data/swastik/swastik/CAR/DCIM3/Movie/"
    destination_folder = "/media/anuj/data/swastik/swastik/CAR/DCIM3/TempJeevan/"
    batch_count = 10
    batch_size = 50
    current_batch = 1
    current_batch_size = 0
    copied_files_count = 0
    makedir(destination_folder+"Batch-1/")
    for file_name in os.listdir(source_folder):
        if current_batch_size > (batch_size):
            current_batch_size = 0
            current_batch += 1
            makedir(destination_folder+"Batch-"+str(current_batch)+"/")
        src_filename = source_folder + file_name
        dst_filename = destination_folder + \
            "Batch-"+str(current_batch) + "/" + file_name
        try:
            copy(src_filename, dst_filename)
            current_batch_size += 1
        except:
            print("Failed to copy: "+src_filename)
