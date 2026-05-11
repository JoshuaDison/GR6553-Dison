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

panel = MapPanel()
panel.title = 'SPC Day 1 Convective Outlook (Valid 01z Mar 31 2023)'
panel.plots = [geo]
panel.area = [-120, -75, 25, 50]
panel.projection = 'lcc'
panel.layers = ['lakes', 'land', 'ocean', 'states', 'coastline', 'borders']

pc = PanelContainer()
pc.size = (12, 8)
pc.panels = [panel]
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

pc = PanelContainer()
pc.size = (12, 8)
pc.panels = [panel]
pc.show()

## -----------------------------Skew-T --------------------##

from siphon.simplewebservice.wyoming import WyomingUpperAir
from metpy.units import units
import metpy.calc as mpcalc
from metpy.plots import SkewT
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import metpy.calc as mpcalc
from metpy.plots import add_metpy_logo, Hodograph, SkewT
from metpy.units import units

## 0z Sounding ##

date = datetime(2023, 3, 31, 0)
station = 'LZK'

df = WyomingUpperAir.request_data(date, station)

p = df['pressure'].values * units.hPa
T = df['temperature'].values * units.degC
Td = df['dewpoint'].values * units.degC
wind_dir = df['direction'].values * units.degrees
wind_speed = df['speed'].values * units.knots
u, v = mpcalc.wind_components(wind_speed, wind_dir)

idx = np.argsort(p)[::-1]
p, T, Td, u, v = p[idx], T[idx], Td[idx], u[idx], v[idx]

valid = (~np.isnan(u)) & (~np.isnan(v))

fig = plt.figure(figsize=(9, 11))
skew = SkewT(fig, rotation=45)

skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[valid], u[valid], v[valid])

skew.ax.set_xlim(-40, 60)
skew.ax.set_ylim(1050, 100)

lcl_p, lcl_t = mpcalc.lcl(p[0], T[0], Td[0])
skew.plot(lcl_p, lcl_t, 'ko')

prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
skew.plot(p, prof, 'k', linewidth=2)

skew.shade_cin(p, T, prof, Td)
skew.shade_cape(p, T, prof)

skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()

plt.title(f'{station} Sounding', loc='left')
plt.title(f'Valid Time: {date}', loc='right')

plt.show()

## -----------------12 Sounding ---------------------##

date = datetime(2023, 3, 31, 12)
station = 'LZK'

df = WyomingUpperAir.request_data(date, station)

p = df['pressure'].values * units.hPa
T = df['temperature'].values * units.degC
Td = df['dewpoint'].values * units.degC
wind_dir = df['direction'].values * units.degrees
wind_speed = df['speed'].values * units.knots
u, v = mpcalc.wind_components(wind_speed, wind_dir)

idx = np.argsort(p)[::-1]
p, T, Td, u, v = p[idx], T[idx], Td[idx], u[idx], v[idx]

valid = (~np.isnan(u)) & (~np.isnan(v))

fig = plt.figure(figsize=(9, 11))
skew = SkewT(fig, rotation=45)

skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[valid], u[valid], v[valid])

skew.ax.set_xlim(-40, 60)
skew.ax.set_ylim(1050, 100)

lcl_p, lcl_t = mpcalc.lcl(p[0], T[0], Td[0])
skew.plot(lcl_p, lcl_t, 'ko')

prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
skew.plot(p, prof, 'k', linewidth=2)

skew.shade_cin(p, T, prof, Td)
skew.shade_cape(p, T, prof)

skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()

plt.title(f'{station} Sounding', loc='left')
plt.title(f'Valid Time: {date}', loc='right')

plt.show()

## -----------------------------18 Z Sounding--------------------------- ##

date = datetime(2023, 3, 31, 18)
station = 'LZK'

df = WyomingUpperAir.request_data(date, station)

p = df['pressure'].values * units.hPa
T = df['temperature'].values * units.degC
Td = df['dewpoint'].values * units.degC
wind_dir = df['direction'].values * units.degrees
wind_speed = df['speed'].values * units.knots
u, v = mpcalc.wind_components(wind_speed, wind_dir)

