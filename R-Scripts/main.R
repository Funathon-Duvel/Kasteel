library(readr)
library(dplyr)
library(ggplot2)
library(forcats)
# import dataframe


inputFile <- Sys.getenv("INPUT_FILE")
outputFile <- Sys.getenv("OUTPUT_FILE")
city <- Sys.getenv("ARGS")

print("=================================")
print("Env variables read in the program")
print("=================================")
print("INPUT_FILE path :", inputFile)
print("OUTPUT_FILE path:", outputFile)
print("ARGS :", city)
print("=================================")

df <- read_csv(inputFile)
# save manipulated data to output folder

# simple copy of input to the output
write_csv(df, outputFile)