import requests, re, time, random, os, glob, tqdm, pathlib
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from tqdm import tqdm_notebook

# global variables
periods = ['s', 'w']
start_url = 'https://www.transfermarkt.de/1-bundesliga/transfers/wettbewerb/L1/plus/?saison_id='
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
competitions_wo_pic = ['GRPL', 'ARGC', 'GBRP', 'SES', 'MARG']
twitter_list = []
facebook_list = []
instagram_list = []
homepage_list = []
player_stats_df = pd.DataFrame(columns=['season',
                                        'player_id',
                                        'competition_id',
                                        'matches',
                                        'goals',
                                        'assists',
                                        'yellow_cards',
                                        'yellow_red_cards',
                                        'red_cards',
                                        'goals_conceded',
                                        'clean_sheets',
                                        'minutes_played'
                                        ])

# helper funcitons
def safe_html_files(rood_path, file_path, url):
    '''
    creating path if not exist and than saving html files if not existant
    '''
    if os.path.isfile(file_path):
        pass
    else:
        resp = requests.get(url, headers=headers)
        time.sleep(random.random()+1.05)
        if resp.status_code != 200:
            print(f'URL "{url}" raised an error: {resp.status_code}')
        pathlib.Path(rood_path).mkdir(parents=True, exist_ok=True) 
        with open(file_path, 'w') as file:
            file.write(resp.text)

def extract_team_name_and_id(team_link):
    '''
    finding team name and id in team_links from transfermarkt.de
    '''
    regex_groups = re.search(r'\/(.*)\/transfers\/verein\/(.*)\/saison_id\/(.*)', team_link, re.M)
    team_name = regex_groups[1]
    team_id = regex_groups[2]
    return team_name, team_id

def find_receiving_teams(overview_soup):
    '''
    finding receiving team names and ids from transfer overviews
    '''
    receiving_team_names = []
    receiving_team_ids = []
    teams_soup = overview_soup.find_all('h2')
    for teams in teams_soup:
        team_link = teams.find('a', class_ = 'vereinprofil_tooltip')
        if team_link is not None:
            team_link = team_link.get("href")
            team_name, team_id = extract_team_name_and_id(team_link)
            receiving_team_names.append(team_name)
            receiving_team_ids.append(team_id)
    return receiving_team_names, receiving_team_ids

def create_list_of_receiving_teams(receiving_teams, transfers_per_team):
    '''
    creating a list of all receiving teams
    '''
    receiving_teams_n = []
    for i, team in enumerate(receiving_teams):
        for j in range(transfers_per_team[i]):
            receiving_teams_n.append(team)
    return receiving_teams_n

def find_giving_teams(giving_team_soup):
    '''
    creating a list if all giving team names and ids
    '''
    team_link = giving_team_soup.find('a').get('href')
    giving_team_name, giving_team_id = extract_team_name_and_id(team_link)
    return giving_team_name, giving_team_id

def get_table_value(rows, table_header):
    '''
    finding tables in soup object
    '''
    for row in rows:
        helpers = row.find_all(text=re.compile(table_header))
        if helpers is not None:
            for helper in helpers:
                return helper.find_next('td').get_text()

def lstrip_if_exist(var, char):
    '''
    left strip unwanted parts of a string if it exists
    '''
    if var is not None:
        if type(var) == str:
            return var.lstrip(char)
        else:
            return var
    else:
        return np.nan

def get_social_media_links(rows):
    '''
    extract socila media links from player overview soup
    '''
    twitter = np.nan
    facebook = np.nan
    instagram = np.nan
    homepage = np.nan
    for row in rows:
        helpers = row.find_all(text=re.compile('Social Media'))
        if helpers is not None:
            for helper in helpers:
                if helpers is not None:
                    all_as = helper.find_next('td').find_all('a')
                    for a in all_as:
                        if a.get('title') == 'Twitter':
                            twitter = a.get('href')
                        if a.get('title') == 'Facebook':
                            facebook = a.get('href')
                        if a.get('title') == 'Instagram':
                            instagram = a.get('href')
                        if a.get('title') == 'Offizielle Homepage':
                            homepage = a.get('href')
    twitter_list.append(twitter)
    facebook_list.append(facebook)
    instagram_list.append(instagram)
    homepage_list.append(homepage)
    return twitter_list, facebook_list, instagram_list, homepage_list

