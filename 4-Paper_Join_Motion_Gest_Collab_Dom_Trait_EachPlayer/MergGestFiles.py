#THIS CODE MERGE GESTURES FILES OF PLAYERS AS A BIG FILE
import Importing_all_files_in_list_1
import CSVwriter
import CSVreader
class MergGestFiles():
    def mergGestFiles(self,gestfolder,out):

        input_file = gestfolder

        # Reading files from folder
        # Becareful there should not be may things except folders

        files = Importing_all_files_in_list_1.importingfiles ()
        files.get_candidates (input_file)
        print ("*" * 100)
        print (files.filelist)
        lst_files = files.filelist

        for file in lst_files:
            print ("start to read: ", file)
            csvreader = CSVreader.CSVReader ()
            lst_all_rows_plyr = csvreader.csvReader (file)

            csvwrt = CSVwriter.CSVWriter ()
            csvwrt.csv_wrt(lst_all_rows_plyr, out)






