import sys
import argparse
import requests

def main():
    args = sys.argv
    limit , search , pollutant = input_parser(args)

    if search and pollutant:
        json_object = connection(10000)
        count = filter_by_city_and_pollutant(json_object,search,pollutant)
        print(f"Total Records Filtered From= {json_object["total"]} \nTotal Records shown : {count}")
    elif search:
        json_object = connection(10000)
        count = filter_by_city(json_object,search)
        print(f"Total Records Filtered From= {json_object["total"]} \nTotal Records shown : {count}")
    elif pollutant:
        json_object = connection(10000)
        count = filter_by_pollutant(json_object,pollutant)
        print(f"Total Records Filtered From= {json_object["total"]} \nTotal Records shown : {count}")
    else:
        json_object = connection(limit)
        for _ in json_object["records"]:
                print(f"City: {_['city']:20}  Station: {_['station']:60} Pollutant: {_['pollutant_id']:10} Avg of pollutant: {_['pollutant_avg']:20}")
        print(f"Total Records = {json_object["total"]} \nTotal Records shown : {json_object["count"]}")

def connection(limit):
    if limit < 1:
        sys.exit("limit should be atleast 1")
    else:
        receivedinfo = requests.get(f"https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001d4415597d1e6417b52df82a374d00590&format=json&limit={limit}")
        return receivedinfo.json()

def input_parser(args):
    #if no command line args
    if len(args)== 1:
        sys.exit("Pass -h as commanline argument for help")

    #parsing
    parser = argparse.ArgumentParser(
        prog="\nAir Quality Data Multi Filter",
        description=" Get city , station , pollutant , avg polution records",
    )
    parser.add_argument('-l', '--limit' , type = int , default = 10000)    #no of rows to be printed
    parser.add_argument('-s', '--search' , type = str , default = None , nargs = "*" , action = "append" , help = "city/cities to be filtered")  #city/cities to be filtered
    parser.add_argument('-p', '--pollutant' , type = str , default = None , nargs = "*" , action = "append" ,help ="pollutant(s) to be filtered")  #pollutant(s) to be filtered
    args = parser.parse_args()
    return args.limit,args.search,args.pollutant

def filter_by_city(json_obj,search_string):
    count = 0
    for search_string in search_string[0]:
        for _ in json_obj["records"]:
            if (_["city"]).lower() == search_string.lower():
                print(f"City: {_['city']:20}  Station: {_['station']:40} Pollutant: {_['pollutant_id']:10} Avg of pollutant: {_['pollutant_avg']:20}")
                count += 1
    return count

def filter_by_pollutant(json_obj,search_string):
    count = 0
    for search_string in search_string[0]:
        for _ in json_obj["records"]:
            if (_["pollutant_id"]).lower() == search_string.lower():

                print(f"City: {_['city']:20}  Station: {_['station']:40} Pollutant: {_['pollutant_id']:10} Avg of pollutant: {_['pollutant_avg']:20}")
                count += 1
    return count


def filter_by_city_and_pollutant(json_obj,search_string,pollutant):
    count = 0
    for search_string in search_string[0]:
        for search_string_p in pollutant[0]:
            for _ in json_obj["records"]:
                if (_["pollutant_id"]).lower() == search_string_p.lower() and (_["city"]).lower() == search_string.lower():

                    print(f"City: {_['city']:20}  Station: {_['station']:40} Pollutant: {_['pollutant_id']:10} Avg of pollutant: {_['pollutant_avg']:20}")
                    count += 1
    return count



if __name__ == "__main__":
    main()
