import requests


country_dict = {
    'qatar': '🇶🇦',
    'equateur': '🇪🇨',
    'senegal': '🇸🇳',
    'pays-Bas': '🇳🇱',
    'angleterre': '🏴󠁧󠁢󠁥󠁮󠁧󠁿',
    'iran': '🇮🇷',
    'usa': '🇺🇸',
    'pays de galles': '🏴󠁧󠁢󠁷󠁬󠁳󠁿',
    'argentine': '🇦🇷',
    'arabie saoudite': '🇦🇪',
    'mexique': '🇲🇽',
    'pologne': '🇵🇱',
    'france': '🇫🇷',
    'australie': '🇦🇺',
    'danemark': '🇩🇰',
    'tunisie': '🇹🇳',
    'espagne': '🇪🇸',
    'costa rica': '🇨🇷',
    'allemagne': '🇩🇪',
    'japon': '🇯🇵',
    'belgique': '🇧🇪',
    'canada': '🇨🇦',
    'maroc': '🇲🇦',
    'croatie': '🇭🇷',
    'brésil': '🇧🇷',
    'serbie': '🇷🇸',
    'suisse': '🇨🇭',
    'cameroun': '🇨🇲',
    'portugal': '🇵🇹',
    'ghana': '🇬🇭',
    'uruquay': '🇺🇾',
    'corée du sud': '🇰🇷',
}


def get_flag(country):
    """Return the flag of the given country"""
    return country_dict[country.lower()] if country.lower() in country_dict else 'Country not found'
