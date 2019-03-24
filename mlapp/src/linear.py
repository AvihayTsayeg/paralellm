from parallelm.components.connectable_component import ConnectableComponent
from parallelm.mlops import mlops
from parallelm.mlops.stats.multi_line_graph import MultiLineGraph

from mlapp.src.printer.kprinter import print_data


class Linear(ConnectableComponent):
    def __init__(self, engine):
        super(self.__class__, self).__init__(engine)

    def _materialize(self, parent_data_objs, user_data):
        for param in parent_data_objs:
            prent_param = "parent param is: {param}".format(param=param)
            print_data(self._logger, prent_param)

        mlt = MultiLineGraph().name("Multi-line graph example").labels(["lable-1", "lable-2", "lable-3"])
        for x in range(100):
            mlt.data([x, x + 1, 0.5 * x])
            mlops.set_stat(mlt)

        return ["s3://Kenshoo/this is the linear model path/model.pmml"]
