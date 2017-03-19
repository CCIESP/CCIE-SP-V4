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

c.add("Welcome to the CCIE-SPv4 MOCK LAB random task generator!")
c.add("Please use these tasks with the prebuilt two ISP topology.")
c.add("As with the real lab you only have 5 hours to complete these tasks.")
c.add("Your topology should be prebuilt and pre IP'ed (v4/v6).")
c.add("Please stop and verify before you start your timer!")
c.addBreaks()
c.addSection("Core Routing")
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
c.add("Multicast for ISP1 to be added soon")
c.addBreaks()

#ISP2's Multicast
c.add("Multicast for ISP2 to be added soon")
c.addBreaks()

#ISP1 Core QoS
CORE_QOS_CLASSES = ["Voice", "Video", "Business", "Critical", "Best Effort"]
CORE_QOS_DECISION = ["QGROUP", "EXP", "NONE"]
CORE_QOS_BEST_EFFORT = ["WRED", "Tail Drop", "CBWFQ remaining bandwidth"]

ISP1_NUMBER_OF_CORE_QOS = random.randint(3,5)
c.add("ISP1 Core QoS")
c.add("ISP1 today honors %s classes of QoS in the Core." % ISP1_NUMBER_OF_CORE_QOS)
if random.choice(CORE_QOS_DECISION) == "EXP":
    if ISP1_NUMBER_OF_CORE_QOS == 3:
        c.add("ISP1 honors the following classes: Voice (EXP5), Business (EXP2) and Best Effort (EXP0).")
        c.addTask("ISP1 gives EXP5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP1 gives EXP2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    elif ISP1_NUMBER_OF_CORE_QOS == 4:
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
    if ISP1_NUMBER_OF_CORE_QOS == 3:
        c.add("ISP1 honors the following classes: Voice (QGroup5), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP1 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP1 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP1 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    elif ISP1_NUMBER_OF_CORE_QOS == 4:
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
    c.add("While ISP1 does honor %s classes of markings they have decided to not do anythings with the markings on a per hop basis, consider yourself lucky?" % ISP1_NUMBER_OF_CORE_QOS)
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
        c.addBreaks()
    elif ISP2_NUMBER_OF_CORE_QOS == 4:
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
    if ISP2_NUMBER_OF_CORE_QOS == 3:
        c.add("ISP2 honors the following classes: Voice (QGroup5), Business (QGroup2) and Best Effort (QGroup0).")
        c.addTask("ISP2 gives QGroup5 priority treatment in the LLQ and polices that rate to %s percent." % random.randint(20, 40))
        c.addTask("ISP2 gives QGroup2 CBWFQ treatment and a bandwidth guarantee of %s percent." % random.randint(20, 35))
        c.addTask("ISP2 protects the rest of the traffic in the Best Effort queue via %s." % random.choice(CORE_QOS_BEST_EFFORT))
        c.addBreaks()
    elif ISP2_NUMBER_OF_CORE_QOS == 4:
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
    c.add("While ISP2 does honor %s classes of markings they have decided to not do anythings with the markings on a per hop basis, consider yourself lucky?" % ISP2_NUMBER_OF_CORE_QOS)
    c.addBreaks()

c.addHeader("Service Provider based services")
c.add("This section is worth 26% of the total points")
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

#next up, Central services L3VPN and DIA using direct PE and L2-PE/L3-PE setup.
#QoS
#IGP tweaks on L3VPN PE-CE protocols (timers? etc?)
#interAS policies
#VIRL base configs
#peering with the "internet" and peering RPL policies.


c.output()
