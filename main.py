from DAL.DBChannel import DBChannel

channels = DBChannel()

list_channels = channels.get_all_channels()
single_channel = channels.get_channel(10)

print(single_channel)