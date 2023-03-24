burgers = [
  {
    "id": 0,
    "name": "Tribute Burger",
    "description": "A mouth-watering honest beef burger",
    "type": "beef",
    "ingredients": {
      "beef": 11,
      "american cheese": 2,
      "burger sauce":5,
      "french mustard":1,
      "pickes": 4,
      "coleslaw": 6,
      "lettuce":4
    },
    "addresses": [
      {
        "addressId": 0,
        "number": "75",
        "line1": "Venn Street",
        "line2": "Clapham",
        "postcode": "SW4 0BD",
        "country": "United Kingdom"
      }
    ]
  },
  {
    "id": 1,
    "name": "Pulled Mooshie",
    "type": "vegan",
    "description": "Spicy vegan burger with jackfruit",
    "ingredients": {
      "jackfruit": 2,
      "cucumber": 4,
      "tomatoes":5,
      "gluten free bun": 0,
      "burger sauce": 11
    },
    "addresses": [
      {
        "addressId": 0,
        "number": "104",
        "line1": "Brick Lane",
        "line2": "Shoreditch",
        "postcode": "E1 6RL",
        "country": "United Kingdom"
      }
    ]
  }
]


burgers_in_ua=[

{
                   "addressId": "7",
                   "name": "Farsh. Burgers and Meat",
                   "street": "Kateriniska",
                   "house_num": "14",
                   "postcode": "65026",
                   "city": "Odesa"
},
{
                   "addressId": "5",
                   "name": "Sailor Jack",
                   "street": "Preobrazhenska",
                   "house_num": "17",
                   "postcode": "65000",
                   "city": "Odesa"
},
{
                   "addressId": "3",
                   "name": "Delicateka",
                   "street": "Drukarska",
                   "house_num": "11",
                   "postcode": "79000",
                   "city": "Lviv"
},
{
                   "addressId": "9",
                   "name": "Night Burger",
                   "street": " Velikogo",
                   "house_num": "14",
                   "postcode": "79053",
                   "city": "Lviv"
},
{
                   "addressId": "8",
                   "name": "Burger Farm",
                   "street": "Shevchenka",
                   "house_num": "56",
                   "postcode": "02000",
                   "city": "Kyiv"
}
]

print(burgers_in_ua)


burgers[0]["addresses"].clear()
burgers[1]["addresses"].clear()
burgers[0]["addresses"].append(burgers_in_ua[4])
burgers[0]["addresses"].append(burgers_in_ua[0])
burgers[0]["addresses"].append(burgers_in_ua[1])
burgers[0]["addresses"].append(burgers_in_ua[2])
burgers[1]["addresses"].append(burgers_in_ua[3])
burgers[1]["addresses"].append(burgers_in_ua[2])
print(burgers)

client_burger=input('Який бургер бажаєте: Vegan or Beef?')
print(client_burger)

client_burger=client_burger.lower()
print(client_burger)
type(client_burger)

type_0=burgers[0]["type"]
type_1=burgers[1]["type"]
if client_burger==type_0:
    client_choose=burgers[0]["name"]
    print("Your burger:"+client_choose)
if client_burger==type_1:
    client_choose=burgers[1]["name"]
    print("Your burger:"+client_choose)
if client_burger!=type_0 and client_burger!=type_1:
    print("Incorrect input")

    ing_0 = burgers[0]["ingredients"]
    ing_1 = burgers[1]["ingredients"]

    if client_burger == type_0:
        if all(ing_0.values()):
            print("burger is ready for order")
        else:
            print('no ingredients for your burger')
    if client_burger == type_1:
        if all(ing_1.values()):
            print("burger is ready for order")
        else:
            print('no ingredients for your burger')


ing_0=burgers[0]["ingredients"]
ing_1=burgers[1]["ingredients"]
adr_0=burgers[0]["addresses"]
adr_1=burgers[1]["addresses"]

if client_burger==type_0:
   if all(ing_0.values()):
       print(adr_0)
   else:
        print('no ingredients for your burger')
if client_burger==type_1:
    if all(ing_1.values()):
       print(adr_1)
    else:
         print('no ingredients for your burger')