from Tests.Add_to_Cart import TestCart
from Tests.sigin_grocery import TestSignInPage
from Tests.BaseTest import BaseTest


class Test_Execution_Class(BaseTest):

    driver = BaseTest().setUp()

    def test_homepage(self):

        uidriver = TestSignInPage(self.driver)
        uidriver.userName()
        uidriver.passwordEnter()
        uidriver.submit()
        uidriver.verifyMessage()
        uidriver.grocerystore()

    def test_addToCart(self):

        uidriver = TestCart(self.driver)
        uidriver.itemSearch("Bread")
        uidriver.addtocart1()
        uidriver.itemSearch("Milk")
        uidriver.addtocart1()
        uidriver.itemSearch("Jam")
        uidriver.addtocart1()
        uidriver.cartClick()
        uidriver.cartVerify()


