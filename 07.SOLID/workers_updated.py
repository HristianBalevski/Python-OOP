from abc import ABC, abstractmethod
import time


class AbstractWorker(ABC):

    @abstractmethod
    def work(self):
        pass

    def eat(self):
        pass


class Workable(AbstractWorker, ABC):
    def work(self):
        print("I'm normal worker. I'm working.")


class Eatable(AbstractWorker, ABC):
    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class Worker(Workable, Eatable):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)

        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        self.worker.eat()


class Robot(Workable, ABC):

    def work(self):
        print("I'm a robot. I'm working....")


manager = Manager()
manager.set_worker(Worker())
manager.manage()
manager.lunch_break()

manager.set_worker(SuperWorker())
manager.manage()
manager.lunch_break()

manager.set_worker(Robot())
manager.manage()
manager.lunch_break()
