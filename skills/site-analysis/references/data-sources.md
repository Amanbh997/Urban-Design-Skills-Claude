# Data Sources Reference

Comprehensive directory of open and publicly accessible data sources for
multi-scale site analysis. Organized by category with source descriptions,
geographic coverage, data formats, update frequency, and access methods.

---

## GIS Portals and Mapping Agencies

### United States

| Source | Coverage | Data Types | URL |
|--------|----------|------------|-----|
| USGS National Map | US | Topography, hydrology, land cover, imagery | https://www.usgs.gov/the-national-map-data-delivery |
| USGS 3DEP (3D Elevation Program) | US | LiDAR, DEM, contours (1m, 3m, 10m) | https://www.usgs.gov/3d-elevation-program |
| Census TIGER/Line | US | Boundaries, roads, water, parcels | https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html |
| USDA NRCS Web Soil Survey | US | Soil types, properties, suitability ratings | https://websoilsurvey.nrcs.usda.gov |
| FEMA Flood Map Service | US | Flood zones, BFE, floodways | https://msc.fema.gov |
| EPA EnviroMapper | US | Environmental sites, facilities, monitoring | https://enviro.epa.gov |
| National Wetlands Inventory | US | Wetland locations and classification | https://www.fws.gov/program/national-wetlands-inventory |

### International

| Source | Coverage | Data Types | URL |
|--------|----------|------------|-----|
| OpenStreetMap | Global | Roads, buildings, land use, POI, transit | https://www.openstreetmap.org |
| Copernicus Open Access Hub | Global | Sentinel satellite imagery (10m optical, SAR) | https://dataspace.copernicus.eu |
| USGS Earth Explorer | Global | Landsat imagery (30m), SRTM DEM (30m) | https://earthexplorer.usgs.gov |
| Natural Earth | Global | Country boundaries, coastlines, populated places | https://www.naturalearthdata.com |
| Ordnance Survey Open Data | UK | Topography, boundaries, roads, terrain | https://osdatahub.os.uk |
| Geoportail | France | Topography, cadastre, imagery, land use | https://www.geoportail.gouv.fr |
| Geoscience Australia | Australia | Topography, geology, water, hazards | https://www.ga.gov.au/data-pubs |

### Municipal Open Data Portals

Many cities and counties maintain open data portals with local GIS datasets
including parcels, zoning, building footprints, infrastructure, and permits.
Search for "[city name] open data" or "[county name] GIS" to find local
portals. Common platforms:
- ArcGIS Hub (hub.arcgis.com) -- hosts thousands of municipal datasets
- Socrata (data.socrata.com) -- municipal open data platform
- CKAN-based portals -- used by many governments worldwide

---

## Census and Demographics

### United States

| Source | Data Types | Geography | Update | URL |
|--------|------------|-----------|--------|-----|
| US Census Bureau Decennial Census | Population, households, race, age | Block level | 10 years | https://data.census.gov |
| American Community Survey (ACS) | Income, housing, education, commuting, employment | Tract level (5-year estimates) | Annual | https://data.census.gov |
| LEHD/LODES (OnTheMap) | Employment location, commute flows, job-housing | Block level | Annual | https://onthemap.ces.census.gov |
| Census Reporter | Pre-formatted census profiles by geography | Tract, county, metro | Continuous | https://censusreporter.org |

### International

| Source | Coverage | Data Types | URL |
|--------|----------|------------|-----|
| Eurostat | EU | Population, income, housing, labor | https://ec.europa.eu/eurostat |
| UK Office for National Statistics | UK | Census, demographics, economy | https://www.ons.gov.uk |
| Statistics Canada | Canada | Census, demographics, economy | https://www.statcan.gc.ca |
| Australian Bureau of Statistics | Australia | Census, demographics, economy | https://www.abs.gov.au |
| World Bank Open Data | Global | Population, development indicators | https://data.worldbank.org |
| UN Data | Global | Demographic and social statistics | https://data.un.org |

---

## Transportation Data

### Network and Infrastructure

| Source | Coverage | Data Types | Format | URL |
|--------|----------|------------|--------|-----|
| OpenStreetMap | Global | Road network, classification, cycling, paths | OSM XML, PBF | https://www.openstreetmap.org |
| HPMS (Highway Performance Monitoring System) | US | Traffic volumes, road condition | Tabular | https://www.fhwa.dot.gov/policyinformation/hpms.cfm |
| State DOT Traffic Count Maps | US (by state) | ADT counts by road segment | Web map, tabular | [varies by state] |
| National Bridge Inventory | US | Bridge locations, condition, capacity | Tabular | https://www.fhwa.dot.gov/bridge/nbi.cfm |

### Transit

| Source | Coverage | Data Types | Format | URL |
|--------|----------|------------|--------|-----|
| Transitland | Global | Transit routes, stops, schedules | GTFS, API | https://www.transit.land |
| OpenMobilityData | Global | GTFS feeds from 1,300+ agencies | GTFS | https://mobilitydatabase.org |
| National Transit Database (NTD) | US | Ridership, service data, financials | Tabular | https://www.transit.dot.gov/ntd |

### Accessibility Scores

