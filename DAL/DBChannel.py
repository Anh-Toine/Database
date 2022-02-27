from DAL.DB import DB
from Entities.Channel import Channel
class DBChannel:

    data = DB()

    def get_all_channels(self):
        return self.data.execute_select("channel","genre","genre_id")
    
    def get_channel(self, channelid: int):
        return self.data.execute_select("channel","genre","genre_id", params={'channel_id':channelid})

    def add_channel(self, channel:Channel):
      pass
    
