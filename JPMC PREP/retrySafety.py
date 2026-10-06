# The interviewer asks:
# "The payment service occasionally returns 503. Modify this function to retry safely."

# Before writing code, tell me:
# What conditions would you check before deciding whether a retry is safe?

import requests

def process_payment(payment_id):
    response = requests.post(
        "https://payment-service/pay",
        json={"payment_id": payment_id},
        timeout=5
    )

    if response.status_code == 200:
        return True

    return False