from random import randint, choice
import requests
from time import sleep

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


url = "http://www.intmobile.ge/order.php"

user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532M Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot; http://www.jobboerse.com/bot.htm) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
]
# Names ყოველი შემთხვევისთვის ;დ

# names = ["Dachi", "Giorgi", "Luka", "Andria", "Aleksandre", "Saba", "Nika", "Demetre",
#          "Sandro", "Mari", "Ana", "Elene", "Lile", "Nino", "Anastasia", "Barbare",
#          "Salome", "Lizi", "Nia", "Nita", "Sesili", "Lika", "Anamaria", "Gvanca", "Vache",
#          "Dato", "Irakli", "Natia", "Davit", "Aleksandra", "Nikoloz", "Ilia", "Lana",
#          "Nuca", "Natali", "Masho", "Misho", "Mikheil"]
#
# surnames = ["Abzianidze", "Abakeli", "Abashidze", "Abulashvili", "Agladze", "Antauri",
#             "Balanchivadze", "Gagua", "Gomarteli", "Gomareli", "Gomiashvili", "Gongadze", "Gonashvili",
#             "Gondauri", "Gopadze", "Kopadze", "Gorganeli", "Gorgasalidze", "Dadiani", "Vepkhvadze",
#             "Firtskhalava", "Labadze", "Kikodze", "Chikovani", "Chochia", "Wereteli"]


while (True):
    mastercard_prefix = "5280"
    last_eight_number = random_with_N_digits(12)
    full_number = mastercard_prefix + str(last_eight_number)
    month = "0" + str(randint(1,9))
    end_year = str(randint(19,27))
    cvc_code = str(randint(101,999))
    # ესეც იქნებ მოუნდეს ვინმეს ;დ
    # card_name = choice(names) + " " + choice(surnames)
    usr_agent_header = {
        "User-Agent": choice(user_agents)
    }
    data_to_send = {
        #"cardname" : card_name,
        "cardname": "No+Cardholdername",
        "kqjwehbcn": full_number,
        "hheryt": month,
        "ncnbgh1": end_year,
        "mndfhgrg": cvc_code
    }
    test_sender = requests.post(url, data=data_to_send, headers=usr_agent_header)
    if test_sender.status_code == 200:
        print("Data Sent Successfully:", data_to_send)