idx = np.argsort(p)[::-1]
p, T, Td, u, v = p[idx], T[idx], Td[idx], u[idx], v[idx]

valid = (~np.isnan(u)) & (~np.isnan(v))

fig = plt.figure(figsize=(9, 11))
skew = SkewT(fig, rotation=45)

skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[valid], u[valid], v[valid])

skew.ax.set_xlim(-40, 60)
skew.ax.set_ylim(1050, 100)

lcl_p, lcl_t = mpcalc.lcl(p[0], T[0], Td[0])
skew.plot(lcl_p, lcl_t, 'ko')

prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
skew.plot(p, prof, 'k', linewidth=2)

skew.shade_cin(p, T, prof, Td)
skew.shade_cape(p, T, prof)

skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()


plt.title(f'{station} Sounding', loc='left')
plt.title(f'Valid Time: {date}', loc='right')

plt.show()

#%%
##------------------------------------ Radar -----------------##

from metpy.io import Level2File
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from metpy.calc import azimuth_range_to_lat_lon
from metpy.plots import USCOUNTIES
from metpy.units import units
import matplotlib.gridspec as gridspec

## ---------------- 2:01 -------------------##

f=Level2File('KLZK20230331_190103_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-40,vmax=40,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:01 UTC")
plt.savefig('Radar1901.png')
plt.show()

## ---------------- 2:06 -------------------##

f=Level2File('KLZK20230331_190630_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-40,vmax=40,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:06 UTC")
plt.savefig('Radar1906.png')

plt.show()

## ---------------- 2:11 pm -------------------------##

f=Level2File('KLZK20230331_191147_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1) ## plotting the figure size

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-40,vmax=40,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:11 UTC")
plt.savefig('Radar1911.png')

plt.show()

## ---------------- 2:17 pm -------------------------## 

f=Level2File('KLZK20230331_191705_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-60,vmax=60,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:17 UTC")
plt.savefig('Radar1917.png')

plt.show()

## ---------------- 2:22 pm -------------------------##

f=Level2File('KLZK20230331_192215_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-60,vmax=60,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:22 UTC")
plt.savefig('Radar1922.png')

plt.show()

## ----------------- 2:27 pm ----------------------------##

f=Level2File('KLZK20230331_192732_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-60,vmax=60,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:27 UTC")
plt.savefig('Radar1927.png')

plt.show()

## ----------------- 2:32 pm ----------------------------##

f=Level2File('KLZK20230331_193250_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-60,vmax=60,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:32 UTC")
plt.savefig('Radar1932.png')

plt.show()

## ----------------- 2:38 pm ----------------------------##

f=Level2File('KLZK20230331_193806_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-60,vmax=60,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:38 UTC")
plt.savefig('Radar1938.png')

plt.show()


## ----------------- 2:43 pm ----------------------------##

f=Level2File('KLZK20230331_194310_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-60,vmax=60,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:43 UTC")
plt.savefig('Radar1943.png')

plt.show()

## ----------------- 2:48 pm ----------------------------##

f=Level2File('KLZK20230331_194827_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-60,vmax=60,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:48 UTC")
plt.savefig('Radar1948.png')

plt.show()

## ----------------- 2:53 pm ----------------------------##

f=Level2File('KLZK20230331_195326_V06')

ref_sweep=0; vel_sweep=1

az=np.array([ray[0].az_angle for ray in f.sweeps[ref_sweep]])

diff=np.diff(az); crossed=diff<-180; diff[crossed]+=360; avg_spacing=diff.mean()

az=(az[:-1]+az[1:])/2; az[crossed]+=180

az=np.concatenate(([az[0]-avg_spacing],az,[az[-1]+avg_spacing]))
az=units.Quantity(az,'degrees')

ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"):
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap='RdYlGn_r',vmin=-60,vmax=60,transform=ccrs.PlateCarree())
    else:
        pcm=ax.pcolormesh(xlocs,ylocs,data,cmap=cmap,transform=ccrs.PlateCarree())

    ax.set_extent([cent_lon-0.28,cent_lon+0.28,cent_lat-0.28,cent_lat+0.28])
    ax.set_aspect('equal','datalim')
    ax.set_title(title)
    plt.colorbar(pcm,ax=ax)

plt.suptitle("KLZK Radar - 03/31/2023 19:53 UTC")
plt.savefig('Radar1953.png')

plt.show()

#%% --------------------------- Upper Atmosphere------------------------
import pygrib
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import metpy.calc as mpcalc
from metpy.units import units

# ---------------------------------------------------------
# OPEN GRIB2 FILE
# ---------------------------------------------------------
grb = pygrib.open('gfs.0p25.2023033100.f000.grib2')

# 500‑mb Geopotential Height
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   # raw s^-1

# 500‑mb Winds
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

# Convert to knots for barbs
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

# ---------------------------------------------------------
# MAP PROJECTION (YOUR BLOCK)
# ---------------------------------------------------------
mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# ---------------------------------------------------------
# ABSOLUTE VORTICITY COLOR SET (YOUR STYLE)
# ---------------------------------------------------------
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))

colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))

# ---------------------------------------------------------
# SHADED ABSOLUTE VORTICITY (×1e5)
# ---------------------------------------------------------
cf = ax.contourf(lons, lats, avor_500 * 1e5,
                 clevs_500_avor, colors=colors,
                 extend='max', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)

# ---------------------------------------------------------
# 500‑MB GEOPOTENTIAL HEIGHT CONTOURS
# ---------------------------------------------------------
clevs_500_hght = np.arange(4800, 6200, 60)

cs = ax.contour(lons, lats, hght_500,
                clevs_500_hght, colors='black',
                linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

# ---------------------------------------------------------
# WIND BARBS (EVERY 20TH)
# ---------------------------------------------------------
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

# ---------------------------------------------------------
# TITLES (NEW)
# ---------------------------------------------------------
plt.title('500‑mb Geopotential Height • Absolute Vorticity • Winds', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 00Z Analysis', loc='right')

plt.show()

##-------------------------------- 03z-------------------- ##


grb = pygrib.open('gfs.0p25.2023033100.f003.grib2')

# 500‑mb Geopotential Height
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   # raw s^-1

# 500‑mb Winds
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

# Convert to knots for barbs
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))

colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))

cf = ax.contourf(lons, lats, avor_500 * 1e5,
                 clevs_500_avor, colors=colors,
                 extend='max', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)

clevs_500_hght = np.arange(4800, 6200, 60)

cs = ax.contour(lons, lats, hght_500,
                clevs_500_hght, colors='black',
                linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('500‑mb Geopotential Height • Absolute Vorticity • Winds', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 03Z Analysis', loc='right')

plt.show()

##-------------------------------------------- 06z--------------------##
grb = pygrib.open('gfs.0p25.2023033100.f006.grib2')

# 500‑mb Geopotential Height
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   # raw s^-1

# 500‑mb Winds
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

# Convert to knots for barbs
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))

colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))

cf = ax.contourf(lons, lats, avor_500 * 1e5,
                 clevs_500_avor, colors=colors,
                 extend='max', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)

clevs_500_hght = np.arange(4800, 6200, 60)

cs = ax.contour(lons, lats, hght_500,
                clevs_500_hght, colors='black',
                linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('500‑mb Geopotential Height • Absolute Vorticity • Winds', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 06Z Analysis', loc='right')

plt.show()

##-------------------------------------------- 09z--------------------##
grb = pygrib.open('gfs.0p25.2023033100.f009.grib2')

# 500‑mb Geopotential Height
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   # raw s^-1

# 500‑mb Winds
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

# Convert to knots for barbs
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))

colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))

