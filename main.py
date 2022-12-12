from tools.match import Match
from tools.flags import get_flag, get_flag_dict

from video.create_base_video import save_base_video


def get_match():
    """Return a match object with the two countries and the max score"""
    country1 = input('Enter the first country: ')
    if country1 not in get_flag_dict():
        print('Country not found'); return
    country2 = input('Enter the second country: ')
    if country2 == country1:
        print('The two countries must be different'); return
    if country2 not in get_flag_dict():
        print('Country not found'); return
    max_score = input('Enter the max score: ')
    if not max_score.isdigit():
        print('The max score must be a number'); return
    return Match(country1, country2, get_flag(country1), get_flag(country2), max_score)


def main():
    match = get_match()
    if match is None:
        return
    for m in match.possibilities():
        print(m)
    # save_base_video('test')


if __name__ == '__main__':
    main()
