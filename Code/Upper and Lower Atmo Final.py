#%% --------------------------- Upper Atmosphere------------------------
import pygrib
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import metpy.calc as mpcalc
from metpy.units import units

grb = pygrib.open('gfs.0p25.2023033100.f000.grib2')

# 500‑mb Geopotential Height #
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity #
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   

# 500‑mb Winds #
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

## Vorticity ##
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))
colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))
cf = ax.contourf(lons, lats, avor_500 * 1e5,clevs_500_avor, colors=colors,extend='max', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('Absolute Vorticity (1e×10⁻⁵ s⁻¹)')


## Heights ##
clevs_500_hght = np.arange(4800, 6200, 60)
cs = ax.contour(lons, lats, hght_500,clevs_500_hght, colors='black',linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice], uwnd_kt[wind_slice].m,vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)
plt.title('500‑mb Geopotential Height (m) • Absolute Vorticity (s^-1) • Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 00Z Analysis', loc='right')
plt.savefig('UpperAtmo00z.png')

plt.show()

##-------------------------------- 03z-------------------- ##
grb = pygrib.open('gfs.0p25.2023033100.f003.grib2')

# 500‑mb Geopotential Height #
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity #
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   

# 500‑mb Winds #
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

## Vorticity ##
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))
colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))
cf = ax.contourf(lons, lats, avor_500 * 1e5,clevs_500_avor, colors=colors,extend='max', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('Absolute Vorticity (1e×10⁻⁵ s⁻¹)')


## Heights ##
clevs_500_hght = np.arange(4800, 6200, 60)
cs = ax.contour(lons, lats, hght_500,clevs_500_hght, colors='black',linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice], uwnd_kt[wind_slice].m,vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)
plt.title('500‑mb Geopotential Height (m) • Absolute Vorticity (s^-1) • Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 03Z Analysis', loc='right')
plt.savefig('UpperAtmo03z.png')
plt.show()

##-------------------------------------------- 06z--------------------##

grb = pygrib.open('gfs.0p25.2023033100.f006.grib2')

# 500‑mb Geopotential Height #
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity #
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   

# 500‑mb Winds #
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

## Vorticity ##
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))
colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))
cf = ax.contourf(lons, lats, avor_500 * 1e5,clevs_500_avor, colors=colors,extend='max', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('Absolute Vorticity (1e×10⁻⁵ s⁻¹)')


## Heights ##
clevs_500_hght = np.arange(4800, 6200, 60)
cs = ax.contour(lons, lats, hght_500,clevs_500_hght, colors='black',linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice], uwnd_kt[wind_slice].m,vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)
plt.title('500‑mb Geopotential Height (m) • Absolute Vorticity (s^-1) • Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 06Z Analysis', loc='right')
plt.savefig('UpperAtmo06z.png')
plt.show()

##-------------------------------------------- 09z--------------------##

grb = pygrib.open('gfs.0p25.2023033100.f009.grib2')

# 500‑mb Geopotential Height #
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity #
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   

# 500‑mb Winds #
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

## Vorticity ##
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))
colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))
cf = ax.contourf(lons, lats, avor_500 * 1e5,clevs_500_avor, colors=colors,extend='max', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('Absolute Vorticity (1e×10⁻⁵ s⁻¹)')


## Heights ##
clevs_500_hght = np.arange(4800, 6200, 60)
cs = ax.contour(lons, lats, hght_500,clevs_500_hght, colors='black',linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice], uwnd_kt[wind_slice].m,vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)
plt.title('500‑mb Geopotential Height (m) • Absolute Vorticity (s^-1) • Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 09Z Analysis', loc='right')
plt.savefig('UpperAtmo09z.png')
plt.show()

##-------------------------------------------- 12z--------------------##

grb = pygrib.open('gfs.0p25.2023033100.f012.grib2')

# 500‑mb Geopotential Height #
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity #
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   

# 500‑mb Winds #
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

