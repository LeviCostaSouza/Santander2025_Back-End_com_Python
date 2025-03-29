from datetime import timezone,datetime,timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print (data_oslo)

print (data_sao_paulo)