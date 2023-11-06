# classmethod
class By:

    CSS_SELECTOR = 'css selector'
    XPATH = 'xpath'

    @classmethod
    def valid(cls, value):
        return value in (cls.CSS_SELECTOR, cls.XPATH)


print(By.valid('css selector'))
