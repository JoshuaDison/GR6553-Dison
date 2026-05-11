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

## axis limits ## 

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
plt.savefig('SkewSounding00z.png')

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
plt.savefig('SkewSounding12z.png')
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
plt.savefig('SkewSounding18z.png')
plt.show()

## Sounding Movie 
import imageio.v2 as imageio
import glob
import re

# Collect all radar frames
files = glob.glob("SkewSounding*.png")

def natural_key(x):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', x)]

files = sorted(files, key=natural_key)

# Load images
images = [imageio.imread(f) for f in files]

# Create GIF
imageio.mimsave("SkewT_Sounding_Loop.gif", images, duration=1000.0)