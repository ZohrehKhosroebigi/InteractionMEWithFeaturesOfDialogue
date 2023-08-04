class AddingPlayerID():
    def addingPlayerID(self,df,pleft,pright):

        df[["LeftID"]] = pleft
        df[["RightID"]] = pright

        self.data=df
        return self.data

