import pandas as pd
import os
import streamlit as st
import numpy as np
import datetime as dt
from twelvedata import TDClient
from opensea import OpenseaAPI
from opensea import utils
from TweleveDataMCForecast import MCSimulation 




#Streamlit UI
st.sidebar.header("Sort and Filter")
asset_categories = st.sidebar.selectbox("Assets", ['NFT', 'Cryptocurrencies'])
st.header(f"Crypto API Tracker - {asset_categories}")




#Opensea API Key
opensea_api = OpenseaAPI(apikey="7913a9c0377249d2998900d7ce6d38b3")


#Twelve Data API Key
td = TDClient(apikey="d1d0c43b0fb445518d1435c2b90c9cdc") 


#Defined Functions

#Pull NFT Stats Function
def pull_nft_stats(user_input):
    contract = opensea_api.contract(asset_contract_address = user_input)
    name = contract['collection']['slug']
    nft_stats = opensea_api.collection_stats(collection_slug = name)
    nft_stats_df = pd.DataFrame.from_dict(nft_stats)
    nft_stats_df = nft_stats_df[['stats']].round(decimals = 2)
    return(nft_stats_df)

#Pull Socials Function
def get_socials(name, telegram, twitter, instagram, discord, website):
    st.subheader(f'{name} Socials')
    st.write(f'Website: {website}')
    st.write(f'Discord: {discord}')
    st.write(f'Twitter: {twitter}')
    st.write(f'Telegram: {telegram}')
    st.write(f'Instagram: {instagram}')

#NFT Assets

#Main NFT Code
if asset_categories == 'NFT':
    
    filters = st.sidebar.selectbox("Filters", ['Statistics', 'Compare'])
    
    #Filter Selection
    #Statistics Filter
    if filters == 'Statistics':
        #User input Code
        st.subheader('Collection Contract Address')
        user_input_stats = str(st.text_input('What NFT Contract Address would you like to explore? ')) 
        
        #Check for user input
        if len(user_input_stats) > 1:
            
             #Contract Data
        
            contract_data = opensea_api.contract(asset_contract_address = user_input_stats)
            description = contract_data['collection']['description']
            date_of_creation = contract_data['collection']['created_date']
            discord = contract_data['collection']['discord_url']
            website = contract_data['collection']['external_url']
            name = (contract_data['collection']['name']).title()
            telegram = contract_data['collection']['telegram_url']
            twitter = contract_data['collection']['twitter_username']
            instagram = contract_data['collection']['instagram_username']
            address = contract_data['address']
            #Project Description
            st.subheader(f"{name}")
            st.subheader('Project Summary:')
            st.write(f'{description}')
            
            #Collection statistics
            st.subheader('Collection Statistics')
            user_input = user_input_stats
            st.write(pull_nft_stats(user_input))
            
            #Project Socials
            st.write(get_socials(name, telegram, twitter, instagram, discord, website))

        #Compare Filter
    elif filters == 'Compare':
        st.subheader("Comparing NFT Collections")
        user_input_compare_first = str(st.text_input("What is the first NFT collection you would like to compare?"))
        response_2 = ''
        user_input_compare_second = str(st.text_input("What is the second NFT collection you would like to compare?", key = response_2))
        
        #Checking for user input
        if len(user_input_compare_first) > 1:
            if len(user_input_compare_second) > 1:

                #Contract Data
                #First set of contract data
                contract_data_first = opensea_api.contract(asset_contract_address = user_input_compare_first)
                description1 = contract_data_first['collection']['description']
                date_of_creation1 = contract_data_first['collection']['created_date']
                discord1 = contract_data_first['collection']['discord_url']
                website1 = contract_data_first['collection']['external_url']
                name1 = (contract_data_first['collection']['name']).title()
                telegram1 = contract_data_first['collection']['telegram_url']
                twitter1 = contract_data_first['collection']['twitter_username']
                instagram1 = contract_data_first['collection']['instagram_username']
                address1 = contract_data_first['address']

                #Second set of Contract Data
                contract_data_second = opensea_api.contract(asset_contract_address = user_input_compare_second)
                description2 = contract_data_second['collection']['description']
                date_of_creation2 = contract_data_second['collection']['created_date']
                discord2 = contract_data_second['collection']['discord_url']
                website2 = contract_data_second['collection']['external_url']
                name2 = (contract_data_second['collection']['name']).title()
                telegram2 = contract_data_second['collection']['telegram_url']
                twitter2 = contract_data_second['collection']['twitter_username']
                instagram2 = contract_data_second['collection']['instagram_username']
                address2 = contract_data_second['address']

                #Creating two Columns for comparison
                col1, col2 = st.columns(2)

                #Defining the two columns
                with col1:
                    #Project Desciption
                    st.subheader(f'{name1}')
                    st.subheader('Project Summary')
                    st.write(f'{description1}')

                    #Collection 1 Statistics
                    st.subheader(f'{name1} Statistics')
                    user_input = user_input_compare_first
                    st.write(pull_nft_stats(user_input))
                
                with col2:
                    #Project Desciption
                    st.subheader(f'{name2}')
                    st.subheader('Project Summary')
                    st.write(f'{description2}')

                    #Collection 1 Statistics
                    st.subheader(f'{name2} Statistics')
                    user_input = user_input_compare_second
                    st.write(pull_nft_stats(user_input))


