from parallelm.components.connectable_component import ConnectableComponent


class Linear(ConnectableComponent):
    def __init__(self, engine):
        super(self.__class__, self).__init__(engine)

    def _materialize(self, parent_data_objs, user_data):
        model_path = self._params["output-model"]
        self._logger.info("*****************writing model file %s ******************************" % model_path)
        with open(model_path, "w") as model_file:
            model_file.writelines(["line1", "line2", "line3"])
        self._logger.info("######################Finished writing model file %s ########################" % model_path)