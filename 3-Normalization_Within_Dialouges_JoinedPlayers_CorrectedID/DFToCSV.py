import os
class DfToCSV():
    def dfToCSV(self,dataframe,filename):


        # Check if the CSV file already exists
        if os.path.exists(filename):
            # Append the DataFrame without the header
            dataframe.to_csv(filename, mode='a', header=False, index=False)
        else:
            # Write the DataFrame with the header
            dataframe.to_csv(filename, index=False)