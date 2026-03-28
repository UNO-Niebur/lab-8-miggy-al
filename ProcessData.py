#ProcessData.py
#Name: Miguel Alvarado
#Date: 3/27/2026
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    IDNum = data[3]
    year = data[5]
    major = data[6]
  
    student_ID = makeID(first, last, IDNum)
    Major_Year = makeMajorYear(major, year)
    output = last + "," + first + "," +student_ID + "," + Major_Year + "\n"
    outFile.write(output)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, IDNum):
  #print(first, last, IDNum)
  idlen = len(IDNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + IDNum[idlen - 3: ]
  #print(id)
  return id

def makeMajorYear(major , year):
  major_ab = major[:3].upper()

  #The students year
  year_ab = ""
  if year == "Freshman":
    year_ab = "FR"
  elif year == "Sophomore":
    year_ab = "SO"
  elif year == "Junior":
    year_ab = "JR"
  elif year == "Senior":
    year_ab = "SR"

  return major_ab + "-" + year_ab

if __name__ == '__main__':
  main()
