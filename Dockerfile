FROM python:3.8-slim-buster

ENV BASE_DIR=/app 
WORKDIR ${BASE_DIR}
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV SECRET_KEY=$SECRET_KEY
ENV DEBUG_VALUE=$DEBUG_VALUE
ENV STRIPE_PUBLISHABLE_KEY=$STRIPE_PUBLISHABLE_KEY
ENV STRIPE_SECRET_KEY=$STRIPE_SECRET_KEY
ENV STRIPE_PRICE_ID=$STRIPE_PRICE_ID

WORKDIR /app/stripe_api
EXPOSE 8000
ENTRYPOINT [ "python3" ]
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]