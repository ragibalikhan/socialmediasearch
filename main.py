from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import os
from googleapiclient.discovery import build

API_KEY = 'AIzaSyAj_kWqJLHraay-DZxYPmdItuh0BOw3IHM'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')

        # Call function to check account availability for different platforms
        account_info = {
            'Twitter': check_twitter_account(query),
            'Instagram': check_instagram_account(query),
            'Facebook': check_facebook_account(query),
            'Pinterest': check_pinterest_account(query),
            'Quora': check_quora_account(query),
            'Reddit': check_reddit_account(query),
            'Telegram': check_telegram_account(query),
            'Youtube': check_youtube_account(query)
        }

        # Pass the extracted information to the template and render it appropriately
        return render_template('results.html', account_info=account_info)

    return render_template('index.html')


def check_twitter_account(query):
    # Make request to Twitter URL to check account availability
    response = requests.get(f'https://twitter.com/{query}')

    # Check if account exists by scraping the data
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        error_page = soup.find('div', {'class': 'errorpage-topbar'})

        if error_page:
            return {
                'exists': False
            }
        else:
            return {
                'exists': True,
                'profile_link': f'https://twitter.com/{query}'
            }

    return {
        'exists': False
    }


def check_instagram_account(query):
    # Make request to Instagram URL to check account availability
    response = requests.get(f'https://www.instagram.com/{query}')

    # Check if account exists by scraping the data
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        main_section = soup.find('main')

        if main_section:
            error_section = main_section.find('div', {'class': 'error-container'})

            if error_section:
                return {
                    'exists': False
                }
            else:
                return {
                    'exists': True,
                    'profile_link': f'https://www.instagram.com/{query}'
                }

    return {
        'exists': False
    }


def check_facebook_account(query):
    # Make request to Facebook URL to check account availability
    response = requests.get(f'https://www.facebook.com/{query}')

    # Check if account exists by scraping the data
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        error_section = soup.find('div', {'class': '_2phz'})

        if error_section:
            return {
                'exists': False
            }
        else:
            return {
                'exists': True,
                'profile_link': f'https://www.facebook.com/{query}'
            }

    return {
        'exists': False
    }


def check_pinterest_account(query):
    # Make request to Pinterest URL to check account availability
    response = requests.get(f'https://www.pinterest.com/{query}')

    # Check if account exists by scraping the data
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        error_section = soup.find('div', {'class': 'centeredContainer'})

        if error_section:
            return {
                'exists': False
            }
        else:
            return {
                'exists': True,
                'profile_link': f'https://www.pinterest.com/{query}'
            }

    return {
        'exists': False
    }


def check_quora_account(query):
    # Make request to Quora URL to check account availability
    response = requests.get(f'https://www.quora.com/profile/{query}')

    # Check if account exists by scraping the data
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        error_section = soup.find('div', {'class': 'Layout-message'})

        if error_section:
            return {
                'exists': False
            }
        else:
            return {
                'exists': True,
                'profile_link': f'https://www.quora.com/profile/{query}'
            }

    return {
        'exists': False
    }


def check_reddit_account(query):
    # Make request to Reddit URL to check account availability
    response = requests.get(f'https://www.reddit.com/user/{query}')

    # Check if account exists by scraping the data
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        error_page = soup.find('div', {'class': 'ErrorPage__container'})

        if error_page:
            return {
                'exists': False
            }
        else:
            return {
                'exists': True,
                'profile_link': f'https://www.reddit.com/user/{query}'
            }

    return {
        'exists': False
    }


def check_telegram_account(query):
    # Make request to Telegram URL to check account availability
    response = requests.get(f'https://telegram.me/{query}')

    # Check if account exists by scraping the data
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        description_section = soup.find('div', {'class': 'tgme_page_description'})

        if description_section:
            return {
                'exists': True,
                'profile_link': f'https://telegram.me/{query}'
            }

    return {
        'exists': False
    }


def check_youtube_account(query):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Search for the channel using the query
    search_response = youtube.search().list(
        q=query,
        part='id',
        type='channel',
        maxResults=1
    ).execute()

    # Check if a channel is found
    if 'items' in search_response and len(search_response['items']) > 0:
        channel_id = search_response['items'][0]['id']['channelId']
        profile_link = f'https://www.youtube.com/channel/{channel_id}'
        return {
            'exists': True,
            'profile_link': profile_link
        }

    return {
        'exists': False
    }


if __name__ == '__main__':
    app.run(debug=True)
