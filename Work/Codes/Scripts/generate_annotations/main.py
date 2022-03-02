
from fileinput import filename
import json
from os import mkdir

from pathlib import Path


def makedir(path):
    try:
        path = Path(path)
        path.mkdir(parents=True)
        print("Directory created")
    except FileExistsError as e:
        print("Output directory already exists.")


def get_json_data(file_name):
    with open(file_name, "r") as file:
        return json.load(file)


def write_to_json(new_annotations, new_annotation_path):
    with open(new_annotation_path, 'w') as f:
        f.write(json.dumps(new_annotations))


def create_annotations(all_annotations, ANNOTATIONS_OUTPUT_PATH):

    for annotation in all_annotations:
        filename = annotation["filename"].split("/")[-1]

        filename = filename.split('.')[0]+".json"
        new_annotation = {}
        new_annotation["objects"] = []
        for object in annotation["objects"]:
            sign = {}

            sign["bbox"] = {}
            sign["label"] = object["name"]
            sign["bbox"]["center_x"] = object["relative_coordinates"]["center_x"]
            sign["bbox"]["center_y"] = object["relative_coordinates"]["center_y"]
            sign["bbox"]["width"] = object["relative_coordinates"]["width"]
            sign["bbox"]["height"] = object["relative_coordinates"]["height"]

            new_annotation["objects"].append(sign)
        write_to_json(new_annotation, ANNOTATIONS_OUTPUT_PATH+filename)


if __name__ == "__main__":
    ITSD_FILE_PATH = "/mnt/c/Users/jeeva/Documents/GitHub/BTP/Work/Data/ITSD_Annotations.json"
    ANNOTATIONS_OUTPUT_PATH = "/mnt/c/Users/jeeva/Documents/GitHub/BTP/Work/Data/ITSD_Annotations/"
    makedir(ANNOTATIONS_OUTPUT_PATH)

    all_annotations = get_json_data(ITSD_FILE_PATH)


    create_annotations(all_annotations,ANNOTATIONS_OUTPUT_PATH)