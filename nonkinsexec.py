from subprocess import Popen
def buildp(amt,btrli,buildc):
    buildc+=amt
    for i in range(0,len(btrli)):
        try:
            Popen(btrli[i])
        except Exception as err:
            print("Error: " + str(err) + " on string " + btrli[i])
