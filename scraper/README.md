# Scraping transfer-, team-, and player-level data from transfermarkt.de

The script includes different levels of customisability. If you want all data use the following lines of code:
'''python
import scraper
seasons = [2019, 2020] # add all seasons that you are interested in
df = scraper.scrape_bundesliga_transfer_data(seasons)
scraper.create_output_df(df)
'''

For everyone that is only interested in specific party of the data, I split up the functionality.

**Be aware that the scraper takes several minutes per season**