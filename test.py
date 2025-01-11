
from functools import wraps
import time
import os
from pandas import array
import pandas
a = [1, 2, 3]


class EnergyTracker:
    def __init__(self):
        self.rapl_path = "/sys/class/powercap/intel-rapl"
        self.domains = self._get_domains()
        self.state = "idle"

    def _get_domains(self):
        socket = 0
        domains = {}
        while True:
            socket_path = self.rapl_path + "/intel-rapl:" + str(socket)
            if not os.path.exists(socket_path):
                break
            domains[open(socket_path+"/name").read().strip()
                    ] = socket_path + "/energy_uj"
            domain = 0
            while True:
                domain_path = socket_path + "/intel-rapl:" + \
                    str(socket) + ":" + str(domain)
                if not os.path.exists(domain_path):
                    break
                domains[open(domain_path+"/name").read().strip()
                        ] = domain_path+"/energy_uj"
                domain += 1
                print(
                    open(domains[open(domain_path+"/name").read().strip()]).read().strip())
            socket += 1
        return domains

    def _get_energy(self):
        energy = {}
        for domain in self.domains:
            energy[domain] = int(open(self.domains[domain]).read().strip())
        return energy

    def start(self):
        if self.state == "idle":
            self.start_energy = self._get_energy()
            self.start_time = time.time()
            self.state = "running"
        else:
            print("Already running")

    def stop(self):
        if self.state == "running":
            self.stop_energy = self._get_energy()
            self.stop_time = time.time()
            self.state = "idle"
        else:
            print("Not running")

    def compute(self):
        if self.state == "running":
            return
        energy = {}
        for domain in self.domains:
            energy[domain] = self.stop_energy[domain] - \
                self.start_energy[domain]
        return energy

    def save_csv(self, filename):
        energy = self.compute()
        duration = self.stop_time - self.start_time
        with open(filename, "w") as f:
            f.write("Domain, Energy (micro joules), Duration (s)\n")
            for domain in energy:
                f.write(f"{domain}, {energy[domain]}, {duration}\n")


def measure_energy(func, fname):
    @wraps(func)
    def wrapper(*args, **kwargs):
        et = EnergyTracker()
        et.start()
        result = func(*args, **kwargs)
        et.stop()
        et.save_csv(f"{fname}")
        return result
    return wrapper


evaluated_args = {}
raw_args = {'data': '[1,2]'}
for key, value in raw_args.items():
    try:
        evaluated_args[key] = eval(value, globals(), locals())
    except Exception as e:
        evaluated_args[key] = value
et = EnergyTracker()
et.start()
result = array(**evaluated_args)
et.stop()
et.save_csv(f"pandas-array-2025-01-09 05:50:27.846075.csv")
# measure_energy(array,'pandas-array-2025-01-09 05:50:27.846075.csv')(**evaluated_args)
