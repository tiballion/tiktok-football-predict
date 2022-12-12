from tools.match import Match
from tools.flags import get_flag

from video.create_base_video import save_base_video


def main():
    country1 = input('Enter the first country: ')
    country2 = input('Enter the second country: ')
    match = Match(country1, country2, get_flag(country1), get_flag(country2), 3)
    for m in match.possibilities():
        print(m)
    # save_base_video('test')


if __name__ == '__main__':
    main()
