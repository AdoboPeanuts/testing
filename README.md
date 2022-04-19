# Project-1-University-of-Toronto

## Background
Our project is to create  a user-friendly NFT and cryptocurrency dashboard, that will allow users to  make investment decisions by predicting the performance of the underlying asset classes over time. Our project focuses specifically on the field of trading, as it seeks to inform the user’s future trading activity and decisions.

The platform will consist of historical and real time (last 15 mins) data, complete with relevant line charts, bar charts and other illustrations. We’ll also obtain the bulk of our data from OpenSea and Twelve Data.

#### Files:
CustomModule.py

MCForecastTools.py 

Project_1_Final.py

### Data Preparation

### Custom Module - Importing API from Twelve Data to enable us to build the crypto dataframes and importing APIs from Opensea to allow us collect NFT data for this project.

#### # Opensea API Key - setting 
opensea_api = OpenseaAPI(apikey="7913a9c0377249d2998900d7ce6d38b3")

#### # Twelve Data API Key
td = TDClient(apikey="d1d0c43b0fb445518d1435c2b90c9cdc") 

#### # Cryptocurrency DF Function
Creating the cyptocurrency dataframe functions using the following parameters; time series, symbol, exchange, interval, outputsize, start date, end date and timezone.

#### # NFT DF Function
Creating the NFT dataframe functions to pull NFT statistics from OpenSea using the Asset Contract Address.

#### # NFT Socials Function
def get_socials(name, telegram, twitter, instagram, discord, website):
         
#### # Cryptocurrency Library
Setting up the cryptocurrency library for the sample seven cryptocurrencies selected below for this project.

BTC , ETH , XRP , BNB , SOL , ADA , LUNA 

### Setting up the user interface for the project output on Streamlit. The codes are contained in the file titled Project_1_Final.py

* Importing relevant libraries and dependencies (CustomModule and MCForecastTools).

  import pandas as pd

  import os

  import streamlit as st

  import numpy as np

  import datetime as dt

  from twelvedata import TDClient

  from opensea import OpenseaAPI

  from opensea import utils

  import CustomModule as cm

  from MCForecastTools import MCSimulation

#### # Streamlit UI
Creating the side bar to filter asset categories for "NFT" and "Cryptocurrencies" to give users a drop down to select either "NFT" and "Cryptocurrencies"

Creating the header as "Cryto API Tracker"

#### # Opensea API Key
The Opensea API key is to pull NFT statistics from OpenSea as stated in the custom module.

opensea_api = OpenseaAPI(apikey="7913a9c0377249d2998900d7ce6d38b3")

#### # Twelve Data API Key
The Twelve Data API key is to allow us access to cyrptocurrency data frames from Twelve Data as stated in the custom module.

td = TDClient(apikey="d1d0c43b0fb445518d1435c2b90c9cdc")
