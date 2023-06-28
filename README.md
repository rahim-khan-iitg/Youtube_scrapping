# YouTube Comments Scraper

This repository contains a script that scrapes comments from YouTube videos using the YouTube Data API v3.

## Requirements

- Python 3.11.0
- A Google account with access to the YouTube Data API v3

## Setup

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Follow the instructions [here](https://developers.google.com/youtube/registering_an_application) to create a project, enable the YouTube Data API v3, and obtain an API key.
4. Set the `YOUTUBE_API_KEY` environment variable to your API key.

## Usage

To scrape comments from a video, run the script with the video ID as an argument:

```
python scraper.py VIDEO_ID
```
you can see it in action at https://rahim-khan.azurewebsites.net/
The script will output the comments to a file named `comments_VIDEO_ID.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
