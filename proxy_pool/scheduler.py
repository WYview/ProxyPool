TESTER_CYCLE=20
GETTER_CYCLE=20
TESTER_ENABLED=True
GETTER_ENABLED=True
API_ENABLED=True

from multiprocessing import Process
from .api import app
from .getter import Getter
from .tester import Tester
import time

class Scheduler():
    def schedule_tester(self,cycle=TESTER_CYCLE):
        """
        Test the proxy on time
        """
        tester=Tester()
        while True:
            print('Tester is running')
            tester.run()
            time.sleep(cycle)


    def schedule_getter(self,cycle=GETTER_CYCLE):
        """
        Get the proxy on time
        """
        getter=Getter()
        while True:
            print('Start to get the proxy')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        Start to run server in order to provide api to the user.
        """
        app.run()

    def run(self):
        """
        This is the api provided by class 'Scheduler' in order to let the user start this ProxyPool.
        """
        print('ProxyPool is starting to run')
        if TESTER_ENABLED:
            tester_process=Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process=Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process=Process(target=self.schedule_api)
            api_process.start()
        
