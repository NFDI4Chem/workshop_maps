#! /usr/bin/python3

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import numpy as np
import pathlib

p = pathlib.Path("output/")
p.mkdir(parents=True, exist_ok=True)

# output file names
output="germany_workshops_annotated_rdm.png"
# output="germany_workshops_annotated_chemotion.png"
outputlegend="legend_%s"%(output)

output = "output/" + output
outputlegend = "output/" + outputlegend

# change font
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["mathtext.fontset"] = "dejavusans"
plt.rcParams['mathtext.rm'] = 'dejavusans'
plt.rcParams['mathtext.it'] = 'dejavusans:italic'
plt.rcParams['mathtext.bf'] = 'dejavusans:bold'

params = {'text.usetex': False, 'mathtext.fontset': 'dejavusans'}
plt.rcParams.update(params)

#colors
#nfdi4chemblack25 = (0/255, 0/255, 0/255, 0.25)
nfdi4chemblack25 = (191/255, 191/255, 191/255)
nfdi4chempetrol = (0/255, 156/255, 188/255)
nfdi4chemorange = (238/255, 166/255, 0/255)
nfdi4chemyellow = (241/255, 222/255, 30/255)
nfdi4chemviolett = (149/255, 86/255, 158/255)
nfdi4chemred = (227/255, 6/255, 19/255)	

# to separat legend and figure, a while loop starts here (not the most elegant way to do it but it works)
m = 0
while m <2 :
	#load map of europe and chose right NUTS Level, source Eurostat NUTS 2021 
	#(https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts)
	df = geopandas.read_file("NUTS_RG_20M_2021_4326/NUTS_RG_20M_2021_4326.shp")
# use if you want germany without borders
#	mapdf = df[df["NAME_LATN"]=="Deutschland"]

# use if you want germany with borders
	tmpdf = df[df["CNTR_CODE"]=="DE"]
	mapdf = tmpdf[df["LEVL_CODE"]==1]

	#load information from location.dat
	city, long, lat, status, topic, kind = np.loadtxt("location_rdm.dat", unpack=True, dtype='str')
#	city, long, lat, status, topic, kind = np.loadtxt("location_chemotion.dat", unpack=True, dtype='str')
#	city, long, lat, status, topic, kind = np.loadtxt("location.dat", unpack=True, dtype='str')

	#define figure
	fig=plt.figure(figsize=(4,4), dpi=300)
	ax=fig.add_subplot(111)

	#plot map
	#mapdf.plot(ax=ax, color=nfdi4chempetrol, edgecolor="white", linewidth=0.1)
#	mapdf.plot(ax=ax, color=nfdi4chemblack25, edgecolor=nfdi4chemblack25, linewidth=0.5) #style 01
#	mapdf.plot(ax=ax, color=nfdi4chemblack25, edgecolor="black", linewidth=0.5) #style 02, borerstlye 01
	mapdf.plot(ax=ax, color=nfdi4chemblack25, edgecolor="white", linewidth=0.5) #borderstlye 02
#	mapdf.plot(ax=ax, color=nfdi4chemblack25, edgecolor="black", linewidth=0.2) #style 03

	n=0
	citychecklist = []
	labelcheck = [0, 0, 0, 0]
	while n<len(city):
		topiclabel = None
		if m == 1:
			ms = 35
		else:
			ms = 20

		#plot locations dependend of status and topic, kind is not taken into account
		if topic[n] =='RDM':
			markersymbol = 'o'
			if status[n] =='done':
				colordata = nfdi4chempetrol
				if labelcheck[0] == 0:
					topiclabel = 'RDM (past)'
					labelcheck[0] = 1
			else:
				colordata = nfdi4chemorange
				if labelcheck[1] == 0:
					topiclabel = 'RDM (planned)'
					labelcheck[1] = 1
		else:
			markersymbol = 's'
			if status[n] =='done':
				colordata = nfdi4chempetrol
				if labelcheck[2] == 0:
					topiclabel = 'Chemotion ELN (past)'
					labelcheck[2] = 1
			else:
				colordata = nfdi4chemorange
				if labelcheck[3] == 0:
					topiclabel = 'Chemotion ELN (planned)'
					labelcheck[3] = 1

		#avoid distortion of the plot by treating the coordinates right
		# change markersize when multiple events are at the same location
		if city[n] in citychecklist:
			if citychecklist.count(city[n]) ==1:
				latfloat=float(lat[n])-0.3
				coordinates = {"latitude": [long[n]], "longitude": [latfloat]}
			if citychecklist.count(city[n]) ==2:
				longfloat=float(long[n])+0.19
				coordinates = {"latitude": [longfloat], "longitude": [lat[n]]}
			if citychecklist.count(city[n]) ==3:
				longfloat=float(long[n])+0.19
				latfloat=float(lat[n])-0.3
				coordinates = {"latitude": [longfloat], "longitude": [latfloat]}
			dftest = pd.DataFrame(coordinates)
		else:
#			ms = standardms
			coordinates = {"latitude": [long[n]], "longitude": [lat[n]]}
			dftest = pd.DataFrame(coordinates)
		locations = geopandas.GeoDataFrame(coordinates, geometry=geopandas.points_from_xy(dftest.longitude, dftest.latitude),crs = "EPSG:4326")

#		locations.plot(ax=ax, marker=markersymbol, markersize=ms, color=colordata, label=topiclabel, linestyle='None') #style 01, style 02 borderstyle 01
		locations.plot(ax=ax, marker=markersymbol, markersize=ms, color=colordata, label=topiclabel, linestyle='None', edgecolor="black", linewidth=0.2) #style 03
# add location name to point
		if not city[n] in citychecklist:
			x = locations.geometry.x
			y = locations.geometry.y
			if city[n]=="Aachen":
				plt.annotate(city[n], xy=(x,y), xytext=(0,-7.0), textcoords="offset points", ha="center", size="5")
			if city[n]=="Mainz":
				plt.annotate(city[n], xy=(x,y), xytext=(-4.0,0), textcoords="offset points", size="5")				
			elif city[n]=="Hannover" or city[n]=="Halle":
				plt.annotate(city[n], xy=(x,y), xytext=(0,4.0), textcoords="offset points", ha="center", size="5")
			else:
				plt.annotate(city[n], xy=(x,y), xytext=(4.0,-2.0), textcoords="offset points", size="5")

#for x, y, label in zip(cities.geometry.x, cities.geometry.y, cities.name):
#    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")
		citychecklist.append(city[n])
		n += 1
		
	if m==0:
		plt.axis([5,15.2,47,55])
		plt.title("Institutional workshops")
		plt.axis('off')
		plt.savefig(output, bbox_inches='tight', pad_inches=0.05, transparent=True)
	else:
		plt.legend(loc="lower left", numpoints=1, frameon=False)
		plt.axis([4,15,44,46])
		plt.axis('off')
		plt.savefig(outputlegend, bbox_inches='tight', pad_inches=0.05, transparent=True)
	plt.clf()
	m += 1