def find_secondary_positions(soup):
    '''
    finding players' secondary positions
    '''
    nebenpositionen = np.nan
    if soup.select('div[class*="nebenposition"]') is not None:
        for i in soup.select('div[class*="nebenposition"]'):
            nebenpositionen = i.get_text()
            nebenpositionen = nebenpositionen.replace('Nebenposition:', '').replace('\n', ' ').replace('\r', '')
    return nebenpositionen

def get_keeper_stats(stats, player_id, competitions, season):
    '''
    extracting keeper stats from player soup

    ATTENTION: fragile as this only applies to the leagues detected
    for this specific usage. Future transfers could need an update of
    the competitions_wo_pic list
    '''
    if any(x in competitions for x in competitions_wo_pic): 
        c = sum(el in competitions for el in competitions_wo_pic)
        stats = stats[0:len(competitions)*9+c]
    else:
        stats = stats[0:len(competitions)*9]
    i = 0
    for competition in competitions:
        if competition in competitions_wo_pic:
            stats.pop(i)
            stats[i] = competition
            temp_list = [season, player_id]
            temp_list.extend(stats[i:i+9])
            temp_list.insert(5, np.nan)
            player_stats_df.loc[len(player_stats_df)] = temp_list
            i += 9
        else:
            stats[i] = competition
            temp_list = [season, player_id]
            temp_list.extend(stats[i:i+9])
            temp_list.insert(5, np.nan)
            player_stats_df.loc[len(player_stats_df)] = temp_list
            i += 9
    return player_stats_df

def get_player_stats(stats, player_id, competitions, season):
    '''
    extracting player stats from player soup

    ATTENTION: fragile as this only applies to the leagues detected
    for this specific usage. Future transfers could need an update of
    the competitions_wo_pic list
    '''
    if any(x in competitions for x in competitions_wo_pic):
        c = sum(el in competitions for el in competitions_wo_pic)
        stats = stats[0:len(competitions)*8+c]
    else:
        stats = stats[0:len(competitions)*8]
    i = 0
    for competition in competitions:
        if competition in competitions_wo_pic:
            stats.pop(i)
            stats[i] = competition
            temp_list = [season, player_id]
            temp_list.extend(stats[i:i+8])
            temp_list[9:9] = [np.nan, np.nan]
            player_stats_df.loc[len(player_stats_df)] = temp_list
            i += 8
        else:    
            stats[i] = competition
            temp_list = [season, player_id]
            temp_list.extend(stats[i:i+8])
            temp_list[9:9] = [np.nan, np.nan]
            player_stats_df.loc[len(player_stats_df)] = temp_list
            i += 8
    return player_stats_df

def get_number_of_players(position, soup):
    '''
    counting the numer of players per position in teams soup
    '''
    players = 0
    player_tds = soup.find_all('td', class_ = f'zentriert rueckennummer bg_{position}')
    if player_tds is not None:
        for player_td in player_tds:
            players += 1
        return players
    else:
        return np.nan
    
def get_players_avg_age(position, soup):
    '''
    extracting the average age per position for each team
    '''
    players_age_soup = soup.find('td', class_ = f'bg_{position} ma_pos')
    if players_age_soup is not None:
        players_age = players_age_soup.find_next('td', class_ = 'zentriert').get_text()
        return players_age
    else:
        return np.nan

# ------------------------- main code -----------------------

def get_transfers_html(seasons):
    '''
    Scrapes all non-loan, external transfers from the Bundesliga from 
    transfermarkt.de for a given list of seasons and saves html files 
    to the hard drive

    Parameters
    ----------
    seasons: list of strings in the format ['20XX', '20XX']
    '''
    for season in tqdm_notebook(seasons):
        for period in periods:
            period_url = f'{start_url}{season}&s_w={period}&leihe=0&intern=0'
            rood_path = './data/raw/overview/'
            file_path = f'./data/raw/overview/{season}_{period}_overview.html'
            safe_html_files(rood_path, file_path, period_url)