| Source | Data Types | URL |
|--------|------------|-----|
| Walk Score | Walk Score, Transit Score, Bike Score | https://www.walkscore.com |
| AllTransit | Transit connectivity and access metrics | https://alltransit.cnt.org |

---

## Environmental and Climate Data

### Climate and Weather

| Source | Coverage | Data Types | Format | URL |
|--------|----------|------------|--------|-----|
| NOAA Climate Data Online | US + Global | Temperature, precipitation, wind, historical records | Tabular (CSV) | https://www.ncdc.noaa.gov/cdo-web |
| Iowa Environmental Mesonet | US | Wind roses, ASOS/AWOS station data | Images, tabular | https://mesonet.agron.iastate.edu |
| EnergyPlus Weather Data | Global (2,100+ stations) | EPW weather files for building simulation | EPW | https://energyplus.net/weather |
| Climate Explorer (KNMI) | Global | Climate data analysis and visualization | Web tool | https://climexp.knmi.nl |
| WorldClim | Global | Temperature, precipitation, bioclimatic variables | Raster (GeoTIFF) | https://www.worldclim.org |

### Air Quality

| Source | Coverage | Data Types | URL |
|--------|----------|------------|-----|
| EPA AirNow | US | Real-time AQI, PM2.5, ozone, NO2 | https://www.airnow.gov |
| EPA Air Quality System (AQS) | US | Historical monitoring data | https://www.epa.gov/aqs |
| European Environment Agency | EU | Air quality maps and data | https://www.eea.europa.eu/themes/air |
| OpenAQ | Global | Aggregated air quality data | https://openaq.org |

### Flood and Water

| Source | Coverage | Data Types | URL |
|--------|----------|------------|-----|
| FEMA Flood Map Service Center | US | Flood zones, BFE, FIRM maps | https://msc.fema.gov |
| USGS National Water Information | US | Stream gauges, groundwater, water quality | https://waterdata.usgs.gov |
| Global Flood Monitor | Global | Real-time and historical flood events | https://www.globalfloodmonitor.org |
| Aqueduct Water Risk Atlas | Global | Water stress, flood risk, drought risk | https://www.wri.org/aqueduct |

### Ecology and Land Cover

| Source | Coverage | Data Types | URL |
|--------|----------|------------|-----|
| NLCD (National Land Cover Database) | US | Land cover classification (30m) | https://www.mrlc.gov |
| CORINE Land Cover | EU | Land cover classification (100m) | https://land.copernicus.eu |
| GBIF (Global Biodiversity Information) | Global | Species occurrence records | https://www.gbif.org |
| US Fish & Wildlife ECOS | US | Endangered species, critical habitat | https://ecos.fws.gov |
| iNaturalist | Global | Community biodiversity observations | https://www.inaturalist.org |

---

## Property and Land Use Data

| Source | Coverage | Data Types | URL |
|--------|----------|------------|-----|
| County Assessor / Tax Records | US (by county) | Parcels, ownership, assessed value, building data | [varies by county] |
| Regrid (formerly Loveland) | US | Nationwide parcel data (commercial) | https://regrid.com |
| Zillow Research Data | US | Home values, rents, market indices | https://www.zillow.com/research/data |
| CoStar (commercial) | US | Commercial property data (subscription) | https://www.costar.com |
| Realtor.com Research | US | Listing data, market trends | https://www.realtor.com/research |
| Land Registry | UK | Property sales, ownership | https://www.gov.uk/government/organisations/land-registry |

---

## Noise and Acoustic Data

| Source | Coverage | Data Types | URL |
|--------|----------|------------|-----|
| US DOT National Transportation Noise Map | US | Modeled road and aviation noise | https://maps.dot.gov/BTS/NationalTransportationNoiseMap |
| FAA Airport Noise | US | Airport noise contours (DNL) | https://www.faa.gov/noise |
| European Noise Directive Maps | EU | Strategic noise maps for agglomerations | [varies by member state] |
| NoiseModelling (open source) | Any | Open-source noise modeling tool | https://noise-planet.org/noisemodelling.html |

---

## Heritage and Cultural Resources

| Source | Coverage | Data Types | URL |
|--------|----------|------------|-----|
| National Register of Historic Places | US | Listed properties and districts | https://www.nps.gov/subjects/nationalregister |
| National Park Service CRGIS | US | Cultural resource GIS data | https://www.nps.gov/crgis |
| SHPO Databases (by state) | US | State-level historic resource inventories | [varies by state] |
| Historic England | England | Listed buildings, scheduled monuments | https://historicengland.org.uk/listing/the-list |
| UNESCO World Heritage List | Global | World Heritage sites | https://whc.unesco.org |
| Native Land Digital | Global | Indigenous territories, treaties, languages | https://native-land.ca |

---

## Analysis Tools (Free and Open Source)

### GIS and Mapping

| Tool | Purpose | URL |
|------|---------|-----|
| QGIS | Full-featured desktop GIS (free, open source) | https://qgis.org |
| Google Earth Pro | 3D globe, historical imagery, measurement | https://earth.google.com |
| Google Earth Engine | Cloud-based geospatial analysis (free for research) | https://earthengine.google.com |
| Mapbox | Web mapping, geocoding, routing APIs | https://www.mapbox.com |
| Kepler.gl | Open-source large-scale data visualization | https://kepler.gl |
| Felt | Collaborative web mapping | https://felt.com |

