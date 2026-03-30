# Modern Genset Panel V3

## Overview
A single-page HTML dashboard for monitoring and controlling a Medium Voltage (MV) Genset (generator set). The UI displays real-time engine data, diagnostics, alarms, control modes, and tag data.

## Project Structure
- `modern-genset-panel-v3.html` — The entire application in a single self-contained HTML file
- `server.py` — Simple Python HTTP server that serves the HTML file on port 5000

## Tech Stack
- Pure HTML/CSS/JavaScript (no build system)
- Tailwind CSS (via CDN)
- Font Awesome icons (via CDN)

## Running the App
The app is served via a Python HTTP server:
```
python server.py
```
Listens on `0.0.0.0:5000`.

## Deployment
Configured as a static site deployment with the root directory as the public directory.
