# Cross Validation Splitter
This program will handle .csv files and split them into X folds for performing cross validation with different machine learning classifiers.

## Installation
This will use pandas. It is encouraged to install conda.

## Usage
You will need to pass command line arguments into this program. There should be 4 command line arguments, the relative path to the .csv file you are trying to split, the amount of folds you want, a path for the output files, and the split name. 
An example would be python3 Splitter.py ./example_data/data.csv 10 ./split_data learningData

## Author
Ryan Dalrymple

## Expansion
In the future, this may be expanded to handle different file types and other things of that nature. For now, it uses pandas to work with .csv files that are formatted with a header row and are separated by commas.