### Transportation Analysis

| Tool | Purpose | URL |
|------|---------|-----|
| OpenTripPlanner | Multimodal trip planning and isochrone generation | https://www.opentripplanner.org |
| Valhalla | Open-source routing and isochrone engine | https://github.com/valhalla/valhalla |
| A/B Street | Open-source traffic simulation | https://abstreet.org |
| SUMO | Open-source traffic simulation | https://sumo.dlr.de |

### Environmental Analysis

| Tool | Purpose | URL |
|------|---------|-----|
| Ladybug Tools | Environmental analysis for Grasshopper/Rhino | https://www.ladybug.tools |
| EnergyPlus | Building energy simulation | https://energyplus.net |
| DIVA for Rhino | Daylighting and energy analysis | https://www.solemma.com |
| SunCalc | Sun position calculator (web) | https://www.suncalc.org |
| Windy.com | Real-time wind and weather visualization | https://www.windy.com |

### Data Processing

| Tool | Purpose | URL |
|------|---------|-----|
| Python (GeoPandas, Rasterio, Shapely) | Geospatial data processing | https://geopandas.org |
| R (sf, terra, tmap) | Statistical and spatial analysis | https://r-spatial.org |
| DeckGL | Large-scale data visualization for the web | https://deck.gl |
| Turf.js | Geospatial analysis in JavaScript | https://turfjs.org |

---

## API References for Programmatic Access

### Geospatial APIs

| API | Purpose | Auth | Rate Limit | Documentation |
|-----|---------|------|------------|---------------|
| OpenStreetMap Overpass API | Query OSM data by area/tag | None | Fair use | https://wiki.openstreetmap.org/wiki/Overpass_API |
| Mapbox APIs | Geocoding, routing, isochrones, static maps | API key | 100K/month free | https://docs.mapbox.com |
| Google Maps Platform | Geocoding, directions, places, elevation | API key | $200/month free credit | https://developers.google.com/maps |
| US Census Geocoder | Address geocoding, geography lookup | None | Reasonable use | https://geocoding.geo.census.gov |
| US Census Data API | Demographic and economic data | API key | No hard limit | https://www.census.gov/data/developers.html |

### Environmental APIs

| API | Purpose | Auth | Documentation |
|-----|---------|------|---------------|
| NOAA Web Services | Weather data, forecasts, alerts | None | https://www.weather.gov/documentation/services-web-api |
| EPA ECHO API | Facility compliance, air emissions, water discharge | None | https://echo.epa.gov/tools/web-services |
| OpenWeatherMap | Current weather, forecasts, historical | API key | https://openweathermap.org/api |
| AirVisual API | Air quality data, forecasts | API key | https://www.iqair.com/air-pollution-data-api |
| USGS Water Services | Stream flow, groundwater levels | None | https://waterservices.usgs.gov |

### Transportation APIs

| API | Purpose | Auth | Documentation |
|-----|---------|------|---------------|
| Transitland API | Transit routes, stops, schedules globally | API key | https://www.transit.land/documentation |
| OpenTripPlanner API | Multimodal routing and isochrones | Self-hosted | https://docs.opentripplanner.org |
| Walk Score API | Walk, Transit, and Bike Score | API key | https://www.walkscore.com/professional/api.php |
| HERE Routing API | Multimodal routing, isochrones, traffic | API key | https://developer.here.com |

### Property and Land Use APIs

| API | Purpose | Auth | Documentation |
|-----|---------|------|---------------|
| Regrid API | Parcel data, ownership, zoning | API key (paid) | https://regrid.com/api |
| Zillow API | Home values, market data | API key | https://www.zillow.com/howto/api/APIOverview.htm |
| OpenAddresses | Address point data globally | None | https://openaddresses.io |

---

## Data Collection Checklist

Before beginning analysis, use this checklist to identify available data for
the project location:

- [ ] DEM / Topographic data (resolution: ___)
- [ ] Flood zone maps (source: ___)
- [ ] Soil data (source: ___)
- [ ] Aerial/satellite imagery (date: ___, resolution: ___)
- [ ] Census / demographic data (year: ___, geography level: ___)
- [ ] Traffic counts (source: ___, date: ___)
- [ ] Transit schedules / GTFS (agency: ___)
- [ ] Zoning map and ordinance (source: ___)
- [ ] Parcel / cadastral data (source: ___)
- [ ] Building footprints with heights (source: ___)
- [ ] Heritage register data (source: ___)
- [ ] Utility maps (water: ___, sewer: ___, electric: ___, gas: ___)
- [ ] Climate / weather data (station: ___, distance: ___ km)
- [ ] Wind rose data (station: ___, years of record: ___)
- [ ] Noise data / traffic noise model (source: ___)
- [ ] Air quality monitoring (station: ___, distance: ___ km)
- [ ] Property sales / rental data (source: ___)
- [ ] Development pipeline / permit data (source: ___)
