# Web Scraper

The Web Scraper is a Django-based web application that allows users to enter a URL and scrape its content to retrieve relevant information. It includes a feature to clear the page content if an incorrect URL is entered, along with error handling to display appropriate messages.

## Features

- Scrapes content from a specified URL.
- Displays relevant information retrieved from the URL, such as links.
- Provides a clear button to remove content from the page.
- Error handling for invalid URLs.

## Installation

1. Clone the repository:

    git clone https://github.com/your-username/web-scraper.git

2. Navigate to the project directory:

    cd web_scrapper

3. Install dependencies:

    pip install -r requirements.txt

4. Set up environment variables:

    - Create a `.env` file in the root directory.
    - Add the following line to the `.env` file and replace `YOUR_SECRET_KEY` with your Django secret key:

    SECRET_KEY=YOUR_SECRET_KEY

5. Run migrations:

    python manage.py migrate

6. Start the development server:

    python manage.py runserver

7. Access the application at `http://127.0.0.1:8000/` in your web browser.

## Usage

1. Enter a valid URL in the input field.
2. Click the "Scrape" button to retrieve information from the URL.
3. The retrieved information will be displayed in a table format.
4. Click the "Clear" button to remove the content from the page.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository's `main` branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Bootstrap](https://getbootstrap.com/) - Frontend framework used for styling.
- [Django](https://www.djangoproject.com/) - Web framework used for backend development.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Python library for web scraping.