def extract_transfer_data(seasons):
    '''
    Extracts transfer data from html files saved with 'get_transfers_html()'
    Returns a dataframe
    
    Parameters
    ----------
    seasons: list of strings in the format ['20XX', '20XX']
    '''
    player_links = []
    player_names = []
    leistungsdaten_links = []
    teams = []
    transfer_values = []
    player_ids = []
    transfers_per_team = []
    receiving_team_ids = []
    receiving_team_names = []
    season_list = []
    giving_team_ids = []
    giving_team_names = []
    period_list = []

    for season in seasons:
        for period in periods:
            path = f'./data/raw/overview/{season}_{period}_overview.html'
            html_file = open(path, 'r', encoding='utf-8')
            source_code = html_file.read()
            html_file.close()
            soup = BeautifulSoup(source_code, "html.parser")
            receiving_team_names_season, receiving_team_ids_season = find_receiving_teams(soup)
            receiving_team_names.extend(receiving_team_names_season)
            receiving_team_ids.extend(receiving_team_ids_season)
            for tag in soup.find_all(text=re.compile('Zugang')):
                giving_team_soups = tag.findParent('table').find_all('td',class_ ='no-border-links')
                for giving_team_soup in giving_team_soups:
                    giving_team_name, giving_team_id = find_giving_teams(giving_team_soup)
                    giving_team_names.append(giving_team_name)
                    giving_team_ids.append(giving_team_id)
                player_soup = tag.findParent('table').find_all('div',class_ ='di nowrap')
                i = 0
                for player in player_soup:
                    player_name = player.get_text()
                    player_names.append(player_name)
                    links = player.find_all('a')
                    i += 1

                    for link in links:
                        raw_link = link["href"]
                        player_link = f'https://www.transfermarkt.de{raw_link}'
                        player_links.append(player_link)
                        raw_link_parts = re.search(r'^.([^.]*)\/([^.]*)\/([^.]*)\/([^.]*).*$', raw_link, re.M)
                        leistungsdaten_link = f'https://www.transfermarkt.de/{raw_link_parts[1]}/leistungsdaten/spieler/{raw_link_parts[4]}/plus/0?saison={season-1}'
                        leistungsdaten_links.append(leistungsdaten_link)
                        player_id = raw_link_parts[4]
                        player_ids.append(player_id)
                        season_list.append(season)
                        period_list.append(period)
                
                transfers_per_team.append(i)
                transfer_value_soup = tag.findParent('table').find_all('td',class_ ='rechts')
                for transfer_value in transfer_value_soup:
                    transfer_value = transfer_value.get_text()
                    transfer_values.append(transfer_value)
                    
    receiving_team_ids_n = create_list_of_receiving_teams(receiving_team_ids, transfers_per_team)                
    receiving_team_names_n = create_list_of_receiving_teams(receiving_team_names, transfers_per_team) 

    transfer_values = transfer_values[1::2]

    i = 1
    while i < len(transfer_values)+1:
        transfer_values.insert(i, 'filler')
        giving_team_names.insert(i, 'filler')
        giving_team_ids.insert(i, 'filler')
        i += 2

    df = pd.DataFrame({'season' : season_list,
                    'period' : period_list,
                    'receiving_team_ids': receiving_team_ids_n,
                    'receiving_team_names':receiving_team_names_n,
                    'giving_team_ids': giving_team_ids,
                    'giving_team_names': giving_team_names, 
                    'player_ids':player_ids,
                    'player_names':player_names,
                    'player_links':player_links, 
                    'leistungsdaten_links_prev_season':leistungsdaten_links, 
                    'transfer_values':transfer_values})

    df['receiving_team_kader_links_prev_season'] = df['player_names']
    df['receiving_team_leistungsdaten_links_prev_season'] = df['player_names']
    df['giving_team_kader_links_prev_season'] = df['player_names']
    df['giving_team_leistungsdaten_links_prev_season'] = df['player_names']
    df['receiving_team_overview_links_prev_season'] = df['player_names']
    df['giving_team_overview_links_prev_season'] = df['player_names']

    for i in range(len(df['season'])):
        df['receiving_team_kader_links_prev_season'].iloc[i] = f'https://www.transfermarkt.de/{df["receiving_team_names"].iloc[i]}/kader/verein/{df["receiving_team_ids"].iloc[i]}/saison_id/{df["season"].iloc[i]-1}'
        df['receiving_team_leistungsdaten_links_prev_season'].iloc[i] = f'https://www.transfermarkt.de/{df["receiving_team_names"].iloc[i]}/leistungsdaten/verein/{df["receiving_team_ids"].iloc[i]}/plus/1?reldata=%26{df["season"].iloc[i]-1}'
        df['giving_team_kader_links_prev_season'].iloc[i] = f'https://www.transfermarkt.de/{df["giving_team_names"].iloc[i]}/kader/verein/{df["giving_team_ids"].iloc[i]}/saison_id/{df["season"].iloc[i]-1}'
        df['giving_team_leistungsdaten_links_prev_season'].iloc[i] = f'https://www.transfermarkt.de/{df["giving_team_names"].iloc[i]}/leistungsdaten/verein/{df["giving_team_ids"].iloc[i]}/plus/1?reldata=%26{df["season"].iloc[i]-1}'
        df['receiving_team_overview_links_prev_season'].iloc[i] = f'https://www.transfermarkt.de/{df["receiving_team_names"].iloc[i]}/startseite/verein/{df["receiving_team_ids"].iloc[i]}/saison_id/{df["season"].iloc[i]-1}'
        df['giving_team_overview_links_prev_season'].iloc[i] = f'https://www.transfermarkt.de/{df["giving_team_names"].iloc[i]}/startseite/verein/{df["giving_team_ids"].iloc[i]}/saison_id/{df["season"].iloc[i]-1}'
        
    df = df[df['transfer_values'] != 'filler']
    return df


