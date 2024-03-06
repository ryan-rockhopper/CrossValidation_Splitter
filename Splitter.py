import sys
import pandas as pd

#Check command line arguments
if len(sys.argv) < 5:
    print("The command line arguments are incorrect. Refer to README and try again.")
    sys.exit()

dataFilePath    = sys.argv[1]

try:
    numberOfSplits  = int(sys.argv[2])
except Exception as e:
    print(f"The number of splits could not be parsed. The exception is: {e}")

outputPath      = sys.argv[3]
splitName       = sys.argv[4]

#Attempt to open the file and count the number of rows
try:
    fullData = pd.read_csv(dataFilePath)
except Exception as e:
    print(f"There was an error opening the data.csv. The exception is: {e}")
    sys.exit()

shuffledData    = fullData.sample(frac=1).reset_index(drop=True) #Shuffles the data in the dataframe and resets the index so it starts at 0 again.
rowCount        = shuffledData.shape[0]
splitSize       = rowCount // numberOfSplits

segments = [shuffledData.iloc[i*splitSize:(i+1)*splitSize] for i in range(numberOfSplits)] #Splits into numberOfSplits dataframes from the shuffled data

fileNames = []
for i in range(numberOfSplits):
    outputName = "/" +splitName + "_split" + str(i) + ".csv"
    fileNames.append(outputName)

#Attempt to write the dataframes to a .csv
for i in range(numberOfSplits):
    totalPath = outputPath + fileNames[i]
    try:
        segments[i].to_csv(totalPath, index=False)
    except Exception as e:
        print(f"There was an error writing to {totalPath}. The exception is: {e}")