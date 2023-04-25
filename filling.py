for i in range(1620, 2002):
        f = open('/Volumes/2tDisk/newfile'+str(i),"wb")
        f.seek((1073741824)-1)
        f.write(b"\0")
        f.close()
        print("/Volumes/2tDisk/newfile"+str(i))
