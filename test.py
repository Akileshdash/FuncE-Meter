from pandas import isna
from pyJoules.handler.csv_handler import CSVHandler
from pyJoules.energy_meter import measure_energy
import pandas as pd
import time
a = [1, 2, 3, 4]
df_0 = pd.read_csv('/home/shiva/Downloads/data.csv')

handler = CSVHandler("pandas-isna-2024-12-02 15:46:24.550676.csv")

evaluated_args = {}
raw_args = {}
for key, value in raw_args.items():
    try:
        evaluated_args[key] = eval(value, globals(), locals())
    except Exception as e:
        evaluated_args[key] = value

measure_energy(isna, handler=handler)(**evaluated_args)
handler.save_data()
