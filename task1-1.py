from itertools import combinations as comb

Kevin = {"Halsey", "Taylor Swift", "Mitski","Joji","Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"}
Stuart = {"Kendrik Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeekend", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrik Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}
Edith = {"Metallica", "Billie Eilish", "TheWeekend", "Mitski", "NF", "Conan Gray", "Kendrik Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}

DJ = ['Kevin', 'Stuart', 'Bob', 'Edith']
DJObject = [Kevin, Stuart, Bob, Edith]

djName = []
djiIntersection = []

for dj1, dj2 in comb(DJ, 2): 
    djName.append(f"{dj1} and {dj2}")

for djSet1, djSet2 in comb(DJObject, 2):
    percentage = ((len(djSet1.intersection(djSet2))/10)*100)
    djiIntersection.append(percentage)

output = list(zip(djName, djiIntersection))
output = sorted(output, key=lambda x: x[1], reverse=True)
print(output)

# Output: 
# [
#    ('Kevin and Bob', 40.0), 
#    ('Stuart and Bob', 40.0), 
#    ('Stuart and Edith', 40.0), 
#    ('Bob and Edith', 40.0), 
#    ('Kevin and Edith', 30.0), 
#    ('Kevin and Stuart', 10.0)
# ]
    


