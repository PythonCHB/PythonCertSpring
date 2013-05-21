#!/usr/bin/env python

"""
The basic from for the address book

This gets a Panel to itself
"""

import wx

class A_Book_Form(wx.Panel):
    def __init__(self, a_entry, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.a_entry = a_entry

        ## create text boxes to edit: first name, last name, phone, email.
        self.fname_text = wx.TextCtrl(self)
        self.lname_text = wx.TextCtrl(self)
        self.phone_text = wx.TextCtrl(self)
        self.email_text = wx.TextCtrl(self)

        ## use a FlexGridSizer:
        S = wx.FlexGridSizer(rows=0, cols=2, vgap=8, hgap=8)
        S.AddGrowableCol(idx=1, proportion=1)

        S.Add(wx.StaticText(self, label="First Name:"), 0,
              wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        S.Add(self.fname_text, flag=wx.EXPAND)
        
        S.Add(wx.StaticText(self, label="Last Name:"), 0,
              wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        S.Add(self.lname_text, flag=wx.EXPAND)
        
        S.Add(wx.StaticText(self, label="Phone Number:"), 0,
              wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        S.Add(self.phone_text, flag=wx.EXPAND)
        
        S.Add(wx.StaticText(self, label="Email Address:"), 0,
              wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        S.Add(self.email_text, flag=wx.EXPAND)

        #Put the whole thing in another sizer to give it some space
        Outer_Sizer = wx.BoxSizer(wx.VERTICAL)
        Outer_Sizer.Add(S, 0, wx.ALL|wx.EXPAND, 10)
        self.SetSizerAndFit(Outer_Sizer)

        self.load_data()

    def load_data(self):
        """
        load the data into the form from the data dict
        """
        data = self.a_entry
        self.fname_text.Value = data[u'first_name'] 
        self.lname_text.Value = data[u'last_name']
        self.phone_text.Value = data[u'phone']
        self.email_text.Value = data[u'email']

    def save_data(self):
        """
        save the data from the form from the data dict
        """
        data = self.a_entry
        data[u'first_name'] = self.fname_text.Value
        data[u'last_name'] = self.lname_text.Value 
        data[u'phone'] = self.phone_text.Value
        data[u'email'] = self.email_text.Value


# I like to have a little test app so it can be done on its own
if __name__ == "__main__":

    # a sample entry:
    entry = {u'email': u'PythonCHB@gmail.com',
             u'first_name': u'Chris',
             u'last_name': u'Barker',
             u'phone': u'123-456-7890'}

    app = wx.App(False)
    f = wx.Frame(None)
    p = A_Book_Form(entry, f)
    f.Show()
    app.MainLoop()