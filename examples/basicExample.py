""" Basic Example

		Copyright (c) 2004 Colin Stewart (http://www.owlfish.com/)
		All rights reserved.
		
		Redistribution and use in source and binary forms, with or without
		modification, are permitted provided that the following conditions
		are met:
		1. Redistributions of source code must retain the above copyright
		   notice, this list of conditions and the following disclaimer.
		2. Redistributions in binary form must reproduce the above copyright
		   notice, this list of conditions and the following disclaimer in the
		   documentation and/or other materials provided with the distribution.
		3. The name of the author may not be used to endorse or promote products
		   derived from this software without specific prior written permission.
		
		THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
		IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
		OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
		IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
		INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
		NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
		DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
		THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
		(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
		THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
		
		If you make any bug fixes or feature enhancements please let me know!
		
		A simple example - a counting web site.
		Note that increments in modern browsers go up twice because two 
		requests are made - one for '/' and one for '/favicon.ico'
"""
import logging, time

from wsgiutils import SessionClient, wsgiAdaptor, wsgiServer
class TestApp:
	def requestHandler (self, request):
		session = request.getSession()
		count = session.get ('counter', 0)
		count += 1
		session ['counter'] = count
		request.sendContent ("<html><body><h1>Visits: %s</h1></body></html>" % str (count), "text/html")
		
	
testclient = SessionClient.LocalSessionClient('session.dbm', 'testappid')
testadaptor = wsgiAdaptor.wsgiAdaptor (TestApp(), 'siteCookieKey', testclient)
server = wsgiServer.WSGIServer (('localhost', 1088), {'/': testadaptor.wsgiHook})
server.serve_forever()