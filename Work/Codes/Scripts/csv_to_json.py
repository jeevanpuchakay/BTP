import json
import csv


def get_csv_data(labels_path):
    labels = []
    with open(labels_path) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for row in csv_reader:
            row["center_x"] = int(row["center_x"])/1920
            row["center_y"] = int(row["center_y"])/1080
            row["width"] = int(row["width"])/1920
            row["height"] = int(row["height"])/1080
            labels.append(row)
    return labels


def generate_new_labels(csv_labels, file_names):
    new_labels = {}
    for idx, file_name in enumerate(file_names):

        template = {}

        template["filename"] = file_name
        template["objects"] = []
        new_labels[file_name] = template

    count = 1
    for label in new_labels:
        new_labels[label]["frame_id"] = count
        count += 1
    for label in csv_labels:
        object = {}
        object["relative_coordinates"] = {}
        object["relative_coordinates"]["center_x"] = label["center_x"]
        object["relative_coordinates"]["center_y"] = label["center_y"]
        object["relative_coordinates"]["width"] = label["width"]
        object["relative_coordinates"]["height"] = label["height"]
        object["name"] = label["name"]
        new_labels[label["filename"]]["objects"].append(object)

    final_labels = []

    for filename in new_labels:
        final_labels.append(new_labels[filename])

    return final_labels


def write_to_json(new_annotations, new_annotation_path):
    with open(new_annotation_path, 'w') as f:
        f.write(json.dumps(new_annotations))


def get_file_names(ALL_FILE_NAMES_PATH):
    file_names = []
    with open(ALL_FILE_NAMES_PATH) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for row in csv_reader:
            file_names.append(row["name"])
    return file_names


if __name__ == "__main__":

    LABELS = "/mnt/c/Users/jeeva/Documents/GitHub/BTP/Work/Data/ITSD/labels.csv"
    NEW_LABELS_PATH = "/mnt/c/Users/jeeva/Documents/GitHub/BTP/Work/Data/ITSD/ITSDGroundTruth.json"
    ALL_FILE_NAMES_PATH = "/mnt/c/Users/jeeva/Documents/GitHub/BTP/Work/Data/ITSD/temp.csv"

    csv_labels = get_csv_data(LABELS)
    file_names = get_file_names(ALL_FILE_NAMES_PATH)
    new_labels = generate_new_labels(csv_labels, file_names)

    write_to_json(new_labels, NEW_LABELS_PATH)
