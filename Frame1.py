#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(254, 155), size=wx.Size(527, 616),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(511, 578))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(511, 578),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(40, 48), size=wx.Size(432, 56),
              style=wx.TE_MULTILINE,
              value=u'13456788,13446788,13456988,12456788,13456798')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(40, 152), size=wx.Size(432, 400),
              style=wx.TE_MULTILINE, value=u'')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'\u8f93\u5165\u82e5\u5e72\u6570\u5b57\u5e8f\u5217,\u4ee5\u9017\u53f7\u5206\u9694,\u5982: 12345678,87654321,23654980',
              name='staticText1', parent=self.panel1, pos=wx.Point(40, 16),
              size=wx.Size(335, 13), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'\u70b9\u51fb\u6309\u94ae,\u751f\u6210\u7ed3\u679c',
              name='button1', parent=self.panel1, pos=wx.Point(40, 112),
              size=wx.Size(432, 31), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        s = self.TextCtrl1.GetValue().strip()
        a = s.split(",")
        for n in a:
            n.get
                
        
        
        event.Skip()
