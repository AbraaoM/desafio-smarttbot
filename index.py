from datetime import datetime

import pandas

dataframe = pandas.read_csv('bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv')

startDate = "01/01/2020"#input("Data de início (DD/MM/AAAA): ")
finishDate = "01/02/2020"#input("Data de fim (DD/MM/AAAA): ")

startDateTimestamp = datetime.timestamp(datetime.strptime(startDate, "%d/%m/%Y"))
finishDateTimestamp = datetime.timestamp(datetime.strptime(finishDate, "%d/%m/%Y"))

interval = dataframe[dataframe['Timestamp'] >= startDateTimestamp]

interval = interval[interval['Timestamp'] <= finishDateTimestamp]

print(interval)