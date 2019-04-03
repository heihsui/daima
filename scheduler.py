import time

from multiprocessing import Process

from proxypool.api import app
from proxypool.getter import Getter
from proxypool.setting import *
from proxypool.tester import Tester


class Scheduler():
    def schedule_tester(self,cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self,cycle=GETTER_CYCLE):
        """
        定时获取代理
        :param cycle:
        :return:
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API
        :return:
        """
        app.run(API_HOST,API_PORT)

    def run(self):
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        if GETTER_ENABLED:
            tester_process = Process(target=self.schedule_getter)
            tester_process.start()
        if API_ENABLED:
            tester_process = Process(target=self.schedule_api)
            tester_process.start()

if __name__ == '__main__':
    Scheduler()