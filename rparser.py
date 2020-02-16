import utility
import re
from direction import Directions

FILE_1="test/test_data/normal_short_file.dat"
FILE_2="test/test_data/text_before_short_file.dat"
FILE_3="test/test_data/no_place_command.dat"
FILE_4="test/test_data/invalid_inbetween.dat"


class Parser:
    """Parser class is the class that takes the commands file path as input and genrates an array of commands which can
    then be refered by external clinets to determine the next command to execute.
    
    Raises:
        SyntaxError: In case the commands file is invalid this exception is raised.
    """
    
    #The list of commands that are valid
    validCommandNames=['PLACE','REPORT','LEFT','RIGHT','MOVE']
    
    def __init__(self,fileName:str):
        """The constructor takes a file name and reads through it to produce an array of commands to be refered to later.
        
        Arguments:
            fileName {str} -- The complete path of the file which contains the commands.
        
        Raises:
            SyntaxError: If the file of commands is invalid, this error is thrown.
        """
        self.source=fileName
        self.allCommands=[]
        valid,lineNo,message=self.isValid()
        if not valid:
            raise SyntaxError(f"The format of the input file '{fileName}' is not valid. Please check the file at line no {lineNo} for the error {message}.")
        self.makeCommandArray()


    def validatePlaceParameters(self,val:str[]):
        """This method takes an array of parameters that come along woth the PLACE command and 
        validates the parameters 
        
        Arguments:
            val {str[]} -- An array of strings containing the parameters to be validate.
        
        Returns:
            boolean -- True if all parameters passed through 'val' are valid. Otherwise returns false.
        """

        valid=False
        message=""

        if len(val)==3:
            try:
                x=int(val[0])
                valid= x>=0
            except:
                valid=False
                message="Non integer Value in X"
            try:
                y=int(val[1])
                valid=valid and y>=0 
            except:
                valid=False
                message="Non integer Value in Y"

            try:
                y=Directions.getDirectionValue(val[2])
            except:
                valid=False
                message=f"Unidentified direction in input file. Please ensure the values for direction are {Directions.validDirectionNames()}"

        return valid,message

# - The first valid command to the robot is a PLACE command, after that, any
#   sequence of commands may be issued, in any order, including another PLACE
#   command. The application should discard all commands in the sequence until
#   a valid PLACE command has been executed.

    def isValid(self):
        """Checks if the command file that is passed is in a valid format
        
        Returns:
            boolean,int,str -- If the format is valid, 
                                The line number of the error, if any.
                                The error message, if any.

        """
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
        """Converts the list of commands in a string format to a commands array. 
        """
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



class Command:
    """The class that represents one command read from the command file. It contains the following attributes.

        Attributes:
            name {str} -- The name of the commans
            parameters {str[]} -- An array of parameters which are associated with the command(name)

    """

    def __init__(self,line):
        """The constructor. This takes a string line as input and breakes it into a command and parameters, after validating them.
        
        Arguments:
            line {str} -- The command and paramaters as passed from the command file.
        """
        fullStr=utility.validateString(line).strip()
        splitStr=re.split("[ ,]{1}",fullStr)
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
            splitStr=re.split("[,]{1}",fullStr[commIndex+1:].strip())
            self.name=fullStr[0:commIndex].strip()
            self.parameters=[p.strip() for p in splitStr]

    def __eq__(self,val:Command):
        """The method is used to compare if two command objects have same values.
        
        Arguments:
            val {Command} -- The object against which this object is being compared to.
        
        Returns:
            boolean -- True if the command name and the list of parameters in order are matching.
        """
        if not isinstance(val,Command):
            return False
        
        if self.name==val.name and len(self.parameters)==len(val.parameters):
            for index in range(len(self.parameters)):
                if val.parameters[index]!=self.parameters[index]:
                    return False
        else:
            return False

        return True


    def __str__(self):str:
        """Generates a string equivalent of the Command object.
        
        Returns:
            str -- The string equivalent of the object.
        """
        return f"name={self.name} and parameters are {self.parameters}"
