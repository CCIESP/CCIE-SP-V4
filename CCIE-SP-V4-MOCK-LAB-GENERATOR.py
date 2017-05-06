# CCIE SP lab section task generator
import random
import os

#create classes that will allow for different types of output: printed to the terminal/HTML/file.
class ConfigGenerator:
    def __init__(self):
        self._config = ''
        self._task = 1
        self._section = 1

    def addBreaks(self):
        self._config = self._config + '\n' * 2

    def addHrule(self):
        self._config = self._config + '-' * 75 + '\n'

    def addHeader(self, string):
        self._section = self._section + 1
        self._config = self._config + str(self._section) + ". " + string + '\n'
        self._task = 1

    def add(self, string):
        self._config = self._config + string + '\n'

    def addTask(self, string):
        self._config = self._config + '[ ]' + str(self._section) + "." + str(self._task) + " " + string + '\n'
        self._task = self._task + 1

    def addSection(self, string):
        self._config = self._config + str(self._section) + ". " + string + '\n'

    def output(self):
        print self._config

class HtmlGenerator(ConfigGenerator):

    def __init__(self):
        self._filename = open('CCIE-SPv4-MOCK-LAB.html', 'w')
        self._config = ''
        self._config = '<!DOCTYPE html><html><head>'
        self._config = self._config + '<link rel="stylesheet" href="https://picturepan2.github.io/spectre/css/spectre.css" />'
        self._config = self._config + '</head><body>'
        self._config = self._config + '<div class="container"><div class="columns"><div class="column col-12">'
        self._task = 1
        self._section = 1

    def addHeader(self, string):
        self._section = self._section + 1
        self._config = self._config + '<h2>' + str(self._section) + ". " + string + '</h2><br>';
        self._task = 1

    def addBreaks(self):
        self._config = self._config + '<br>'

    def addHrule(self):
        self._config = self._config + '<hr>'

    def addSection(self, string):
        self._config = self._config + '<h2>' + str(self._section) + ". " + string + '</h2><br>';

    def add(self, string):
        self._config = self._config + string + '<br>';

    def addTask(self, string):
        self._config = self._config + '<input type="checkbox">' + str(self._section) + "." + str(self._task) + " " + string + '</input><br>'
        self._task = self._task + 1

    def output(self):
        self._config = self._config + '</div></body></html>'
        self._filename.write(self._config)
        self._filename.close()

class FileGenerator(ConfigGenerator):
    def __init__(self):
        self._filename = open('CCIE-SPv4-MOCK-LAB.txt', 'w')
        self._config = ''
        self._task = 1
        self._section = 1

    def output(self):
        self._filename.write(self._config)
        self._filename.close()

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

#define network nodes in each SP via lists
ISP1 = ["PE1", "PE2", "P1", "P2", "ASBR1"]
ISP2 = ["PE3", "PE4", "P3", "P4", "ASBR2"]
ISP1_PE = ["PE1", "PE2"]
ISP1_P = ["P1", "P2"]
ISP1_ASBR = ["ASBR1"]
ISP2_PE = ["PE3", "PE4"]
ISP2_P = ["P3", "P4"]
ISP2_ASBR = ["ASBR2"]

#list all IGP types the SP may use
IGP1 = ["IS-IS", "OSPF"]
IGP2 = ["IS-IS", "OSPF"]
auth_type = ["interface", "area"]
ospf_adv_type = ["specific network statements", "the interface command", "a very broad network statement"]

#PE-CE peering protocols

c.add("Welcome to the CCIE-SPv4.1 MOCK LAB random task generator!")
c.add("Please use these tasks with the prebuilt two ISP topology.")
c.add("As with the real lab you only have 4.5 hours (assume the worst) to complete these tasks.")
c.add("Your topology should be prebuilt and pre IP'ed (v4/v6).")
c.add("Please stop and verify before you start your timer!")
c.addBreaks()
c.addSection("Core Routing")
c.add("This section is worth 30% of the total points")
c.addHrule()

ISP1_IGP = random.choice(IGP1)
ISP2_IGP = random.choice(IGP2)