## Vorticity ##
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))
colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))
cf = ax.contourf(lons, lats, avor_500 * 1e5,clevs_500_avor, colors=colors,extend='max', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('Absolute Vorticity (1e×10⁻⁵ s⁻¹)')


## Heights ##
clevs_500_hght = np.arange(4800, 6200, 60)
cs = ax.contour(lons, lats, hght_500,clevs_500_hght, colors='black',linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice], uwnd_kt[wind_slice].m,vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)
plt.title('500‑mb Geopotential Height (m) • Absolute Vorticity (s^-1) • Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 12Z Analysis', loc='right')
plt.savefig('UpperAtmo12z.png')
plt.show()

##-------------------------------------------- 15z--------------------##

grb = pygrib.open('gfs.0p25.2023033100.f015.grib2')

# 500‑mb Geopotential Height #
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity #
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   

# 500‑mb Winds #
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

## Vorticity ##
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))
colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))
cf = ax.contourf(lons, lats, avor_500 * 1e5,clevs_500_avor, colors=colors,extend='max', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('Absolute Vorticity (1e×10⁻⁵ s⁻¹)')


## Heights ##
clevs_500_hght = np.arange(4800, 6200, 60)
cs = ax.contour(lons, lats, hght_500,clevs_500_hght, colors='black',linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice], uwnd_kt[wind_slice].m,vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)
plt.title('500‑mb Geopotential Height (m) • Absolute Vorticity (s^-1) • Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 15Z Analysis', loc='right')
plt.savefig('UpperAtmo15z.png')
plt.show()
## -----------------------------------18z----------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f018.grib2')

# 500‑mb Geopotential Height #
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity #
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   

# 500‑mb Winds #
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

## Vorticity ##
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))
colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))
cf = ax.contourf(lons, lats, avor_500 * 1e5,clevs_500_avor, colors=colors,extend='max', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('Absolute Vorticity (1e×10⁻⁵ s⁻¹)')


## Heights ##
clevs_500_hght = np.arange(4800, 6200, 60)
cs = ax.contour(lons, lats, hght_500,clevs_500_hght, colors='black',linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice], uwnd_kt[wind_slice].m,vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)
plt.title('500‑mb Geopotential Height (m) • Absolute Vorticity (s^-1) • Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 18Z Analysis', loc='right')
plt.savefig('UpperAtmo18z.png')
plt.show()

##-------------------------------------------- 21z--------------------##

grb = pygrib.open('gfs.0p25.2023033100.f021.grib2')

# 500‑mb Geopotential Height #
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity #
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   

# 500‑mb Winds #
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

## Vorticity ##
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))
colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))
cf = ax.contourf(lons, lats, avor_500 * 1e5,clevs_500_avor, colors=colors,extend='max', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('Absolute Vorticity (1e×10⁻⁵ s⁻¹)')


## Heights ##
clevs_500_hght = np.arange(4800, 6200, 60)
cs = ax.contour(lons, lats, hght_500,clevs_500_hght, colors='black',linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice], uwnd_kt[wind_slice].m,vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)
plt.title('500‑mb Geopotential Height (m) • Absolute Vorticity (s^-1) • Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 21Z Analysis', loc='right')
plt.savefig('UpperAtmo21z.png')
plt.show()

##-------------------------------------------- 24z--------------------##

grb = pygrib.open('gfs.0p25.2023033100.f024.grib2')

# 500‑mb Geopotential Height #
gh_msg = grb.select(name='Geopotential height', level=500)[0]
hght_500 = gh_msg.values
lats, lons = gh_msg.latlons()

# 500‑mb Absolute Vorticity #
avor_msg = grb.select(name='Absolute vorticity', level=500)[0]
avor_500 = avor_msg.values   

# 500‑mb Winds #
u_msg = grb.select(name='U component of wind', level=500)[0]
v_msg = grb.select(name='V component of wind', level=500)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')
uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

