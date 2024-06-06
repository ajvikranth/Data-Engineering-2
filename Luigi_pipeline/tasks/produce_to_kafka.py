import luigi
from kafka_produce.produce import produce

class KafkaProduce(luigi.Task):

    data = luigi.DictParameter()
    topic = luigi.Parameter()
    produced = False

    def run(self):
        self.produced = produce(str(self.topic),dict(self.data))

    def complete(self):
        return self.produced