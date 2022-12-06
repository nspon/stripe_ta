from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Item
import stripe

# Create your views here.

def item(request, id: int) -> HttpResponse:
    """A view for the requested item rendered with the `'item.html'` template.

    :param request: an incoming request, required default parameter.
    :param id: id of the item selected.
    :return: a rendered HTTP response with the id passed.
    :rtype: HttpResponse 
    """

    return render(request, 'api/item.html', {'id': id})

@csrf_exempt
def stripe_config(request) -> JsonResponse:
    """A view to return the Stripe public key configured for the server.

    :param request: an incoming request, required default parameter.
    :return: a JSON with the Stripe public key value.
    :rtype: JsonResponse
    """

    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request, id: int) -> JsonResponse:
    """A view to instantiate a Stripe CheckoutSession object. Upon a successful payment, configures 
    a URL for the `'success/'` endpoint, with the sessionId passed as a query. A rejected 
    payment returns the item page via the `'item/{id}/'` endpoint. STRIPE_SECRET_KEY,
    STRIPE_PUBLISHABLE_KEY and STRIPE_PRICE_ID should be configured as environmental variables.

    :param request: an incoming request, required default parameter.
    :param id: id of the item requested.
    :return: a JSON with the key-value pairs for the id Checkout session instantiated
    and Stripe public key.
    :rtype: JsonResponse
    """

    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'api/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + f'api/item/{id}/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'quantity': 1,
                        'price': settings.STRIPE_PRICE_ID
                    }
                ]
            )
            context = {
                'session_id': checkout_session.id,
                'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
            }
            return JsonResponse(context)
        except Exception as e:
            return JsonResponse({'error': str(e)})

def success(request) -> HttpResponse:
    """A view for the requested item rendered with the `'success.html'` template.

    :param request: an incoming request, required default parameter.
    :return: a rendered HTTP response with the session id passed as query.
    :rtype: HttpResponse 
    """
    return render(request, 'api/success.html')
