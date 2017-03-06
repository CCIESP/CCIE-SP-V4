# CCIE SP lab section task generator
import random
import sys
import os

#create classes that will allow for different types of output: printed to the terminal/HTML/file.
class ConfigGenerator:
    def __init__(self):
        self.config = ''

    def addBreaks(self):
        self.config = self.config + '\n' * 2

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


hook = True
while hook is True:
    os.system('cls')
    type_of_output = raw_input("Would you like output to be a text file or html file? ").upper()
    if type_of_output == "HTML":
        c = HtmlGenerator()
        hook = False
    elif type_of_output == "TEXT":
        c = FileGenerator()
        hook = False
    else:
        print "Please just enter 'TEXT' or 'HTML'!"
        raw_input("Please hit enter to retry.")
        hook = True

#c = FileGenerator()

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
#ISP1's IGP
c.add("ISP1's IGP")
c.addTask("Configure ISP 1 to use the following IGP: %s" % ISP1_IGP)
if ISP1_IGP == "IS-IS":
    c.addTask("Use the IS-IS PID of 1.")
    c.addTask("Create the NSAP based on the router's loopback address and places all routers in area 49.0001.")
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

#ISP2's IGP
c.add("ISP2's IGP")
c.addTask("Configure ISP 2 to use the following IGP: %s" % ISP2_IGP)
if ISP2_IGP == "IS-IS":
    c.addTask("Use the IS-IS PID of 2.")
    c.addTask("Create the NSAP based on the router's loopback address and places all routers in area 49.0002.")
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

#ISP1's BGP
c.add("ISP1's BGP")
BGP_PEER_TYPE = ["Full Mesh", "RR", "Confederation"]
BGP_SESSION_TYPE = ["peer-groups/neighbor-groups", "neighbor statements"]
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
c.addBreaks()

#ISP2's BGP
c.add("ISP2's BGP")
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
c.addBreaks()


MPLS_ENABLE = ["interface commands", "mpls auto configuration"]
MPLS_TYPE = ["LDP", "RSVP-TE", "BGP+LABEL"]
MPLS_TYPE_RANDOM = random.choice(MPLS_TYPE)
MPLS_LABEL_TYPE = ["an access list.", "a single command."]
MPLS_AUTH = ["per neighbor", "fall back password"]
TE_PATH = ["dynamic", "strict", "loose"]
TE_ROUTE = ["autoroute announce", "Forwarding Adjacency", "a static route"]
MPLS_TTL = ["copy the IP TTL to the MPLS TTL", "ignore the IP TTL of the customer only", "ignore the IP TTL of all packets"]

#ISP1's MPLS
c.add("ISP1's MPLS")
if MPLS_TYPE_RANDOM == "LDP":
    c.addTask("Enable MPLS LDP on all IGP links in ISP1 using %s." %random.choice(MPLS_ENABLE))
    c.addTask("Enable MPLS LDP/IGP SYNC on all devices.")
    c.addTask("Enable MPLS Session Protection on all devices.")
    c.addTask("Enable MPLS LDP authentication using a %s methodolgy with the password 'cisco'." % random.choice(MPLS_AUTH))
    if random.randint(0,1) == 0:
        c.addTask("Distribute labels for LDP for all IGP links.")
    else:
        c.addTask("Distribute labels for LDP for Loopbacks ONLY using %s" % random.choice(MPLS_LABEL_TYPE))
elif MPLS_TYPE_RANDOM == "RSVP-TE":
    c.add("This entire section needs to be reviewed and tested in VIRL! it maybe removed in the future!")
    c.addTask("Enable MPLS RSVP-TE on all IGP links in ISP1.")
    c.addTask("Build TE tunnels from PE1 to PE2 and PE2 to PE2 using %s path options and utilize the tunnel via %s." % (random.choice(TE_PATH), random.choice(TE_ROUTE)))
    c.addTask("Enable the following features on the TE tunnel: Record Route and TE description PE#-->PE#.")
else:
    c.add("This entire section needs to be reviewed and tested in VIRL! it maybe removed in the future!")
    c.addTask("Enable BGP+LABEL in ISP1 to work based on the BGP architecture above.")
c.addTask("Configure the devices in ISP1 to do the following with an TTL: %s." % random.choice(MPLS_TTL))
c.addBreaks()

#ISP2's MPLS
c.add("ISP2's MPLS")
MPLS_TYPE_RANDOM = random.choice(MPLS_TYPE)
if MPLS_TYPE_RANDOM == "LDP":
    c.addTask("Enable MPLS LDP on all IGP links in ISP2 using %s." %random.choice(MPLS_ENABLE))
    c.addTask("Enable MPLS LDP/IGP SYNC on all devices.")
    c.addTask("Enable MPLS Session Protection on all devices.")
    c.addTask("Enable MPLS LDP authentication using a %s methodolgy with the password 'cisco'." % random.choice(MPLS_AUTH))
    if random.randint(0,1) == 0:
        c.addTask("Distribute labels for LDP for all IGP links.")
    else:
        c.addTask("Distribute labels for LDP for Loopbacks ONLY using %s" % random.choice(MPLS_LABEL_TYPE))
