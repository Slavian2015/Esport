
import pandas as pd
import os
from datetime import datetime, timedelta
main_path_data = os.path.abspath("./data")


all_cardsBD = pd.read_csv(main_path_data + '\\all_cards.csv')
id = 373736
df = all_cardsBD[(all_cardsBD['Mid'].isin([id]))]




timer = df.iloc[0]['Mdate'] + ' ' + df.iloc[0]['Mtime']
print(timer)
server_time = datetime.now()
print(server_time)


timer = pd.to_datetime(timer)
server_time = (server_time + timedelta(hours=10))
server_time = pd.to_datetime(server_time)
diff = server_time - timer
# print(diff)


totalMinute, second = divmod(diff.seconds, 60)
hour, minute = divmod(totalMinute, 60)
dif = f"{hour}:{minute:02}:{second:02}"
# print(dif)

if diff > pd.Timedelta(0):
    print("1")



else:
    print("2")
