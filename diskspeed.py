import time, os, sys

def writetofile(filename,mysizeMB):
    mystring = "Live like Jumanji"
    writeloops = int(100000*mysizeMB/len(mystring))
    try:
        f = open(filename, 'w')
    except:
        raise
    for x in range(0, writeloops):
        f.write(mystring)

    f.close()
    os.remove(filename)


def diskspeedmeasure(dirname):
    filesize = 1
    maxtime = 0.5
    filename = os.path.join(dirname,'outputTESTING.txt')
    start = time.start()
    loopcounter = 0
    while True:
        try:
            writetofile(filename, filesize)
        except:
            raise
        loopcounter +=1
        diff = time.time() - start
        if diff > maxtime:
            break
    return (loopcounter*filesize)/diff


if __name__ == "__main__":
    
    if len(sys.argv) >=2:
        dirname = sys.argv[1]
        if not os.path.isdir(dirname):
            print("Specific Argument is not a directory. Start over")
            sys.exit(1)
    else:

        dirname = os.getcwd()
        print("Use Current Working Directory")

    try:

        speed = diskspeedmeasure(dirname)
        print("`Disk writing speed: %.2f Mbytes per second" % speed )
    except IOError, e:
        if e.errno == 13:
            print("Cannot Create Test file. Chech the directory rights", dirname)
    except:
        print("Something went wrong, Chech Connection")
        raise 

    print("DONE")
    