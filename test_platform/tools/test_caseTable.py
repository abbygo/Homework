# abby
import time
from unittest import TestCase
from test_platform.tools.login_api import db, CaseTable

class TestCaseTable(TestCase):
    def test_add_case(self):
        case1 = CaseTable(case_title='登录页面样式与UI不一致', case_content='登录页面样式与UI不一致内容', case_author='123456',
                          case_project='ygfyy', case_executor='liyi', case_priority='高', case_remarks='优先测试',
                          case_create_time=time.strftime('%Y-%m-%d %H:%M', time.localtime())
                          )
        case2 = CaseTable(case_title='登录页面有错别字', case_content='登录页面有错别字内容', case_author='123456')
        db.session.add(case1)
        db.session.add(case2)
        db.session.commit()