cf = ax.contourf(lons, lats, avor_500 * 1e5,
                 clevs_500_avor, colors=colors,
                 extend='max', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)

clevs_500_hght = np.arange(4800, 6200, 60)

cs = ax.contour(lons, lats, hght_500,
                clevs_500_hght, colors='black',
                linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('500‑mb Geopotential Height • Absolute Vorticity • Winds', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 09Z Analysis', loc='right')

plt.show()

##-------------------------------------------- 12z--------------------##
grb = pygrib.open('gfs.0p25.2023033100.f012.grib2')

# 500‑mb Geopotential Height
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   # raw s^-1

# 500‑mb Winds
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

# Convert to knots for barbs
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))

colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))

cf = ax.contourf(lons, lats, avor_500 * 1e5,
                 clevs_500_avor, colors=colors,
                 extend='max', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)

clevs_500_hght = np.arange(4800, 6200, 60)

cs = ax.contour(lons, lats, hght_500,
                clevs_500_hght, colors='black',
                linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('500‑mb Geopotential Height • Absolute Vorticity • Winds', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 12Z Analysis', loc='right')

plt.show()

##-------------------------------------------- 15z--------------------##
grb = pygrib.open('gfs.0p25.2023033100.f015.grib2')

# 500‑mb Geopotential Height
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   # raw s^-1

# 500‑mb Winds
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

# Convert to knots for barbs
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))

colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))

cf = ax.contourf(lons, lats, avor_500 * 1e5,
                 clevs_500_avor, colors=colors,
                 extend='max', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)

clevs_500_hght = np.arange(4800, 6200, 60)

cs = ax.contour(lons, lats, hght_500,
                clevs_500_hght, colors='black',
                linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('500‑mb Geopotential Height • Absolute Vorticity • Winds', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 15Z Analysis', loc='right')

plt.show()
## -----------------------------------18z----------------------------##
grb = pygrib.open('gfs.0p25.2023033100.f018.grib2')

# 500‑mb Geopotential Height
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   # raw s^-1

# 500‑mb Winds
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

# Convert to knots for barbs
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))

colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))

cf = ax.contourf(lons, lats, avor_500 * 1e5,
                 clevs_500_avor, colors=colors,
                 extend='max', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)

clevs_500_hght = np.arange(4800, 6200, 60)

cs = ax.contour(lons, lats, hght_500,
                clevs_500_hght, colors='black',
                linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('500‑mb Geopotential Height • Absolute Vorticity • Winds', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 18Z Analysis', loc='right')

plt.show()

##-------------------------------------------- 21z--------------------##
grb = pygrib.open('gfs.0p25.2023033100.f021.grib2')

# 500‑mb Geopotential Height
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   # raw s^-1

# 500‑mb Winds
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

# Convert to knots for barbs
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))

colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))

cf = ax.contourf(lons, lats, avor_500 * 1e5,
                 clevs_500_avor, colors=colors,
                 extend='max', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)

clevs_500_hght = np.arange(4800, 6200, 60)

cs = ax.contour(lons, lats, hght_500,
                clevs_500_hght, colors='black',
                linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('500‑mb Geopotential Height • Absolute Vorticity • Winds', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 21Z Analysis', loc='right')

plt.show()

##-------------------------------------------- 24z--------------------##
grb = pygrib.open('gfs.0p25.2023033100.f024.grib2')

# 500‑mb Geopotential Height
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   # raw s^-1

# 500‑mb Winds
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

# Convert to knots for barbs
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))

colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))

cf = ax.contourf(lons, lats, avor_500 * 1e5,
                 clevs_500_avor, colors=colors,
                 extend='max', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)

clevs_500_hght = np.arange(4800, 6200, 60)

