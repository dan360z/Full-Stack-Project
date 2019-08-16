$(function() {
    $("#payment-form").submit(function() {
        var form = this;
        var card = {
            // Takes the values from the payment form
            number: $("#id_credit_card_number").val(),
            exp: $('#id_card_expiry').val(),
            cvc: $("#id_cvv").val()
        };
    
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#credit-card-errors").hide();
            // Adds the stripe id to the form
            $("#id_stripe_id").val(response.id);
            /* Prevents the credit card details from being submitted
            to the server */
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            form.submit();
        } else {
            $("#stripe-error-message").text(response.error.message);
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});