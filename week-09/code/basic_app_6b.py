#!/usr/bin/env python

"""
Example of the very basic, minimal framework for a wxPython application

This version adds a BoxSizer for laying out buttons on the panel
"""

import wx


class AppLogic(object):
    """
    A class to hold the application Application Logic.

    You generally don't want the real logic of the app mixed
    in with the GUI

    In a real app, this would be a substantial collection of 
    modules, classes, etc...
    """
    def file_open(self, filename="default_name"):
        """This method opens a file"""
        print "Open a file: "
        print "I'd be opening file: %s now"%filename

    def file_close(self):
        """This method closes a file"""
        print "Close a file: "
        print "I'd be closing a file now"

class ButtonPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        ## add two buttons:
        theButton1 = wx.Button(self, label="Push Me")
        theButton1.Bind(wx.EVT_BUTTON, self.onButton)

        ## add two buttons:
        theButton2 = wx.Button(self, label="Push Me Also")
        theButton2.Bind(wx.EVT_BUTTON, self.onButton)

        ## do the layout
        ## (try uncommenting the other, and see what happens...)
        S = wx.BoxSizer(wx.VERTICAL)
        #S = wx.BoxSizer(wx.HORIZONTAL)
        
        S.Add(theButton1, 0, wx.GROW | wx.ALL, 4)
        S.Add(theButton2, 0, wx.GROW | wx.ALL, 4)
        
        self.SetSizerAndFit(S)
        
    def onButton(self, evt=None):
        print "You pushed one of the buttons!"


class TestFrame(wx.Frame):
    def __init__(self, app_logic, *args, **kwargs):
        kwargs.setdefault('title', "Simple test App")
        wx.Frame.__init__(self, *args, **kwargs)

        self.app_logic = app_logic

        # put the Panel on the frame
        self.buttonPanel = ButtonPanel(self)

        # Build up the menu bar:
        menuBar = wx.MenuBar()
        
        fileMenu = wx.Menu()
        openMenuItem = fileMenu.Append(wx.ID_ANY, "&Open", "Open a file" )
        self.Bind(wx.EVT_MENU, self.onOpen, openMenuItem)

        closeMenuItem = fileMenu.Append(wx.ID_ANY, "&Close", "Close a file" )
        self.Bind(wx.EVT_MENU, self.onClose, closeMenuItem)

        exitMenuItem = fileMenu.Append(wx.ID_EXIT, "Exit", "Exit the application")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
        menuBar.Append(fileMenu, "&File")
        
        helpMenu = wx.Menu()
        helpMenuItem = helpMenu.Append(wx.ID_HELP, "Help", "Get help")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)
        

    def onOpen(self, evt=None):
        print "open menu selected"
        self.app_logic.file_open()

    def onClose(self, evt=None):
        print "close menu selected"
        self.app_logic.file_close()

    def onExit(self, evt=None):
        print "Exit the program here"
        print "The event passed to onExit is type ", type(evt),
        self.Close()


class TestApp(wx.App):
    def OnInit(self):
        """
        App initilization goes here -- not much to do, in this case
        """
        app_logic = AppLogic()
        f = TestFrame(app_logic, parent=None)
        f.Show()

        return True

if __name__ == "__main__":
    app = TestApp(False)
    app.MainLoop()

