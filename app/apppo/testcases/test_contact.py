"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/7 4:16 下午'
"""
import yaml

from app.apppo.page.app import App


class TestContact:
    def setup_class(self):
        self.app = App().start()

    def setup(self):
        self.main = self.app.goto_main()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        name = "hogwarts_5"
        phonenum = "13100000005"
        editpage = self.main.goto_addresslist().click_addcontact().addcontact_menual()
        editpage.edit_contact(name, phonenum)
        editpage.verify_ok()

    # def test_delcontact(self):
    #     name = "hogwarts_3"
    #
    def test_yaml(self):
        # pyyaml
        with open("../datas/caps.yml") as f:
            datas = yaml.safe_load(f)

            print(datas)
            # desires = datas['desirecaps']
            # ip = datas['server']['ip']
            # port = datas['server']['port']
