from geopy import Nominatim
import math
import webbrowser
import time


def distance(location_la, location_lo, location2_la, location2_lo):
    print("calculating distance...")

    R = 6373.0

    lat1 = math.radians(location_la)
    lon1 = math.radians(location_lo)
    lat2 = math.radians(location2_la)
    lon2 = math.radians(location2_lo)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    print("Distance: ", distance)
    return(distance)




def get_coordinates(adress_list):
    print("getting coordinates...")
    co_adress_list = []

    locator = Nominatim(user_agent="myGeocoder")
    

    for a in adress_list:
        time.sleep(2)
        temp = locator.geocode(a)

        try:
            temp_la = temp.latitude
            temp_lo = temp.longitude
            co_adress_list.append([temp_la,temp_lo])
 
            if a not in adress_coordinates:
                adress_coordinates[a] = [temp_la, temp_lo]
                
        except:
            print("adress not found, please try again ..."+str(a))
            global Navigation
            Navigation = False
           
 
    return co_adress_list






def find_best(adress_list, formatted_list):

    print("finding best route...")

    best = 10

    # print("adress list: ", adress_list)
    # print("formatted list: ", formatted_list)

    starting_point_coor = formatted_list[0]

    destination_coors = formatted_list[1:]

    points = [None]*4
    print("")
    print("Remaining Adress List: ")
    print("")
    for a in adress_list[1:]:
        print(a)
    print("")

    i = 0 
    j = 1

    print("destination_coors: ", destination_coors)
    while j < len(formatted_list):
        
        new_best = min(best, distance(formatted_list[i][0], formatted_list[i][1], formatted_list[j][0], formatted_list[j][1]))
        
        if new_best < best:

            ### The Points array = [starting lo, starting la, destination lo, destination la] ### 

            points[0] = formatted_list[i][0]
            points[1] = formatted_list[i][1]
            points[2] = formatted_list[j][0]
            points[3] = formatted_list[j][1]

            best = new_best
        
        j+=1

    if best != 10:
        return points
    else:
        print("something went wrong please try again...")
        global Navigation
        Navigation = False
        
        


def get_adress_from_coor_dic(adress_coordinates_dic, coords, current_adress):

    listOfItems = adress_coordinates_dic.items()
    for adress,coordinates  in listOfItems:
        if adress != current_adress and coordinates == coords:
            return adress

def get_adress_from_coor(adress_coordinates, points):
    print("getting adress from coordinates... ")
    adress = ""
    start_result = get_adress_from_coor_dic(adress_coordinates, [points[0], points[1]], adress)
    end_result = get_adress_from_coor_dic(adress_coordinates, [points[2], points[3]], start_result)
    print("")
    print("Current: ", start_result)
    print("Destination: ", end_result)


    return start_result, end_result


def update_destination(adress_list, ending_adress):

    starting_adress = adress_list[0]
    adress_list.remove(starting_adress)
    adress_list.remove(ending_adress)
    adress_list.insert(0, ending_adress)

    return adress_list





if __name__ == "__main__":

    print("Best Path Planner")
    print("")
    print("")

    Navigation = True

    print("Example Input: 'Hanurit 1, Ashdod, Israel'")

    starting_point = input("please type your strating adress as in the example above: ")


    ex_adress_list = [starting_point, "Hanurit 13, Ashdod, Israel","Rosh Pina 6, Ashdod, Israel", "Hanurit 24, Ashdod, Israel", "Harash 10, Ashdod, Israel", "Rotem 12, Ashdod, Israel", "Gedera 2, Ashdod, Israel"]
    
    adress_coordinates = {}
    formatted_list = get_coordinates(ex_adress_list)

    while Navigation == True  and len(ex_adress_list)>2:

        points = find_best(ex_adress_list, formatted_list)


        s, d = get_adress_from_coor(adress_coordinates, points)
        # print("best possible destination: " +d)
        webbrowser.open("https://www.google.com/maps/place/"+d)

        print("")
        next_destination = input("hit enter for your next destination...")
        print("")
        ex_adress_list = update_destination(ex_adress_list, d)
        formatted_list = update_destination(formatted_list, [points[2], points[3]])


        

        if len(ex_adress_list) == 2:
            # print("best possible destination: " +d)
            # webbrowser.open("https://www.google.com/maps/place/"+d)
            break
        if len(ex_adress_list) < 2:
            break
    
    print("")
    print("Final destionation, good job!")







# df = pd.read_csv('go_track_trackspoints.csv')



# adress = "Hanurit 13, ashdod"


# webbrowser.open("https://www.google.com/maps/place/"+adress)
