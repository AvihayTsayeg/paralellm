from parallelm.components.connectable_component import ConnectableComponent
from parallelm.mlops import mlops
from parallelm.mlops.stats.table import Table

from printer.kprinter import print_data


class Logistic(ConnectableComponent):
    def __init__(self, engine):
        super(self.__class__, self).__init__(engine)
        print_data(self._logger, "***************Logistic**********************")


    def _materialize(self, parent_data_objs, user_data):
        print_data(self._logger, "***************Logistic**********************")
        for param in parent_data_objs:
            prent_param = "logistic -----------> parent param is: {param}".format(param=param)
            print_data(self._logger, prent_param)

        tbl = Table().name("Table example").cols(["Worker", "Requests"])
        for index in range(0, 10):
            tbl.add_row(["kenshoo-worker-{}".format(index), index + 3])
        mlops.set_stat(tbl)

        return ["s3://Kenshoo/this is the logistic model path/model.pmml"]
