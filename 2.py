#just some predefining
lines = []
approved = 0

# counts the amount of the asked letter in the password
def counter(letter, password):
    count = 0
    for i in password:
        if i == letter:
            count += 1
    return count

#opens the file and saves it into a list with every line call
with open(r"2input.txt") as f:
    lines = list(map(str, f.readlines()))
#parses the lines to use them 
for x in lines:
    re_x = x.replace("-"," ")
    re_x_final = re_x.replace(":", " ")
    sp_x = re_x_final.split(" ")
    sp_x.pop(3)
    print(sp_x)
    #checks if the conditions are met and counts the number of times it is met among the whole file
    if int(sp_x[0]) <= counter(sp_x[2], sp_x[3]) and int(sp_x[1]) >= counter(sp_x[2], sp_x[3]):
        approved += 1
        print(approved)