#Cryptocurrency assets

#Code for Crypto DataFrame
#Defined Crypto Functions

def create_ts(user_inputc):
            ts = td.time_series(
                symbol = user_inputc,
                exchange = "Binance",
                interval = '1day',
                outputsize=5000,
                start_date = '2020-01-15',
                end_date = '2022-01-15',
                timezone="America/New_York",
                )
            crypto_df = ts.as_pandas()
            crypto_df = crypto_df.round(2)
            return crypto_df


#Cryptocurrency asset code
if asset_categories == "Cryptocurrencies":
    
    #User imput code
    st.subheader('CryptoCurrency Ticker')
    user_inputc = st.text_input("What Crypto Currency Trading Pair are you looking for?")
    st.write("Ex: BTC/USD, ETH/USD")

    if len(user_inputc) > 1:
        
        
        #Executing the Crypto DataFrame
        st.write(create_ts(user_inputc))


        # Percentage return global code  
        st.subheader('Percentage Change')

        # Define Data Frame
        crypto_df_new = create_ts(user_inputc)
        crypto_df_close = crypto_df_new.drop(columns= ['open','high','low'])
        pct_change_raw = crypto_df_close.pct_change()
        
        
        # Rename percentage change columns 
        pct_change= pct_change_raw.rename(columns= {'close':'pct_daily_return'}).dropna().copy()
        st.write(pct_change)  

        # Create sharpe ratio subheader
        st.subheader ('Sharpe Ratio') 
        
        # Calculate annualized Standard Deviation
        std_annual = (pct_change.std()*np.sqrt(252))
        
        # Calculate annualized Mean Return
        mean_returns_annual = (pct_change.mean()*252)
        
        # Calculate annualized Sharpe Ratio
        sharpe_ratio = (mean_returns_annual/std_annual)
        st.write(sharpe_ratio)

        # Create Monte Carlo Simulation subheader
        st.subheader ('Monte Carlo Simulation') 
        
        #BTC and ETH Dataframe for MCS
        #BTC DataFrame
        btc = td.time_series(
                symbol = 'BTC/USD',
                exchange = "Binance",
                interval = '1day',
                outputsize=5000,
                start_date = '2020-01-15',
                end_date = '2022-01-15',
                timezone="America/New_York",
                )
        btc_df = btc.as_pandas()
        btc_df = btc_df.round(2)
            
        #ETH DataFrame
        eth = td.time_series(
                symbol = 'ETH/USD',
                exchange = "Binance",
                interval = '1day',
                outputsize=5000,
                start_date = '2020-01-15',
                end_date = '2022-01-15',
                timezone="America/New_York",
                )
        eth_df = eth.as_pandas()
        eth_df = eth_df.round(2)

        # Configuring a Monte Carlo simulation to forecast 30 years cumulative returns
        

        MC_thirtyyear = MCSimulation(
            portfolio_data = crypto_df_close,
            weights = [.50,.50],
            num_simulation = 500,
            num_trading_days = 252*30
        )
        
        # Running a Monte Carlo simulation to forecast 30 years cumulative returns
        MC_equal_wght= MC_thirtyyear.calc_cumulative_return()
        st.write(MC_equal_wght) 
        





