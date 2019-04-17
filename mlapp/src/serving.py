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


    def _materialize(self, parent_data_objs, user_data):

        model_path = self._params["input-model"]
        self._logger.info("******************** reading model input file %s ***************" % model_path)
        with open(model_path, "r") as f:
            self._logger.info(f.readlines())
        self._logger.info("********************Finish reading model input file %s ***************" % model_path)


