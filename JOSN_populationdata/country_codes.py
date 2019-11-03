# from pygal.i18n import COUNTRIES
from pygal_maps_world.i18n import COUNTRIES


# for c in sorted(COUNTRIES.keys()):
#     print(c,COUNTRIES[c]);


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if country_name == name:
            return code;
    return None;


# print(get_country_code('China'));
