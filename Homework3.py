favorite_film1=input("What is your favorite film?:")
favorite_film1_year=input("What is release date?:")
favorite_film1_description=input("What is this movie about?:")
favorite_film1_oscar=input("Did this movie win an oscar?:")

print ('Film:'+favorite_film1,'Release date:'+favorite_film1_year,'Description:'+favorite_film1_description,'Oscar:'+favorite_film1_oscar, sep="\n" )
print(f"favorite_film1={type(favorite_film1)};favorite_film1_year={type(favorite_film1_year)}; favorite_film1_description={type(favorite_film1_description)};favorite_film1_oscar={type(favorite_film1_oscar)} ")
int(favorite_film1_year)
bool(favorite_film1_oscar)

#upper
print(favorite_film1.upper())
print(favorite_film1_description.upper())

#split
print(favorite_film1.split())
print(favorite_film1_description.split())

#count
x=favorite_film1.upper()
print(x.count("THE"))
y=favorite_film1_description.upper()
print(y.count("LED"))


#find
print(x.find("THE"))
print(y.find("LED"))