from random import randint
import requests
from time import sleep

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


url = "http://www.intmobile.ge/order.php"


while (True):
    mastercard_prefix = "5280"
    last_eight_number = random_with_N_digits(12)
    full_number = mastercard_prefix + str(last_eight_number)
    month = "0" + str(randint(1,9))
    end_year = str(randint(19,27))
    cvc_code = str(randint(101,999))
    data_to_send = {
        "cardname": "No+Cardholdername",
        "kqjwehbcn": full_number,
        "hheryt": month,
        "ncnbgh1": end_year,
        "mndfhgrg": cvc_code
    }
    test_sender = requests.post(url, data=data_to_send)
    if test_sender.status_code == 200:
        print("Data Sent Successfully:", data_to_send)