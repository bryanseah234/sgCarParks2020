# PRD: sgCarParks2020

## Overview
A Python Flask web app that helps Singapore residents find the nearest HDB car park to their current location using SVY21 coordinate input. Loads data from an official HDB car park CSV, computes Euclidean distance to each car park, and returns the nearest match. Built as a capstone/learning project.

## Goals
- Load and parse the official HDB car park information CSV
- Accept SVY21 (x, y) coordinates from the user
- Find the nearest car park using Euclidean distance
- Serve results via a Flask web interface
- Return car park number and address

## Non-Goals
- Real-time availability data (does not use HDB real-time API)
- GPS/geolocation auto-detection
- Multiple nearby car parks (returns only the single nearest)
- Mobile app or native GPS integration
- Routing or directions

## User Stories
- As a driver, I want to find the nearest HDB car park by entering my current SVY21 coordinates.
- As a student, I want to build a location-based search using CSV data and Flask.

## Tech Stack
- **Language**: Python 3.x
- **Framework**: Flask
- **Libraries**: `math` (stdlib), `csv parsing` (stdlib)
- **Data**: `hdb-carpark-information.csv` (official HDB open data)

## Architecture
```
sgCarParks2020/
├── main.py                      # Flask app + all business logic
├── hdb-carpark-information.csv  # HDB open data (included in repo)
├── templates/
│   ├── index.html               # Home page with coordinate input form
│   └── search.html              # Results page
└── static/                      # CSS/JS assets
```

**Functions:**
- `store()` → parses CSV into list of dicts
- `calculate(x1, y1, x0, y0)` → Euclidean distance
- `input_coords(x, y)` → adds `distance` field to each car park dict
- `sortByDistance(x, y)` → insertion sort on `carpark_data` list by distance
- `nearestCarpark(x, y)` → returns `(car_park_no, address)` of nearest

**Routes:**
- `GET /` → `index.html`
- `GET /search?xcoords=&ycoords=` → finds nearest and renders `search.html`

## Features (detailed)

### CSV Parsing
- Reads `hdb-carpark-information.csv` line by line
- Extracts: `car_park_no`, `address`, `x_coord`, `y_coord`, `car_park_type`, `type_of_parking_system`, `short_term_parking`, `free_parking`, `night_parking`, `car_park_decks`, `gantry_height`, `car_park_basement`
- All values stored as strings (coordinates converted to float at calculation time)

### Distance Search
- Euclidean distance in SVY21 metre units
- Insertion sort (O(n²)) to sort all car parks by distance
- Returns car park number and address of index 0 (nearest)

### Security Headers
```python
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
Cache-Control: no-cache, no-store, must-revalidate
```

## Data / Config
| File | Description |
|------|-------------|
| `hdb-carpark-information.csv` | Source: data.gov.sg; 2000+ car parks with SVY21 coordinates |

## Deployment / Run
```bash
pip install flask
python main.py
# open http://localhost:5000
# Enter SVY21 x,y coordinates (e.g. 28092, 29574 for Toa Payoh)
```

## Constraints & Notes
- **SVY21 coordinates**: Singapore's local projection system, not GPS lat/lng; typical range x: 2000–48000, y: 18000–50000
- **Euclidean ≠ geodesic**: uses straight-line distance, not walking/driving distance
- **Mutable global state**: `carpark_data` is modified in place by `sortByDistance` — not thread-safe; concurrent requests will corrupt results
- **Performance**: insertion sort on 2000+ records is fine for a single-user local app
- **Data freshness**: CSV is a static snapshot; HDB may have added/closed car parks since download
