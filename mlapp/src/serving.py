try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain
pipmain(['install', 'ansible'])

from parallelm.components.connectable_component import ConnectableComponent
from parallelm.mlops import mlops
from parallelm.mlops.stats.bar_graph import BarGraph

from printer.kprinter import print_data


# noinspection PyUnresolvedReferences
from ansible import cli
# noinspection PyUnresolvedReferences
import requests

class Serving(ConnectableComponent):
    def __init__(self, engine):
        super(self.__class__, self).__init__(engine)
        self._logger.info(__file__)
        print_data(self._logger, "***************Serving**********************")

    def _materialize(self, parent_data_objs, user_data):
        print_data(self._logger, "***************Serving**********************")
        for param in parent_data_objs:
            prent_param = "serving -----------> parent param is: {param}".format(param=param)
            print_data(self._logger, prent_param)

        for k,v in self._params.items():
            params_info = "serving -----------> key: {key} ==> value: {value}".format(key=k, value=v)
            print_data(self._logger, params_info)

        mlt = BarGraph().name("Kenshoo Bar graph example").cols(["bar", "bar2"]).data([1500, 2000])
        mlops.set_stat(mlt)

        return []
