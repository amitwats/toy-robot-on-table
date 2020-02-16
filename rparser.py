import utility
import re
from direction import Directions

FILE_1="test/test_data/normal_short_file.dat"
FILE_2="test/test_data/text_before_short_file.dat"
FILE_3="test/test_data/no_place_command.dat"
FILE_4="test/test_data/invalid_inbetween.dat"


class Parser:
    
    validCommandNames=['PLACE','REPORT','LEFT','RIGHT','MOVE']
    
    def __init__(self,fileName):
        self.source=fileName
        self.allCommands=[]
        valid=self.isValid()
        if not valid:
            raise SyntaxError(f"The format of the input file '{fileName}' is not valid. Please check the file")
        self.makeCommandArray()



    # Valid format is below
    #
    # PLACE X,Y,F
    # MOVE
    # LEFT
    # RIGHT
    # REPORT

    # def getCommandType(val):
    #     fullStr=utility.validateString(val)
    #     splitStr=fullStr.split(" ")
    #     if len(fullStr)==0: return ""
    #     else: return splitStr[0]

    # def processCommand(self,cmd):
    #     pass

    def validatePlaceParameters(self,val):
        valid=False
        message=""
        valid=valid and val.len==3
        try:
            x=int(val[0])
            valid=True
        except:
            valid=False
            message="Non integer Value in X"

        try:
            y=int(val[1])
            valid=True
        except:
            valid=False
            message="Non integer Value in Y"

        try:
            y=Directions.getDirectionValue(val[2])
            valid=True
        except:
            valid=False
            message=f"Unidentified direction in input file. Please ensure the values for direction are {Directions.validDirectionNames()}"

        valid=valid and isinstance(val[0],int),message

# - The first valid command to the robot is a PLACE command, after that, any
#   sequence of commands may be issued, in any order, including another PLACE
#   command. The application should discard all commands in the sequence until
#   a valid PLACE command has been executed.

    def isValid(self):
        # check the first PLACE command
        startParsing=False
        lineNo=0
        message="No starting command found. The input should have atleast 1 PLACE command."
        with open(self.source) as fil:
            for line in fil:
                lineNo=lineNo+1
                command=Command(line)
                if not startParsing:
                    if command.name=="PLACE":
                        startParsing=True
                if startParsing:
                    if command.name not in Parser.validCommandNames:
                        return False,lineNo,f"The command {command.name} on line {lineNo} is invalid."
                    if command.name=="PLACE":
                        self.validatePlaceParameters(command.parameters)
        if startParsing:
            return True,lineNo,message
        else:
            return False,lineNo,"No starting command found. The input should have atleast 1 PLACE command."




    def makeCommandArray(self):
        # check the first PLACE command
        self.allCommands=[]
        startParsing=False
        with open(self.source) as fil:
            for line in fil:
                command=Command(line)
                if not startParsing:
                    if command.name=="PLACE":
                        startParsing=True
                if startParsing:
                    if command.name in Parser.validCommandNames:
                        self.allCommands.append(command)



        #     lines=[line.strip() for line in f]
        
        
        # for line in lines:
        #     print(Parser.getCommandType(line))        

        # pass

class Command:

    # def getCommandType(val):
    #     fullStr=utility.validateString(val)
    #     splitStr=fullStr.split(" ")
    #     if len(fullStr)==0: return ""
    #     else: return splitStr[0]


    def __init__(self,line):
        fullStr=utility.validateString(line).strip()
        # splitStr=fullStr.split(" ")
        splitStr=re.split("[ ,]{1}",fullStr)
        
        splitStrBlank=re.split("[ ]]{1}",fullStr)
        commIndex=fullStr.find(" ")
        if commIndex>0:
            comm=fullStr[0:commIndex]
        else:
            comm=fullStr

        if len(comm)==0: 
            self.name= ""
            self.parameters=[]
        elif commIndex<=0:
            self.name= fullStr
            self.parameters=[]
        else:
            splitStr=re.split("[,]{1}",fullStr[commIndex:])
            self.name=fullStr[0:commIndex].strip()
            self.parameters=splitStr


        # if len(fullStr)==0: 
        #     self.name= ""
        #     self.parameters=[]
        # else: 
        #     self.name=splitStr[0]
        #     self.parameters=splitStr[1:]

    def __str__(self):
        return f"name={self.name} and parameters are {self.parameters}"
        
# read LINE until you find the first PLACE line
# 
# read line
#TRIM LINE
# determine type of command, remember PLace CAN RE-OCCUrE 
#   PLACE, MOVE, REPORT
# IF PLACE

def testFile():
    testFileName="test/test_data/normal_short_file.dat"

    with open(testFileName) as f:
        lines=[line.rstrip() for line in f]
    for line in lines:
        print(Parser.getCommandType(line))

def testConstructor():
    testFileName="test/test_data/normal_short_file.dat"
    p=Parser(testFileName)
    p.isValid()

def testCommand():
    # c=Command("PLACE 5,5,NORTH")
    c=Command("REPORT")
    # c=Command("")
    #print(c)
    print(c.name)
    print(c.parameters)

def testParsing():
    p=Parser(FILE_1)
    #p=Parser(FILE_3)
    #p=Parser(FILE_4)
    p=Parser(FILE_2)
    print(p.source)
    x=p.isValid()
    print(f"The val is {p.isValid()}")
    print(f"Iteratimg the command array")
    for cm in p.allCommands:
        print(cm)

if __name__ == "__main__":
    # testFile()
    #testConstructor()
    #testCommand()
    testParsing()
    pass

