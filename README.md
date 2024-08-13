# Crypto Coin Ranking Application

This repository contains my research on cryptocurrency coin pumping. The research has been implemented into a user-friendly, GUI-based application that allows users to explore and analyze the phenomenon of crypto coin pumping. The application can be run using the `main.py` script.

## Database Setup

Before using the application, make sure you have your own `crypto_db` SQL database. If you don't have one, you can create the database using the `create_database` function found in the `pull_price.ipynb` notebook.

## Usage

To run the application, use the following command:

```bash
cd gui
python main.py
```

## Application Overview

The application is organized into several key sections accessible from the side menu:

1. **Price Database Status:**
   - Displays the status of your crypto coin price database, indicating whether the data is up-to-date. Users can easily update the database using the "Update Database" button.

2. **Pumping Database:**
   - Contains the history of coin pumping activities, providing detailed information such as market, base price, latest price, and duration of the pump. The technical statistics derived from this data are used to train the machine learning model.

3. **Technical Statistics:**
   - Presents various technical indicators and statistics, such as the slope, adjusted slope, and Aroon indicator for different markets. These statistics are essential for predicting the coin ranking using the machine learning model.

4. **Coin Ranking:**
   - The core functionality of the application, where the trained machine learning model ranks cryptocurrencies based on the technical statistics and criteria set by the user.