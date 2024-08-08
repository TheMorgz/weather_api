# weather_api

A weather API implementation using Django Rest Framework.

## Prerequisites

- Python 3.12
- Virtualenv

## Setup

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd weather_api
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Copy the `.env-example` file to `.env` and update it with your API key.

    ```sh
    cp weather_api/.env-example weather_api/.env
    ```

    Edit the [`.env`](command:_github.copilot.openSymbolInFile?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmorgz%2FCode%2Fweather_api%2Fweather_api%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22.env%22%5D "/Users/morgz/Code/weather_api/weather_api/.env") file and replace [`your-api-key`](command:_github.copilot.openSymbolFromReferences?%5B%22your-api-key%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fmorgz%2FCode%2Fweather_api%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fmorgz%2FCode%2Fweather_api%2FREADME.md%22%2C%22path%22%3A%22%2FUsers%2Fmorgz%2FCode%2Fweather_api%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A33%2C%22character%22%3A62%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fmorgz%2FCode%2Fweather_api%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fmorgz%2FCode%2Fweather_api%2FREADME.md%22%2C%22path%22%3A%22%2FUsers%2Fmorgz%2FCode%2Fweather_api%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A39%2C%22character%22%3A535%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fmorgz%2FCode%2Fweather_api%2Fweather_api%2Fmanage.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fmorgz%2FCode%2Fweather_api%2Fweather_api%2Fmanage.py%22%2C%22path%22%3A%22%2FUsers%2Fmorgz%2FCode%2Fweather_api%2Fweather_api%2Fmanage.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A14%2C%22character%22%3A26%7D%7D%5D%5D "Go to definition") with your actual API key.

5. **Run database migrations:**

    ```sh
    python weather_api/manage.py migrate
    ```

6. **Run the development server:**

    ```sh
    python weather_api/manage.py runserver
    ```

    The API will be available at [`http://127.0.0.1:8000`](command:_github.copilot.openSymbolFromReferences?%5B%22http%3A%2F%2F127.0.0.1%3A8000%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fmorgz%2FCode%2Fweather_api%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fmorgz%2FCode%2Fweather_api%2FREADME.md%22%2C%22path%22%3A%22%2FUsers%2Fmorgz%2FCode%2Fweather_api%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A53%2C%22character%22%3A34%7D%7D%5D%5D "Go to definition").

## Running Tests

To run the tests, use the following command:

```sh
env/bin/python weather_api/weather/tests.py