def scrape_player_details(df):
    '''
    Scrapes player detail data from previously scraped player links
    
    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    for player_link in tqdm_notebook(df['player_links'].unique()):
        player_id = re.search(r'\/(?!.*\/)([0-9]+)', player_link)[1]
        rood_path = './data/raw/player/'
        file_path = f'./data/raw/player/player_{player_id}.html'
        safe_html_files(rood_path, file_path, player_link)


def scrape_player_stats(df):
    '''
    Scrapes player stats from previously scraped player stats links
    
    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    for leistungsdaten_link in tqdm_notebook(df['leistungsdaten_links_prev_season'].unique()):
        groups = re.search(r'\/\/www\.transfermarkt\.de\/(.*)\/leistungsdaten\/spieler\/(.*)\/plus\/0\?saison=(.+)',
                        leistungsdaten_link)
        player_id = groups[2]
        season = groups[3]
        rood_path = './data/raw/player_leistungsdaten/'
        file_path = f'./data/raw/player_leistungsdaten/season_{season}_player_{player_id}.html'
        safe_html_files(rood_path, file_path, leistungsdaten_link)


def scrape_team_details(df):
    '''
    Scrapes team details from previously scraped team links

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    kader_list = list(df['receiving_team_kader_links_prev_season'])
    kader_list.extend(df['giving_team_kader_links_prev_season'])
    kader_list = list(set(kader_list))
    for kader_link in tqdm_notebook(kader_list):
        re_groups = re.search(r'www\.transfermarkt\.de\/(.*)\/kader\/verein\/(.*)\/saison_id\/(.*)', 
                            kader_link)
        team_id = re_groups[2]
        season = re_groups[3]
        rood_path = './data/raw/teams/'
        file_path = f'./data/raw/teams/season_{season}_team_{team_id}.html'
        safe_html_files(rood_path, file_path, kader_link)


def scrape_team_stats(df):
    '''
    Scrapes team stats from previously scraped team links

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    leistungsdaten_list = list(df['receiving_team_leistungsdaten_links_prev_season'])
    leistungsdaten_list.extend(df['giving_team_leistungsdaten_links_prev_season'])
    leistungsdaten_list = list(set(leistungsdaten_list))

    for leistungsdaten_link in tqdm_notebook(leistungsdaten_list):
        re_groups = re.search(r'https:\/\/www\.transfermarkt\.de\/(.*)\/leistungsdaten\/verein\/(.*)\/plus\/1\?reldata=%26(.*)',
                        leistungsdaten_link)
        team_id = re_groups[2]
        season = re_groups[3]
        rood_path = './data/raw/teams_leistungsdaten/'
        file_path = f'./data/raw/teams_leistungsdaten/leistungsdaten_season_{season}_team_{team_id}.html'
        safe_html_files(rood_path, file_path, leistungsdaten_link)

