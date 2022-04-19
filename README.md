# Project-1-University-of-Toronto

## Background
Our project is to create  a user-friendly NFT and cryptocurrency dashboard, that will allow users to  make investment decisions by predicting the performance of the underlying asset classes over time. Our project focuses specifically on the field of trading, as it seeks to inform the user’s future trading activity and decisions.

The platform will consist of historical and real time (last 15 mins) data, complete with relevant line charts, bar charts and other illustrations. We’ll also obtain the bulk of our data from OpenSea and Twelve Data.

### Files:
CustomModule.py

Project_1_Final.py

MCForecastTools.py 

### Data Preparation

### Custom Module - Importing API from Twelve Data to enable us to build the crypto data frames and importing APIs from Opensea to allow us to collect NFT data for this project.

##### #Opensea API Key - setting 
opensea_api = OpenseaAPI(apikey="7913a9c0377249d2998900d7ce6d38b3")

##### #Twelve Data API Key
td = TDClient(apikey="d1d0c43b0fb445518d1435c2b90c9cdc") 

##### #Cryptocurrency DF Function
Creating the cyptocurrency dataframe functions using the following parameters; time series, symbol, exchange, interval, outputsize, start date, end date and timezone.

##### #NFT DF Function
Creating the NFT dataframe functions to pull NFT statistics from OpenSea using the Asset Contract Address.

##### #NFT Socials Function
def get_socials(name, telegram, twitter, instagram, discord, website):
         
##### #Cryptocurrency Library
Setting up the cryptocurrency library for the sample seven cryptocurrencies selected below for this project using the data frame functions listed above.

BTC , ETH , XRP , BNB , SOL , ADA , LUNA 
