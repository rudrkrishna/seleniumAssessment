from Tests.Add_to_Cart import TestCart
from Tests.filter_besan import Test_filter
from Tests.sigin_grocery import TestSignInPage
from Tests.BaseTest import BaseTest


class Test_Execution_Class(BaseTest):

    # webdriver setup
    driver = BaseTest().setUp()

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






