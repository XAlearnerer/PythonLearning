import json;
from country_codes import get_country_code

import pygal;
import pygal_maps_world.maps

# 加载数据到列表中
filename = "population_data.json";
with open(filename) as f:
    pop_data = json.load(f);

cc_populations = {};

for pop_dict in pop_data:
    if pop_dict['Year'] == "2010":
        country_name = pop_dict["Country Name"];
        popution = int(float(pop_dict['Value']));
        # print(country_name + " : " + str(popution));
        code = get_country_code(country_name);
        if code:
            # print(code + "  " + str(popution));
            cc_populations[code] = popution;
        # else:
        # print("Error + " + country_name);

#wm = pygal.Worldmap();
wm = pygal_maps_world.maps.World()
wm.title = "World Popution in 2010";
wm.add('2010', cc_populations);

wm.render_to_file("Popution.svg");



