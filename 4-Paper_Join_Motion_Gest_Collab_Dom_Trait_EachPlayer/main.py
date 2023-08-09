#THIS CODE ADD COLLABORATION, DOMINANCE, AND TRAITS TO ME MORMED
#must check the output using R and uploading R code in github
import Importing_all_files_in_list_1
import Check_existed_folder_to_create_2
import CSV_DF_reader
import DFToCSV
import MergGestFiles
input_file_norm = "iOutpu_Normalized_MinMax_Motion_Players_CorrectedID_AcrosSessions"
#Creating output folder
output_folderCSV = "Output_Join_Motion_Collab_Dom_Trait_Per_Session_WithinSession_"
output_file=output_folderCSV+"/Output_Join_Motion_Collab_Dom_Trait_Per_Session_WithinSession_.csv"
finaloutputfoler = Check_existed_folder_to_create_2.createfolder ()
finaloutputfoler.createfolder (output_folderCSV)
############################################################
input_file_motion = "iCSV_Output_Gesture_Frame_Timestampe"
output_merged_gest="BigAggregatedGest.csv"
finaloutputfoler = Check_existed_folder_to_create_2.createfolder ()
finaloutputfoler.createfolder (output_folderCSV)
output_file_merged_gest=output_merged_gest+"/MergeGest.csv"

merg_gestf=MergGestFiles.MergGestFiles()#AGGREGATE ALL GEST FILES
merg_gestf.mergGestFiles(input_file_motion,output_merged_gest)

#IMPORTING THE BIG GEST FILE
csvdfreader = CSV_DF_reader.CSVDFReader ()
df_gest=csvdfreader.csvdfReader (output_merged_gest)
############################################################
#IMPORTING ALL MOTION FILES
motion_files = Importing_all_files_in_list_1.importingfiles ()
motion_files.get_candidates (input_file_norm)
print ("*" * 100)
print (motion_files.filelist)
lst_files_motion_norm= motion_files.filelist
####################################################
#reading collaboration score
input_file_collab = "Collaboration/collaboration_assessment.csv"
#IMPORTING ALL Collaboration FILES
csvdfreader = CSV_DF_reader.CSVDFReader ()
df_collab=csvdfreader.csvdfReader (input_file_collab)
######################
#reading Dominance score
input_file_dominance = "Dominance/MedianDomScoreEachPlayer.csv"
#IMPORTING ALL DOMINANCE FILES
csvdfreader = CSV_DF_reader.CSVDFReader ()
df_dom=csvdfreader.csvdfReader (input_file_dominance)
######################

#######################
for file in lst_files_motion_norm:
    # READING motion FILE
    csvdfreader = CSV_DF_reader.CSVDFReader ()
    df_norm = csvdfreader.csvdfReader (file)
    ######## adding bfi features
    # Merge 'df1' with 'df2' based on the common key 'Key_Column'
    temp_df_aggregated_1 = df_norm.merge (df_collab[['Session', 'MedianCollaboration']], on='Session',
                                          how='left')  # add collab to each session
    temp_df_aggregated_2 = temp_df_aggregated_1.merge (df_collab[['Session', 'Deltai']], on='Session',
                                                  how='left')  # add deltai to each session
    temp_df_aggregated_3 = temp_df_aggregated_2.merge (df_dom[['ID', 'MedianDomScore']], on='ID',
                                                       how='left')  # add dominance to each session
    print()
########################################################
    df_aggr_gest_motion = temp_df_aggregated_3.merge (df_gest[['ID', "Frame","Gesture"]], on=["ID","Frame"], how='left')  # add dominance to each session

    dftocsv = DFToCSV.DfToCSV ()
    dftocsv.dfToCSV (df_aggr_gest_motion, output_file)

#
