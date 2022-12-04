// Make a request to the '/config/' endpoint; parse the response JSON; obtain Stripe public key.
fetch("/api/config/")
.then((result) => { return result.json(); })
.then((data) => {
// Initialize an instance of Stripe.js with the public key value obtained.
    const stripe = Stripe(data.publicKey);
    var buyButton = document.getElementById('buy-button');
    buyButton.addEventListener('click', function() {
        // Instantiate a new Checkout Session object using the server-side '/buy/{id}' endpoint.
        fetch('../../buy/'+"{{ id }}", {method: 'GET'})              
        .then(response => {let jsonResponse = response.json(); console.log(jsonResponse); return jsonResponse})
        // Redirect to Stripe Session Checkout passing the sessionId from the fetch response.
        .then(session => stripe.redirectToCheckout({ sessionId: session.session_id }))
    })
});