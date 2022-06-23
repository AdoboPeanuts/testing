# Background 
In project 1, we created a user-friendly NFT and Cryptocurrency Dashboard, which allowed users to make investment decisions by predicting the performance of the underlying asset classes over time. Project 1 focused specifically on the field of trading, as it seeks to inform the user’s future trading activity and decisions.
Our dashboard consists of a User Interface(UI) hosted by Streamlit, comprised of historical and very recent data, complete with relevant line charts, bar charts and other illustrations. Please see the file FinalProject.py for our code.

So the objective of project 2, is how we can use Sentiment Analysis to predict the closing prices of Crypto Currencies. Specifically we wanted to see the impact that twitter tweets have on Cryptocurrencies. For the scope of this project we wanted to mainly focus on doing a Sentiment Analysis first on Crypto, before we do it on NFTs (due to time)

# Finding Data 
In the past project we used API keys, to source the bulk of our input data from OpenSea for NFTs, and TwelveData for cryptocurrencies. Further, we prepare two input modules, namely CustomModule.py and MCForecastTools.py where, using Python and Pandas.

In project 2, due to time, we focused our attention to three main cryptos, Bitcoin, Etheuruem, and Dodge Coin. We pulled the data on these cryptos from Kaggle. Then we obtained the Twitter API access key to obtain the data from Twitter to analyze the tweets.
## CustomModule.py file (Project 1)
In this file we import the necessary libraries and dependencies from pandas, streamlit, numpy, TwelveData, OpenSea and the MCForecastTools.py module. 
We begin by inputting the OpenSea and TwelveData API keys. We subsequently define the Cryptocurrency function ‘create_ts(user_inputc, td)’ that will create a time series from TwelveData using Binance as an exchange over a 5 year date range. We follow up by converting the time series to  a chronological Pandas dataframe by using TwelveData’s  ‘as_pandas()’ function. 
For NFTs we define a function to pull NFT statistics (i.e., contract name, statistics, and social media handles) from OpenSea and different social media channels. We complete this function by converting our NFT statistics into a Pandas dataframe. 
We complete the Custom Module, by creating functions (similar to the generic Cryptocurrency function above) that will retrieve data for Bitcoin, Ethereum, Ripple, Binance, Solana, Cardano, and Terra  over the same date range discussed above, and run the module. 
## MCForecastTools.py (Project 1)
Using the MCForecastTools.py file from our API module, we import dependencies from TwelveData and CustomModule that relates to our Monte Carlo Simulation. Leaving most of the code unchanged, we substitute the word stocks for ‘cryptocurrencies,’ and run the module. 

# Data Cleanup & Analysis (Project 1)
In the ProjectFinal.py module, we import our libraries and dependencies from Pandas, Streamlit, Numpy, OpenSea, CustomModule and MCForecastTools. 

## Streamlit UI (Project 1)
We configure a sidebar for our Streamlit UI that allows the user to sort and filter assets between NFTs and Cryptocurrencies. We also create a header in the main section of the UI called “Crypto API Tracker.”  together with an input box. 

### API Keys
We inserted the OpenSea and TwelveData keys to pull the required data in Project 1.
We inserted the Twitter Api key to pull out the tweets from Twitter for Project 2
### NFT Assets(Project 1)
Using an if function for the Statistics dropdown option, we create an input text for the input box described above, that prompts the user to enter the NFT contract address they wish to explore. 
Using a nested if function, we write that, should the NFT contract input statistics be valid, OpenSea will display the specific NFT contract data, date created, social media addresses, and project summary in Streamlit. 
Otherwise, we use a nested if function, to determine that, should the user choose ‘Compare’ from the dropdown list, they will be prompted to input 2 NFT contract addresses, which will return the data (contract data, date created, social media addresses, and project summary) from the nested if function for the two NFT contracts being compared. This data will appear in side-by-side columns. 

### Cryptocurrency Assets: General(Project 1) 
We create an if function to determine that, if the user chooses Cryptocurrencies (instead of NFTs) from the sidebar dropdown list, the input box in the main section of the UI will prompt the user to input the name of a specific cryptocurrency (always on a per USD basis). 
We create a nested if function to determine that, if the user  enters a cryptocurrency in the box above, a new dataframe called ‘Percent Change’ will be created, which denotes the daily percentage change of the selected cryptocurrency. We further clean this data frame by dropping unwanted columns, and by using a dictionary to rename the ‘close’ column to ‘daily_return.’ Finally, we prepare a line chart of daily returns for the selected cryptocurrency using Streamlit’s ‘line_chart’ command. 

We continue our analysis by writing the code for our Sharpe Ratio, where we create variables for Standard Deviation and Mean Returns. Similarly, we prepare the code for our cumulative returns and illustrate our findings in a  bar (Sharpe Ratio) and line chart (Cumulative Returns). We find that, over a two-year period, Terra (Luna), Solana, and Binance have all enjoyed superior Sharpe Ratios to Bitcoin and Ethereum, thereby providing a greater return to risk profile. 

### Cryptocurrency Assets: Monte Carlo Simulations(Project 1)
In this section, we use the MCForecastTools.py module to prepare forecasts over a 5, 10 and 20 year period, and illustrate our results in the cumulative returns and distribution plots. We highlight that the results of our 20 year simulation cannot be relied upon, given the extremely volatile returns  upper Confidence interval results. We conclude that, over a five-year period a portfolio comprised of Bitcoin(70%) and Ethereum (30%) will likely result in a loss of almost half the investor’s initial capital, or gain a few times the initial investment, thus illustrating the very volatile nature of a cryptocurrency portfolio.

### Scope & Limitations (Project 2)
One of the main issues we encountered was that Twitter API has essential access only to Twitter API, which obviously limited the data that we could be
pulling out and analyzing.
To not complete things and  mitigate the aforementioned API data, we obtained our Crypto data (on Bitcoin, Ethereum, and Dodgecoin) from a source called Kaggle, which already had pre-pulled twitter API data for each of the respective digital currencies we ranthe SA model on.  

### Analysis (Project 2)

