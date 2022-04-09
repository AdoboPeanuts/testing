import streamlit as st
from opensea import OpenseaAPI
from opensea import utils
import pandas as pd


#Streamlit UI
st.sidebar.header("Sort and Filter")
asset_categories = st.sidebar.selectbox("Assets", ['NFT', 'Cryptocurrencies'])
st.header(f"Crypto API Tracker - {asset_categories}")


st.sidebar.selectbox("Filters", ['Statistics', 'Easter Egg :)', 'Compare'])


#Opensea API Code
opensea_api = OpenseaAPI(apikey="7913a9c0377249d2998900d7ce6d38b3")
opensea_api


#NFT Assets 

if asset_categories == 'NFT': 
    #User input Code
    st.subheader('Collection Contract Address')
    user_input = st.text_input('What NFT Contract Address would you like to explore? ')  
    user_input_as_str = str(user_input)
    #Contract Data
    if len(user_input_as_str) > 1:
        contract_data = opensea_api.contract(asset_contract_address = user_input)

        description = contract_data['collection']['description']

        date_of_creation = contract_data['collection']['created_date']

        discord = contract_data['collection']['discord_url']

        website = contract_data['collection']['external_url']

        name = contract_data['collection']['name']
        name_cap = name.title()

        telegram = contract_data['collection']['telegram_url']

        twitter = contract_data['collection']['twitter_username']

        instagram = contract_data['collection']['instagram_username']

        address = contract_data['address']
        #Project Description
        st.subheader(f"{name}")
        st.subheader('Project Summary:')
        st.write(f'{description}')
        #Collection statistics
        def pull_nft_stats(user_input):
            contract = opensea_api.contract(asset_contract_address = user_input)
            name = contract['collection']['slug']
            nft_stats = opensea_api.collection_stats(collection_slug = name)
            nft_stats_df = pd.DataFrame.from_dict(nft_stats)
            nft_stats_df = nft_stats_df[['stats']].round(decimals = 2)
            return(nft_stats_df)
        st.subheader('Collection Statistics')
        st.write(pull_nft_stats(user_input))
        #Project Socials
        def get_socials(name_cap, telegram, twitter, instagram, discord, website):
            st.subheader(f'{name_cap} Socials')
            st.write(f'Website: {website}')
            st.write(f'Discord: {discord}')
            st.write(f'Twitter: {twitter}')
            st.write(f'Telegram: {telegram}')
            st.write(f'Instagram: {instagram}')
        st.write(get_socials(name_cap, telegram, twitter, instagram, discord, website))