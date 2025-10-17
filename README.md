The goal of this project is to create stats from a JSON file. 

It takes in entry json file and a threshold value
Json file objects contains a status value (bad, ok, error) and a value 


The core function keeps ok objects and values >= threshold
Then returns ok count, total value and average count