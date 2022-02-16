# Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες.
# Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με μόνο γράμματα και τον κενό χαρακτήρα (space).
# Χωρείστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό και ξεκινείστε να αφαιρείτε ζευγάρια λέξεων αν το άθροισμα των γραμμάτων τους είναι 20.
# Βγάλτε τα στατιστικά για το μήκος των λέξεων που έμειναν, πχ. 10 λέξεις του ενός γράμματος, 12 λέξεις των 2 γραμμάτων, 3 λέξεις των 3 γραμμάτων κτλ.
# Τα ζεύγη δεν χρειάζεται να είναι από συνεχόμενες λέξεις.

first_file = open("ascii.txt", 'r')
new_file = open("edited_file.txt", 'w')
for line in first_file:
    k = line
whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
edit = ''.join(filter(whitelist.__contains__, k))
new_file.write(edit)
list_edit = edit.split()

i = len(list_edit)
j = 0
new_file.close()
new_file = open("edited_file.txt", 'w')

while j < i - 1:
    if (len(list_edit[j]) + len(list_edit[j + 1])) == 20:
        list_edit.pop(j + 1)
        list_edit.pop(j)
        i = len(list_edit)
    else:
        j = j + 1

# print(list_edit)

for element in list_edit:
    new_file.write(element + " ")

position = 0
num_letters = 1
times = 0

while num_letters <= 30:
    for words in list_edit:
        if len(list_edit[position]) == num_letters:
            times = times + 1
            position= position + 1
        else:
            position = position + 1
    if times>0:
        print(times, " words of ", num_letters, " letters")
    times = 0
    num_letters = num_letters+1
    position = 0