import os

# Path to the input file (.csv)
inputFile = os.getenv('INPUT_FILE', 'input.csv')
# Path to the output file (.csv)
outputFile = os.getenv('OUTPUT_FILE', 'output.csv')

# City (column to add in csv)
city = os.getenv('CITY','Paris')

print('========================')
print('Env variables read in the program')
print('INPUT_FILE :', inputFile)
print('OUTPUT_FILE :', outputFile)
print('CITY', city)
print('========================')