launch options:

-make a new project directory; navigate to it
-in the directory, create a no-extension file titled 'envvars'
-within this file, 
-clone the repo: git clone https://github.com/nspon/stripe_ta
-open the no-extension 'envvars' file, edit the environment variables dummy values to store the following:
    SECRET_KEY - Django secret key for the project
    STRIPE_PUBLISHABLE_KEY - public Stripe API key
    STRIPE_SECRET_KEY - private Stripe API key
    STRIPE_PRICE_ID - Stripe product price ID
