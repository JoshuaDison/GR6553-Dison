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

## reflectivity ## 
ref_hdr=f.sweeps[ref_sweep][0][4][b'REF'][0]
ref_range=(np.arange(ref_hdr.num_gates+1)-0.5)*ref_hdr.gate_width+ref_hdr.first_gate
ref_range=units.Quantity(ref_range,'kilometers')
ref=np.array([ray[4][b'REF'][1] for ray in f.sweeps[ref_sweep]])

## velocity ## 
vel_hdr=f.sweeps[vel_sweep][0][4][b'VEL'][0]
vel_range=(np.arange(vel_hdr.num_gates+1)-0.5)*vel_hdr.gate_width+vel_hdr.first_gate
vel_range=units.Quantity(vel_range,'kilometers')
vel=np.array([ray[4][b'VEL'][1] for ray in f.sweeps[vel_sweep]])

cent_lon=f.sweeps[0][0][1].lon; cent_lat=f.sweeps[0][0][1].lat

fig=plt.figure(figsize=(8,8)); spec=gridspec.GridSpec(2,1)

## the various fields ## 

fields=[('Reflectivity (dBZ)',ref,ref_range,'Spectral_r'),('Velocity (m/s)',vel,vel_range,'RdYlGn_r')]

for i,(title,var_data,var_range,cmap) in enumerate(fields):
    data=np.ma.array(var_data); data[np.isnan(data)]=np.ma.masked
    xlocs,ylocs=azimuth_range_to_lat_lon(az,var_range,cent_lon,cent_lat)
    crs=ccrs.LambertConformal(central_longitude=cent_lon,central_latitude=cent_lat)
    ax=fig.add_subplot(spec[i],projection=crs)
    ax.add_feature(USCOUNTIES,linewidth=0.5)

    if title.startswith("Velocity"): ## to enchance the velocity colors ## 
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


##------------------------- Radar Movie-------------------------------##

import imageio.v2 as imageio
import glob
import re

# Collect all radar frames
files = glob.glob("Radar*.png")

def natural_key(x):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', x)]

files = sorted(files, key=natural_key)

# Load images
images = [imageio.imread(f) for f in files]

# Create GIF
imageio.mimsave("Long_Radar_Loop.gif", images, duration=1000.0)