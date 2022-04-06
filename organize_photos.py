import os
import sys


def extract_place(name: str):
    place = name.split('_')[1]
    return place


def make_place_directories(places: list):
    for place in places:
        os.mkdir(place)


def organize_photos(directory: str):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print("\033[91mPlease ensure you have extracted "
              "the Photos folder in this directory")
        sys.exit()
    originals = os.listdir()
    places = []
    for photo in originals:
        place_name = extract_place(photo)
        if place_name not in places:
            places.append(place_name)

    make_place_directories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


if __name__ == "__main__":
    organize_photos("Photos")
