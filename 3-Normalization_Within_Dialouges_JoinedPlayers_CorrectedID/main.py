
#THIS CODE IS NORMALIZATION USING MINMAX. NORMALIZATION IS ACROSS ALL SESSIONS.
#IT MEANS ME OF ALL PLAYERS ARE AGGREGATED. THEN MINMAX IS COMPUTED
import CSV_DF_reader
import Importing_all_files_in_list_1
import Check_existed_folder_to_create_2
import Normailize_MinMAx
import DFToCSV
import GetName
import pandas as pd

input_file = "iOutpu_Motion_Joined_C0_Players_CorrectedID"
output_norm= "Outpu_Normalized_MinMax_Motion_Players_CorrectedID_AcrosSessions"
csvname_ALL= output_norm + "/Outpu_Normalized_MinMax_Motion_Players_CorrectedID_AcrosSessions.csv"
finaloutputfoler = Check_existed_folder_to_create_2.createfolder ()
finaloutputfoler.createfolder (output_norm)


# Reading files from folder
# Becareful there should not be may things except folders

files = Importing_all_files_in_list_1.importingfiles ()
files.get_candidates (input_file)
print ("*" * 100)
print (files.filelist)
lst_files=files.filelist
#####################
wf = open ("report.txt", "w")
wf.write("Start\n")
#############################
#creat a list of names for df to have df for each player.
#The purpos is to creat a big file of each player info
lst_dfs_each_ply=[]
for i in range(len(lst_files)):
    lst_dfs_each_ply.append("df_left_"+str(i))
    lst_dfs_each_ply.append ("df_right_" + str (i))
#creat a dict of df
dict_df = {}
for i in lst_dfs_each_ply:
    dict_df[i] = pd.DataFrame ()
################################



for fileidx in range (len(lst_files)):
    df_left = pd.DataFrame ()
    df_right = pd.DataFrame ()

    print ("start to read: ", lst_files[fileidx])
    #reading file
    get_name= GetName.GetName()
    pleft, pright, session, _=get_name.getName(lst_files[fileidx])
    csvdfreader = CSV_DF_reader.CSVDFReader ()
    csvdfreader.csvdfReader(lst_files[fileidx])

    ##########
#ADDING VALUES TO EACH KEY OF DICT. IT CREATS TWO DICT OF CO-PLAYERS INFO
    dict_df["df_left_"+str(fileidx)]["Session"]=csvdfreader.df_motion["Session"]
    dict_df["df_left_"+str(fileidx)]["Frame"]=csvdfreader.df_motion["Frame"]
    dict_df["df_left_"+str(fileidx)]["MotionEnergy"]=csvdfreader.df_motion["LeftPlayerMotion"]
    dict_df["df_left_"+str(fileidx)]["ID"]=pleft
    dict_df["df_right_" + str (fileidx)]["Session"] = csvdfreader.df_motion["Session"]
    dict_df["df_right_" + str (fileidx)]["Frame"] = csvdfreader.df_motion["Frame"]
    dict_df["df_right_" + str (fileidx)]["MotionEnergy"] = csvdfreader.df_motion["RightPlayerMotion"]
    dict_df["df_right_" + str (fileidx)]["ID"] = pright

    print()

#CONCAT DF OF COPLAYERS TO HAVE AN AGGREGATED ONE.
df_all_players = pd.concat(dict_df.values(), join='inner', keys=dict_df.keys(), axis=0,ignore_index=True)

#calling normalization class min max
dict_norm_minmax= Normailize_MinMAx.MinMax ()
dict_norm_minmax.minMax(df_all_players,"MotionEnergy")

dftocsv= DFToCSV.DfToCSV()
dftocsv.dfToCSV(dict_norm_minmax.df_norm, csvname_ALL)




    
