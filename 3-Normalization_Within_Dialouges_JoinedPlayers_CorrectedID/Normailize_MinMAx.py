import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# this class takes list of dict of player motion and create a dict for each palyer motion
class MinMax():

    def minMax(self,df_file,header):
        self.df_norm=df_file
        # create a scaler object
        scaler = MinMaxScaler ()
        # fit and transform the data.
        self.df_norm[[header]] = scaler.fit_transform (self.df_norm[[header]])

        return self.df_norm

