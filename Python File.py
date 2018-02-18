import sys
import pjsua as pj
import threading
import time

# Log for the call back of class
def logcallback(level, str, len):
    print(str),

# Class gives us the notification with respect to account registration
class MyAccCallback(pj.AccCallback):
    def __init__(self, acc):
        pj.AccCallback.__init__(self,acc)

# To get class events from call callback
class SRDialCallback(pj.DialCallback):
    def __init__(self, call=None):
        pj.DialCallback.__init__(self, call)

        def on_state(self):
            print("Call is ON :", self.call.info().state_text),
            print ("Last code is :", self.call.info().last_code),
            print ("("    + self.call.info().last_reason +  ")")

# update regarding changes
def on_media_state(self):
    global lib
    if self.call.info().media_state == pj.MediaState.ACTIVE:

        #Connecting the call to a different sound device
        call_slot = self.call.info().conf_slot
        lib.conf_connect(call_slot, 0)
        lib.conf_connect(0, call_slot)
        print ("Hi. Have a nice day!")
        print (lib)

# Main loop Part
try:
    # Starting
    # Creating the library instance of Lib Class
    lib = pj.Lib()
    # Instantiate library with default configuration
    lib.init(log_cfg = pj.LogConfig(level=3, callback=log_cb))
    # UDP configuration by binding up with 5060
    trans_conf = pj.TransportConfig()

    print "--------REGISTRATION STARTS BELOW--------"
    print "\n\n"

    trans_conf.port = 5060
    client_IP=raw_input ("Enter the IP Adderess of your client :     ")
    print "Port number for SIP calls: 5060"

    trans_conf.bound_addr = client_IP
    transport = lib.create_transport(pj.Transporttype.UDP,trans_conf)
    # Initiate the instance for Library Class
    lib.start()
    lib.set_null_snd_dev()
    #Registration server configuration
    #creating header sip register

    Server_IP=raw_input("Enter the IP address of your server:    ")
    name=raw_input("Enter username:    ")
    secret=raw_input("Enter password:     ")
    display_name=raw_input("Do you want to use same Display name and username ? Enter valid entry Y/N ?")
    if display_name=="Y" or display_name=="y":
        new_display_name=ab
    else:
        new_display_name=raw_input("Enter display name:   ")
    acc_conf = pj.AccountConfig(domain = Server_IP, username = name, password = secret, display = display_name)

    # registrar = 'sip:' + + ':5060', proxy = 'sip:'+Server_IP+':5060'

    acc_conf.id = "sip:"+name
    acc_conf.reg_uri = 'sip:'+Server_IP+':5060'
    acc_callback = MyAccCallback(acc_conf)
    acc = lib.create_account(acc_conf, cb=acc_callback)

    # AccCallback Class Instance
    acc.set_callback(acc_callback)
    print('\n\n')
    print "Registration is completed"
    print('Status=  ',acc.info().reg_status. \
        '(' + acc.info().reg_reason + ')')

    wanna_call=raw_input("Do you want to make a call now ?? Y/N\n")
    print "\n"

    if wanna_call=="y" or wanna_call=="Y":

        # Starts calling process
    Destination_URI=raw_input("Enter destination URI: ")
    call = acc.make_call(Destiantion_URI, SRDialCallback())

    # Client Side Waiting for ENTER Command to exit
    print ('Press <ENTER> to exit and destroy library')
    input = sys.stdin.readline().rstrip('\r\n')

    # To shut down the library
    lib.destroy()
    lib = None

else:

print "Unregistering"
time.sleep(2)
print "Destroying the librarires"
time.sleep(2)
lib.destroy()
lib = None
sys.exit(1)

except pj.Error, e:

print ("Exception:  " + str(e))
lib.destroy()
lib = None
sys.exit(1)
