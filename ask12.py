# H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς.
# Χρησιμοποιείστε αρχικά την διεύθυνση https://drand.cloudflare.com/public/latest για να βρείτε ποιος είναι ο τελευταίος γύρος
# και στην συνέχεια πάρτε τις τελευταίες 100 τιμές (πεδίο randomness) μέσα από το https://drand.cloudflare.com/public/{round}.
# Μετατρέψτε αυτές τις τιμές σε δυαδικό και εμφανίστε το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά και το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενες μονάδες.


from urllib.request import Request, urlopen
import re


req = Request('https://drand.cloudflare.com/public/latest',
              headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data = str(data, 'UTF-8')   #convert to string

count = 0

#print(data, "\n")


pattern = r"{\"round\":(.*?)\,"
pattern2 = r"\"randomness\":\"(.*?)\""

round = re.search(pattern, data).group(1)
round = int(round)
randomness = re.search(pattern2, data).group(1)
stri = randomness

# takes 99 previous rounds
for i in range(98):
    round = round - 1
    req = Request('https://drand.cloudflare.com/public/%s' % round,
                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data = str(data, 'UTF-8')
    randomness = re.search(pattern2, data).group(1)
    stri = stri + randomness        # adds all randomness in a string

main = ' '.join(format(ord(c), 'b') for c in stri)
main = main.split()
max0 = 0
max1 = 0
count0 = 0
count1 = 0
x = 0

# checks the list for 0 and 1 's
while x < len(main):
    if main[x] == "110000":
        count0 = count0 + 1
        while x < len(main) - 1 and main[x + 1] == main[x]:
            count0 = count0 + 1
            x = x + 1
            if x >= len(main) - 1 or main[x + 1] != main[x]:
                break
        x = x + 1
        if count0 > max0:
            max0 = count0
        count0 = 0
    elif main[x] == "110001":
        count1 = count1 + 1
        while x < len(main) - 1 and main[x + 1] == main[x]:
            count1 = count1 + 1
            x = x + 1
            if x >= len(main) - 1 or main[x + 1] != main[x]:
                break
        x = x + 1
        if count1 > max1:
            max1 = count1
        count1 = 0
    else:
        x = x + 1
print(max0)
print(max1)
