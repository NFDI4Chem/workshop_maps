# NFDI4Chem_Maps
This Python script plots the locations given in location.dat on a map of Germany. If you add something to location.dat the plot will be updated automatically. To download the latest images go to the [actions tab](https://github.com/NFDI4Chem/workshop_maps/actions), click on the latest run and download the artifacts from there by clicking on the name "images".

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