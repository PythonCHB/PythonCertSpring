import wx

def file_open(obj):
    """This method opens a file"""
    print "Open a file from file_open()"

def file_close(obj):
    """This method closes a file"""
    print "Close a file from file_close()"
    

 
class MyForm(wx.Frame):

 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "wx.Menu Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)
 
        menuBar = wx.MenuBar()
        
        fileMenu = wx.Menu()
        openMenuItem = fileMenu.Append(wx.NewId(), "Open",
                                       "Open a file" )
        self.Bind(wx.EVT_MENU, file_open, openMenuItem )
        closeMenuItem = fileMenu.Append(wx.NewId(), "Close",
                                       "Close a file" )
        self.Bind(wx.EVT_MENU, file_close, closeMenuItem )
        exitMenuItem = fileMenu.Append(wx.NewId(), "Exit",
                                       "Exit the application")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
        menuBar.Append(fileMenu, "&File")
        
        helpMenu = wx.Menu()
        helpMenuItem = helpMenu.Append(wx.NewId(), "Help",
                                       "Get help")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

    def onExit(self, obj):
        print "Exit the program here"
        print "The object passed to onExit is type ", type(obj),\
              "and has attributes", dir(obj)
        

 
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
