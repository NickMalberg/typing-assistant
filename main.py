from pynput import keyboard
from pynput.keyboard import Key
import csv
import atexit
from collections import deque

key_map_single_keys = {}
key_map_words = {}
word = ""
cache = deque(maxlen=3)


def on_press(key):
    global word
    try:
        if key.char in key_map_single_keys:
            key_map_single_keys[key.char] += 1
        else:
            key_map_single_keys[key.char] = 1

        # Initialize the 'word' variable
        if word == "":

            word = key.char
        else:
            word += key.char  # Append the character to the 'word' variable
        cache.append(key.char)

    except AttributeError:
        print(f"key: {key}")
        if key in key_map_single_keys:
            key_map_single_keys[key] += 1
        else:
            key_map_single_keys[key] = 1

        if f"{key}" == "Key.backspace":
            word = word[:-1]  # Remove the last character from the 'word' variable

        if f"{key}" == "Key.space" or f"{key}" == "Key.enter":
            if word in key_map_words:
                key_map_words[word] += 1
            else:
                key_map_words[word] = 1

            print(f"word: {word}")
            word = ""
        cache.append(key)
        print(f"cache: {cache}")


def save_key_map():
    data_dir = "data/"
    with open(
        f"{data_dir}key_map.csv", mode="w", newline="", encoding="utf-8"
    ) as key_map_file:
        key_map_writer = csv.writer(
            key_map_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        for key, value in key_map_single_keys.items():
            key_map_writer.writerow([key, value])

    with open(
        f"{data_dir}key_map_words.csv", mode="w", newline="", encoding="utf-8"
    ) as key_map_words_file:
        key_map_words_writer = csv.writer(
            key_map_words_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        for key, value in key_map_words.items():
            key_map_words_writer.writerow([key, value])


def on_release(key):
    if cache.count(Key.esc) == 3:
        # Stop listener
        return False


def main():

    print("starting Keylogger")
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    atexit.register(save_key_map)


if __name__ == "__main__":
    main()
