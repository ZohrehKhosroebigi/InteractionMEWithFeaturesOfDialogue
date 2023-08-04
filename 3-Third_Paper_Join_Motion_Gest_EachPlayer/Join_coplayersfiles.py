#This class takes one file_Grid and add to dict and then take another one and check if the same session is and joint same sessions together
import GetName
class JoinColumns():
    def __init__(self):
        self.getname= GetName.GetName()
        self.dict_pairs_files={}
    def joinClumns(self,file):
        player,session,rst=self.getname.getName(file)
        sessionnames=self.dict_pairs_files.keys()
        if session not in sessionnames:
            self.dict_pairs_files[session]=[file]
        elif session in sessionnames:
            tmplst=[]
            tmplst=self.dict_pairs_files[session]
            player_old, session_old, rst_old = self.getname.getName (tmplst[0])
            player_old=player_old.split("P")
            player_old=int(player_old[1])
            player=player.split("P")
            player=int(player[1])
            if player_old>player:
                tmplst.insert(0,file)
            elif player_old< player:
                tmplst.append(file)
            self.dict_pairs_files[session]=tmplst
        return self.dict_pairs_files





