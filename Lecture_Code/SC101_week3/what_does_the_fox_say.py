"""
File: what_does_the_fox_say.py
Name: Shane Liu
-------------------------
This program shows the basic concepts of Python dict
by inputting data from Youtube video What Does the Fox Say.
"""


def main():
    """
    Add some sound of animals!
    """
    sounds = {}
    sounds['dog'] = 'woof'
    sounds['cat'] = 'meow'
    sounds['bird'] = 'tweet'
    sounds['fox'] = 'ringdingdingdingdingring'
    sounds['fox'] = 'wapapapapow'
    print_dict(sounds)


def print_dict(d):
    """
    : param d: dict, containing the sound of animals
    """
    # Method 1:
    for animals in d:
        sound = d[animals]
        print(animals, '-->', sound)
    # Method 2:
    for animals, sound in d.items():
        print(animals, '-->', sound)


if __name__ == '__main__':
    main()