## Vorticity ##
clevs_500_avor = list(range(-8, 1, 1)) + list(range(8, 46, 1))
colors1 = plt.cm.YlOrRd(np.linspace(0, 1, 48))
colors2 = plt.cm.BuPu(np.linspace(0.5, 0.75, 8))
colors = np.vstack((colors2, (1, 1, 1, 1), colors1))
cf = ax.contourf(lons, lats, avor_500 * 1e5,clevs_500_avor, colors=colors,extend='max', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('Absolute Vorticity (1e×10⁻⁵ s⁻¹)')

## Heights ##
clevs_500_hght = np.arange(4800, 6200, 60)
cs = ax.contour(lons, lats, hght_500,clevs_500_hght, colors='black',linewidths=1.0, transform=datacrs)
plt.clabel(cs, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))

ax.barbs(lons[wind_slice], lats[wind_slice], uwnd_kt[wind_slice].m,vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)
plt.title('500‑mb Geopotential Height (m) • Absolute Vorticity (s^-1) • Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 24Z Analysis', loc='right')
plt.savefig('UpperAtmo24z.png')
plt.show()

#%%

##----------------- Lower Atmosphere 0z ------------------##

grb = pygrib.open('gfs.0p25.2023033100.f000.grib2')

tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15
lats, lons = tmp_msg.latlons()

# 850mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,clevs_tmp, cmap='coolwarm', extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850mb Geopotential Height
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,clevs_hgt, colors='black',linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))
ax.barbs(lons[wind_slice], lats[wind_slice],uwnd_kt[wind_slice].m, vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height (m) • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 00Z Analysis', loc='right')
plt.savefig('LowerAtmo00z.png')
plt.show()

##------------------------------03z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f003.grib2')

tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15
lats, lons = tmp_msg.latlons()

# 850mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,clevs_tmp, cmap='coolwarm', extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850mb Geopotential Height
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,clevs_hgt, colors='black',linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))
ax.barbs(lons[wind_slice], lats[wind_slice],uwnd_kt[wind_slice].m, vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height (m) • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 03Z Analysis', loc='right')
plt.savefig('LowerAtmo03z.png')
plt.show()

##------------------------------06z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f006.grib2')

tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15
lats, lons = tmp_msg.latlons()

# 850mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,clevs_tmp, cmap='coolwarm', extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850mb Geopotential Height
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,clevs_hgt, colors='black',linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))
ax.barbs(lons[wind_slice], lats[wind_slice],uwnd_kt[wind_slice].m, vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height (m) • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 06Z Analysis', loc='right')
plt.savefig('LowerAtmo06z.png')
plt.show()

##------------------------------09z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f009.grib2')

tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15
lats, lons = tmp_msg.latlons()

# 850mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,clevs_tmp, cmap='coolwarm', extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850mb Geopotential Height
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,clevs_hgt, colors='black',linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))
ax.barbs(lons[wind_slice], lats[wind_slice],uwnd_kt[wind_slice].m, vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height (m) • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 09Z Analysis', loc='right')
plt.savefig('LowerAtmo09z.png')
plt.show()

##------------------------------12z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f012.grib2')

tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15
lats, lons = tmp_msg.latlons()

# 850mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,clevs_tmp, cmap='coolwarm', extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850mb Geopotential Height
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,clevs_hgt, colors='black',linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))
ax.barbs(lons[wind_slice], lats[wind_slice],uwnd_kt[wind_slice].m, vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height (m) • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 12Z Analysis', loc='right')
plt.savefig('LowerAtmo12z.png')
plt.show()

##------------------------------15z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f015.grib2')

tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15
lats, lons = tmp_msg.latlons()

# 850mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,clevs_tmp, cmap='coolwarm', extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850mb Geopotential Height
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,clevs_hgt, colors='black',linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))
ax.barbs(lons[wind_slice], lats[wind_slice],uwnd_kt[wind_slice].m, vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height (m) • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 15Z Analysis', loc='right')
plt.savefig('LowerAtmo15z.png')
plt.show()

##------------------------------18z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f018.grib2')

tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15
lats, lons = tmp_msg.latlons()

# 850mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,clevs_tmp, cmap='coolwarm', extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850mb Geopotential Height
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,clevs_hgt, colors='black',linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))
ax.barbs(lons[wind_slice], lats[wind_slice],uwnd_kt[wind_slice].m, vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height (m) • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 18Z Analysis', loc='right')
plt.savefig('LowerAtmo18z.png')
plt.show()

##------------------------------21z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f021.grib2')

tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15
lats, lons = tmp_msg.latlons()

# 850mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,clevs_tmp, cmap='coolwarm', extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850mb Geopotential Height
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,clevs_hgt, colors='black',linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))
ax.barbs(lons[wind_slice], lats[wind_slice],uwnd_kt[wind_slice].m, vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height (m) • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 21Z Analysis', loc='right')
plt.savefig('LowerAtmo21z.png')
plt.show()

##------------------------------24z----------------------------------##

grb = pygrib.open('gfs.0p25.2023033100.f024.grib2')

tmp_msg = grb.select(name='Temperature', level=850)[0]
tmp_850 = tmp_msg.values - 273.15
lats, lons = tmp_msg.latlons()

# 850mb Geopotential Height
hgt_msg = grb.select(name='Geopotential height', level=850)[0]
hgt_850 = hgt_msg.values

# 850mb Winds
u_msg = grb.select(name='U component of wind', level=850)[0]
v_msg = grb.select(name='V component of wind', level=850)[0]

uwnd = u_msg.values * units('m/s')
vwnd = v_msg.values * units('m/s')

uwnd_kt = uwnd.to('kt')
vwnd_kt = vwnd.to('kt')

mapcrs = ccrs.LambertConformal(central_longitude=-100, central_latitude=35,standard_parallels=(30, 60))
datacrs = ccrs.PlateCarree()

fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], datacrs)

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

