from parallelm.components.connectable_component import ConnectableComponent
from parallelm.mlops import mlops

from mlapp.src.printer.kprinter import print_data


class Fetcher(ConnectableComponent):
    def __init__(self, engine):
        super(self.__class__, self).__init__(engine)

    def _materialize(self, parent_data_objs, user_data):
        for k,v in self._params.items():
            params_info = "key: {key} ==> value: {value}".format(key=k, value=v)
            print_data(self._logger, params_info)

        for x in range(100):
            mlops.set_stat("k graph", x)
        return ["s3://kenshoo/this is your report/report.txt"]


