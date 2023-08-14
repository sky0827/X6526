import yaml
import logging.config
import csv

class Util:
    # 读取配置文件
    @classmethod
    def get_conf(cls):
        with open ('../config/conf.yaml','r',encoding='UTF-8') as f:
            data=yaml.load(f,Loader=yaml.FullLoader)
            return data   # 以字典格式返回配置文件中的所有内容

    # 读取测试数据
    @classmethod
    def get_testdata(cls,csv_file,line):
        logging.info('=========开始读取login测试数据=========')
        with open ('../data/login.csv','r',encoding='UTF-8') as f:
            reader=csv.reader(f)
            for index,data in enumerate(reader,1):
                if index == line:
                    return data

# 将配置文件设置为全局
conf_file=Util.get_conf()['loggerConfigPath']
logging.config.fileConfig(conf_file)  # 查找到配置文件存放的路径
logger=logging.getLogger() # 设置配置文件全局变量

if __name__ == '__main__':
    print(Util.get_testdata(Util.get_conf()['testData'],2))
