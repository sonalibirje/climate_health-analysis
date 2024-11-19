# Climate-Driven Early Warning System for Chronic Disease Exacerbations

## Overview
This project analyzes the relationship between climate factors (e.g., air quality, temperature, humidity, extreme weather events) and the exacerbation of chronic diseases (e.g., asthma, cardiovascular diseases, diabetes). It integrates climate, health, and demographic data to provide predictive insights and early warnings for at-risk populations across regions such as Europe, Asia, and North America over the last 15 years.

The system combines structured data (stored in PostgreSQL) and semi-structured data (stored in MongoDB) to build a robust predictive model and interactive visualizations.

---

## Objectives
- **Data Integration**: Combine structured (health, demographics) and semi-structured (climate) data from multiple sources.
- **Predictive Analysis**: Develop machine learning models to predict chronic disease exacerbations based on climate conditions.
- **Visualization**: Create interactive dashboards to communicate insights to both technical and non-technical audiences.
- **Real-Time Alerts**: Provide early warnings for regions and demographics at high risk of health impacts.

---

## Data Sources
### Climate Data
- **Air Quality**: [OpenAQ API](https://openaq.org/#/) (PM2.5, PM10, NO2, CO, O3)
- **Temperature & Humidity**: [OpenWeatherMap API](https://openweathermap.org/api), [NOAA Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/)
- **Extreme Weather Events**: [NASA EarthData](https://earthdata.nasa.gov/), [ReliefWeb](https://reliefweb.int/)

### Health Data
- **Chronic Disease Indicators**: [CDC Chronic Disease Indicators](https://www.cdc.gov/cdi/index.html), [WHO Global Health Observatory](https://www.who.int/data)
- **Hospitalization and Mortality Rates**: [Eurostat](https://ec.europa.eu/eurostat)

### Demographics
- **Population & Income Levels**: [World Bank Open Data](https://data.worldbank.org/)
- **Healthcare Access**: [UNICEF Data](https://data.unicef.org/)

---