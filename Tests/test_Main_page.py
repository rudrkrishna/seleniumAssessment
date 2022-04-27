import time

from Tests.Add_to_Cart import TestCart
from Tests.filter_besan import Test_filter
from Tests.sigin_grocery import TestSignInPage
from Tests.BaseTest import BaseTest
from Tests.Address_manage import AddressTest

# class where the execution starts
class Test_Execution_Class(BaseTest):

    # webdriver setup
    baseTest = BaseTest()
    driver = baseTest.setUp()

    # method which runs the login and navigating to grocery store test case
    def test_homepage(self):
        # Instance of SignInPage class
        uidriver = TestSignInPage(self.driver)

        # calling the method which enters the username
        uidriver.userName()

        # calling the method which enters the password
        uidriver.passwordEnter()

        # calling the method which performs button click
        uidriver.submit()

        # verifying the login status
        uidriver.verifyMessage()

        # Entering the grocery store
        uidriver.grocerystore()

    # method which runs the add to cart test case
    def test_addToCart(self):

        # Instance of SignInPage class
        uidriver = TestCart(self.driver)

        # Searching for Braed in grocery
        uidriver.itemSearch(uidriver.item1)

        # Adding one Bread item to cart
        uidriver.addtocart1()

        # Searching for Milk in grocery store
        uidriver.itemSearch(uidriver.item2)

        # Adding one searched item to cart
        uidriver.addtocart1()

        # Searching for Item in grocery
        uidriver.itemSearch(uidriver.item3)

        # Adding one searched item to cart
        uidriver.addtocart1()

        # Navigating to cart page
        uidriver.cartClick()

        # verifying the cart for added products
        uidriver.cartVerify()

    # method which runs filter test case
    def test_Besan_filter(self):

        # Instance of SignInPage class
        uidriver = Test_filter(self.driver)

        # navigates to homepage
        uidriver.gotoHomePage()

        # searches for item
        uidriver.itemSearch(uidriver.searchData)

        # sets the filter
        uidriver.setfilter()

        # Verifies the filter
        uidriver.verifyFilter()
    # method which runs the manage address test case
    def test_manageAddress(self):

        uidriver = AddressTest(self.driver)
        uidriver.navigateToProfile()
        uidriver.manageAddr()
        uidriver.addNewAddr()
        uidriver.enterAddress()
        uidriver.saveAddress()
        uidriver.verifySavedAddress()

     # method which runs logout functionality test case
    def test_logoutandquit(self):
        uidriver = AddressTest(self.driver)
        uidriver.logout()
        self.baseTest.tearDown()








