import os
import schedule
from bs4 import BeautifulSoup
import requests
import json
import time
import shutil
from apscheduler.schedulers.blocking import BlockingScheduler
import logging


class Monitor:
    headers = {'content-type': 'application/json'}
    report_filepath = "/root/ChromeDownload/test/report/html/"
    jtl_filepath = "/root/ChromeDownload/test/report/jtl/"
    run_filepath = "/root/ChromeDownload/test"
    his_filepath = "/root/ChromeDownload/test/his_report/"

    def test(self):
        # os.chdir("/root/ChromeDownload/test")
        # logging.basicConfig(format='%(asctime)s %(message)s', filename='logging.log', level=logging.INFO)
        # logging.info("开始执行！")
        # 先删除html文件
        os.chdir(self.report_filepath)
        files = os.listdir(self.report_filepath)
        if len(files) > 0:
            for f in files:
                os.remove(f)
        # 再删除jtl文件
        os.chdir(self.jtl_filepath)
        jtl_files = os.listdir(self.jtl_filepath)
        if len(jtl_files) > 0:
            for j in jtl_files:
                os.remove(j)
        # 执行脚本
        print("开始执行！")
        os.chdir(self.run_filepath)
        os.system("ant")
        print("执行成功！")
        # 执行完成后将报告复制到历史记录中
        time_str = time.strftime("%Y%m%d-%H:%M-",time.localtime())
        os.chdir(self.report_filepath)
        files = os.listdir(self.report_filepath)
        if len(files) > 0:
            shutil.copyfile(self.report_filepath+"produce_TestReport.html", self.his_filepath+time_str+"produce_TestReport.html")
        # 报告文档查询错误数failureNum
        file = open("produce_TestReport.html", "r", encoding="utf-8")
        soup = BeautifulSoup(file, 'lxml')
        failureNum = soup.select("#failureNum")[0].get_text()
        num = int(failureNum)
        print(num)
        if num > 0:
            # print("接口监控报错！错误数："+str(num)+"\n报告名称："+"\n报告查看路径：https://www.baidu.com")
            data = {'msgtype': 'text', 'text': {"content": "接口监控报错！\n错误数："+str(num)+"\n报告名称："+time_str+"produce_TestReport.html"+"\n"
                    "报告查看路径：http://192.168.123.156:8090/"+time_str+"produce_TestReport.html"}}
            res = requests.post(
                "https://oapi.dingtalk.com/robot/send?access_token=827f4476678b6319c7e05b9a1f2df24bc3b46160165"
                "ca46db7676c33d9889831", headers=self.headers, data=json.dumps(data))
            print(res.status_code)
        self.find_slow_interface(soup)
        file.close()
        # os.chdir("/root/ChromeDownload/test")
        # logging.basicConfig(format='%(asctime)s %(message)s', filename='logging.log', level=logging.INFO)
        # logging.info("执行完成！")
        # logging.info("---------------------------------------")

    def find_slow_interface(self, soup):
        responseTime_list = soup.select("#responseTime")
        responseName_list = soup.select("#responseName")
        interface_list = soup.select("#interface")
        interface_set = []
        response_file = open(self.report_filepath + 'response_time.txt', 'w', encoding="utf-8")
        response_file.write('------------------------------------------------------------------\n')
        for i, k, y in zip(responseTime_list, responseName_list, interface_list):
            end = i.get_text().index(' ')
            response_time = i.get_text()[0: end]
            interface = y.get_text()
            if int(response_time) >= 3000 and interface not in interface_set:
                interface_set.append(interface)
                responseName = k.get_text()
                response_file.write(f"接口名称：{responseName} {interface}         {response_time}ms\n")
        response_file.close()


if __name__ == '__main__':
    m = Monitor()
    m.test()
