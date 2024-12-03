import time
import io
import contextlib
import datetime

MEASURE_ENERGY_IMPORT = "from pyJoules.energy_meter import measure_energy"
CSV_HANDLER_IMPORT = "from pyJoules.handler.csv_handler import CSVHandler"
INIT_DATA = open("init.config").read()


class Runner:

    def run(self, mname: str, fname: str, args, frquency: int, interval: int, csv: str, dataset: dict) -> str:
        output = io.StringIO()
        dataframes = """import pandas\n"""
        for data in dataset:
            dataframes += f"""{data} = pandas.read_csv("{dataset[data]}")\n"""
        with contextlib.redirect_stdout(output):
            for _ in range(frquency):
                if not csv:
                    csv = f"{mname.strip()}-{fname.strip()}-{datetime.datetime.now()}.csv"
                try:
                    exec(
                        f"""
{INIT_DATA}
{dataframes}
{MEASURE_ENERGY_IMPORT}
{CSV_HANDLER_IMPORT}
handler = CSVHandler("{csv}")
from {mname.strip()} import {fname}

evaluated_args = {{}}
raw_args = {args}
for key, value in raw_args.items():
    try:
        evaluated_args[key] = eval(value, globals(), locals())
    except Exception as e:
        evaluated_args[key] = value  

measure_energy({fname}, handler=handler)(**evaluated_args)
handler.save_data()

""")
                    time.sleep(interval)
                except SyntaxError as e:
                    print("Syntax Error:")
                    print(f"Message: {e.msg}")
                    print(f"Line: {e.lineno}, Offset: {e.offset}")
                    print(f"Text: {e.text.strip() if e.text else None}")
                except Exception as e:
                    print(f"Exception occurred:{e}")
        return output.getvalue() + f"Wrote measurement to {csv}"