def scrape_team_overview(df):
    '''
    Scrapes team overviews from previously scraped team links

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    overview_list = list(df['receiving_team_overview_links_prev_season'])
    overview_list.extend(df['giving_team_overview_links_prev_season'])
    overview_list = list(set(overview_list))

    for overview_link in tqdm_notebook(overview_list):
        re_groups = re.search(r'.*verein\/([0-9]+)\/saison_id\/([0-9]+)',
                        overview_link)
        team_id = re_groups[1]
        season = re_groups[2]
        rood_path = './data/raw/teams_overview/'
        file_path = f'./data/raw/teams_overview/overview_season_{season}_team_{team_id}.html'
        safe_html_files(rood_path, file_path, overview_link)

def scrape_bundesliga_transfer_data(seasons):
    '''
    Scrapes transfer, team and player details for each season from
    transfermakrt.de

    Note: this will take a couple of minutes per season

    Parameters
    ----------
    seasons: a list of seasons of the format [20XX, 20XX, ...]
    '''
    print(f'scraping transfer overview for seasons {seasons}')
    get_transfers_html(seasons)
    df = extract_transfer_data(seasons)
    print(f'scraping player details')
    scrape_player_details(df)
    print(f'scraping player stats')
    scrape_player_stats(df)
    print(f'scraping team details')
    scrape_team_details(df)
    print(f'scraping team stats')
    scrape_team_stats(df)
    print(f'scraping team overviews')
    scrape_team_overview(df)
    return df

# ------------------- extracting data from html -------------------------------
def get_player_statics(df):
    '''
    Extracts player statistics for each player that was transferred in the 
    selected seasons using extract_transfer_data()
    ----------
    df as returned from extract_transfer_data()
    '''
    dates_of_birth = []
    places_of_birth = []
    sizes = []
    nationalities = []
    positions = []
    strong_feet = []
    consultants = []
    outfitters = []
    player_id_helper = []
    countries_of_birth = []
    nebenpositionen = []

    for player_id in df['player_ids'].unique():
        path = f'./data/raw/player/player_{player_id}.html'
        html_file = open(path, 'r', encoding='utf-8')
        source_code = html_file.read()
        html_file.close()
        soup = BeautifulSoup(source_code, "html.parser")
        
        spielerdaten = soup.find("table", class_ = 'auflistung')
        rows = spielerdaten.find_all('tr')
        for row in rows:
            helpers = row.find_all(text=re.compile('Geburtsort'))
            if helpers is not None:
                for helper in helpers:
                    if helper.find_next('td').find('img') is not None:
                        country_of_birth = helper.find_next('td').find('img').get('title')
            else:
                country_of_birth = np.nan

        twitter_list, facebook_list, instagram_list, homepage_list = get_social_media_links(rows)        
        date_of_birth = get_table_value(rows, 'Geburtsdatum')
        place_of_birth = get_table_value(rows, 'Geburtsort')
        place_of_birth = lstrip_if_exist(place_of_birth,'\n')
        place_of_birth = lstrip_if_exist(place_of_birth,' Happy Birthday')
        size = get_table_value(rows, 'Größe')
        size = lstrip_if_exist(size, ' m')
        nationality = get_table_value(rows, 'Nationalität')
        nationality = lstrip_if_exist(nationality,'\n ')
        position = get_table_value(rows, 'Position')
        position = lstrip_if_exist(position,'\n ')
        strong_foot = get_table_value(rows, 'Fuß')
        consultant = get_table_value(rows, 'Spielerberater')
        consultant = lstrip_if_exist(consultant,'\n')
        outfitter = get_table_value(rows, 'Ausrüster')
        nebenposition = np.nan
        nebenposition = find_secondary_positions(soup)
        nebenpositionen.append(nebenposition)
        dates_of_birth.append(date_of_birth)
        places_of_birth.append(place_of_birth)
        sizes.append(size)
        nationalities.append(nationality)
        positions.append(position)
        strong_feet.append(strong_foot)
        consultants.append(consultant)
        outfitters.append(outfitter)
        player_id_helper.append(player_id)
        countries_of_birth.append(country_of_birth)

    players_static = pd.DataFrame({'player_id':player_id_helper,
                        'dates_of_birth': dates_of_birth,
                        'country_of_birth': countries_of_birth,
                        'places_of_birth':places_of_birth,
                        'sizes': sizes,
                        'nationalities':nationalities,
                        'positions': positions,
                        'secondary_posistions': nebenpositionen,
                        'strong_feet':strong_feet,
                        'consultants': consultants,
                        'outfitters':outfitters,
                        'twitter':twitter_list,
                        'facebook':facebook_list,
                        'instagram':instagram_list,
                        'homepage':homepage_list
        })
    players_static.replace([None, 'k.A.', '', ' ', 'k. A.', ' k. A.', 'k. A. '], np.nan, inplace=True)
    players_static['player_id'] = players_static['player_id'].astype('int')
    return players_static


def get_player_stats(df):
    '''
    Extracts player stats for each player that was transferred in the 
    selected seasons using extract_transfer_data()

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    for leistungsdaten in tqdm_notebook(df['leistungsdaten_links_prev_season']):
        groups = re.search(r'h*\/spieler\/(.*)\/plus\/0\?saison=(.*)',
                            leistungsdaten)
        player_id = groups[1]
        season = groups[2]
        file_path = f'./data/raw/player_leistungsdaten/season_{season}_player_{player_id}.html'
        season = int(season) + 1 
        html_file = open(file_path, 'r', encoding='utf-8')
        source_code = html_file.read()
        html_file.close()
        soup = BeautifulSoup(source_code, "html.parser")
        if not soup.find_all('table', class_ = 'items'):
            temp_list = [season, player_id, np.nan, np.nan, np.nan, np.nan,
                         np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
            player_stats_df.loc[len(player_stats_df)] = temp_list
        else:
            label = soup.find(text=re.compile('Position'))
            position = label.find_next('span').get_text()
            position = re.sub(r"(?:[;\n']|\s{2,})",r'',position)
            table = soup.find_all('table', class_ = 'items')[0]
            rows = table.find_all('td')
            competitions = []
            games_played_column = []
            helper_list = []
            for row in rows:
                links = row.find_all('a')
                for link in links:
                    if link is not None:
                        competition = re.search('\/*wettbewerb\/([a-zA-Z0-9]+)*',
                                         link.get("href"))[1]
                        if competition not in competitions:
                            competitions.append(competition)
            stats = [competitions[0]]
            for row in rows:
                helpers = row.select(f"a[href*='{competitions[0]}']")
                for helper in helpers:
                    values = helper.find_all_next('td')
                    for value in values:
                        if value.get_text() != '':
                            stats.append(value.get_text())
            if position == 'Torwart':
                player_stats_df = get_keeper_stats(stats, player_id, competitions, season)
            else:
                player_stats_df = get_player_stats(stats, player_id, competitions, season)          
    return player_stats_df


def ohe_player_stats(df):
    '''
    One hot encodes and cleans player stats to be able to merge them

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    player_stats_df = get_player_stats(df)
    player_stats_df_ohe = pd.get_dummies(player_stats_df, columns=['competition_id'])
    player_stats_df_ohe['minutes_played'] = player_stats_df_ohe['minutes_played'].str.replace("'", '').str.replace(".", '')
    player_stats_df_ohe = player_stats_df_ohe.apply(pd.to_numeric, errors='coerce', axis=1)
    player_stats_df_ohe_grouped =  player_stats_df_ohe.groupby(['season', 'player_id']).sum().reset_index()
    player_stats_df_ohe_grouped['player_id'] = player_stats_df_ohe_grouped['player_id'].astype('float')
    return player_stats_df_ohe_grouped


def get_player_national_debut(df):
    '''
    Extracts player national debuts for each player that was transferred in the 
    selected seasons using extract_transfer_data()

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    national_debuts = []
    id_check = []    
    for leistungsdaten in tqdm_notebook(df['leistungsdaten_links_prev_season']): 
        groups = re.search(r'h*\/spieler\/(.*)\/plus\/0\?saison=(.*)',
                            leistungsdaten)
        player_id = groups[1]
        season = groups[2]
        if player_id in id_check:
            pass
        else:
            id_check.append(player_id)
            file_path = f'./data/raw/player_leistungsdaten/season_{season}_player_{player_id}.html'
            html_file = open(file_path, 'r', encoding='utf-8')
            source_code = html_file.read()
            html_file.close()
            soup = BeautifulSoup(source_code, "html.parser")
            if soup.find(text=re.compile('Länderspielkarriere')) is not None:
                national_soup = soup.find(text=re.compile('Länderspielkarriere'))
                tbs = national_soup.find_all_next('td', class_ = 'zentriert')
                i = 0
                for tb in tbs:
                    if i == 3:
                        national_debut = tb.get_text()
                        national_debut = re.sub(r"(?:[;\n']|\s{2,})",r'',national_debut)
                        national_debuts.append(national_debut)
                    i += 1
            else:
                national_debuts.append(None)
    player_national_debuts = pd.DataFrame({'player_id':id_check,
                                            'national_debuts':national_debuts                                     
                                        })
    player_national_debuts['player_id'] = player_national_debuts['player_id'].astype('int')
    return player_national_debuts

def create_players_df(df):
    '''
    create a pandas DataFrane including all extracted player data

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    player_static = get_player_statics(df)
    player_national_debuts = get_player_national_debut(df)
    player_stats_df_ohe_grouped = ohe_player_stats(df)
    players_static = player_static.merge(player_national_debuts, how='left',on='player_id')
    return player_stats_df_ohe_grouped.merge(players_static, how='left', on='player_id')

def get_team_data(df):
    '''
    Extracts team data for each team that either transferred a player to the 
    Bundesliga or received a player in the Bundesliga in the selected seasons
    using extract_transfer_data()

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    team_df = pd.DataFrame(columns=['season', 
                                    'team_id',
                                    'keeper', 
                                    'avg_keepers_age', 
                                    'defender', 
                                    'avg_defenders_age',
                                    'midfielder',
                                    'avg_midfielder_age',
                                    'striker',
                                    'avg_strikers_age'])

    positions = ['Torwart', 'Abwehr', 'Mittelfeld', 'Sturm']
    kader_list = list(df['receiving_team_kader_links_prev_season'])
    kader_list.extend(df['giving_team_kader_links_prev_season'])
    kader_list = list(set(kader_list))
    for kader in tqdm_notebook(kader_list):
        groups = re.search(r'.*verein\/([0-9]+)\/saison_id\/([0-9]+)',
                            kader)
        team_id = groups[1]
        season = groups[2]
        
        file_path = f'./data/raw/teams/season_{season}_team_{team_id}.html'
        html_file = open(file_path, 'r', encoding='utf-8')
        source_code = html_file.read()
        html_file.close()
        soup = BeautifulSoup(source_code, "html.parser")
        season = int(season) +1
        team_list = [season, team_id]
        for position in positions:
            team_list.append(get_number_of_players(position, soup))
            team_list.append(get_players_avg_age(position, soup))

        team_df.loc[len(team_df)] = team_list
    return team_df

def get_contract_length(df):
    '''
    Extracts players' contract length for each player that was transferred in 
    the selected seasons using extract_transfer_data()

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    contracts_df = pd.DataFrame(columns=['player_id',
                                        'Vertrag bis',
                                        'season'])

    for kader in list(df['giving_team_kader_links_prev_season'].unique()):
        groups = re.search(r'.*verein\/([0-9]+)\/saison_id\/([0-9]+)',
                            kader)
        team_id = int(groups[1])
        season = int(groups[2])        
        file_path = f'./data/raw/teams/season_{season}_team_{team_id}.html'
        html_file = open(file_path, 'r', encoding='utf-8')
        source_code = html_file.read()
        html_file.close()
        soup = BeautifulSoup(source_code, "html.parser")

        season = season + 1
        transfers = df[['season', 'period', 'player_ids', 'giving_team_ids',
                         'receiving_team_ids', 'transfer_values']]
        sub_df = transfers[transfers['season'] == season]
        team_season_transfers = sub_df[sub_df['giving_team_ids'] == str(team_id)]
            
        player_id_list = []
        trs = soup.find_all('tr', class_ = ['odd', 'even'])
        for tr in trs:
            for td in tr.find_all('td'):
                a_tag = td.find('a', class_ = 'spielprofil_tooltip')
                if a_tag is not None:
                    player_id_list.append(int(a_tag.get('id')))
        
        player_id_list = player_id_list[::2]
        if team_id == 515:
            contracts_df.loc[len(contracts_df)] = temp_list
            for id_ in team_season_transfers['player_ids']:
                temp_list = [id_, 'without_contract', season]
                contracts_df.loc[len(contracts_df)] = temp_list
                
        elif soup.find('table', class_ = 'items') is not None:
            contract_df = pd.read_html(str(soup.find('table', class_ = 'items')))[0]
            contract_df = contract_df[::3]
            contract_df = pd.DataFrame(contract_df['Vertrag bis'])
            contract_df['player_id'] = player_id_list
            contract_df.set_index('player_id', inplace=True)
            for id_ in team_season_transfers['player_ids']:
                id_ = int(id_)
                if id_ in contract_df.index:
                    temp_list = [id_, contract_df.loc[id_]['Vertrag bis'], season]
                else:
                    temp_list = [id_, np.nan, season]
                contracts_df.loc[len(contracts_df)] = temp_list
        else:
            for id_ in team_season_transfers['player_ids']:
                temp_list = [id_, np.nan, season]
                contracts_df.loc[len(contracts_df)] = temp_list
    return contracts_df

def get_team_table_info(df):
    '''
    Extracts table infos for each team

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    teams_table_info = pd.DataFrame(columns=['season', 
                                            'team_id',
                                            'final_table_position', 
                                            'no_of_matches', 
                                            'goal_diff', 
                                            'points'
    ])
    overview_list = list(df['receiving_team_overview_links_prev_season'])
    overview_list.extend(df['giving_team_overview_links_prev_season'])
    overview_list = list(set(overview_list))
    for overview in tqdm_notebook(overview_list):
        groups = re.search(r'.*verein\/([0-9]+)\/saison_id\/([0-9]+)',
                            overview)
        team_id = groups[1]
        season = groups[2]
        
        file_path = f'./data/raw/teams_overview/overview_season_{season}_team_{team_id}.html'
        html_file = open(file_path, 'r', encoding='utf-8')
        source_code = html_file.read()
        html_file.close()
        soup = BeautifulSoup(source_code, "html.parser")
        table = soup.find('tr', class_ = 'table-highlight')
        season = int(season) + 1
        team_list = [season, team_id]
        if table is not None:
            tds = table.find_all('td', class_ = 'zentriert')
            table_info = [season, team_id]

            if tds is not None:
                for i, value in enumerate(tds):
                    if value.get_text() != '':
                        table_info.append(value.get_text())
            else:
                table_info = [season, team_id, np.nan, np.nan, np.nan, np.nan]
        else:
            table_info = [season, team_id, np.nan, np.nan, np.nan, np.nan]
        teams_table_info.loc[len(teams_table_info)] = table_info
    return teams_table_info

def create_teams_df(df):
    '''
    Create a pandas DataFrame containing all team data

    Parameters
    ----------
    df as returned from extract_transfer_data()
    '''
    team_data = get_team_data(df)
    team_table_info = get_team_table_info(df)
    complete_teams_df = team_data.merge(team_table_info, how='left',
                             on = ['season','team_id'])
    complete_teams_df['team_id'] = complete_teams_df['team_id'].astype('float')
    complete_teams_df['season'] = complete_teams_df['season'].astype('float')
    return complete_teams_df

def create_output_df(df):
    '''
    Extracts player and team data for each player that was transferred in the 
    selected seasons using scrape_bundesliga_transfer_data()

    Parameters
    ----------
    df as returned from scrape_bundesliga_transfer_data()
    '''
    transfers = df[['season', 'period', 'player_ids', 'giving_team_ids',
                    'receiving_team_ids', 'transfer_values']]
    transfers[['season', 'player_ids', 'giving_team_ids', 'receiving_team_ids']] = transfers[['season', 'player_ids', 'giving_team_ids', 'receiving_team_ids']].apply(pd.to_numeric, errors='coerce', axis=1)
    print('creating players dataframe')
    players_df = create_players_df(df)
    output_df = transfers.merge(players_df, 
                                how='right',
                                left_on=['season', 'player_ids'],
                                right_on=['season', 'player_id'])
    output_df = output_df.rename({'competition_id': 'competition_id_prev_season'}, axis=1)
    print('creating teams dataframe')
    teams_df = create_teams_df(df)
    output_df = output_df.merge(teams_df, 
                                how ='left', 
                                left_on = ['season', 'giving_team_ids'], 
                                right_on = ['season', 'team_id'],
                                )
    output_df = output_df.merge(teams_df, 
                                how ='left', 
                                left_on = ['season', 'receiving_team_ids'], 
                                right_on = ['season', 'team_id'],
                                suffixes = ('_giving_team', '_receiving_team')
                                )
    contracts = get_contract_length(df)
    output_df = output_df.merge(contracts,
                                how='left',
                                left_on=['season', 'player_ids'],
                                right_on=['season', 'player_id'])
    return output_df
    