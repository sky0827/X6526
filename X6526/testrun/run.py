import unittest,time
from HTMLTestRunner import HTMLTestRunner
from common.util import Util

test_case_dir=Util.get_conf()['testCaseDir']
report_dir=Util.get_conf()['reportDir']

dis=unittest.defaultTestLoader.discover(test_case_dir,pattern='sound_test.py')   # 执行以_test结尾的py文件

#  生成测试报告执行
# now_time=time.strftime('%Y-%m-%d %H %M %S')  # 设置时间格式
# report_name=report_dir+'/'+now_time+'test_reoprt.html'  # 设置测试报告的名字
# runner=HTMLTestRunner(
#     title='百度首页搜索测试练习报告',
#     description='v1.0测试结果',
#     stream=open(report_name,'wb'),
#     verbosity=2
# )
# runner.run(dis)

runner=unittest.TextTestRunner()
runner.run(dis)