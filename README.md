# Earth Fireball Impacts Visualization

This project visualizes NASA fireball data (detected meteor events) from 2010 to 2025 using interactive maps and data analysis. It creates both an interactive web map showing impact locations and a bar chart of the highest energy events.

## Features

- Interactive web map showing fireball locations worldwide
- Circle markers sized by impact energy
- Tooltips showing date and location information
- Analysis of top 20 highest energy fireball events
- Data visualization using Folium and Seaborn

## Requirements

- Python 3.x
- Required packages:
  - nasapy (wrapper for NASA API)
  - pandas
  - numpy
  - folium
  - matplotlib
  - seaborn
 
## Interactive Web Map

## Bar chart
<img width="2560" height="1080" alt="Screenshot 2025-11-07 at 3 32 20 PM" src="https://github.com/user-attachments/assets/8b7b9e31-ff3a-447a-a9bc-57394ad35f91" />

## Installation
<img width="2560" height="1080" alt="Screenshot 2025-11-07 at 3 40 56 PM" src="https://github.com/user-attachments/assets/de61a4a7-a7d7-42e7-ab3f-aea03ea10f43" />

```bash
pip install nasapy pandas numpy folium matplotlib seaborn
```

## Usage

1. Run the script:
```bash
python fireballs.py
```

2. Two outputs will be generated:
   - `fireball_map.html`: An interactive web map showing all fireball events
   - A matplotlib window showing the top 20 highest energy fireball events

## Data Source

The data is fetched from NASA's fireball database using the `nasapy` package. It includes meteor events from 2010-01-01 to 2025-10-31.

## Visualization Details

- **Map**: Each circle represents a fireball event
  - Size: Proportional to the energy of the impact
  - Color: Red fill with black outline
  - Tooltip: Shows date and geographical coordinates

- **Bar Chart**: Shows the top 20 fireball events by energy
  - X-axis: Date of event
  - Y-axis: Energy value
  - Title: "Top 20 Fireball Energy Values by Date"
