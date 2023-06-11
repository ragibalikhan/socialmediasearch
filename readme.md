# Social Media Searcher

This is a Flask web application that allows you to check the availability of social media accounts on various platforms such as Twitter, Instagram, Facebook, Pinterest, Quora, Reddit, Telegram, and YouTube. The application utilizes web scraping and the YouTube API to fetch account information.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3 installed on your machine.
- The required Python packages installed. You can install them by running the following command:
- pip install -r requirements.txt 

## Usage

1. Clone the repository:

git clone https://github.com/your-username/social-media-searcher.git


2. Navigate to the project directory:

cd socialmediasearcher


3. Obtain a YouTube API key by following the instructions [here](https://developers.google.com/youtube/registering_an_application).

4. Open the `app.py` file and replace `'YOUR_API_KEY'` with your YouTube API key in the `API_KEY` variable.

5. Run the application:

python main.py


6. Open your web browser and visit [http://localhost:5000](http://localhost:5000).

7. Enter the social media account name you want to check in the search bar and click the "Search" button.

8. The application will display the availability and profile link of the account on different platforms.

## Screenshots

![Screenshot 1](/screenshots/screenshot1.png)
![Screenshot 2](/screenshots/screenshot2.png)

## Demo

You can try out the running web application [here](https://social-media-searcher.onrender.com/).

**Note:** The demo version may have limited capabilities compared to running the application locally due to API restrictions.

## License

This project is licensed under the [MIT License](LICENSE).


