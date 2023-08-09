import os
import sys
import shutil


class createfolder():
    def createfolder(self,foldername):
        if not os.path.exists(foldername):
            os.makedirs(foldername)
            print("successful for "+str(foldername))
        """else:
            try:
                shutil.rmtree (foldername)
            except OSError as e:
                print ("Error: %s - %s." % (e.inputfile, e.strerror))
"""
