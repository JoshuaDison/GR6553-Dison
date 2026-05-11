## Final Project ##

import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from metpy.calc import azimuth_range_to_lat_lon
from metpy.cbook import get_test_data
from metpy.io import Level2File
from metpy.plots import USCOUNTIES
from metpy.units import units
import geopandas as gpd
import matplotlib.pyplot as plt
from metpy.plots import PlotGeometry, MapPanel, PanelContainer
import cartopy.feature as cf
import geopandas
from metpy.cbook import get_test_data
from metpy.plots import MapPanel, PanelContainer, PlotGeometry

## ---------------------------- SURFACE MAP -------------------------------##


## 0100 Sounding ## -----------------------------------

day1_outlook01 = geopandas.read_file('day1otlk_20230331_0100_cat.lyr.geojson')


geo = PlotGeometry()
geo.geometry = day1_outlook01['geometry']
geo.fill = day1_outlook01['fill']
geo.stroke = day1_outlook01['stroke']
geo.labels = day1_outlook01['LABEL']
geo.label_fontsize = 'large'

## Producing the Graphic ## 

panel = MapPanel()
panel.title = 'SPC Day 1 Convective Outlook (Valid 01z Mar 31 2023)'
panel.plots = [geo]
panel.area = [-120, -75, 25, 50]
panel.projection = 'lcc'
panel.layers = ['lakes', 'land', 'ocean', 'states', 'coastline', 'borders']

pc = PanelContainer()
pc.size = (12, 8)
pc.panels = [panel]
plt.savefig('SPC0100.png')
pc.show()

## 1200 Sounding ## ------------------------------------

day1_outlook12 = geopandas.read_file('day1otlk_20230331_1200_cat.lyr.geojson')


geo = PlotGeometry()
geo.geometry = day1_outlook12['geometry']
geo.fill = day1_outlook12['fill']
geo.stroke = day1_outlook12['stroke']
geo.labels = day1_outlook12['LABEL']
geo.label_fontsize = 'large'

panel = MapPanel()
panel.title = 'SPC Day 1 Convective Outlook (Valid 12z Mar 31 2023)'
panel.plots = [geo]
panel.area = [-120, -75, 25, 50]
panel.projection = 'lcc'
panel.layers = ['lakes', 'land', 'ocean', 'states', 'coastline', 'borders']

pc = PanelContainer()
pc.size = (12, 8)
pc.panels = [panel]
plt.savefig('SPC1200.png')
pc.show()

## 1300 Sounding ## ------------------------------------------

day1_outlook13 = geopandas.read_file('day1otlk_20230331_1300_cat.lyr.geojson')


geo = PlotGeometry()
geo.geometry = day1_outlook13['geometry']
geo.fill = day1_outlook13['fill']
geo.stroke = day1_outlook13['stroke']
geo.labels = day1_outlook13['LABEL']
geo.label_fontsize = 'large'

panel = MapPanel()
panel.title = 'SPC Day 1 Convective Outlook (Valid 13z Mar 31 2023)'
panel.plots = [geo]
panel.area = [-120, -75, 25, 50]
panel.projection = 'lcc'
panel.layers = ['lakes', 'land', 'ocean', 'states', 'coastline', 'borders']

pc = PanelContainer()
pc.size = (12, 8)
pc.panels = [panel]
plt.savefig('SPC1300.png')
pc.show()

## 1630 Sounding ## -------------------------------------------------

day1_outlook16 = geopandas.read_file('day1otlk_20230331_1630_cat.lyr.geojson')


geo = PlotGeometry()
geo.geometry = day1_outlook16['geometry']
geo.fill = day1_outlook16['fill']
geo.stroke = day1_outlook16['stroke']
geo.labels = day1_outlook16['LABEL']
geo.label_fontsize = 'large'

panel = MapPanel()
panel.title = 'SPC Day 1 Convective Outlook (Valid 1630z Mar 31 2023)'
panel.plots = [geo]
panel.area = [-120, -75, 25, 50]
panel.projection = 'lcc'
panel.layers = ['lakes', 'land', 'ocean', 'states', 'coastline', 'borders']

pc = PanelContainer() ## producing the image ## 
pc.size = (12, 8)
pc.panels = [panel]
plt.savefig('SPC1630.png')
pc.show()
