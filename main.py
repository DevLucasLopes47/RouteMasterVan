!pip install googlemaps numpy 
import googlemaps  
import numpy as np 
from itertools import permutations  

API_KEY = 'AIzaSyBisYZ5bSObj0El3tes2TKusf2xiDQik3U'
gmaps = googlemaps.Client(key=API_KEY)

enderecos_cache = {} 

def geocode_address(address):
    if address in enderecos_cache: 
        return enderecos_cache[address]  

    try:
        geocode_result = gmaps.geocode(address)  
    except googlemaps.exceptions.HTTPError as e:
        print(f"Erro ao geocodificar o endereço: {e}") 
        return None  

    if geocode_result:
        location = geocode_result[0]['geometry']['location']  
        enderecos_cache[address] = (location['lat'], location['lng'])  
        return (location['lat'], location['lng'])  
    else:
        print(f"Não foi possível geocodificar o endereço: {address}")
        return None 

def calculate_euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)  

def create_distance_matrix(locations):
    n = len(locations)  
    distance_matrix = np.zeros((n, n))  
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i, j] = calculate_euclidean_distance(locations[i], locations[j]) 
    return distance_matrix 

def get_all_routes(start_location, end_location, waypoints):
    all_routes = list(permutations(waypoints))  
    all_routes = [[start_location] + list(route) + [end_location] for route in all_routes]  
    return all_routes 

def get_route_distance(route):
    total_distance = 0  
    total_duration = 0 
    route_details = []  

    for i in range(len(route) - 1):
        leg_start = route[i]  
        leg_end = route[i + 1]  
        try:
            response = gmaps.distance_matrix(leg_start, leg_end, mode="driving", language="pt-BR")  
            if response["status"] == "OK":
                leg_distance = response["rows"][0]["elements"][0]["distance"]["text"]  
                leg_duration = response["rows"][0]["elements"][0]["duration"]["text"]  
                start_address = response["origin_addresses"][0]  
                end_address = response["destination_addresses"][0]  

                route_details.append({
                    "start_address": start_address,
                    "end_address": end_address,
                    "distance": leg_distance,
                    "duration": leg_duration
                }) 

                total_distance += response["rows"][0]["elements"][0]["distance"]["value"]  
                total_duration += response["rows"][0]["elements"][0]["duration"]["value"]  
            else:
                print(f"Erro ao calcular a distância para o trecho:")
                print(f"De: {leg_start}, Para: {leg_end}")
                print(f"Detalhes da resposta da API: {response}")
        except KeyError as e:
            print(f"Erro ao obter informações para o trecho de {leg_start} para {leg_end}: {e}")  
        except Exception as e:
            print(f"Erro ao calcular a distância para o trecho de {leg_start} para {leg_end}: {e}")  
    return total_distance, total_duration, route_details  

def get_optimized_routes(start_location, end_location, waypoints):
    all_routes = get_all_routes(start_location, end_location, waypoints) 
    routes_sorted = sorted(all_routes, key=lambda route: get_route_distance(route)[0])  
    return routes_sorted  

def main():
    start_location = geocode_address("Praça Bernardino de Lima, 45 - Centro, Nova Lima - MG, 34000-279, Brasil")
    end_location = geocode_address("unibh,buritis, belo horizonte")

    if not start_location or not end_location: 
        print("Não foi possível geocodificar as localizações.")
        return

    waypoints = []  
    for i in range(3): 
        going = input(f"Usuário {i+1}, você vai usar a van hoje? (s/n): ").strip().lower()
        if going == 's':
            address_or_cep = input(f"Usuário {i+1}, informe seu endereço ou CEP: ").strip()  
            location = geocode_address(address_or_cep)  
            if location:
                waypoints.append(location)  
        else:
            print(f"Usuário {i+1}, você não vai mais usar a van hoje.")

    if not waypoints: 
        print("Nenhum usuário irá utilizar a van hoje.")
        return

    routes = get_optimized_routes(start_location, end_location, waypoints)  

    best_route = routes[0]

    faculdade_location = geocode_address("Faculdade UNIBH, Buritis, Belo Horizonte - MG, Brasil")
    final_route = best_route[:-1] + [faculdade_location]  

    print("Melhor Rota:")
    total_distance, total_duration, route_details = get_route_distance(final_route)  
    for detail in route_details:
        print(f"De {detail['start_address']} para {detail['end_address']}:")
        print(f"  Distância: {detail['distance']}")
        print(f"  Duração: {detail['duration']}")
    print(f"Distância total da rota: {total_distance / 1000:.2f} km")  
    print(f"Duração total da rota: {total_duration / 60:.2f} minutos") 

if __name__ == "__main__":
    main()  # Executa a função principal se o script for executado diretamente
