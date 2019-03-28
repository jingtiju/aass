import allure, pytest

class Test_1:
    @allure.step(title="66666")
    def test_1(self):
        print("*" * 50)
        allure.attach("111", "111111", allure.attach_type.TEXT)
        with open("./cc.jpg", "rb") as f:
            allure.attach("aa", f.read(), allure.attach_type.JPG)
        assert True
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_2(self):
        print("#" * 50)
        allure.attach("2222", "2222", allure.attach_type.TEXT)

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_3(self):
        print("#" * 50)
        allure.attach("2222", "2222", allure.attach_type.TEXT)

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_4(self):
        print("#" * 50)
        allure.attach("2222", "2222", allure.attach_type.TEXT)

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_5(self):
        print("#" * 50)
        allure.attach("2222", "2222", allure.attach_type.TEXT)

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_6(self):
        print("#" * 50)
        allure.attach("2222", "2222", allure.attach_type.TEXT)