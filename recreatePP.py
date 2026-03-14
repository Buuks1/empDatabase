def solution(S):
    photos = {}
    cleaned = S.replace(".", ",")
    lines = cleaned.strip().split('\n')
    for photoid, photo in enumerate(lines):
        trimmed = photo.split(',')
        name = trimmed[0]
        type = trimmed[1]
        city = trimmed[2].strip()
        date_time = trimmed[3].strip()
        photos[photoid] = {
            'id': photoid,
            'name': name,
            'type': type,
            'city': city,
            'date': date_time
        }

    cities = {}
    for photo in photos.values():
        city_group = photo['city']
        if city_group not in cities:
            cities[city_group] = []
        cities[city_group].append(photo)

    for city_group in cities:
        cities[city_group].sort(key = lambda p: p['date'])
        
    for city_group in cities:
        group = cities[city_group]
        photo_count = len(group)
        for i in range (photo_count):
            photo = group[i]
            number = i + 1
            count_str = str(number)
            if len(count_str) < 2:
                count_str = '0' + count_str
            new_name = city_group + count_str + '.' + photo['type']
            photo['new_name'] = new_name

    new_string = ""
    for photo in photos.values():
        new_string = new_string + photo['new_name'] + "\n"
    return new_string

class Photo:
    def __init__(self, S):
        photos = {}
        cleaned = S.replace(".", ",")
        lines = cleaned.strip().split('\n')
        for photoid, photo in enumerate(lines):
            trimmed = photo.split(',')
            name = trimmed[0]
            type = trimmed[1]
            city = trimmed[2].strip()
            date_time = trimmed[3].strip()
            self.id = photoid
            self.name = name
            self.ext = type
            self.city = city
            self.date = date_time
            photos[self.id] = self
        sorted_photos = sorted(photos)



mystr = """photo.jpg, Warsaw, 2013-09-05 14:08:15
Jay.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11"""

print(solution(mystr))