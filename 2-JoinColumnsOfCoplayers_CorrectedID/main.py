#THIS CODE TAKE MOTION ENERGY FILES IN ONE COLUMN FORMAT AND JOIN THE COLUMNS OF CO-PLAYERS

#*****NOTE: CORRECT THE LEFT, RIGHT AND ORDER OF PLAYERS NUMBER MANUALY.
#NOTE LEFT SHOULD BE AT FIRST AND THEN RIGHT, THE ORDER IS IMPORTANT DURING WRITING IN CSV FILE

import Importing_all_files_in_list_1
import Check_existed_folder_to_create_2
import CSVwriter
import GetName
import pandas as pd

#######################################
input_file = "iOutput_Motion_EachPly"
output_joined= "Outpu_Motion_Joined_C0_Players"
csvname_ALL= output_joined + "/Outpu_Motion_Joined_C0_Players.csv"
finaloutputfoler = Check_existed_folder_to_create_2.createfolder ()
finaloutputfoler.createfolder (output_joined)
# Reading files from folder

files = Importing_all_files_in_list_1.importingfiles ()
files.get_candidates (input_file)
print ("*" * 100)
print (files.filelist)
lst_files=files.filelist


#####CREATE A DICT THAT EACH SESSION IS THE KEY AND FILE OF THE SESSION, MEANS PLYAERS IN THE SESSION ARE THE VALUE OF THE KEY
dict_session_files={}
for file in lst_files:
    getname= GetName.GetName()
    ply,session,_=getname.getName(file)
    if session in list(dict_session_files.keys()):
        dict_session_files[session]= dict_session_files[session], file
    else:
        dict_session_files[session]=file
##############################################

for session_number, player_file in dict_session_files.items():

#EXTRACTING THE PLAYER ID AND SESSION NUMBER FOR EACH FILE
    getname = GetName.GetName ()
    ply1, session, _ = getname.getName (player_file[0])
    getname = GetName.GetName ()
    ply2, session, _ = getname.getName (player_file[1])
    print(session)
    filename=ply1+"_"+ply2+"_"+session+"_"+"_Motion_Joined_C0_Players.csv"
    outputfile=output_joined+"/"+filename
    df1 = pd.read_csv (player_file[0], index_col=None, header=0)
    df2=pd.read_csv (player_file[1], index_col=None, header=0)
    for item1, item2 in zip(df1.iterrows(),df2.iterrows()):
        file1=item1[1]# to ignore index
        file2=item2[1]# to ignore index
        file1=file1.to_dict()#convert series to dict
        file2=file2.to_dict()#convert series to dict
        #JOIN BOTH PLAYERS INFO
        dict_joined={}
        dict_joined={"Session":file1["Session"], "Frame":file1["Frame"], "LeftPlayerMotion":file1["MotionEnergy"], "RightPlayerMotion":file2["MotionEnergy"]}
        csv_wrt= CSVwriter.CSVWriter()
        csv_wrt.csv_wrt_dict_auto(dict_joined, outputfile)




#
#
