DEX Table Scraper

This script uses Selenium with Firefox WebDriver to scrape data from a dynamic table on a decentralized exchange (DEX) web page. It collects token pair data, including name, price, and 24-hour volume, and exports it to a CSV file.

    ⚠️ Note: Most of the actual data has been deleted from the script for authenticity and privacy reasons.

📦 Features

    Automates browser using Firefox and Selenium.

    Adds cookies to bypass authentication or simulate a session.

    Extracts trading pairs, prices, and 24h volume.

    Saves the full HTML page source.

    Exports the scraped data to a data.csv file.

🔧 Requirements

    Python 3.7+

    Geckodriver (placed in the script directory or system path)

    Firefox browser installed

Install dependencies:

pip install selenium pandas

🚀 Usage

    Make sure geckodriver.exe is in the same directory or in your system PATH.

    Update the url and cookies list in the script to match your target page and session.

    Run the script:

python scraper.py

    Output:

        data.csv – structured token data

        page_source.html – raw HTML content of the page

📁 Output Example

Pair           | Price       | 24h Volume
-----------------------------------------
USDT/ETH       | $1.00       | $2,304,592
BTC/USDC       | $29,523.44  | $1,943,884
...

📌 Notes

    The script assumes the DEX table uses the .ds-dex-table class and specific child selectors.

    Adjust range(2, 102) or CSS selectors based on the actual structure of the site.

    Add your own exception handling and delay logic if the site uses heavy JavaScript rendering or anti-bot protection.

🔐 Legal Disclaimer

This project is for educational purposes only. Scraping websites without permission may violate their terms of service. Always ensure compliance before running any web automation.
