
#OC principle
#programming to interfaces -- we are making the recommendation making its own class
#Single responsibility: this is the only class in charge of creating the recommendations!

import csv

filename = "/src/movies/movie_results.csv"

# initializing the titles and rows list
fields = []
rows = []
resultados =[]

# recommend_with_true_rating
def recommend_with_true_rating(pref_key):
    with open(filename, 'r') as csvfile:
        #creating a csv reader object
        csvreader = csv.reader(csvfile)
     
        # extracting field names through first row
        fields = next(csvreader)
 
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
           # print(row)
        #list of everything in col 0
        #        print(rows[0][1])
    col = [x[0] for x in rows]
    #print(col)
    print("Magic key: ",pref_key)
    pref_key = str(pref_key)
    #finding the first 10 / top ten movies from the category match
    result_counter =0
    if pref_key in col:
        for x in range(0,len(rows)):
            if pref_key == rows[x][0]:
                if result_counter < 10:
                    print(rows[x][1])
                    resultados.append(rows[x][1])
                    result_counter+=1
    return resultados

            

        
   # print(fields)

def recommend_with_false_rating(pref_key):
    with open(filename, 'r') as csvfile:
        #creating a csv reader object
        csvreader = csv.reader(csvfile)
     
        # extracting field names through first row
        fields = next(csvreader)
 
        # extracting each data row one by one
        for row in reversed(list(csvreader)):
            rows.append(row)
           # print(row)
        #list of everything in col 0
        #        print(rows[0][1])
    col = [x[0] for x in rows]
   # print(col)
    print("Magic key: ",pref_key)
    pref_key = str(pref_key)
    #finding the first 10 / top ten movies from the category match
    result_counter =0
    if pref_key in col:
        for x in range(0,len(rows)):
            if pref_key == rows[x][0]:
                if result_counter < 10:
                    print(rows[x][1])
                    resultados.append(rows[x][1])
                    result_counter+=1
    return resultados
