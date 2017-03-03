# CCIE SP lab section task generator
import random
import sys
import os

#create classes that will allow for different types of output: printed to the terminal/HTML/file.
class ConfigGenerator:
    def __init__(self):
        self.config = ''

    def addBreaks(self):
        self.config = self.config + '\n' * 3

    def addHrule(self):
        self.config = self.config + '-' * 75 + '\n'

    def addHeader(self, string):
        self.config = self.config + str(self.section) + ". " + string + '\n'

    def add(self, string):
        self.config = self.config + string + '\n'

    def addTask(self, string):
        self.config = self.config + '[ ]' + str(self.section) + "." + str(self.task) + " " + string + '\n'
        self.task = self.task + 1

    def addSection(self, string):
        self.config = self.config + string + '\n'

    def output(self):
        print self.config

class HtmlGenerator(ConfigGenerator):

    def __init__(self):
        self.filename = open('CCIE-SPv4-MOCK-LAB.html', 'w')
        self.config = ''
        self.config = '<!DOCTYPE html><html><head>'
        self.config = self.config + '<link rel="stylesheet" href="https://picturepan2.github.io/spectre/css/spectre.css" />'
        self.config = self.config + '</head><body>'
        self.config = self.config + '<div class="container"><div class="columns"><div class="column col-12">'

    def addHeader(self, string):
        self.config = self.config + '<h2>' + str(self.section) + ". " + string + '</h2><br>';

    def addBreaks(self):
        self.config = self.config + '<br>'

    def addHrule(self):
        self.config = self.config + '<hr>'

    def addSection(self, string):
        self.config = self.config + '<h4>' + string + '</h4><br>';

    def add(self, string):
        self.config = self.config + string + '<br>';

    def addTask(self, string):
        self.config = self.config + '<input type="checkbox">' + str(self.section) + "." + str(self.task) + " " + string + '</input><br>'
        self.task = self.task + 1

    def output(self):
        self.config = self.config + '</div></body></html>'
        self.filename.write(self.config)
        self.filename.close()

class FileGenerator(ConfigGenerator):
    def __init__(self):
        self.filename = open('CCIE-SPv4-MOCK-LAB.txt', 'w')
        self.config = ''

    def output(self):
        self.filename.write(self.config)
        self.filename.close()

#this triggers the type of output, select HtmlGenerator for an html file, select ConfigGenerator for a screen print and select FileGenerator for a txt file.
c = FileGenerator()

#define network nodes in each SP via lists
ISP1 = ["PE1", "PE2", "P1", "P2", "ASBR1"]
ISP2 = ["PE3", "PE4", "P3", "P4", "ASBR2"]
ISP1_PE = ["PE1", "PE2"]
ISP1_P = ["P1", "P2"]
ISP1_ASBR = ["ASBR1"]
ISP1_CE = ["CE1", "CE2", "CE3", "CE4"]
ISP2_PE = ["PE3", "PE4"]
ISP2_P = ["P3", "P4"]
ISP2_ASBR = ["ASBR2"]
ISP2_CE = ["CE5", "CE6", "CE7", "CE8"]
#list all IGP types the SP may use
IGP1 = ["IS-IS", "OSPF"]
IGP2 = ["IS-IS", "OSPF"]
auth_type = ["interface", "area"]
ospf_adv_type = ["specific network statements", "the interface command", "a very broad network statement"]

#PE-CE peering protocols
PE_CE_PROT = ["OSPF", "RIPv2", "EIGRP", "STATIC", "BGP"]
ConfigGenerator.section = 1
ConfigGenerator.task = 1

c.add("Welcome to the CCIE-SPv4 MOCK LAB random task generator!")
c.add("Please use these tasks with the prebuilt two ISP topology.")
c.add("As with the real lab you only have 5 hours to complete these tasks.")
c.add("Your topology should be prebuilt and pre IP'ed (v4/v6).")
c.add("Please stop and verify before you start your timer!")
c.addBreaks()
c.addHeader("Core Routing")
c.add("This section is worth 27% of the total points")
c.addHrule()

ISP1_IGP = random.choice(IGP1)
ISP2_IGP = random.choice(IGP2)

