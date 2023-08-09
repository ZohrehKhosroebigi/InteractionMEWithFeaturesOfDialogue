from sklearn.preprocessing import MinMaxScaler

class MinMax():

    def minMax(self,df_file,header):
        self.df_norm=df_file
        # create a scaler object
        scaler = MinMaxScaler ()
        # fit and transform the data.
        self.df_norm[[header]] = scaler.fit_transform (self.df_norm[[header]])
        self.df_norm[[header]]=self.df_norm[[header]].round(4)
        return self.df_norm

