class DecTest(object):
    """
    Testing the use of decorators and an init method.
    """

    def __init__(self, inName='NoName'):
        """Set some defaults for this class"""
        # Changing '_name' to 'name' still works, why?
        self._internal_name = inName

    @property
    def name(self):
        return self._internal_name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            # Why do i need to use '_name' and not 'name'?
            self._internal_name = value
        else:
            raise ValueError('Expected String! Got %s' % type(value))

if __name__ == '__main__':
    # Should Use Setter and Getter
    decNoInit = DecTest()
    decNoInit.name = 'Matt'
    assert decNoInit.name == 'Matt'
    print 'decNoInit: %s' % decNoInit.name

    # Attempting to alter a 'private' variable directly.
    decAlterPrivateAttr = DecTest('Matt')
    assert decAlterPrivateAttr.name == 'Matt'
    print 'decAlterPrivateAttr Default Value: %s' % decAlterPrivateAttr.name
    decAlterPrivateAttr._internal_name = 'Steven'
    assert decAlterPrivateAttr.name == 'Steven'
    print 'decAlterPrivateAttr Altered Private Variable Directly: %s' % decAlterPrivateAttr.name

    # Defer to default value.
    decDefault = DecTest()
    assert decDefault.name == 'NoName'
    print 'decDefault.name: %s' % decDefault.name

    # Init method will allow us to store an int, bypassing the setter method.
    """
    # TODO: How can i use my setter function within my __init__() method,
    # To perform type checking when an instance is constructed?
    """
    decUseInit = DecTest(2)
    print 'decUseInit Init Value: %s' % decUseInit.name
    # Here we use the setter method, and an error is thrown.
    decUseInit.name = 100
    print 'decUseInit Setter Value: %s' % decUseInit.name