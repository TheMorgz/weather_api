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

    Edit the `.env` file and replace `your-api-key` with your actual API key.

5. **Run database migrations:**

    ```sh
    python weather_api/manage.py migrate
    ```

6. **Run the development server:**

    ```sh
    python weather_api/manage.py runserver
    ```

    The API will be available at http://127.0.0.1:8000.

## Running Tests

To run the tests, use the following command:

```sh
env/bin/python weather_api/weather/tests.py