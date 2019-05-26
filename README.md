# Course-project: Dynamic New York City map on python
Project done by Solomiya Shuptar & Vladyslav Bilyk

Building a map using info about New York City subway stations and air pollution
------

#### Have you ever wondered how many people ride the NY metro each day?

#### And what impact does it have on the air quality?

#### We have done a research on that and vizualised it so you can observe it.


Web-app
======
[Click here](http://vladbilyk.pythonanywhere.com/)

Note: The web-app isn't fully working, only the old map can be generated due to the free account restrictions. You can generate the new map by yourself after cloning the repo and running `render.py` which is a flask app

Project structure
======

`data` - python package with modules collecting data

---`pollution.py` API

---`get_new_file.py` website data in txt format

---`info_ADT.py`, `info.py` ADT modules

---`json_data.py` rewrites data into json format

---`points_feat.py` creates points from data

`docs` - documentation folder

`map` - map creating modules

---`folium_map.py` creates the map

---`radius.py` calculates the CircleMarker radius

---`unchanged.py` data for calculating radius

`templates` - html pages

`vendor` - css, images etc.

Video presentation
======
[Click here](https://youtu.be/PO1QPNkAJqo)

More detailed info
======
[Wiki](https://github.com/soliashuptar/Course-project/wiki)