cs = ax.contour(lons, lats, hght_500,
                clevs_500_hght, colors='black',
                linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('500‑mb Geopotential Height • Absolute Vorticity • Winds', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 24Z Analysis', loc='right')

plt.show()

#%%

##----------------- Lower Atmosphere 0z ------------------##

grb = pygrib.open('gfs.0p25.2023033100.f000.grib2')

# 850‑mb Temperature (convert to °C)
tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15   # K → °C
lats, lons = tmp_msg.latlons()

# 850‑mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850‑mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 850‑mb Temperature fill (°C)
clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,
                 clevs_tmp, cmap='coolwarm',
                 extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850‑mb Geopotential Height contours
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,
                    clevs_hgt, colors='black',
                    linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

# 850‑mb Wind Barbs
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 00Z Analysis', loc='right')

plt.show()

##------------------------------03z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f003.grib2')

# 850‑mb Temperature (convert to °C)
tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15   # K → °C
lats, lons = tmp_msg.latlons()

# 850‑mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850‑mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 850‑mb Temperature fill (°C)
clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,
                 clevs_tmp, cmap='coolwarm',
                 extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850‑mb Geopotential Height contours
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,
                    clevs_hgt, colors='black',
                    linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

# 850‑mb Wind Barbs
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 03Z Analysis', loc='right')

plt.show()

##------------------------------06z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f006.grib2')

# 850‑mb Temperature (convert to °C)
tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15   # K → °C
lats, lons = tmp_msg.latlons()

# 850‑mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850‑mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 850‑mb Temperature fill (°C)
clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,
                 clevs_tmp, cmap='coolwarm',
                 extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850‑mb Geopotential Height contours
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,
                    clevs_hgt, colors='black',
                    linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

# 850‑mb Wind Barbs
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 06Z Analysis', loc='right')

plt.show()

##------------------------------09z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f009.grib2')

# 850‑mb Temperature (convert to °C)
tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15   # K → °C
lats, lons = tmp_msg.latlons()

# 850‑mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850‑mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 850‑mb Temperature fill (°C)
clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,
                 clevs_tmp, cmap='coolwarm',
                 extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850‑mb Geopotential Height contours
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,
                    clevs_hgt, colors='black',
                    linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

# 850‑mb Wind Barbs
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 09Z Analysis', loc='right')

plt.show()

##------------------------------12z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f012.grib2')

# 850‑mb Temperature (convert to °C)
tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15   # K → °C
lats, lons = tmp_msg.latlons()

# 850‑mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850‑mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 850‑mb Temperature fill (°C)
clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,
                 clevs_tmp, cmap='coolwarm',
                 extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850‑mb Geopotential Height contours
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,
                    clevs_hgt, colors='black',
                    linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

# 850‑mb Wind Barbs
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 12Z Analysis', loc='right')

plt.show()

##------------------------------15z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f015.grib2')

# 850‑mb Temperature (convert to °C)
tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15   # K → °C
lats, lons = tmp_msg.latlons()

# 850‑mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850‑mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 850‑mb Temperature fill (°C)
clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,
                 clevs_tmp, cmap='coolwarm',
                 extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850‑mb Geopotential Height contours
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,
                    clevs_hgt, colors='black',
                    linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

# 850‑mb Wind Barbs
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 15Z Analysis', loc='right')

plt.show()

##------------------------------18z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f018.grib2')

# 850‑mb Temperature (convert to °C)
tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15   # K → °C
lats, lons = tmp_msg.latlons()

# 850‑mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850‑mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 850‑mb Temperature fill (°C)
clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,
                 clevs_tmp, cmap='coolwarm',
                 extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850‑mb Geopotential Height contours
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,
                    clevs_hgt, colors='black',
                    linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

# 850‑mb Wind Barbs
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 18Z Analysis', loc='right')

plt.show()

##------------------------------21z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f021.grib2')

# 850‑mb Temperature (convert to °C)
tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15   # K → °C
lats, lons = tmp_msg.latlons()

# 850‑mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850‑mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 850‑mb Temperature fill (°C)
clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,
                 clevs_tmp, cmap='coolwarm',
                 extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850‑mb Geopotential Height contours
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,
                    clevs_hgt, colors='black',
                    linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

# 850‑mb Wind Barbs
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 21Z Analysis', loc='right')

plt.show()

##------------------------------24z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f024.grib2')

# 850‑mb Temperature (convert to °C)
tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15   # K → °C
lats, lons = tmp_msg.latlons()

# 850‑mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850‑mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,
                               standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 850‑mb Temperature fill (°C)
clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,
                 clevs_tmp, cmap='coolwarm',
                 extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
                  extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850‑mb Geopotential Height contours
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,
                    clevs_hgt, colors='black',
                    linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

# 850‑mb Wind Barbs
wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice],
         uwnd_kt[wind_slice].m,
         vwnd_kt[wind_slice].m,
         pivot='middle', color='black',
         transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 24Z Analysis', loc='right')

plt.show()












