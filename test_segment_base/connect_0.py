# A simple test script for all this.
# In the real world, it is likely that the code controlling the server
# will be in the same class as that getting the notifications.
def test(verbose=0):
	import win32com.client.dynamic, win32com.client.connect
	import win32com.server.policy
	server = win32com.client.dynamic.Dispatch(win32com.server.util.wrap(ConnectableServer()))
	connection = win32com.client.connect.SimpleConnection()
	client = ConnectableClient()
	connection.Connect(server, client, IID_IConnectDemoEvents)
	CheckEvent(server, client, "Hello", verbose)
	CheckEvent(server, client, str2bytes("Here is a null>\x00<"), verbose)
	CheckEvent(server, client, u"Here is a null>\x00<", verbose)
	val = u"test-\xe0\xf2" # 2 extended characters.
	CheckEvent(server, client, val, verbose)
	if verbose:
		print "Everything seemed to work!"
	# Aggressive memory leak checking (ie, do nothing!) :-)  All should cleanup OK???
