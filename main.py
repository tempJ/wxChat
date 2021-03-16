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
## Class frame
###########################################################################

class frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.server_socket
		self.IP = '0.0.0.0'
		self.PORT = 1024
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		bSizer_top = wx.BoxSizer( wx.HORIZONTAL )
		
		self.panel_empty = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_top.Add( self.panel_empty, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer_ipport = wx.BoxSizer( wx.VERTICAL )
		
		self.panel_ip = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.staticText_ip = wx.StaticText( self.panel_ip, wx.ID_ANY, u"IP:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.staticText_ip.Wrap( -1 )
		bSizer4.Add( self.staticText_ip, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_ip = wx.TextCtrl( self.panel_ip, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.textCtrl_ip, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.panel_ip.SetSizer( bSizer4 )
		self.panel_ip.Layout()
		bSizer4.Fit( self.panel_ip )
		bSizer_ipport.Add( self.panel_ip, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panel_port = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.staticText_port = wx.StaticText( self.panel_port, wx.ID_ANY, u"PORT:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.staticText_port.Wrap( -1 )
		bSizer5.Add( self.staticText_port, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_port = wx.TextCtrl( self.panel_port, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.textCtrl_port, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.panel_port.SetSizer( bSizer5 )
		self.panel_port.Layout()
		bSizer5.Fit( self.panel_port )
		bSizer_ipport.Add( self.panel_port, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer_top.Add( bSizer_ipport, 2, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.panel_empty = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_top.Add( self.panel_empty, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer.Add( bSizer_top, 1, wx.EXPAND, 5 )
		
		bSizer_bottom = wx.BoxSizer( wx.HORIZONTAL )
		
		self.staticText_ip = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.staticText_ip.Wrap( -1 )
		bSizer_bottom.Add( self.staticText_ip, 2, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer_butt = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_login = wx.Button( self, wx.ID_ANY, u"Link", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_butt.Add( self.button_login, 1, wx.ALL, 5 )
		
		self.button_close = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_butt.Add( self.button_close, 1, wx.ALL, 5 )
		
		
		bSizer_bottom.Add( bSizer_butt, 1, wx.EXPAND, 5 )
		
		
		bSizer.Add( bSizer_bottom, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		#button event
		self.button_login.Bind(wx.EVT_BUTTON, self.login)
		self.button_close.Bind(wx.EVT_BUTTON, self.close)
	
	def __del__( self ):
		pass
		
	def login( self, event ):
		if self.tcp_ip_link( self ):
			#import chat.py panel/bsizer 전환
		
	def tcp_ip_link( self ):
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.IP = self.textCtrl_ip.GetLineText()
		self.PORT = int(self.textCtrl_port.GetLineText())
		
		server_socket.bind((IP, PORT)) #bind 실패할 경우 추가
		server_socket.listen(0)
	
	def close(self, event):
		self.close()