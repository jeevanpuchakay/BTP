import numpy as np
from PIL import Image
from ISR.models import RDN
import os


home_path = "/mnt/g/Drive/BTP/Pictures/"


def get_unrecognised_pictures_list():
    unrecognised_pictures_path = home_path + "Det/PicturesWithUnRecognizedSigns/"
    unrecognised_pictures_list = []
    for file_name in os.listdir(unrecognised_pictures_path):
        unrecognised_pictures_list.append(file_name.split('_det')[0]+".png")

    return unrecognised_pictures_list


if __name__ == "__main__":
    unrecognised_pictures_list = get_unrecognised_pictures_list()

    all_pictures_path = home_path + "AllPicturesFromVideos/"
    output_directory = "/mnt/g/Results/"
    failed_pictures_list = []
    for file_name in unrecognised_pictures_list:
        try:
            print(all_pictures_path+file_name)
            img = Image.open(all_pictures_path+file_name)
            img = img.convert("RGB")
            lr_img = np.array(img)

            rdn = RDN(weights='psnr-small')
            sr_img = rdn.predict(lr_img, by_patch_of_size=50)
            enhanced_image = Image.fromarray(sr_img)
            enhanced_image.save(
                output_directory+file_name.split('.')[0]+"_res"+".jpg")

        except:
            print("Processing "+file_name+" is Failed.\n")
            failed_pictures_list.append(file_name)

    with open('failed.txt', 'w') as f:
        for item in failed_pictures_list:
            f.write("%s\n" % item)
