# Cheap-Flight-Alert-Py

This script tracks flight prices for specified destinations and sends email notifications when prices drop below a certain threshold.

## Overview
The Flight Price Tracker consists of three main components:
1. `data_manager`: Handles the retrieval and update of data from a Google Sheet containing destination information.
2. `flight_search`: Searches for flight prices using the Skyscanner Flight Search API.
3. `notification_manager`: Manages the sending of email notifications to users.

## Setup
1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
