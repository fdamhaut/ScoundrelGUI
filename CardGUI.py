import wx

TL = 0
BL = 1
TR = 2
BR = 3
CARDS_SUIT = {0: 'C', 1: 'D', 2: 'H', 3: 'S'}

def getBottomPos(o):
    return o.GetSize().GetHeight() + o.GetPosition().y

def getRightPos(o):
    return o.GetSize().GetWidth() + o.GetPosition().x

def resize(bm, size):
    image = bm.ConvertToImage()
    image = image.Scale(size[0], size[1], wx.IMAGE_QUALITY_HIGH)
    return wx.Bitmap(image)

class CardFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='TESTING')

        self.cards = [0, 13, 26, 39]

        self.sizeScale = 3
        self.damp = 5
        self.size = [64*self.sizeScale, 89*self.sizeScale]

        totalsize = [i*2+3*self.damp for i in self.size]

        self.panel = wx.Panel(self)

        self.topleft = wx.BitmapButton(self.panel, pos=(self.damp, self.damp), size=self.size, style=wx.NO_BORDER, id=TL)
        self.botleft = wx.BitmapButton(self.panel, pos=(self.damp, getBottomPos(self.topleft)+self.damp), size=self.size, style=wx.NO_BORDER, id=BL)
        self.topright = wx.BitmapButton(self.panel, pos=(getRightPos(self.topleft)+self.damp, self.damp), size=self.size, style=wx.NO_BORDER, id=TR)
        self.botright = wx.BitmapButton(self.panel, pos=(getRightPos(self.botleft)+self.damp, getBottomPos(self.topright)+self.damp), size=self.size, style=wx.NO_BORDER, id=BR)

        self.panel.Bind(wx.EVT_BUTTON, self.next, self.topleft)
        self.panel.Bind(wx.EVT_BUTTON, self.next, self.botleft)
        self.panel.Bind(wx.EVT_BUTTON, self.next, self.topright)
        self.panel.Bind(wx.EVT_BUTTON, self.next, self.botright)

        self.assignImage(self.topleft, self.cards[TL])
        self.assignImage(self.topright, self.cards[TR])
        self.assignImage(self.botleft, self.cards[BL])
        self.assignImage(self.botright, self.cards[BR])

        self.panel.Fit()
        self.panel.SetSize([i+self.damp for i in self.panel.GetSize()])

        self.Center()
        self.Fit()
        self.Show()

    def next(self, event):
        obj = event.GetEventObject()
        c = self.cards[obj.GetId()]
        self.cards[obj.GetId()] = int(c/13)*13 + (c+1) % 13
        self.assignImage(obj, self.cards[obj.GetId()])

    def assignImage(self, obj, cardID):
        card = str((cardID%13)+1)+CARDS_SUIT[int(cardID/13)]
        bm = resize(wx.Bitmap("Cards/" + card + ".png", wx.BITMAP_TYPE_ANY), self.size)
        obj.SetBitmap(bm)



app = wx.App()

cf = CardFrame()

app.MainLoop()