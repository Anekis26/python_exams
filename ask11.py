# H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς.
# Χρησιμοποιείστε αρχικά την διεύθυνση https://drand.cloudflare.com/public/latest για να βρείτε ποιος είναι ο τελευταίος γύρος και στην
# συνέχεια πάρτε τις τιμές (πεδίο randomness) των 20 τελευταίων γύρων μέσα από το https://drand.cloudflare.com/public/{round}.
# Μετατρέψτε αυτές τις τιμές σε ένα δεκαεξαδικό κείμενο και υπολογίστε την εντροπία του.
# Η εντροπία υπολογίζεται ως το αρνητικό άθροισμα της πιθανότητας εμφάνισης ενός συμβόλου (εδώ δεκαεξαδικού ψηφίου) επί τον λογάριθμο αυτής της πιθανότητας (https://en.wikipedia.org/wiki/Entropy_(information_theory))

from urllib.request import Request, urlopen
import json

#finds the data about the current round
req = Request('https://drand.cloudflare.com/public/latest',
              headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
d = json.loads(data)
latest_round = d["round"]

# finds the data for other rounds
counter = 0
randomness_list = ['']*20


round = latest_round
req1 = Request('https://drand.cloudflare.com/public/' + str(round),
              headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data1 = urlopen(req1).read()
d1 = json.loads(data1)
randomness_list[counter] = d1["randomness"]
counter = counter + 1
round = round - 1
while counter < 20:
    req1 = Request('https://drand.cloudflare.com/public/' + str(round),
                   headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data1 = urlopen(req1).read()
    d1 = json.loads(data1)
    # print(d1["round"])
    randomness_list[counter] = d1["randomness"]
    counter = counter+1
    round = round - 1

# text to hex the whole list
counter = 0
while counter < 20:
    randomness_list[counter] = randomness_list[counter].encode("utf-8").hex()
    counter = counter + 1

# moving the whole list to a single string
long_str = ""
for elements in randomness_list:
    long_str = long_str + elements

