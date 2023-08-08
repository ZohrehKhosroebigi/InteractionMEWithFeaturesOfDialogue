class GetName():
    def getName(self,file):
        tmp=file.split("/")
        tmp=tmp[1].split("_")
        self.player=tmp[0]
        self.session=tmp[1]
        self.rst=tmp[2]
        return self.player,self.session,self.rst