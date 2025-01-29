# Sportsbot Spider Setup & Execution

This guide will walk you through setting up and running a Scrapy spider to scrape various sports reference sites

Please make sure to respect the sports reference [bot policy](https://www.sports-reference.com/bot-traffic.html)

## Prerequisites

Ensure you have the following installed:
- Python (>=3.8)
- pip
- Virtual environment (optional but recommended)

## Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/jackpickus/sportsbot.git
   cd sportsbot
   ```
2. **Create a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Scrapy Spider

1. **Navigate to the Scrapy project directory**
   ```sh
   cd sportsbot
   ```
2. **Run the spider**
   ```sh
   scrapy crawl nba_player
   ```
   You can run the other spiders the same way but the above one will output a file called "nba_player.csv"
   Read more about outputting data on the scrapy docs link below


## Custom Settings

Modify `settings.py`:
- `ROBOTSTXT_OBEY`: `False` to allow `nba_player` spider to function properly


## Additional Resources
- Scrapy Documentation: https://docs.scrapy.org/en/latest/
- Troubleshooting: Check Scrapy logs and error messages.

## License

This project is licensed under the [MIT License](LICENSE).

