from Tests.Add_to_Cart import TestCart
from Tests.sigin_grocery import TestSignInPage
from Tests.filter_besan import Test_filter
class KeyWordDriver(TestCart, TestSignInPage, Test_filter):

    def __init__(self, driver):
        self.driver= driver
