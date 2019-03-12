import createmapquestapi
import mapquestclass



def main():

    try:
        routes = createmapquestapi.create_tuples(createmapquestapi.gather_locations())
        encoded_routes = createmapquestapi.url_encode(routes)
        data = createmapquestapi.parse_the_response(createmapquestapi.http_response(encoded_routes))
        list_of_stats = createmapquestapi.gather_stats()
        print()


        for stat in list_of_stats:

            if stat.upper() == 'LATLONG':
                mapquestclass.Lat_Long().look_up(data)
                print()
            elif stat.upper() == 'STEPS':
                steps = mapquestclass.Directions().look_up(data)
                if not steps:
                    print()
                    break
                else:
                    for turn in steps:
                        print(turn)
                print()
            elif stat.upper() == 'TOTALTIME':
                mapquestclass.Time().look_up(data)
                print()
            elif stat.upper() == 'TOTALDISTANCE':
                mapquestclass.Distance().look_up(data)
                print()
            elif stat.upper() == 'ELEVATION':
                e = createmapquestapi.elevation_full_url(mapquestclass.Lat_Long().list_lat_and_lng(data))
                mapquestclass.Elevation().look_up(e)
                print()



        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

    except:
        print()
        print('MAPQUEST ERROR')


if __name__ == '__main__':
    main()





# 460 s burlington ave la ca 90057
# 1215 seward la ca 90038

