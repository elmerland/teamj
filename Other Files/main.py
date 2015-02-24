import csv

#open file and convert to string
fp = open("fgyearbooktablesfull.csv", "r")
file = fp.read()
fp.close()
#split string into rows
file = file.split("\r")
#delete headers
file = file[3:]

#delete trailing lines
for i in range(0, 6):
    del file[-1]

#rebuild file into a useful table
table = []
cornType = ""
location = ""


for row in file:

    if row == ',,,,,,,,,,,,,,':
        cornType = ""
        location = ""
        continue
    row = row.split(',')
    if row[0] is not '':
        cornType = row[0].replace('"', '').strip()
        if len(row) is 16:
            location = row[1].replace('"', '').strip()
        else:
            location = row[1] + ',' + row[2]
            location = location.replace('"', '').strip()
            del row[2]
        row[0] = cornType
        row[1] = location
    else:
        row[0] = cornType
        row.insert(1, location)

    print(row)
    table.append(row)

print(table)

#write to new CSV file
fp = open("toBeImported.csv", "w")
writer = csv.writer(fp)
for row in table:
    writer.writerow(row)

fp.close()