#EVERYTHING IN THIS SECTION WILL NEED TO BE VERIFIED IN TERMS OF TIMERS AND AUTH TYPES AS THIS IS A ROUGH DRAFT, EXPECT ERRORS!
#NEEDS TO ADD ISIS LSP-PASSWORD INTO THIS AS WELL!
#NEED TO ADD THE USE OF KEYCHAIN VS INTERFACE COMMAND!
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
        c.addTask("Configure BFD for IS-IS with a interval/min_rx of %s and a multiplier of %s. Use normal timers on XRv devices." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
        c.addBreaks()
elif ISP1_IGP == "OSPF":
    c.addTask("Use the OSPF PID of 1.")
    c.addTask("Places all interfaces in area 0 via %s." % random.choice(ospf_adv_type))
    c.addTask("Configure authentication per %s." % random.choice(auth_type))
    if random.randint(0,1) == 0:
        c.addTask("Configure OSPF hello timers of %s seconds and dead timers of % s seconds." % (random.randint(1, 10), random.randrange(20, 60, 10)))
        c.addBreaks()
    else:
        c.addTask("Configure BFD for OSPF with a interval/min_rx of %s and a multiplier of %s. Use normal timers on XRv devices." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
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
        c.addTask("Configure BFD for IS-IS with a interval/min_rx of %s and a multiplier of %s. Use normal timers on XRv devices." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
        c.addBreaks()
elif ISP2_IGP == "OSPF":
    c.addTask("Use the OSPF PID of 2.")
    c.addTask("Places all interfaces in area 0 via %s." % random.choice(ospf_adv_type))
    c.addTask("Configure authentication per %s." % random.choice(auth_type))
    if random.randint(0,1) == 0:
        c.addTask("Configure OSPF hello timers of %s seconds and dead timers of % s seconds." % (random.randint(1, 10), random.randrange(20, 60, 10)))
        c.addBreaks()
    else:
        c.addTask("Configure BFD for OSPF with a interval/min_rx of %s and a multiplier of %s. Use normal timers on XRv devices." % (random.randrange(250, 1000, 250), random.randint (3, 5)))
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
        c.addTask("Distribute labels for all IGP links.")
    else:
        c.addTask("Distribute labels for Loopbacks ONLY using %s" % random.choice(MPLS_LABEL_TYPE))
elif MPLS_TYPE_RANDOM == "RSVP-TE":
    c.add("This entire section needs to be reviewed and tested in VIRL! it maybe removed in the future!")
    c.addTask("Enable MPLS RSVP-TE on all IGP links in ISP1.")
    c.addTask("Build TE tunnels from PE1 to PE2 and PE2 to PE2 using %s path options and utilize the tunnel via %s." % (random.choice(TE_PATH), random.choice(TE_ROUTE)))
    c.addTask("Enable the following features on the TE tunnel: Record Route and TE description PE#-->PE#.")
else:
    c.add("This entire section needs to be reviewed and tested in VIRL! it maybe removed in the future!")
    c.addTask("Enable BGP+LABEL in ISP1 to work based on the BGP architecture above.")
    if random.randint(0,1) == 0:
        c.addTask("Distribute labels for all IGP links.")
    else:
        c.addTask("Distribute labels for Loopbacks ONLY.")
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
        c.addTask("Distribute labels for all IGP links.")
    else:
        c.addTask("Distribute labels for Loopbacks ONLY using %s" % random.choice(MPLS_LABEL_TYPE))
elif MPLS_TYPE_RANDOM == "RSVP-TE":
    c.add("This entire section needs to be reviewed and tested in VIRL! it maybe removed in the future!")
    c.addTask("Enable MPLS RSVP-TE on all IGP links in ISP2.")
    c.addTask("Build TE tunnels from PE3 to PE4 and PE4 to PE3 using %s path options and utilize the tunnel via %s." % (random.choice(TE_PATH), random.choice(TE_ROUTE)))
    c.addTask("Enable the following features on the TE tunnel: Record Route and TE description PE#-->PE#.")
else:
    c.add("This entire section needs to be reviewed and tested in VIRL! it maybe removed in the future!")
    c.addTask("Enable BGP+LABEL in ISP2 to work based on the BGP architecture above.")
    if random.randint(0,1) == 0:
        c.addTask("Distribute labels for all IGP links.")
    else:
        c.addTask("Distribute labels for Loopbacks ONLY.")
c.addTask("Configure the devices in ISP2 to do the following with an TTL: %s." % random.choice(MPLS_TTL))
c.addBreaks()

#ISP1's Multicast
#http://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/multiprotocol-label-switching-vpns-mpls-vpns/118983-configure-mpls-00.html
#will need to add all 27 profiles!
c.add("Multicast for ISP1 to be added soon")
c.addBreaks()

#ISP2's Multicast
c.add("Multicast for ISP2 to be added soon")
c.addBreaks()

#ISP1 Core QoS
CORE_QOS_CLASSES = ["Voice", "Video", "Business", "Critical", "Best Effort"]
CORE_QOS_DECISION = ["QGROUP", "EXP", "NONE"]
CORE_QOS_BEST_EFFORT = ["WRED", "Tail Drop", "CBWFQ remaining bandwidth"]
ISP1_QOS = ''
ISP2_QOS = ''

ISP1_NUMBER_OF_CORE_QOS = random.randint(3,5)
c.add("ISP1 Core QoS")
c.add("ISP1 today honors %s classes of QoS in the Core." % ISP1_NUMBER_OF_CORE_QOS)
if random.choice(CORE_QOS_DECISION) == "EXP":
    if ISP1_NUMBER_OF_CORE_QOS == 3:
        c.add("ISP1 honors the following classes: Voice (EXP5), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP1 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP1 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP1_QOS = "EXP3"
        c.addBreaks()
    elif ISP1_NUMBER_OF_CORE_QOS == 4:
        c.add("ISP1 honors the following classes: Voice (EXP5), Video (EXP4), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP1 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives EXP4 CBWFQ treatment and a bandwidth guarantee of %s percent.." % random.randint(20, 40))
        c.addTask("ISP1 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP1_QOS = "EXP4"
        c.addBreaks()
    else:
        c.add("ISP1 honors the following classes: Voice (EXP5), Video (EXP4), Critical (EXP3), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP1 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives EXP4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 30))
        c.addTask("ISP1 gives EXP3 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP1_QOS = "EXP5"
        c.addBreaks()
elif random.choice(CORE_QOS_DECISION) == "QGROUP":
    if ISP1_NUMBER_OF_CORE_QOS == 3:
        c.add("ISP1 honors the following classes: Voice (QGroup5), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP1 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP1 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP1_QOS = "QGROUP3"
        c.addBreaks()
    elif ISP1_NUMBER_OF_CORE_QOS == 4:
        c.add("ISP1 honors the following classes: Voice (QGroup5), Video (QGroup4), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP1 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives QGroup4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 40))
        c.addTask("ISP1 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP1_QOS = "QGROUP4"
        c.addBreaks()
    else:
        c.add("ISP1 honors the following classes: Voice (QGroup5), Video (QGroup4), Critical (QGroup3), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP1 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives QGroup4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 30))
        c.addTask("ISP1 gives QGroup3 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP1 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP1_QOS = "QGROUP5"
        c.addBreaks()
else:
    c.add("While ISP1 does honor %s classes of markings they have decided to not do anythings with the markings on a per hop basis, consider yourself lucky?" % ISP1_NUMBER_OF_CORE_QOS)
    ISP1_QOS = "NONE"
    c.addBreaks()

#ISP2 Core QoS
ISP2_NUMBER_OF_CORE_QOS = random.randint(3,5)
c.add("ISP2 Core QoS")
c.add("ISP2 today honors %s classes of QoS in the Core." % ISP2_NUMBER_OF_CORE_QOS)
if random.choice(CORE_QOS_DECISION) == "EXP":
    if ISP2_NUMBER_OF_CORE_QOS == 3:
        c.add("ISP2 honors the following classes: Voice (EXP5), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP2 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP2 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP2_QOS = "EXP3"
        c.addBreaks()
    elif ISP2_NUMBER_OF_CORE_QOS == 4:
        c.add("ISP2 honors the following classes: Voice (EXP5), Video (EXP4), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP2 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives EXP4 CBWFQ treatment and a bandwidth guarantee of %s percent.." % random.randint(20, 40))
        c.addTask("ISP2 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP2_QOS = "EXP4"
        c.addBreaks()
    else:
        c.add("ISP2 honors the following classes: Voice (EXP5), Video (EXP4), Critical (EXP3), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP2 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives EXP4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 30))
        c.addTask("ISP2 gives EXP3 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP2_QOS = "EXP5"
        c.addBreaks()
elif random.choice(CORE_QOS_DECISION) == "QGROUP":
    if ISP2_NUMBER_OF_CORE_QOS == 3:
        c.add("ISP2 honors the following classes: Voice (QGroup5), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP2 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP2 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP2_QOS = "QGROUP3"
        c.addBreaks()
    elif ISP2_NUMBER_OF_CORE_QOS == 4:
        c.add("ISP2 honors the following classes: Voice (QGroup5), Video (QGroup4), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP2 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives QGroup4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 40))
        c.addTask("ISP2 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP2_QOS = "QGROUP4"
        c.addBreaks()
    else:
        c.add("ISP2 honors the following classes: Voice (QGroup5), Video (QGroup4), Critical (QGroup3), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP2 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives QGroup4 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 30))
        c.addTask("ISP2 gives QGroup3 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP2 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(10, 20))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        ISP2_QOS = "QGROUP5"
        c.addBreaks()
else:
    c.add("While ISP2 does honor %s classes of markings they have decided to not do anythings with the markings on a per hop basis, consider yourself lucky?" % ISP2_NUMBER_OF_CORE_QOS)
    ISP2_QOS = "NONE"
    c.addBreaks()

c.addHeader("Service Provider Architecture and services")
c.add("This section is worth 22% of the total points")
c.addHrule()
L2VPN = ["ETREE", "ELAN", "ELINE"]
ISP1_L2VPN = random.choice(L2VPN)
ISP2_L2VPN = random.choice(L2VPN)
ELINE = ["VPWS", "ELINE", "PSEUDOWIRE"]
ELAN = ["VPLS", "ELAN"]
PL_VS_VPL = ["native", "tagged"]
PL = ["native", "802.3", "EPL"]
VPL = ["tagged", "802.1q", "EVPL"]
SIGNAL = ["BGP", "LDP"]
MARTINI = ["Martini", "LDP"]
KOMPELLA = ["Kompella", "BGP"]
L2_ISP1_CE = ["CE1", "CE2", "CE3", "CE4"]
L2_ISP2_CE = ["CE5", "CE6", "CE7", "CE8"]

#ISP1 L2VPN SERVICES
c.add("ISP1 L2VPN services")
if ISP1_L2VPN == "ELINE":
    #ELINE SERVICES
    ELINE_CE1 = random.choice(L2_ISP1_CE)
    L2_ISP1_CE.remove(ELINE_CE1)
    ELINE_CE2 = random.choice(L2_ISP1_CE)
    L2_ISP1_CE.remove(ELINE_CE2)
    c.addTask("Create a %s service from %s to %s. On each CE use the lowest number interface." % (random.choice(ELINE), ELINE_CE1, ELINE_CE2))
    if random.choice(PL_VS_VPL) == "tagged":
        c.addTask("Use a %s handoff with the vlan number of %s." % (random.choice(VPL), random.randint(1000, 2000)))
    else:
        c.addTask("Use a %s ethernet handoff." % random.choice(PL))
elif ISP1_L2VPN == "ELAN":
    #ELAN SERVICES
    ELAN_NODE = random.randint(2, 4)
    ELAN_CE1 = random.choice(L2_ISP1_CE)
    L2_ISP1_CE.remove(ELAN_CE1)
    ELAN_CE2 = random.choice(L2_ISP1_CE)
    L2_ISP1_CE.remove(ELAN_CE2)
    ELAN_CE3 = random.choice(L2_ISP1_CE)
    L2_ISP1_CE.remove(ELAN_CE3)
    ELAN_CE4 = random.choice(L2_ISP1_CE)
    L2_ISP1_CE.remove(ELAN_CE4)
    if ELAN_NODE == 2:
        c.addTask("Create a %s service from %s to %s. On each CE use the lowest number interface." % (random.choice(ELAN), ELAN_CE1, ELAN_CE2))
    elif ELAN_NODE == 3:
        c.addTask("Create a %s service between %s, %s and %s. On each CE use the lowest number interface." % (random.choice(ELAN), ELAN_CE1, ELAN_CE2, ELAN_CE3))
    else:
        c.addTask("Create a %s service between %s, %s, %s and %s. On each CE use the lowest number interface." % (random.choice(ELAN), ELAN_CE1, ELAN_CE2, ELAN_CE3, ELAN_CE4))
    if random.choice(PL_VS_VPL) == "tagged":
        c.addTask("Use a %s handoff with the vlan number of %s." % (random.choice(VPL), random.randint(1000, 2000)))
    else:
        c.addTask("Use a %s ethernet handoff." % random.choice(PL))
    if random.randint(0,1) == 0:
        c.addTask("Use manual %s style neighbor configuration and %s neighbor label signalling." % (random.choice(MARTINI), random.choice(SIGNAL)))
    else:
        ELAN_SIGNAL = random.choice(SIGNAL)
        c.addTask("Use %s auto neighbor discovery and %s label signalling." % (random.choice(KOMPELLA), ELAN_SIGNAL))
        if ELAN_SIGNAL == "BGP":
            c.addTask("Use the following RT schema of CE1CE2:CE1CE2 for AC discovery, an example for CE1 to CE3 would be 13:13.")
else:
    #ETREE SERVICES
    ETREE = []
    ETREE_CE1 = random.choice(L2_ISP1_CE)
    L2_ISP1_CE.remove(ETREE_CE1)
    ETREE.append(ETREE_CE1)
    ETREE_CE2 = random.choice(L2_ISP1_CE)
    L2_ISP1_CE.remove(ETREE_CE2)
    ETREE.append(ETREE_CE2)
    ETREE_CE3 = random.choice(L2_ISP1_CE)
    L2_ISP1_CE.remove(ETREE_CE3)
    ETREE.append(ETREE_CE3)
    ETREE_HUB = random.choice(ETREE)
    c.addTask("Create an E-TREE for the following three nodes %s %s %s.  The root of the tree is %s.  The spokes should not be able to talk directly." % (ETREE_CE1, ETREE_CE2, ETREE_CE3, ETREE_HUB))
    c.addTask("On each CE use the lowest number interface")
    if random.choice(PL_VS_VPL) == "tagged":
        c.addTask("Use a %s handoff with the vlan number of %s." % (random.choice(VPL), random.randint(1000, 2000)))
    else:
        c.addTask("Use a %s ethernet handoff." % random.choice(PL))
    if random.randint(0,1) == 0:
        c.addTask("Use manual %s style neighbor configuration and %s neighbor label signalling." % (random.choice(MARTINI), random.choice(SIGNAL)))
    else:
        ETREE_SIGNAL = random.choice(SIGNAL)
        c.addTask("Use %s auto neighbor discovery and %s label signalling." % (random.choice(KOMPELLA), ETREE_SIGNAL))
        if ETREE_SIGNAL == "BGP":
            c.addTask("Use the following RT schema of CE1CE2:CE1CE2 for AC discovery, an example for CE1 to CE3 would be 13:13.")

if random.randint(0,1) == 0:
    c.addTask("Do not enable control-word on the service.")
else:
    c.addTask("Configure control-word on the service.")
if random.randint(0,1) == 0:
    c.addTask("Change the MTU of the service to %s." % random.randrange(2000, 9000, 1000))
else:
    c.addTask("Keep the MTU of the service to the default of 1500.")
#this is where other PW based services will be added such as FAT in the future.

c.addBreaks()
#ISP2 L2VPN SERVICES
c.add("ISP2 L2VPN services")
if ISP2_L2VPN == "ELINE":
    #ELINE SERVICES
    ELINE_CE1 = random.choice(L2_ISP2_CE)
    L2_ISP2_CE.remove(ELINE_CE1)
    ELINE_CE2 = random.choice(L2_ISP2_CE)
    L2_ISP2_CE.remove(ELINE_CE2)
    c.addTask("Create a %s service from %s to %s. On each CE use the lowest number interface." % (random.choice(ELINE), ELINE_CE1, ELINE_CE2))
    if random.choice(PL_VS_VPL) == "tagged":
        c.addTask("Use a %s handoff with the vlan number of %s." % (random.choice(VPL), random.randint(1000, 2000)))
    else:
        c.addTask("Use a %s ethernet handoff." % random.choice(PL))
elif ISP2_L2VPN == "ELAN":
    ELAN_NODE = random.randint(2, 4)
    ELAN_CE1 = random.choice(L2_ISP2_CE)
    L2_ISP2_CE.remove(ELAN_CE1)
    ELAN_CE2 = random.choice(L2_ISP2_CE)
    L2_ISP2_CE.remove(ELAN_CE2)
    ELAN_CE3 = random.choice(L2_ISP2_CE)
    L2_ISP2_CE.remove(ELAN_CE3)
    ELAN_CE4 = random.choice(L2_ISP2_CE)
    L2_ISP2_CE.remove(ELAN_CE4)
    if ELAN_NODE == 2:
        c.addTask("Create a %s service from %s to %s. On each CE use the lowest number interface." % (random.choice(ELAN), ELAN_CE1, ELAN_CE2))
    elif ELAN_NODE == 3:
        c.addTask("Create a %s service between %s, %s and %s. On each CE use the lowest number interface." % (random.choice(ELAN), ELAN_CE1, ELAN_CE2, ELAN_CE3))
    else:
        c.addTask("Create a %s service between %s, %s, %s and %s. On each CE use the lowest number interface." % (random.choice(ELAN), ELAN_CE1, ELAN_CE2, ELAN_CE3, ELAN_CE4))
    if random.choice(PL_VS_VPL) == "tagged":
        c.addTask("Use a %s handoff with the vlan number of %s." % (random.choice(VPL), random.randint(1000, 2000)))
    else:
        c.addTask("Use a %s ethernet handoff." % random.choice(PL))
    if random.randint(0,1) == 0:
        c.addTask("Use manual %s style neighbor configuration and %s neighbor label signalling." % (random.choice(MARTINI), random.choice(SIGNAL)))
    else:
        ELAN_SIGNAL = random.choice(SIGNAL)
        c.addTask("Use %s auto neighbor discovery and %s label signalling." % (random.choice(KOMPELLA), ELAN_SIGNAL))
        if ELAN_SIGNAL == "BGP":
            c.addTask("Use the following RT schema of CE1CE2:CE1CE2 for AC discovery, an example for CE1 to CE3 would be 13:13.")
else:
    #ETREE SERVICES
    ETREE = []
    ETREE_CE1 = random.choice(L2_ISP2_CE)
    L2_ISP2_CE.remove(ETREE_CE1)
    ETREE.append(ETREE_CE1)
    ETREE_CE2 = random.choice(L2_ISP2_CE)
    L2_ISP2_CE.remove(ETREE_CE2)
    ETREE.append(ETREE_CE2)
    ETREE_CE3 = random.choice(L2_ISP2_CE)
    L2_ISP2_CE.remove(ETREE_CE3)
    ETREE.append(ETREE_CE3)
    ETREE_HUB = random.choice(ETREE)
    c.addTask("Create an E-TREE for the following three nodes %s %s %s.  The root of the tree is %s.  The spokes should not be able to talk directly." % (ETREE_CE1, ETREE_CE2, ETREE_CE3, ETREE_HUB))
    c.addTask("On each CE use the lowest number interface")
    if random.choice(PL_VS_VPL) == "tagged":
        c.addTask("Use a %s handoff with the vlan number of %s." % (random.choice(VPL), random.randint(1000, 2000)))
    else:
        c.addTask("Use a %s ethernet handoff." % random.choice(PL))
    if random.randint(0,1) == 0:
        c.addTask("Use manual %s style neighbor configuration and %s neighbor label signalling." % (random.choice(MARTINI), random.choice(SIGNAL)))
    else:
        ETREE_SIGNAL = random.choice(SIGNAL)
        c.addTask("Use %s auto neighbor discovery and %s label signalling." % (random.choice(KOMPELLA), ETREE_SIGNAL))
        if ETREE_SIGNAL == "BGP":
            c.addTask("Use the following RT schema of CE1CE2:CE1CE2 for AC discovery, an example for CE1 to CE3 would be 13:13.")

if random.randint(0,1) == 0:
    c.addTask("Do not enable control-word on the service.")
else:
    c.addTask("Configure control-word on the service.")
if random.randint(0,1) == 0:
    c.addTask("Change the MTU of the service to %s." % random.randrange(2000, 9000, 1000))
else:
    c.addTask("Keep the MTU of the service to the default of 1500.")
#this is where other PW based services will be added such as FAT in the future.

c.addBreaks()


c.addHeader("Access and Aggregation")
c.add("This section is worth 21% of the total points")
c.addHrule()

L3_ISP1_CE = ["CE1", "CE2", "CE3", "CE4"]
L3_ISP2_CE = ["CE5", "CE6", "CE7", "CE8"]
PE_CE_PROT = ["OSPF", "RIPv2", "EIGRP", "STATIC", "BGP"]
#BELOW IS A TEST VAR TO FORCE AND IGP
#PE_CE_PROT = ["EIGRP"]
#ISP1 L3VPN SERVICES

ISP1_L3VPN_NETWORK = random.randint(1, 4)
ISP1_L3VPN_CE1 = random.choice(L3_ISP1_CE)
L3_ISP1_CE.remove(ISP1_L3VPN_CE1)
ISP1_L3VPN_CE2 = random.choice(L3_ISP1_CE)
L3_ISP1_CE.remove(ISP1_L3VPN_CE2)
ISP1_L3VPN_CE3 = random.choice(L3_ISP1_CE)
L3_ISP1_CE.remove(ISP1_L3VPN_CE3)
ISP1_L3VPN_CE4 = random.choice(L3_ISP1_CE)
L3_ISP1_CE.remove(ISP1_L3VPN_CE4)
c.add("ISP1 L3VPN services")
if ISP1_L3VPN_NETWORK == 2:
    c.addTask("ISP1 currently has an L3VPN for the following nodes: %s %s." % (ISP1_L3VPN_CE1, ISP1_L3VPN_CE2))
    c.addTask("THE RD and RT methodology is ISP_ASN:CE#CE#, an example for an L3VPN using CE2 and CE3 is 1:23")
    c.addTask("The VRF name on each PE for this L3VPN should be: ISP1-CUST-1.")
    c.addTask("Each PE will exchange routes with the CE on its highest number interface.")
    c.addBreaks()
elif ISP1_L3VPN_NETWORK == 3:
    c.addTask("ISP1 currently has an L3VPN for the following nodes: %s %s %s." % (ISP1_L3VPN_CE1, ISP1_L3VPN_CE2, ISP1_L3VPN_CE3))
    c.addTask("THE RD and RT methodology is ISP_ASN:CE#CE#, an example for an L3VPN using CE2 and CE3 is 1:23")
    c.addTask("The VRF name on each PE for this L3VPN should be: ISP1-CUST-1.")
    c.addTask("Each PE will exchange routes with the CE on its highest number interface.")
    c.addBreaks()
else:
    c.addTask("ISP1 currently has an L3VPN for the following nodes: %s %s %s %s." % (ISP1_L3VPN_CE1, ISP1_L3VPN_CE2, ISP1_L3VPN_CE3, ISP1_L3VPN_CE4))
    c.addTask("THE RD and RT methodology is ISP_ASN:CE#CE#, an example for an L3VPN using CE2 and CE3 is 1:23")
    c.addTask("The VRF name on each PE for this L3VPN should be: ISP1-CUST-1.")
    c.addTask("Each PE will exchange routes with the CE on its highest number interface.")
    c.addBreaks()
c.add("ISP1 L3VPN PE-CE routing")
ISP1_L3VPN_IGP = random.choice(PE_CE_PROT)
if ISP1_L3VPN_IGP == "STATIC":
    c.addTask("Each PE and CE will peer via static routes, redistribute accordingly on each PE.")
elif ISP1_L3VPN_IGP == "RIPv2":
    c.addTask("Each PE and CE will peer via RIPv2.")
    if random.randint(0, 1) == 1:
        c.addTask("Ensure the metric passes transparently through the SP network.")
    else:
        c.addTask("Redistribute RIP on the PE with a metric of %s." % random.randint(3, 10))
    if random.randint(0, 1) == 1:
        c.addTask("Do not enable authentication with the customer.")
    else:
        c.addTask("Enable authentication with the customer using the password 'cisco'.")
    if random.randint(0, 1) == 1:
        c.addTask("Provide the customer a default route.")
    else:
        c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
elif ISP1_L3VPN_IGP == "EIGRP":
    c.addTask("Each PE and CE will peer via EIGRP using ASN %s." % random.randint(1, 65535))
    if random.randint(0, 1) == 1:
        c.addTask("Ensure the metric passes transparently through the SP network.")
    else:
        c.addTask("Redistribute EIGRP on the PE with a metric of %sM bandwidth, %s msec delay, 100 percent reliability, 1 percent load and 1500 MTU." % (random.randrange(100, 1000, 100), random.randrange(100, 1000, 100)))
    if random.randint(0, 1) == 1:
        c.addTask("Do not enable authentication with the customer.")
    else:
        c.addTask("Enable authentication with the customer using the password 'cisco'.")
    if random.randint(0, 1) == 1:
        c.addTask("Provide the customer a default route.")
    else:
        c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
elif ISP1_L3VPN_IGP == "OSPF":
    OSPF_METRIC_TYPE = ("E1","E2")
    OSPF_ROUTE_TYPE = ("External", "Inter area", "Intra area")
    c.addTask("Each PE and CE will peer via OSPF using PID %s." % random.randint(1, 65535))
    if random.randint(0, 1) == 1:
        c.addTask("Ensure the metric passes transparently through the SP network.")
    else:
        c.addTask("Redistribute OSPF on the PE with a metric of %s and type of %s." % (random.randrange(100, 1000, 100), random.choice(OSPF_METRIC_TYPE)))
    if random.randint(0, 1) == 1:
        c.addTask("Do not enable authentication with the customer.")
    else:
        c.addTask("Enable authentication with the customer using the password 'cisco'.")
    if random.randint(0, 1) == 1:
        c.addTask("Provide the customer a default route type %s." % random.choice(OSPF_METRIC_TYPE))
    else:
        c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
    c.addTask("The customer should see the routes from the other sites as %s routes." % random.choice(OSPF_ROUTE_TYPE))
else:
    c.addTask("eBGP will be used as the PE-CE peering protocol.")
    if random.randint(0, 1) == 1:
        c.addTask("Each CE will use the two-byte ASN %s to peer with the PE." % random.randint(64512, 65535))
    else:
        c.addTask("Each CE will use the four-byte ASN %s:%s to peer with the PE." % (random.randint(64512, 65535), random.randint(64512, 65535)))
    if random.randint(0, 1) == 1:
        c.addTask("Do not accept BGP community values from the CE.")
    else:
        c.addTask("Accept BGP community values from the CE.")
    if random.randint(0, 1) == 1:
        c.addTask("Do not enable authentication with the customer.")
    else:
        c.addTask("Enable authentication with the customer using the password 'cisco'.")
    if random.randint(0, 1) == 1:
        c.addTask("The CE will use allowas-in to allow prefixes from other CE's into its BGP RIB.")
    else:
        c.addTask("The PE will use as-override to ensure the CE learns prefixes from other CE's.")
    if random.randint(0, 1) == 1:
        c.addTask("Only accept %s BGP prefixes from the customer, warn at %s percent and once the threshold is passed shutdown the BGP session." % (random.randrange(500, 1000, 100), random.randrange(50, 100, 10)))
        c.addTask("Have the BGP session automatically restart after %s minutes." % random.randint(3, 10))
    else:
        c.addTask("Only accept %s BGP prefixes from the customer, warn at %s percent and do not shut down the session!" % (random.randrange(500, 1000, 100), random.randrange(50, 100, 10)))

if random.randint(0,1) == 0:
    c.addTask("Limit the amount of prefixes in the VRF routing table to %s." % random.randrange(1000, 2000, 100))
else:
    CE_LABEL = ("per-prefix(default)", "per-vrf", "per-CE")
    c.add("This is an untested task and will need to be verified on IOS-XE and IOS-XR.")
    c.addTask("Allocate MPLS labels %s." % random.choice(CE_LABEL))
c.addBreaks()

#ISP2 L3VPN SERVICES
ISP2_L3VPN_NETWORK = random.randint(1, 4)
ISP2_L3VPN_CE1 = random.choice(L3_ISP2_CE)
L3_ISP2_CE.remove(ISP2_L3VPN_CE1)
ISP2_L3VPN_CE2 = random.choice(L3_ISP2_CE)
L3_ISP2_CE.remove(ISP2_L3VPN_CE2)
ISP2_L3VPN_CE3 = random.choice(L3_ISP2_CE)
L3_ISP2_CE.remove(ISP2_L3VPN_CE3)
ISP2_L3VPN_CE4 = random.choice(L3_ISP2_CE)
L3_ISP2_CE.remove(ISP2_L3VPN_CE4)
c.add("ISP2 L3VPN services")
if ISP2_L3VPN_NETWORK == 2:
    c.addTask("ISP2 currently has an L3VPN for the following nodes: %s %s." % (ISP2_L3VPN_CE1, ISP2_L3VPN_CE2))
    c.addTask("THE RD and RT methodology is ISP_ASN:CE#CE#, an example for an L3VPN using CE5 and CE7 is 2:57")
    c.addTask("The VRF name on each PE for this L3VPN should be: ISP2-CUST-1.")
    c.addTask("Each PE will exchange routes with the CE on its highest number interface.")
    c.addBreaks()
elif ISP2_L3VPN_NETWORK == 3:
    c.addTask("ISP2 currently has an L3VPN for the following nodes: %s %s %s." % (ISP2_L3VPN_CE1, ISP2_L3VPN_CE2, ISP2_L3VPN_CE3))
    c.addTask("THE RD and RT methodology is ISP_ASN:CE#CE#, an example for an L3VPN using CE5 and CE7 is 2:57")
    c.addTask("The VRF name on each PE for this L3VPN should be: ISP2-CUST-1.")
    c.addTask("Each PE will exchange routes with the CE on its highest number interface.")
    c.addBreaks()
else:
    c.addTask("ISP2 currently has an L3VPN for the following nodes: %s %s %s %s." % (ISP2_L3VPN_CE1, ISP2_L3VPN_CE2, ISP2_L3VPN_CE3, ISP2_L3VPN_CE4))
    c.addTask("THE RD and RT methodology is ISP_ASN:CE#CE#, an example for an L3VPN using CE5 and CE7 is 2:57")
    c.addTask("The VRF name on each PE for this L3VPN should be: ISP2-CUST-1.")
    c.addTask("Each PE will exchange routes with the CE on its highest number interface.")
    c.addBreaks()
c.add("ISP2 L3VPN PE-CE routing")
ISP2_L3VPN_IGP = random.choice(PE_CE_PROT)
if ISP2_L3VPN_IGP == "STATIC":
    c.addTask("Each PE and CE will peer via static routes, redistribute accordingly on each PE.")
elif ISP2_L3VPN_IGP == "RIPv2":
    c.addTask("Each PE and CE will peer via RIPv2.")
    if random.randint(0, 1) == 1:
        c.addTask("Ensure the metric passes transparently through the SP network.")
    else:
        c.addTask("Redistribute RIP on the PE with a metric of %s." % random.randint(3, 10))
    if random.randint(0, 1) == 1:
        c.addTask("Do not enable authentication with the customer.")
    else:
        c.addTask("Enable authentication with the customer using the password 'cisco'.")
    if random.randint(0, 1) == 1:
        c.addTask("Provide the customer a default route.")
    else:
        c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
elif ISP2_L3VPN_IGP == "EIGRP":
    c.addTask("Each PE and CE will peer via EIGRP using ASN %s." % random.randint(1, 65535))
    if random.randint(0, 1) == 1:
        c.addTask("Ensure the metric passes transparently through the SP network.")
    else:
        c.addTask("Redistribute EIGRP on the PE with a metric of %sM bandwidth, %s msec delay, 100 percent reliability, 1 percent load and 1500 MTU." % (random.randrange(100, 1000, 100), random.randrange(100, 1000, 100)))
    if random.randint(0, 1) == 1:
        c.addTask("Do not enable authentication with the customer.")
    else:
        c.addTask("Enable authentication with the customer using the password 'cisco'.")
    if random.randint(0, 1) == 1:
        c.addTask("Provide the customer a default route.")
    else:
        c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
elif ISP2_L3VPN_IGP == "OSPF":
    OSPF_METRIC_TYPE = ("E1","E2")
    OSPF_ROUTE_TYPE = ("External", "Inter area", "Intra area")
    c.addTask("Each PE and CE will peer via OSPF using PID %s." % random.randint(1, 65535))
    if random.randint(0, 1) == 1:
        c.addTask("Ensure the metric passes transparently through the SP network.")
    else:
        c.addTask("Redistribute OSPF on the PE with a metric of %s and type of %s." % (random.randrange(100, 1000, 100), random.choice(OSPF_METRIC_TYPE)))
    if random.randint(0, 1) == 1:
        c.addTask("Do not enable authentication with the customer.")
    else:
        c.addTask("Enable authentication with the customer using the password 'cisco'.")
    if random.randint(0, 1) == 1:
        c.addTask("Provide the customer a default route type %s." % random.choice(OSPF_METRIC_TYPE))
    else:
        c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
    c.addTask("The customer should see the routes from the other sites as %s routes." % random.choice(OSPF_ROUTE_TYPE))
else:
    c.addTask("eBGP will be used as the PE-CE peering protocol.")
    if random.randint(0, 1) == 1:
        c.addTask("Each CE will use the two-byte ASN %s to peer with the PE." % random.randint(64512, 65535))
    else:
        c.addTask("Each CE will use the four-byte ASN %s:%s to peer with the PE." % (random.randint(64512, 65535), random.randint(64512, 65535)))
    if random.randint(0, 1) == 1:
        c.addTask("Do not accept BGP community values from the CE.")
    else:
        c.addTask("Accept BGP community values from the CE.")
    if random.randint(0, 1) == 1:
        c.addTask("Do not enable authentication with the customer.")
    else:
        c.addTask("Enable authentication with the customer using the password 'cisco'.")
    if random.randint(0, 1) == 1:
        c.addTask("The CE will use allowas-in to allow prefixes from other CE's into its BGP RIB.")
    else:
        c.addTask("The PE will use as-override to ensure the CE learns prefixes from other CE's.")
    if random.randint(0, 1) == 1:
        c.addTask("Only accept %s BGP prefixes from the customer, warn at %s percent and once the threshold is passed shutdown the BGP session." % (random.randrange(500, 1000, 100), random.randrange(50, 100, 10)))
        c.addTask("Have the BGP session automatically restart after %s minutes." % random.randint(3, 10))
    else:
        c.addTask("Only accept %s BGP prefixes from the customer, warn at %s percent and do not shut down the session!" % (random.randrange(500, 1000, 100), random.randrange(50, 100, 10)))

if random.randint(0,1) == 0:
    c.addTask("Limit the amount of prefixes in the VRF routing table to %s." % random.randrange(1000, 2000, 100))
else:
    CE_LABEL = ("per-prefix(default)", "per-vrf", "per-CE")
    c.add("This is an untested task and will need to be verified on IOS-XE and IOS-XR.")
    c.addTask("Allocate MPLS labels %s." % random.choice(CE_LABEL))
c.addBreaks()

#internet/shared services, this section needs some work on the inbound/outbound but what?
c.add("ISP1 Internet or Shared Services offerings.")
if random.randint(0, 1) == 1:
    c.addTask("ISP1 has purchased transit from an upstream provider (which is a VRF inside of CE1 conected to ASBR1) configure this BGP peering session in the global table.")
    c.addTask("Configure an inbound policy to not allow any RFC 1918 addressing or prefixes longer than /24 into the network.")
    c.addTask("Configure an outbound policy to strip all prefixes of their community values and add the community value of 1:1 as they exit.")
    c.addTask("Lastly do not allow any of the internal core links or loopbacks out of the network to the provider.")
    if random.randint(0, 1) == 1:
        c.addTask("ISP1 sales would like a proof of concept that internet will work for L3VPN customers.  Based on how the Internet is configured above select a single L3VPN customer and configure them internet access.")
        c.addBreaks()
    else:
        c.addTask("ISP1 would like to offer a shared services COLO, configure a vrf on PE2 named Services with RD/RT of 999:999.  Select a single L3VPN customer to try out this solution with.")
        c.addBreaks()
else:
    c.addTask("ISP1 has purchased transit from an upstream provider (which is a VRF inside of CE1 conected to ASBR1) configure this BGP peering session in a VRF called Internet.")
    c.addTask("Use the RD of 666:666 and RT imports and exports of 666:666.")
    c.addTask("Configure an inbound policy to not allow any RFC 1918 addressing or prefixes longer than /24 into the network.")
    c.addTask("Configure an outbound policy to strip all prefixes of their community values and add the community value of 1:1 as they exit.")
    c.addTask("Lastly do not allow any of the internal core links or loopbacks out of the network to the provider.")
    if random.randint(0, 1) == 1:
        c.addTask("ISP1 sales would like a proof of concept that internet will work for L3VPN customers.  Based on how the Internet is configured above select a single L3VPN customer and configure them internet access.")
        c.addBreaks()
    else:
        c.addTask("ISP1 would like to offer a shared services COLO, configure a vrf on PE2 named Services with RD/RT of 999:999.  Select a single L3VPN customer to try out this solution with.")
        c.addBreaks()

c.add("ISP2 Internet or Shared Services offerings.")
if random.randint(0, 1) == 1:
    c.addTask("ISP2 has purchased transit from an upstream provider (which is a VRF inside of CE5 conected to ASBR2) configure this BGP peering session in the global table.")
    c.addTask("Configure an inbound policy to not allow any RFC 1918 addressing or prefixes longer than /24 into the network.")
    c.addTask("Configure an outbound policy to strip all prefixes of their community values and add the community value of 2:2 as they exit.")
    c.addTask("Lastly do not allow any of the internal core links or loopbacks out of the network to the provider.")
    if random.randint(0, 1) == 1:
        c.addTask("ISP2 sales would like a proof of concept that internet will work for L3VPN customers.  Based on how the Internet is configured above select a single L3VPN customer and configure them internet access.")
        c.addBreaks()
    else:
        c.addTask("ISP2 would like to offer a shared services COLO, configure a vrf on PE4 named Services with RD/RT of 999:999.  Select a single L3VPN customer to try out this solution with.")
        c.addBreaks()
else:
    c.addTask("ISP2 has purchased transit from an upstream provider (which is a VRF inside of CE5 conected to ASBR2) configure this BGP peering session in a VRF called Internet.")
    c.addTask("Use the RD of 999:999 and RT imports and exports of 999:999.")
    c.addTask("Configure an inbound policy to not allow any RFC 1918 addressing or prefixes longer than /24 into the network.")
    c.addTask("Configure an outbound policy to strip all prefixes of their community values and add the community value of 2:2 as they exit.")
    c.addTask("Lastly do not allow any of the internal core links or loopbacks out of the network to the provider.")
    if random.randint(0, 1) == 1:
        c.addTask("ISP2 sales would like a proof of concept that internet will work for L3VPN customers.  Based on how the Internet is configured above select a single L3VPN customer and configure them internet access.")
        c.addBreaks()
    else:
        c.addTask("ISP2 would like to offer a shared services COLO, configure a vrf on PE4 named Services with RD/RT of 999:999.  Select a single L3VPN customer to try out this solution with.")
        c.addBreaks()

# ISP1 6PE and 6VPE
ISP_V6_TYPES = ("6PE", "6VPE")
V6_ISP1_CE = ["CE1", "CE2", "CE3", "CE4"]
PE_CE_PROT_V6 = ["OSPFV3", "RIPNG", "EIGRP", "STATIC", "BGP"]
SIX_PE_TYPE = ("Full Table", "Default Route")
ISP1_6VPE_CE1 = random.choice(V6_ISP1_CE)
V6_ISP1_CE.remove(ISP1_6VPE_CE1)
ISP1_6VPE_CE2 = random.choice(V6_ISP1_CE)
c.add("ISP1 6PE or 6VPE.")
if random.choice(ISP_V6_TYPES) == "6PE":
    c.addTask("%s has requested to buy IPV6 DIA from ISP1, configure the Internet Edge router to peer IPV6 with the transit provider." % random.choice(V6_ISP1_CE))
    c.addTask("Configure the ingress and egress filtering on the Internet Edge router as above.")
    c.addTask("Peer with the CE via %s.  If an IGP feed them the %s." % (random.choice(PE_CE_PROT), random.choice(SIX_PE_TYPE)))
    c.addBreaks()
else:
    c.addTask("Create an IPV6 L3VPN network between %s and %s." % (ISP1_6VPE_CE1, ISP1_6VPE_CE2))
    ISP1_6VPE_IGP = random.choice(PE_CE_PROT_V6)
    if ISP1_6VPE_IGP == "STATIC":
        c.addTask("Each PE and CE will peer via static routes, redistribute accordingly on each PE.")
        c.addBreaks()
    elif ISP1_6VPE_IGP == "RIPNG":
        c.addTask("Each PE and CE will peer via RIPNG.")
        if random.randint(0, 1) == 1:
            c.addTask("Ensure the metric passes transparently through the SP network.")
        else:
            c.addTask("Redistribute RIP on the PE with a metric of %s." % random.randint(3, 10))
        if random.randint(0, 1) == 1:
            c.addTask("Do not enable authentication with the customer.")
        else:
            c.addTask("Enable authentication with the customer using the password 'cisco'.")
        if random.randint(0, 1) == 1:
            c.addTask("Provide the customer a default route.")
        else:
            c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
        c.addBreaks()
    elif ISP1_6VPE_IGP == "EIGRP":
        c.addTask("Each PE and CE will peer via EIGRP using ASN %s." % random.randint(1, 65535))
        if random.randint(0, 1) == 1:
            c.addTask("Ensure the metric passes transparently through the SP network.")
        else:
            c.addTask("Redistribute EIGRP on the PE with a metric of %sM bandwidth, %s msec delay, 100 percent reliability, 1 percent load and 1500 MTU." % (random.randrange(100, 1000, 100), random.randrange(100, 1000, 100)))
        if random.randint(0, 1) == 1:
            c.addTask("Do not enable authentication with the customer.")
        else:
            c.addTask("Enable authentication with the customer using the password 'cisco'.")
        if random.randint(0, 1) == 1:
            c.addTask("Provide the customer a default route.")
        else:
            c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
        c.addBreaks()
    elif ISP1_6VPE_IGP == "OSPFV3":
        OSPF_METRIC_TYPE = ("E1","E2")
        OSPF_ROUTE_TYPE = ("External", "Inter area", "Intra area")
        c.addTask("Each PE and CE will peer via OSPFv3 using PID %s." % random.randint(1, 65535))
        if random.randint(0, 1) == 1:
            c.addTask("Ensure the metric passes transparently through the SP network.")
        else:
            c.addTask("Redistribute OSPF on the PE with a metric of %s and type of %s." % (random.randrange(100, 1000, 100), random.choice(OSPF_METRIC_TYPE)))
        if random.randint(0, 1) == 1:
            c.addTask("Do not enable authentication with the customer.")
        else:
            c.addTask("Enable authentication with the customer using the password 'cisco'.")
        if random.randint(0, 1) == 1:
            c.addTask("Provide the customer a default route type %s." % random.choice(OSPF_METRIC_TYPE))
        else:
            c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
        c.addTask("The customer should see the routes from the other sites as %s routes." % random.choice(OSPF_ROUTE_TYPE))
        c.addBreaks()
    else:
        c.addTask("eBGP will be used as the PE-CE peering protocol.")
        if random.randint(0, 1) == 1:
            c.addTask("Each CE will use the two-byte ASN %s to peer with the PE." % random.randint(64512, 65535))
        else:
            c.addTask("Each CE will use the four-byte ASN %s:%s to peer with the PE." % (random.randint(64512, 65535), random.randint(64512, 65535)))
        if random.randint(0, 1) == 1:
            c.addTask("Do not accept BGP community values from the CE.")
        else:
            c.addTask("Accept BGP community values from the CE.")
        if random.randint(0, 1) == 1:
            c.addTask("Do not enable authentication with the customer.")
        else:
            c.addTask("Enable authentication with the customer using the password 'cisco'.")
        if random.randint(0, 1) == 1:
            c.addTask("The CE will use allowas-in to allow prefixes from other CE's into its BGP RIB.")
        else:
            c.addTask("The PE will use as-override to ensure the CE learns prefixes from other CE's.")
        if random.randint(0, 1) == 1:
            c.addTask("Only accept %s BGP prefixes from the customer, warn at %s percent and once the threshold is passed shutdown the BGP session." % (random.randrange(500, 1000, 100), random.randrange(50, 100, 10)))
            c.addTask("Have the BGP session automatically restart after %s minutes." % random.randint(3, 10))
        else:
            c.addTask("Only accept %s BGP prefixes from the customer, warn at %s percent and do not shut down the session!" % (random.randrange(500, 1000, 100), random.randrange(50, 100, 10)))
        c.addBreaks()

#ISP2 6PE and 6VPE
V6_ISP2_CE = ["CE5", "CE6", "CE7", "CE8"]
ISP2_6VPE_CE1 = random.choice(V6_ISP2_CE)
V6_ISP2_CE.remove(ISP2_6VPE_CE1)
ISP2_6VPE_CE2 = random.choice(V6_ISP2_CE)
c.add("ISP2 6PE or 6VPE.")
if random.choice(ISP_V6_TYPES) == "6PE":
    c.addTask("%s has requested to buy IPV6 DIA from ISP2, configure the Internet Edge router to peer IPV6 with the transit provider." % random.choice(V6_ISP1_CE))
    c.addTask("Configure the ingress and egress filtering on the Internet Edge router as above.")
    c.addTask("Peer with the CE via %s.  If an IGP feed them the %s." % (random.choice(PE_CE_PROT), random.choice(SIX_PE_TYPE)))
    c.addBreaks()
else:
    c.addTask("Create an IPV6 L3VPN network between %s and %s." % (ISP2_6VPE_CE1, ISP2_6VPE_CE2))
    ISP2_6VPE_IGP = random.choice(PE_CE_PROT_V6)
    if ISP2_6VPE_IGP == "STATIC":
        c.addTask("Each PE and CE will peer via static routes, redistribute accordingly on each PE.")
        c.addBreaks()
    elif ISP2_6VPE_IGP == "RIPNG":
        c.addTask("Each PE and CE will peer via RIPNG.")
        if random.randint(0, 1) == 1:
            c.addTask("Ensure the metric passes transparently through the SP network.")
        else:
            c.addTask("Redistribute RIP on the PE with a metric of %s." % random.randint(3, 10))
        if random.randint(0, 1) == 1:
            c.addTask("Do not enable authentication with the customer.")
        else:
            c.addTask("Enable authentication with the customer using the password 'cisco'.")
        if random.randint(0, 1) == 1:
            c.addTask("Provide the customer a default route.")
        else:
            c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
        c.addBreaks()
    elif ISP2_6VPE_IGP == "EIGRP":
        c.addTask("Each PE and CE will peer via EIGRP using ASN %s." % random.randint(1, 65535))
        if random.randint(0, 1) == 1:
            c.addTask("Ensure the metric passes transparently through the SP network.")
        else:
            c.addTask("Redistribute EIGRP on the PE with a metric of %sM bandwidth, %s msec delay, 100 percent reliability, 1 percent load and 1500 MTU." % (random.randrange(100, 1000, 100), random.randrange(100, 1000, 100)))
        if random.randint(0, 1) == 1:
            c.addTask("Do not enable authentication with the customer.")
        else:
            c.addTask("Enable authentication with the customer using the password 'cisco'.")
        if random.randint(0, 1) == 1:
            c.addTask("Provide the customer a default route.")
        else:
            c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
        c.addBreaks()
    elif ISP2_6VPE_IGP == "OSPFV3":
        OSPF_METRIC_TYPE = ("E1","E2")
        OSPF_ROUTE_TYPE = ("External", "Inter area", "Intra area")
        c.addTask("Each PE and CE will peer via OSPFv3 using PID %s." % random.randint(1, 65535))
        if random.randint(0, 1) == 1:
            c.addTask("Ensure the metric passes transparently through the SP network.")
        else:
            c.addTask("Redistribute OSPF on the PE with a metric of %s and type of %s." % (random.randrange(100, 1000, 100), random.choice(OSPF_METRIC_TYPE)))
        if random.randint(0, 1) == 1:
            c.addTask("Do not enable authentication with the customer.")
        else:
            c.addTask("Enable authentication with the customer using the password 'cisco'.")
        if random.randint(0, 1) == 1:
            c.addTask("Provide the customer a default route type %s." % random.choice(OSPF_METRIC_TYPE))
        else:
            c.addTask("Filter the prefixes on ingress to ensure the customer does not feed a default route into the L3VPN.")
        c.addTask("The customer should see the routes from the other sites as %s routes." % random.choice(OSPF_ROUTE_TYPE))
        c.addBreaks()
    else:
        c.addTask("eBGP will be used as the PE-CE peering protocol.")
        if random.randint(0, 1) == 1:
            c.addTask("Each CE will use the two-byte ASN %s to peer with the PE." % random.randint(64512, 65535))
        else:
            c.addTask("Each CE will use the four-byte ASN %s:%s to peer with the PE." % (random.randint(64512, 65535), random.randint(64512, 65535)))
        if random.randint(0, 1) == 1:
            c.addTask("Do not accept BGP community values from the CE.")
        else:
            c.addTask("Accept BGP community values from the CE.")
        if random.randint(0, 1) == 1:
            c.addTask("Do not enable authentication with the customer.")
        else:
            c.addTask("Enable authentication with the customer using the password 'cisco'.")
        if random.randint(0, 1) == 1:
            c.addTask("The CE will use allowas-in to allow prefixes from other CE's into its BGP RIB.")
        else:
            c.addTask("The PE will use as-override to ensure the CE learns prefixes from other CE's.")
        if random.randint(0, 1) == 1:
            c.addTask("Only accept %s BGP prefixes from the customer, warn at %s percent and once the threshold is passed shutdown the BGP session." % (random.randrange(500, 1000, 100), random.randrange(50, 100, 10)))
            c.addTask("Have the BGP session automatically restart after %s minutes." % random.randint(3, 10))
        else:
            c.addTask("Only accept %s BGP prefixes from the customer, warn at %s percent and do not shut down the session!" % (random.randrange(500, 1000, 100), random.randrange(50, 100, 10)))
        c.addBreaks()

# interAS options, need more to this first.
c.add("MPLS Inter-AS.")
INTERAS_TYPES = ("Option A", "Option B", "Option C")
INTERAS = random.choice(INTERAS_TYPES)
INTERAS_RT = ("rewrite", "import")
c.addTask("ISP 1 and ISP 2 plan on offering services to its customers via MPLS Inter-AS %s" % INTERAS)
if INTERAS == "Option A":
    if random.randint(0, 1) == 1:
        c.addTask("Select a single L3VPN customer in each network and extend services across the ASBR's.")
    else:
        c.addTask("Select a single L3VPN customer and L2VPN customer in each network and extend services across the ASBR's")
    if random.randint(0, 1) == 1:
        c.addTask("Select a single 6VPE customer in each network and extend services across the ASBR's.")
    else:
        c.addTask("Extend the customers multicast across the ASBR's.")
    c.addBreaks()
elif INTERAS == "Option B":
    if random.randint(0, 1) == 1:
        c.addTask("Import the local ISP's RT's as needed on the ASBR.")
    else:
        c.addTask("Instruct the ASBR to import all RT's even if they do not have that local VRF on the box.")
    if random.randint(0, 1) == 1:
        c.addTask("Select a single L3VPN customer in each network and extend services across the ASBR's.")
    else:
        c.addTask("Select a single L3VPN customer and L2VPN customer in each network and extend services across the ASBR's")
    if random.randint(0, 1) == 1:
        c.addTask("Select a single 6VPE customer in each network and extend services across the ASBR's.")
    else:
        c.addTask("Extend the customers multicast across the ASBR's.")
    if random.choice(INTERAS_RT) == "rewrite":
        c.addTask("Rewrite the RT's on the ASBR's so each networks PE's do not need to import any additional RT values.")
    else:
        c.addTask("Have the ASBR and all PE's import each others RT's to ensure all routes are received as needed.")
    c.addBreaks()
else:
    if random.randint(0, 1) == 1:
        c.addTask("Select a single L3VPN customer in each network and extend services across the ASBR's.")
    else:
        c.addTask("Select a single L3VPN customer and L2VPN customer in each network and extend services across the ASBR's")
    if random.randint(0, 1) == 1:
        c.addTask("Select a single 6VPE customer in each network and extend services across the ASBR's.")
    else:
        c.addTask("Extend the customers multicast across the ASBR's.")
    if random.randint(0, 1) == 1:
        c.addTask("Make the existing RR's the L3VPN RR's, make sure it is not in the datapath unless it needs to be.")
    else:
        c.addTask("Make the existing RR's the L3VPN RR's, make sure it remains in the data path no matter what.")
    c.addBreaks()

# go back, add a place holder for segment routing and then overlays such as L2TPv3, DMVPN, etc.
#Edge QoS, PE-CE MCAST
#IGP tweaks on L3VPN PE-CE protocols (timers? etc?)
#NEED TO REORDER SOME TASKS, think about moving away from the blueprint format and going by tech while still following the blueprint,  ie L3VPN as it is now, vs L3VPN ISP side and L3VPN PE-CE
#as the bluerint does in two different sections (2 and 3).
#VIRL base configs

c.output()
