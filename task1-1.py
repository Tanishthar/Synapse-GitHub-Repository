from itertools import combinations as comb

Kevin = {"Halsey", "Taylor Swift", "Mitski","Joji","Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"}
Stuart = {"Kendrik Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeekend", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrik Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}
Edith = {"Metallica", "Billie Eilish", "TheWeekend", "Mitski", "NF", "Conan Gray", "Kendrik Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}

DJ = ['Kevin', 'Stuart', 'Bob', 'Edith']
combination = comb(DJ, 2)

DJObject = [Kevin, Stuart, Bob, Edith]
combination1 = comb(DJObject, 2)

djName = []
djiIntersection = []

for dj1, dj2 in combination: 
    djName.append(f"{dj1} and {dj2}")


for djSet1, djSet2 in combination1:
    intersectionSet = djSet1.intersection(djSet2)
    percentage = ((len(intersectionSet)/10)*100)
    djiIntersection.append(percentage)

output = list(zip(djName, djiIntersection))

output = sorted(output, key=lambda x: x[1], reverse=True)

print(output)
# Kevin and Bob: 40% 
    


