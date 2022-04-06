import os


def extract_place(name: str):
    place = name.split('_')[1]
    return place


def make_place_directories(places: list):
    for place in places:
        os.mkdir(place)


def organize_photos(directory: str):
    originals = os.listdir(directory)
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
