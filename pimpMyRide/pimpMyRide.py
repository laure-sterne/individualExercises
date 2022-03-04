# Demand of differents flights

# Step 1 : Parsing

clientRoger = "Roger 0 5 10"
clientPongo = "Pongo 3 7 14"
clientPerdita = "Perdita 8 10 8"
clientAnita = "Anita 16 3 7"

# za=[1,2,3,4,5,6]
# x,_,_,_,y,_=za

flight = {}

# function which split informations and append in dictionnary
def a(voyageur, voyage):
    nom, depart, duree, prix = voyageur.split()
    voyage['client'] = nom
    voyage['start'] = depart
    voyage['duration'] = duree
    voyage['price'] = prix

    return voyage

# print(a(clientRoger, flight))

allFlights = []
everyone = """Roger 0 5 10
Pongo 3 7 14
Perdita 8 10 8
Anita 16 3 7"""

# function which split all trip on a day by using function a 
def b(tous, voyages):
    splited = tous.split('\n')
    for i in splited:
        voyageuh = a(i, flight)
        voyages.append(voyageuh)
    
    return voyages

b(everyone, allFlights)


# Step 2 : Price

def c(listOfTrips):
    allPrices = 0
    for i in listOfTrips:
       value = i.get('price')
       allPrices += int(value)
    
    return allPrices

print(c(allFlights))


# Step 3 : Compatibility

def d(trips):
    # 
    
    # 

    return

# To be continued...