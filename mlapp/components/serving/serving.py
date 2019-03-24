from parallelm.components.connectable_component import ConnectableComponent
from parallelm.mlops import mlops
from parallelm.mlops.stats.bar_graph import BarGraph


class Serving(ConnectableComponent):
    def __init__(self, engine):
        super(self.__class__, self).__init__(engine)

    def _materialize(self, parent_data_objs, user_data):
        for param in parent_data_objs:
            prent_param = "parent param is: {param}".format(param=param)
            print(prent_param)
            self._logger.info(prent_param)

        for k,v in self._params.items():
            params_info = "key: {key} ==> value: {value}".format(key=k, value=v)
            print(params_info)
            self._logger.info(params_info)

        mlt = BarGraph().name("Kenshoo Bar graph example").cols(["bar", "bar2"]).data([1500, 2000])
        mlops.set_stat(mlt)

        return []
