import csv
class TgridToText():
    def gridtext(self,inputfile,outputfolder):
        for file in inputfile:

            readingfile=open(file,"r",errors='ignore')
            newname=file.split("/")
            name=outputfolder+"/"+newname[1]
            wrtingfile=open(name,"w")

            #count lines
            nline=0
            interval_size=0
            for line in readingfile:
                nline+=1
                line=line.strip()
                #line that includes interval size

                if line.find("intervals: size =")>-1:
                    info=line.split("=")
                    #it contains the size of invervals
                    interval_size=info[1].strip()
                #if line.find("xmin =") :

                if line.find("xmin =")>-1 and interval_size!=0:
                    #print (line.find ("xmin ="))

                    wrtingfile.write(line+",")
                elif line.find ("xmax =")>-1 and interval_size!=0:
                    wrtingfile.write (line + ",")
                elif line.find ("text =")>-1 and interval_size!=0:
                    wrtingfile.write (line + str(",f1 = ")+str("0")+ str(",f2 = ")+str("0")+ str(",f3 = ")+str("0")+ str(",f4 = ")+str("0")+ str(",f5 = ")+str("0")+ str(",f6 = ")+str("0")+ str(",f7 = ")+str("0")+ str(",f8 = ")+str("0")+ str(",f9 = ")+str("0")+
                                      str(",f10 = ")+str("0") + str(",f11 = ")+str("0")+ str(",f12 = ")+str("0")+ str(",f13 = ")+str("0")+ str(",f14 = ")+str("0")+ str(",f15 = ")+str("0")+ str(",f16 = ")+str("0") + str(",f17 = ")+str("0")+ str(",f18 = ")+str("0")+ str(",f19 = ")+str("0")+
                                      str(",f20 = ")+str("0")+str(",f21 = ")+str("0")+ str(",f22 = ")+str("0")+ str(",f23 = ")+str("0")+ str(",f24 = ")+str("0")+ str(",f25 = ")+str("0")+str(",f26 = ")+str("0")+str(",f27 = ")+str("0")+str(",f28 = ")+str("0")+
                                      str(",f29 = ")+str("0")+
                                      str(",f30 = ")+str("0")+str(",f31 = ")+str("0")+str(",f32 = ")+str("0")+str(",f33 = ")+str("0")+str(",f34 = ")+str("0")+"\n")
            readingfile.close()
            wrtingfile.close()
            readingfile=open(name,"r")
            nline=0
            for line in readingfile:
                nline+=1

            if nline!=int(interval_size):
                print("The number of lines are not eqaul")
                print(nline)
                print(interval_size)

