import os
import pandas as pd

def getInputFilePath():
    return os.getenv('INPUT_FILE', 'input.csv')

def getOutputFilePath():    
    return os.getenv('OUTPUT_FILE', 'output.csv')

def getCity():
    return os.getenv('CITY', 'Paris')


# Path to the input file (.csv)
inputFile = getInputFilePath()
# Path to the output file (.csv)
outputFile = getOutputFilePath()
# City (column to add in csv)
city = getCity()

print('=================================')
print('Env variables read in the program')
print('=================================')
print('INPUT_FILE path :', inputFile)
print('OUTPUT_FILE path:', outputFile)
print('CITY :', city)
print('=================================')

# Read csv into DataFrame
inputData = pd.read_csv(inputFile)


def dollarsToEuros(dollar):
    """
    Convert dollar to euros (valid in 21/06/2021)
    The input format is '$1,200.35'
    """
    return 0.84*float(dollar[1::].replace(',',''))

# ============ treatment ============== #

outputData = inputData.copy()
print(f"Add city column (city = {city})")
outputData['city']='Paris'
# change dollars to euros
print("Changing dollars to euros ...")
outputData['price']= outputData['price'].apply(dollarsToEuros)
# Filter columns
outputData = outputData[['id','name','latitude','longitude','price','number_of_reviews','city']]

print("Check transformation")
print(outputData.head(2))
print("Write the output to the file ", outputFile)

# Put the dataFrame to the output
outputData.to_csv(outputFile,sep=';',index=False)

