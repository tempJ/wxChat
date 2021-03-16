# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import socket

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.panel_chat = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_chat.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrl_log = wx.TextCtrl( self.panel_chat, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer9.Add( self.textCtrl_log, 1, wx.EXPAND, 5 )
		
		self.scrollBar = wx.ScrollBar( self.panel_chat, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_VERTICAL )
		bSizer9.Add( self.scrollBar, 0, wx.EXPAND, 5 )
		
		
		self.panel_chat.SetSizer( bSizer9 )
		self.panel_chat.Layout()
		bSizer9.Fit( self.panel_chat )
		bSizer.Add( self.panel_chat, 1, wx.EXPAND, 5 )
		
		bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrl_chat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer.Add( self.textCtrl_chat, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer_butt = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_chat = wx.Button( self, wx.ID_ANY, u"Chat", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_butt.Add( self.button_chat, 1, wx.ALL, 5 )
		
		self.button_exit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_butt.Add( self.button_exit, 1, wx.ALL, 5 )
		
		
		bSizer.Add( bSizer_butt, 1, wx.EXPAND, 5 )
		
		
		bSizer.Add( bSizer, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
        
        #button event
		self.button_chat.Bind(wx.EVT_BUTTON, self.send)
		self.button_exit.Bind(wx.EVT_BUTTON, self.close)
	
	def __del__( self ):
		pass
	
    def recv( self ):
        #while True:/완성해도 GUI 멈출듯
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((main.IP, main.PORT))

        mag = input()

        text = '>> ' + msg + '\n'
        self.textCtrl_log.AppendText(text)
        #구조 이해를 잘못한거같은데 틀만 잡아두고 나중에 전체 수정
        
    def send( self, event ):
        text = 'You>> ' + self.textCtrl_chat.GetLineText() + '\n'
        self.textCtrl_log.AppendText(text)
        self.textCtrl_chat.SetValue('')
        
    def scroll( self, event ):
        #textctrl이 가득 찰 경우 한 줄 추가될 때마다 스크롤 이동

	def close( self, event ):
        #창 종료 말고 socket 통신 해제&main pannel 전환으로 변경
		#self.close()