clevs_tmp = np.arange(-30, 31, 2)
cf = ax.contourf(lons, lats, tmp_850,clevs_tmp, cmap='coolwarm', extend='both', transform=datacrs)

cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True)
cb.set_label('850‑mb Temperature (°C)')

# 850mb Geopotential Height
clevs_hgt = np.arange(1200, 1800, 30)
cs_hgt = ax.contour(lons, lats, hgt_850,clevs_hgt, colors='black',linewidths=1.2, transform=datacrs)
plt.clabel(cs_hgt, fmt='%d')

wind_slice = (slice(None, None, 12), slice(None, None, 12))
ax.barbs(lons[wind_slice], lats[wind_slice],uwnd_kt[wind_slice].m, vwnd_kt[wind_slice].m,pivot='middle', color='black',transform=datacrs)

plt.title('850‑mb Temperature (°C) • 850‑mb Geopotential Height (m) • 850‑mb Winds (kts)', loc='left')
plt.title('GFS 0.25° • 2023‑03‑31 24Z Analysis', loc='right')
plt.savefig('LowerAtmo24z.png')
plt.show()

#%%

## Upper Atmosphere Movie ##
import imageio.v2 as imageio
import glob
import re

# Collect all radar frames
files = glob.glob("Upper*.png")


def natural_key(x):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', x)]

files = sorted(files, key=natural_key)

# Load images
images = [imageio.imread(f) for f in files]

# Create GIF
imageio.mimsave("Upper_Atmo_Loop.gif", images, duration=1000.0)




## Lower Atmosphere Movie ##
import imageio.v2 as imageio
import glob
import re

# Collect all radar frames
files = glob.glob("Lower*.png")

def natural_key(x):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', x)]

files = sorted(files, key=natural_key)

# Load images
images = [imageio.imread(f) for f in files]

# Create GIF
imageio.mimsave("Lower_Atmo_Loop.gif", images, duration=1000.0)

