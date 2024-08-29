import mercadopago
import mercadopago.sdk

def gerar_link_pagamento():
    sdk = mercadopago.SDK("TEST-3150038538350235-082121-0c3c5beeb2afb4a28ed18669c8c6afef-458215381")

    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
    'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
    }

    payment_data = {
        "items": [ 
        {"id": "1", "title": "Relogio citzen eco drive", "quantity": 1, "currecy_id": "BLR", "unit_price": 149.99}],  "back_urls": {
        "success": "fhttps://github.com/Gersondej/Test-de-API/compracerta",
        "failure": "https://github.com/Gersondej/Test-de-API/compraerrada",
        "pending": "https://github.com/Gersondej/Test-de-API/compraerrada"
        },
        "auto_return": "all"
        }
    result = sdk.preference().create(payment_data, request_options)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    return (link_iniciar_pagamento)