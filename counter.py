def countEmail():
    # This first line is provided for you
    file = input('Enter file name:')
    if len(file)<1: file = 'mbox-short.txt'
    file = open(file)
    sender = dict()
    
    for line in file:
        if not line.startswith("From:"): continue
        line = line.split()
        name = line[1]
        if name not in sender:
            sender[name] = 1
        else:
            sender[name] +=1
    value = sender.values()
    maxval = max(value)
    person = max(sender,key = sender.get)
    print(person,maxval)

        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
