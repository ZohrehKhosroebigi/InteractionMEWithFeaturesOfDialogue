#THIS CODE TAKE THE MEA TOOL OUTPUT AND KEEP FIRST COLUMN AND SAVE BY PLAYER ID AND SESSION NUMBER IN CSV FORMAT.
import Importing_all_files_in_list_1
import Check_existed_folder_to_create_2

import GetName
import CSVwriter
input_file_players = "Input_Players"
#Creating output folder
output_folderCSV = "Output_Motion_EachPly"
finaloutputfoler = Check_existed_folder_to_create_2.createfolder ()
finaloutputfoler.createfolder (output_folderCSV)
all_csv_file=output_folderCSV+"/Output_Motion_EachPly.csv"
############################################################
#IMPORTING ALL MOTION FILES
motion_files = Importing_all_files_in_list_1.importingfiles ()
motion_files.get_candidates (input_file_players)
print ("*" * 100)
print (motion_files.filelist)
lst_files_ply = motion_files.filelist

####################################################


###################################
fieldname = ["Session", "ID","Frame", "MotionEnergy"]#csv header
csvwrt = CSVwriter.CSVWriter ()
lst_all_rows=[]

#For players
for file in lst_files_ply: #pairedfiles[0] has left player pairedfiles[1] has right player
    getname = GetName.GetName ()
    lp, ls, _ = getname.getName (file)
    each_csv_file = output_folderCSV +"/"+ lp+"_"+ls+"_Motion_Ply.csv"

    readfile=open(file,"r")

    counter_frame=0


    for linep1 in  readfile:

        counter_frame+=1
        lst_row=[]
        linep1=linep1.split(" ")
        linep1=linep1[0]#just keep the first columns
        linep1 = linep1.strip ("\n")
        lst_row.append(linep1)
        lst_row.insert(0,counter_frame)
        lst_row.insert (0, lp)

        lst_row.insert(0,ls)
        csvwrt.csv_wrt_list (lst_row, each_csv_file,fieldname)#wrtie as big motionfile

        csvwrt.csv_wrt_list (lst_row, all_csv_file,fieldname)#wrtie as big motionfile


