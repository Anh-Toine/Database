class Channel:
    id = 0
    genreid = 0
    channelname = ""
    creationdate = ""
    verified = False
    def __init__(self,genreid:int, channelname:str, creationdate:str, verified:bool):
        self.genreid = genreid
        self.channelname = channelname
        self.creationdate = creationdate
        self.verified = verified
