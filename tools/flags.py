import requests


country_dict = {
    'qatar': '๐ถ๐ฆ',
    'equateur': '๐ช๐จ',
    'senegal': '๐ธ๐ณ',
    'pays-Bas': '๐ณ๐ฑ',
    'angleterre': '๐ด๓ ง๓ ข๓ ฅ๓ ฎ๓ ง๓ ฟ',
    'iran': '๐ฎ๐ท',
    'usa': '๐บ๐ธ',
    'pays de galles': '๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ',
    'argentine': '๐ฆ๐ท',
    'arabie saoudite': '๐ฆ๐ช',
    'mexique': '๐ฒ๐ฝ',
    'pologne': '๐ต๐ฑ',
    'france': '๐ซ๐ท',
    'australie': '๐ฆ๐บ',
    'danemark': '๐ฉ๐ฐ',
    'tunisie': '๐น๐ณ',
    'espagne': '๐ช๐ธ',
    'costa rica': '๐จ๐ท',
    'allemagne': '๐ฉ๐ช',
    'japon': '๐ฏ๐ต',
    'belgique': '๐ง๐ช',
    'canada': '๐จ๐ฆ',
    'maroc': '๐ฒ๐ฆ',
    'croatie': '๐ญ๐ท',
    'brรฉsil': '๐ง๐ท',
    'serbie': '๐ท๐ธ',
    'suisse': '๐จ๐ญ',
    'cameroun': '๐จ๐ฒ',
    'portugal': '๐ต๐น',
    'ghana': '๐ฌ๐ญ',
    'uruquay': '๐บ๐พ',
    'corรฉe du sud': '๐ฐ๐ท',
}


def get_flag(country):
    """Return the flag of the given country"""
    return country_dict[country.lower()] if country.lower() in country_dict else 'Country not found'


def get_flag_dict():
    """Return the dict of all flags"""
    return country_dict