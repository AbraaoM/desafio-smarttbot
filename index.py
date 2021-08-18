from datetime import datetime

import pandas
import numpy

def GetDatabase():
  dataframe = pandas.read_csv('bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv')

  startDate = "01/01/2020"#input("Data de início (DD/MM/AAAA): ")
  finishDate = "01/02/2020"#input("Data de fim (DD/MM/AAAA): ")

  startDateTimestamp = datetime.timestamp(datetime.strptime(startDate, "%d/%m/%Y"))
  finishDateTimestamp = datetime.timestamp(datetime.strptime(finishDate, "%d/%m/%Y"))

  interval = dataframe[dataframe['Timestamp'] >= startDateTimestamp]

  interval = interval[interval['Timestamp'] <= finishDateTimestamp]

  interval = interval.fillna(0)

  return interval


def CalculateEMA(data, emaPeriod = 10, applied_to = 'Close'):

  ema = [(numpy.nansum(data[applied_to].values[:emaPeriod])/emaPeriod)]
  factor = 2 / (emaPeriod + 1)

  for price in data[applied_to].values[emaPeriod+1:]:
    ema.append((price - ema[-1]) * factor + ema[-1])

  return ema

def CalculateBollBands(data, nDeviation = 2, period = 10, applied_to = 'Close'):
  bollBands = {"ema": [], "superiorBand": [], "inferiorBand": []}

  bollBands["ema"] = CalculateEMA(data, period, applied_to)

  for i in range(period, len(data[applied_to].values)):
    deviation = numpy.std(data[applied_to].values[(i-period):i])

    bollBands["inferiorBand"].append(bollBands["ema"][i-period] - nDeviation * deviation)
    bollBands["superiorBand"].append(bollBands["ema"][i-period] + nDeviation * deviation)
  return bollBands

data = GetDatabase()

print(len(data[:50]))
print(CalculateBollBands(data[:50]))




# print(interval['Open'].values)


