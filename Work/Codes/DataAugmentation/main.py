import os
import json
from PIL import Image
from pathlib import Path
import torch
from torchvision import transforms


def rotate_images(input_folder, output_folder, rotation_angle, old_annotations, new_annotations):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".jpg") == False:
            continue
        img = Image.open(input_folder + file_name)
        width, height = img.width, img.height
        rotated_image = img.rotate(rotation_angle, expand=False)
        rotated_image.save(output_folder + file_name)  # , file_name.split('.')[-1].lower())
        x_center, y_center = width / 2, height / 2
        failed_files = []
        try:
            if rotation_angle == -90:
                old_annotation = old_annotations["imgs"][file_name.split('.')[0]]
                new_annotation = old_annotation
                new_annotation["objects"] = []
                for object in old_annotation["objects"]:
                    bbox = object["bbox"]
                    bbox["xmin"] -= x_center
                    bbox["ymin"] -= y_center
                    bbox["xmax"] -= x_center
                    bbox["ymax"] -= y_center
                    bbox["xmin"], bbox["ymin"] = bbox["ymin"], -bbox["xmin"]
                    bbox["xmax"], bbox["ymax"] = bbox["ymax"], -bbox["xmax"]

                    bbox["xmin"], bbox["ymin"] = bbox["xmin"] + x_center, bbox["ymin"] + y_center
                    bbox["xmax"], bbox["ymax"] = bbox["xmax"] + x_center, bbox["ymax"] + y_center
                    new_annotation["objects"].append(bbox)
            elif rotation_angle == -180:
                old_annotation = old_annotations["imgs"][file_name.split('.')[0]]
                new_annotation = old_annotation
                new_annotation["objects"] = []
                for object in old_annotation["objects"]:
                    bbox = object["bbox"]
                    bbox["xmin"] -= x_center
                    bbox["ymin"] -= y_center
                    bbox["xmax"] -= x_center
                    bbox["ymax"] -= y_center
                    bbox["xmin"], bbox["ymin"] = -bbox["xmin"], -bbox["ymin"]
                    bbox["xmax"], bbox["ymax"] = -bbox["xmax"], -bbox["ymax"]

                    bbox["xmin"], bbox["ymin"] = bbox["xmin"] + x_center, bbox["ymin"] + y_center
                    bbox["xmax"], bbox["ymax"] = bbox["xmax"] + x_center, bbox["ymax"] + y_center

                    new_annotation["objects"].append(bbox)
            elif rotation_angle == -270:
                old_annotation = old_annotations["imgs"][file_name.split('.')[0]]
                new_annotation = old_annotation
                new_annotation["objects"] = []
                for object in old_annotation["objects"]:
                    bbox = object["bbox"]
                    bbox["xmin"] -= x_center
                    bbox["ymin"] -= y_center
                    bbox["xmax"] -= x_center
                    bbox["ymax"] -= y_center
                    bbox["xmin"], bbox["ymin"] = bbox["ymin"], -bbox["xmin"]
                    bbox["xmax"], bbox["ymax"] = bbox["ymax"], -bbox["xmax"]

                    bbox["xmin"], bbox["ymin"] = bbox["xmin"] + x_center, bbox["ymin"] + y_center
                    bbox["xmax"], bbox["ymax"] = bbox["xmax"] + x_center, bbox["ymax"] + y_center

                    new_annotation["objects"].append(bbox)
        except KeyError:
            print(file_name + " File details not found in source annotation.")
            failed_files.append(file_name)

    return new_annotations, failed_files


def change_brightness(new_brightness_level, input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if not file_name.endswith(".jpg"):
            continue
        img = Image.open(input_folder + file_name)
        new_image = transforms.ColorJitter(brightness=new_brightness_level)(img)
        new_image.save(output_folder + file_name)
    return


def change_contrast(new_contrast, input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if not file_name.endswith(".jpg"):
            continue
        img = Image.open(input_folder + file_name)
        new_image = transforms.ColorJitter(contrast=new_contrast)(img)
        new_image.save(output_folder + file_name)
    return

def change_hue(new_hue, input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if not file_name.endswith(".jpg"):
            continue
        img = Image.open(input_folder + file_name)
        new_image = transforms.ColorJitter(hue=new_hue)(img)
        new_image.save(output_folder + file_name)
    return


def resize_pictures(new_size, input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if not file_name.endswith(".jpg"):
            continue
        img = Image.open(input_folder + file_name)
        resized_image = img.resize(new_size)
        resized_image.save(output_folder + file_name)


def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def makedir(path):
    try:
        path = Path(path)
        path.mkdir(parents=True)
        print("Directory created")
    except FileExistsError as e:
        print("Output directory already exists.")


def write_to_json(new_annotations, new_annotation_path):
    with open(new_annotation_path, 'w') as f:
        f.write(json.dumps(new_annotations))


def write_to_txt(array, txt_file_path):
    with open(txt_file_path, 'w') as f:
        json.dump(array, f)


if __name__ == "__main__":
    base_path = "/mnt/g/Drive/BTP/TSD"
    input_folder = base_path + "/tt100k_2021/TSD/"
    dataset_name = "tt100k_2021_hu_0_4"
    output_folder = base_path + "/HueVariations/" + dataset_name + "/TSD/"
    annotations_file_path = base_path + "/tt100k_2021/annotations_all.json"
    new_annotations_file_path = base_path + "/HueVariations/" + dataset_name + "/annotations_all.json"
    failed_files_list_path = base_path + "/HueVariations/" + dataset_name + "/failed_files.txt"
    old_annotations = read_json_file(annotations_file_path)
    makedir(output_folder)
    new_annotations = {"types": old_annotations["types"], "imgs": {}}

    # resize_pictures((1024,1024),input_folder=input_folder, output_folder=output_folder)

    change_hue(new_hue=0.4, input_folder=input_folder, output_folder=output_folder)

    # change_contrast(new_contrast=2.5, input_folder=input_folder, output_folder=output_folder)

    # change_brightness(new_brightness_level=3.5, input_folder=input_folder, output_folder=output_folder)

    # new_annotations, failed_files = rotate_images(input_folder, output_folder, -180, old_annotations, new_annotations)

    # write_to_json(new_annotations, new_annotations_file_path)
    # print(failed_files)
    # write_to_txt(failed_files, failed_files_list_path)
