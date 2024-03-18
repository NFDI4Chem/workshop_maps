# NFDI4Chem_Maps
This python script plots the locations given in location.dat on a map of Germany. If you add something to location.dat the plot will be updated automatically. The newest images can be downloaded:

Download Images from [here](https://gitlab.com/B.Golub/nfdi4chem_maps/builds/artifacts/main/download?job=create-images).

The shapes for the plot are from (https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts) if you use the maps, please mention Eurostat as source. 

The locations of the workshops are red from the file location.dat, the columns are:
city longitude latitude status topic kind

city - name of the city (important to check for multiple events)\
longitude/latitude - coordinates of the city\
status - done or planned\
topic - RDM or Chemotion\
kind - online or inperson (not used at the moment)

Example:\
Braunschweig 52.264149 10.526420 done RDM inperson