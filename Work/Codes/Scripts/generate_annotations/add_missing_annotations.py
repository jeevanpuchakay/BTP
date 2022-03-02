
import json
import csv


def get_json_data(file_name):
    with open(file_name, "r") as file:
        return json.load(file)


def get_csv_data(MISSING_LABELS):
    missing_labels = []
    with open(MISSING_LABELS) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for row in csv_reader:
            row["center_x"] = int(row["center_x"])/1920
            row["center_y"] = int(row["center_y"])/1080
            row["width"] = int(row["width"])/1920
            row["height"] = int(row["height"])/1080
            missing_labels.append(row)
    return missing_labels


def add_class_id(labels):
    for label in labels:
        if label["name"] == "regulatory":
            label["class_id"] = 0
        elif label["name"] == "warning":
            label["class_id"] = 1
        elif label["name"] == "information":
            label["class_id"] = 2
        elif label["name"] == "complementary":
            label["class_id"] = 3
    return labels


def make_key_pair(labels):
    new_labels = {}

    for label in labels:
        if label["filename"] not in new_labels.keys():
            new_labels[label["filename"]] = []
        temp_label = {}
        temp_label["class_id"] = label["class_id"]

        temp_label["name"] = label["name"]

        temp_label["relative_coordinates"] = {}
        temp_label["relative_coordinates"]["center_x"] = label["center_x"]
        temp_label["relative_coordinates"]["center_y"] = label["center_y"]
        temp_label["relative_coordinates"]["width"] = label["width"]
        temp_label["relative_coordinates"]["height"] = label["height"]
        new_labels[label["filename"]].append(temp_label)

    return new_labels


def add_missing_labels(current_labels, missing_labels):

    for label in current_labels:
        if label["filename"].split("/")[-1] not in missing_labels.keys():
            continue
        for missed_label in missing_labels[label["filename"].split("/")[-1]]:
            label["objects"].append(missed_label)
    return current_labels



if __name__ == "__main__":

    RESULT_IMPROVED = "/mnt/c/Users/jeeva/Documents/GitHub/BTP/Work/Data/result_Improved.json"
    MISSING_LABELS = "/mnt/c/Users/jeeva/Documents/GitHub/BTP/Work/Data/missing_labels.csv"

    NEW_LABELS = "/mnt/c/Users/jeeva/Documents/GitHub/BTP/Work/Data/ITSD_Annotations.json"

    HEADER_PATH = "/home/anuj/Desktop/hdd1/swastik/swastik/CAR/ImprovedResolution/ImprovedResolution/"

    current_labels = get_json_data(RESULT_IMPROVED)

    missing_labels = get_csv_data(MISSING_LABELS)
    # print(missing_labels)
    missing_labels = add_class_id(missing_labels)

    missing_labels = make_key_pair(missing_labels)

    new_labels = add_missing_labels(current_labels, missing_labels)

    write_to_json(new_labels, NEW_LABELS)