#EVERYTHING IN THIS SECTION WILL NEED TO BE VERIFIED IN TERMS OF TIMERS AND AUTH TYPES AS THIS IS A ROUGH DRAFT, EXPECT ERRORS!
c.addTask("Configure ISP 1 to use the following IGP: %s" % ISP1_IGP)
if ISP1_IGP == "IS-IS":
    c.addTask("Use the IS-IS PID of 1.")
    c.addTask("Create the NSAP based on the router's loopback address and places all routers in area 49.001.")
    c.addTask("Make all interfaces level-2 only interfaces with a metric of %s." % random.randrange(10, 100, 10))
    c.addTask("Configure authentication per interface using the key 'cisco'.")
    if random.randint(0,1) == 0:
        c.addTask("Configure the IS-IS hello timer interval to be %s sec." % random.randrange(5 ,30, 5))
        c.addBreaks()
    else:
        c.addTask("Configure BFD for IS-IS with a interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
        c.addBreaks()
elif ISP1_IGP == "OSPF":
    c.addTask("Use the OSPF PID of 1.")
    c.addTask("Places all interfaces in area 0 via %s." % random.choice(ospf_adv_type))
    c.addTask("Configure authentication per %s." % random.choice(auth_type))
    if random.randint(0,1) == 0:
        c.addTask("Configure OSPF hello timers of %s seconds and dead timers of % s seconds." % (random.randint(1, 10), random.randrange(20, 60, 10)))
        c.addBreaks()
    else:
        c.addTask("Configure BFD for OSPF with a interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
        c.addBreaks()
else:
    c.addTask("ERROR IN ISP1 IGP SELECTION!.")

c.addTask("Configure ISP 2 to use the following IGP: %s" % ISP2_IGP)
if ISP2_IGP == "IS-IS":
    c.addTask("Use the IS-IS PID of 2.")
    c.addTask("Create the NSAP based on the router's loopback address and places all routers in area 49.002.")
    c.addTask("Make all interfaces level-2 only interfaces with a metric of %s." % random.randrange(10, 100, 10))
    c.addTask("Configure authentication per interface using the key 'cisco'.")
    if random.randint(0,1) == 0:
        c.addTask("Configure the IS-IS hello timer interval to be %s sec." % (random.randrange(5 ,30, 5)))
        c.addBreaks()
    else:
        c.addTask("Configure BFD for IS-IS with a interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
        c.addBreaks()
elif ISP2_IGP == "OSPF":
    c.addTask("Use the OSPF PID of 2.")
    c.addTask("Places all interfaces in area 0 via %s." % random.choice(ospf_adv_type))
    c.addTask("Configure authentication per %s." % random.choice(auth_type))
    if random.randint(0,1) == 0:
        c.addTask("Configure OSPF hello timers of %s seconds and dead timers of % s seconds." % (random.randint(1, 10), random.randrange(20, 60, 10)))
        c.addBreaks()
    else:
        c.addTask("Configure BFD for OSPF with a interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
        c.addBreaks()
else:
    c.addTask("ERROR IN ISP2 IGP SELECTION!")

BGP_PEER_TYPE = ["Full Mesh", "RR", "Confederation"]
BGP_SESSION_TYPE = ["peer groups", "neighbor statements"]
BGP_OPTIMIZATION = ["Scan timer", "BGP PIC"]
BGP_RANDOM = random.choice(BGP_PEER_TYPE).upper()
if BGP_RANDOM == "FULL MESH":
    c.addTask("All devices in ISP 1 (BGP ASN 1) will peer via a full iBGP mesh, configure them via %s." % random.choice(BGP_SESSION_TYPE))
    c.addTask("All iBGP peerings should use the authentication key of 'ISP1'")
    if random.randint(0,1) == 0:
        c.addTask("Configure BGP hello timers on each device for a %s seconds hello timer and % s seconds dead timer." % (random.randrange(10, 30, 10), random.randrange(40, 60, 10)))
    else:
        c.addTask("Configure BFD for BGP, if has not already been configured use an interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
elif BGP_RANDOM == "RR":
    c.addTask("All devices in ISP 1 (BGP ASN 1) will peer with %s as route-reflector clients, configure them via %s." % (random.choice(ISP1), random.choice(BGP_SESSION_TYPE)))
    c.addTask("All iBGP peerings should use the authentication key of 'ISP1'")
    if random.randint(0,1) == 0:
        c.addTask("Configure BGP hello timers on each device for a %s seconds hello timer and % s seconds dead timer." % (random.randrange(10, 30, 10), random.randrange(40, 60, 10)))
    else:
        c.addTask("Configure BFD for BGP, if has not already been configured use an interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
else:
    c.addTask("ISP 1 decided to build out BGP confederations using sub-AS 65001 for PE1/PE2 and sub-AS 65011 for P1/P2, configure them via %s." % random.choice(BGP_SESSION_TYPE))
    c.addTask("All iBGP peerings should use the authentication key of 'ISP1'")
    if random.randint(0,1) == 0:
        c.addTask("Configure BGP hello timers on each device for a %s seconds hello timer and % s seconds dead timer." % (random.randrange(10, 30, 10), random.randrange(40, 60, 10)))
    else:
        c.addTask("Configure BFD for BGP, if has not already been configured use an interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
BGP_RANDOM = random.choice(BGP_PEER_TYPE).upper()
if BGP_RANDOM == "FULL MESH":
    c.addTask("All devices in ISP 2 (BGP ASN 2) will peer via a full iBGP mesh, configure them via %s." % random.choice(BGP_SESSION_TYPE))
    c.addTask("All iBGP peerings should use the authentication key of 'ISP2'")
    if random.randint(0,1) == 0:
        c.addTask("Configure BGP hello timers on each device for a %s seconds hello timer and % s seconds dead timer." % (random.randrange(10, 30, 10), random.randrange(40, 60, 10)))
    else:
        c.addTask("Configure BFD for BGP, if has not already been configured use an interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
elif BGP_RANDOM == "RR":
    c.addTask("All devices in ISP 2 (BGP ASN 2) will peer with %s as route-reflector clients, configure them via %s." % (random.choice(ISP2), random.choice(BGP_SESSION_TYPE)))
    c.addTask("All iBGP peerings should use the authentication key of 'ISP2'")
    if random.randint(0,1) == 0:
        c.addTask("Configure BGP hello timers on each device for a %s seconds hello timer and % s seconds dead timer." % (random.randrange(10, 30, 10), random.randrange(40, 60, 10)))
    else:
        c.addTask("Configure BFD for BGP, if has not already been configured use an interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
else:
    c.addTask("ISP 2 decided to build out BGP confederations using sub-AS 65002 for PE3/PE4 and sub-AS 65022 for P3/P4, configure them via %s." % random.choice(BGP_SESSION_TYPE))
    c.addTask("All iBGP peerings should use the authentication key of 'ISP2'")
    if random.randint(0,1) == 0:
        c.addTask("Configure BGP hello timers on each device for a %s seconds hello timer and % s seconds dead timer." % (random.randrange(10, 30, 10), random.randrange(40, 60, 10)))
    else:
        c.addTask("Configure BFD for BGP, if has not already been configured use an interval/min_rx of %s and a multiplier of %s." % (random.randrange(250, 1000, 250), random.randint (3, 5)))




c.output()
