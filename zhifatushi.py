# -*- coding:utf=8 -*-
import wx
import os

class Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,title = '指法图示',size = (1024,420))
		self.panel = wx.Panel(self)
		img = wx.Image(os.getcwd() + '/dazizhifa.jpg' , wx.BITMAP_TYPE_ANY)
		w = img.GetWidth()
		h = img.GetHeight()
		wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(img))

app = wx.PySimpleApp()
frame = Frame()
frame.Show()
app.MainLoop()
