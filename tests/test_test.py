class TestSuite():

    def test_case_1(self, case_data):
        check = "print lol.py"
        data_in_project = case_data
        assert(check == data_in_project)

    def test_greet_user(self, case_data_2):
        check_2 = 'Вас приветствует salon_service_bot!'
        data_in_project = case_data_2
        assert(check_2 == data_in_project)