elif MPLS_TYPE_RANDOM == "RSVP-TE":
    c.add("This entire section needs to be reviewed and tested in VIRL! it maybe removed in the future!")
    c.addTask("Enable MPLS RSVP-TE on all IGP links in ISP2.")
    c.addTask("Build TE tunnels from PE3 to PE4 and PE4 to PE3 using %s path options and utilize the tunnel via %s." % (random.choice(TE_PATH), random.choice(TE_ROUTE)))
    c.addTask("Enable the following features on the TE tunnel: Record Route and TE description PE#-->PE#.")
else:
    c.add("This entire section needs to be reviewed and tested in VIRL! it maybe removed in the future!")
    c.addTask("Enable BGP+LABEL in ISP2 to work based on the BGP architecture above.")
c.addTask("Configure the devices in ISP2 to do the following with an TTL: %s." % random.choice(MPLS_TTL))
c.addBreaks()

#ISP1's Multicast
c.add("Multicast for ISP1 to be added soon")
c.addBreaks()

#ISP2's Multicast
c.add("Multicast for ISP2 to be added soon")
c.addBreaks()

#ISP1 Core QoS
CORE_QOS_CLASSES = ["Voice", "Video", "Business", "Critical", "Best Effort"]
CORE_QOS_DECISION = ["QGROUP", "EXP", "NONE"]
CORE_QOS_BEST_EFFORT = ["WRED", "Tail Drop", "CBWFQ remaining bandwidth"]
NUMBER_OF_CORE_QOS = random.randint(3,5)
c.add("ISP1 Core QoS")
c.add("ISP1 today honors %s classes of QoS in the Core." % NUMBER_OF_CORE_QOS)
if random.choice(CORE_QOS_DECISION) == "EXP":
    if NUMBER_OF_CORE_QOS == 3:
        c.add("ISP1 honors the following classes: Voice (EXP5), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP1 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP1 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    elif NUMBER_OF_CORE_QOS == 4:
        c.add("ISP1 honors the following classes: Voice (EXP5), Video (EXP4), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP1 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives EXP4 CBWFQ treatment and a bandwidth guarantee of %s percent.." % random.randint(20, 40))
        c.addTask("ISP1 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    else:
        c.add("ISP1 honors the following classes: Voice (EXP5), Video (EXP4), Critical (EXP3), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP1 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives EXP4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 30))
        c.addTask("ISP1 gives EXP3 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
elif random.choice(CORE_QOS_DECISION) == "QGROUP":
    if NUMBER_OF_CORE_QOS == 3:
        c.add("ISP1 honors the following classes: Voice (QGroup5), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP1 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP1 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    elif NUMBER_OF_CORE_QOS == 4:
        c.add("ISP1 honors the following classes: Voice (QGroup5), Video (QGroup4), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP1 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives QGroup4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 40))
        c.addTask("ISP1 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    else:
        c.add("ISP1 honors the following classes: Voice (QGroup5), Video (QGroup4), Critical (QGroup3), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP1 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives QGroup4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 30))
        c.addTask("ISP1 gives QGroup3 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
else:
    c.add("While ISP1 does honor %s classes of markings they have decided to not do anythings with the markings on a per hop basis, consider yourself lucky?" % NUMBER_OF_CORE_QOS)
    c.addBreaks()

#ISP2 Core QoS
NUMBER_OF_CORE_QOS = random.randint(3,5)
c.add("ISP2 Core QoS")
c.add("ISP2 today honors %s classes of QoS in the Core." % NUMBER_OF_CORE_QOS)
if random.choice(CORE_QOS_DECISION) == "EXP":
    if NUMBER_OF_CORE_QOS == 3:
        c.add("ISP2 honors the following classes: Voice (EXP5), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP2 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP2 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    elif NUMBER_OF_CORE_QOS == 4:
        c.add("ISP2 honors the following classes: Voice (EXP5), Video (EXP4), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP2 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives EXP4 CBWFQ treatment and a bandwidth guarantee of %s percent.." % random.randint(20, 40))
        c.addTask("ISP2 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    else:
        c.add("ISP2 honors the following classes: Voice (EXP5), Video (EXP4), Critical (EXP3), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP2 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives EXP4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 30))
        c.addTask("ISP2 gives EXP3 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
elif random.choice(CORE_QOS_DECISION) == "QGROUP":
    if NUMBER_OF_CORE_QOS == 3:
        c.add("ISP2 honors the following classes: Voice (QGroup5), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP2 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP2 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    elif NUMBER_OF_CORE_QOS == 4:
        c.add("ISP2 honors the following classes: Voice (QGroup5), Video (QGroup4), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP2 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives QGroup4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 40))
        c.addTask("ISP2 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    else:
        c.add("ISP2 honors the following classes: Voice (QGroup5), Video (QGroup4), Critical (QGroup3), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP2 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives QGroup4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 30))
        c.addTask("ISP2 gives QGroup3 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
else:
    c.add("While ISP2 does honor %s classes of markings they have decided to not do anythings with the markings on a per hop basis, consider yourself lucky?" % NUMBER_OF_CORE_QOS)
    c.addBreaks()

ConfigGenerator.section = 2
ConfigGenerator.task = None
ConfigGenerator.task = 1

c.addHeader("Service Provider based services")
c.add("This section is worth 26% of the total points")
c.addHrule()
c.addTask("Test section")

c.output()
