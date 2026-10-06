# The interviewer asks:
# "The payment service occasionally returns 503. Modify this function to retry safely."

# Before writing code, tell me:
# What conditions would you check before deciding whether a retry is safe?

import random
import time
import requests


def process_payment(payment_id):
    max_retries = 3

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                "https://payment-service/pay",
                json={"payment_id": payment_id},
                timeout=5,
                headers={"Idempotency-Key": payment_id}
            )

            if response.status_code == 200:
                return True

            if response.status_code != 503:
                return False

        except requests.RequestException:
            # Depending on the API semantics, a timeout may mean
            # the payment was actually processed.
            return False

        if attempt < max_retries:
            delay = (2 ** attempt) + random.uniform(0, 0.5)
            time.sleep(delay)

    return False