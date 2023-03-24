from random import randint


random_num = randint(100, 500)
print(random_num)
n=random_num
i=1
s=0
while i<=n:
  s=i+s
  i=i+1
print(s)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
m_car=car.get("model")
print(m_car)

car.update({"year": "2020"})
print(car)

car.update({"color": "Red"})
print(car)

car.pop("model")
print(car)

films = ["Crazy, Stupid, Love.",
        "Seven",
        "Dead Poets Society",
        "Memento",
        "Harry Potter"]
for film in films:
  print(film)
  if film=="Memento":
    break



data = {"results": [
        {
            "series": None,
            "actor": [
                {
                    "imdb_id": "nm0240183",
                    "name": "Nick Dudman"
                },
                {
                    "imdb_id": "nm0460792",
                    "name": "Amanda Knight"
                },
                {
                    "imdb_id": "nm0866566",
                    "name": "Lisa Tomblin"
                }
            ],
            "event_name": "Academy Awards, USA",
            "year": 2012,
            "type": "Nominee",
            "award_name": "Oscar",
            "award": "Best Achievement in Makeup"
        }]}

ID_imbd_id=[]
for i in data["results"][0]["actor"]:
    ID_imbd_id.append(i["imdb_id"])
print(ID_imbd_id)
