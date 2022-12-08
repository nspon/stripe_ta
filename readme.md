
# Stripe integration

## Launch options

### 1. Using Docker
Make and set active a new project directory with shell:

    mkdir dir_name
    cd dir_name

Clone the repo:

    git clone https://github.com/nspon/stripe_ta.git

Navigate to the root directory:

    cd stripe_ta

Open the no-extension **envvars** file, replace the environment variables dummy values
 with the accurate values of the following:
    
    SECRET_KEY - Django secret key for the project
    STRIPE_PUBLISHABLE_KEY - public Stripe API key
    STRIPE_SECRET_KEY - private Stripe API key
    STRIPE_PRICE_ID - Stripe product price ID

(Note: these should be given as they are, without the surrounding quotes or special characters)
Example: 

    SECRET_KEY=e8rfsd8gsdvfckxv8l
    STRIPE_PUBLISHABLE_KEY=pk_test_4rf9ewj9ojersdfvmdxmvlkfdxmf
    STRIPE_SECRET_KEY=sk_test_874yrfe8saifsdjosdjvofdjvd
    STRIPE_PRICE_ID=price_3r89we87erud

Run the docker-compose:

    docker-compose up

This will build the image from the **Dockerfile** at the root directory, install dependencies and launch \
the application at port 8000 of the local host.

Navigate to localhost:8000/api/item/x in a browser to start the checkout for item numbered x.

### 2. Using github only

Make and set active a new project directory with shell:

    mkdir dir_name
    cd dir_name

Clone the repo:

    git clone https://github.com/nspon/stripe_ta.git

Navigate to the root directory:

    cd stripe_ta

Build a virtual environment titled **venv** and activate it:

    python -m venv venv
    venv\Scripts\activate

At the root directory, create a .env.bat file to store the environmental variables in this format
(replace the dummy values with the actual ones). Example:

    SET SECRET_KEY=e8rfsd8gsdvfckxv8l
    SET STRIPE_PUBLISHABLE_KEY=pk_test_4rf9ewj9ojersdfvmdxmvlkfdxmf
    SET STRIPE_SECRET_KEY=sk_test_874yrfe8saifsdjosdjvofdjvd
    SET STRIPE_PRICE_ID=price_3r89we87erud

(these should be given as they are, without the surrounding quotes or special characters)

Run .env.bat to set the variables:

    call .env.bat

Install dependencies:

    pip install -r requirements.txt

Navigate to the **stripe_api** directory and start the server:

    cd stripe_api: 
    python manage.py runserver

Navigate to localhost:8000/api/item/x in a browser to start the checkout for item numbered x.
