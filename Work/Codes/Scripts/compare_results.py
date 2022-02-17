import json

data_folder = "/mnt/c/Users/jeeva/Documents/Work/Data/"

def get_json_data(file_name):
    with open(file_name,"r") as file:
        return json.load(file)

if __name__ == "__main__":

    initial_results = get_json_data(data_folder+"result_Improved_original.json")
    improved_results = get_json_data(data_folder+"result_Improved.json")
    count,count2 =0,0 

    for index, frame in enumerate(initial_results):
        if (len(initial_results[index]["objects"])-len(improved_results[index]["objects"])) != 0:
            count+=1
            count2+=abs(len(initial_results[index]["objects"])-len(improved_results[index]["objects"]))
            print(initial_results[index]["filename"])
    print(count, count2)
