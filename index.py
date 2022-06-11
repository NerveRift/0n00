""""start docstring"""
import sys

# collect data from arguments
def main():
    """"main"""
    # get arguments
    args = sys.argv[1:]
    # check if there are arguments
    if len(args) == 0:
        # no arguments
        error("0n00-0000")
    else:
        # there are arguments
        # check if the arguments securityToken, questionID, answerGiven, exist
        if len(args) == 4:
            # get the arguments and place them into variables
            #securityToken = args[0]
            #questionID = args[1]
            #answerGiven = args[2]

            # check if the securityToken is valid

            # check if questionID is valid

            # get mark scheme if questionID is valid

            # mark answerGiven based on mark scheme

            # calculate score

            # print score

            # check if the security token is correct

            print("4 arguments")



# check if data contains valid security token
# if not, return error 0n00-0000
# if valid, continue


def error(arg):
    """"error"""
    # print error message
    print("Error: " + str(arg))


main()
