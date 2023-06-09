
import jpype
import jpype.imports
from jpype.types import *
import time
classpath = "/Users/bahare/Packages/bayesserver-9.4/Java/bayesserver-10.8.jar"

# Launch the JVM
jpype.startJVM(classpath=[classpath])

# import the Java modules
from com.bayesserver import *
from com.bayesserver.inference import *
from com.bayesserver.analysis import *
from jpype import java
network = Network('sachs')

#  add the nodes/variables

AktLOW = State('LOW')
AktAVG = State('AVG')
AktHIGH = State('HIGH')
Akt = Node('Akt', [AktLOW, AktAVG, AktHIGH])

ErkLOW = State('LOW')
ErkAVG = State('AVG')
ErkHIGH = State('HIGH')
Erk = Node('Erk', [ErkLOW, ErkAVG, ErkHIGH])

JnkLOW = State('LOW')
JnkAVG = State('AVG')
JnkHIGH = State('HIGH')
Jnk = Node('Jnk', [JnkLOW, JnkAVG, JnkHIGH])

MekLOW = State('LOW')
MekAVG = State('AVG')
MekHIGH = State('HIGH')
Mek = Node('Mek', [MekLOW, MekAVG, MekHIGH])

P38LOW = State('LOW')
P38AVG = State('AVG')
P38HIGH = State('HIGH')
P38 = Node('P38', [P38LOW, P38AVG, P38HIGH])

PIP2LOW = State('LOW')
PIP2AVG = State('AVG')
PIP2HIGH = State('HIGH')
PIP2 = Node('PIP2', [PIP2LOW, PIP2AVG, PIP2HIGH])

PIP3LOW = State('LOW')
PIP3AVG = State('AVG')
PIP3HIGH = State('HIGH')
PIP3 = Node('PIP3', [PIP3LOW, PIP3AVG, PIP3HIGH])

PKALOW = State('LOW')
PKAAVG = State('AVG')
PKAHIGH = State('HIGH')
PKA = Node('PKA', [PKALOW, PKAAVG, PKAHIGH])

PKCLOW = State('LOW')
PKCAVG = State('AVG')
PKCHIGH = State('HIGH')
PKC = Node('PKC', [PKCLOW, PKCAVG, PKCHIGH])

PlcgLOW = State('LOW')
PlcgAVG = State('AVG')
PlcgHIGH = State('HIGH')
Plcg = Node('Plcg', [PlcgLOW, PlcgAVG, PlcgHIGH])

RafLOW = State('LOW')
RafAVG = State('AVG')
RafHIGH = State('HIGH')
Raf = Node('Raf', [RafLOW, RafAVG, RafHIGH])

nodes = network.getNodes()
nodes.add(Akt)
nodes.add(Erk)
nodes.add(Jnk)
nodes.add(Mek)
nodes.add(P38)
nodes.add(PIP2)
nodes.add(PIP3)
nodes.add(PKA)
nodes.add(PKC)
nodes.add(Plcg)
nodes.add(Raf)
links = network.getLinks()
links.add(Link(Erk, Akt));
links.add(Link(PKA, Akt));
links.add(Link(Mek, Erk));
links.add(Link(PKA, Erk));
links.add(Link(PKA, Jnk));
links.add(Link(PKC, Jnk));
links.add(Link(PKA, Mek));
links.add(Link(PKC, Mek));
links.add(Link(Raf, Mek));
links.add(Link(PKA, P38));
links.add(Link(PKC, P38));
links.add(Link(PIP3, PIP2));
links.add(Link(Plcg, PIP2));
links.add(Link(Plcg, PIP3));
links.add(Link(PKC, PKA));
links.add(Link(PKA, Raf));
links.add(Link(PKC, Raf));
tableAkt = Akt.newDistribution().getTable()

tableAkt.set(0.6721176592, [ErkLOW, PKALOW, AktLOW])
tableAkt.set(0.3277794919, [ErkLOW, PKALOW, AktAVG])
tableAkt.set(0.0001028489, [ErkLOW, PKALOW, AktHIGH])
tableAkt.set(0.3349505840, [ErkAVG, PKALOW, AktLOW])
tableAkt.set(0.6648697215, [ErkAVG, PKALOW, AktAVG])
tableAkt.set(0.0001796945, [ErkAVG, PKALOW, AktHIGH])
tableAkt.set(7.682262e-05, [ErkHIGH, PKALOW, AktLOW])
tableAkt.set(1.183068e-01, [ErkHIGH, PKALOW, AktAVG])
tableAkt.set(8.816163e-01, [ErkHIGH, PKALOW, AktHIGH])
tableAkt.set(0.62038586, [ErkLOW, PKAAVG, AktLOW])
tableAkt.set(0.37950262, [ErkLOW, PKAAVG, AktAVG])
tableAkt.set(0.00011152, [ErkLOW, PKAAVG, AktHIGH])
tableAkt.set(0.8214081840, [ErkAVG, PKAAVG, AktLOW])
tableAkt.set(0.1782019687, [ErkAVG, PKAAVG, AktAVG])
tableAkt.set(0.0003898473, [ErkAVG, PKAAVG, AktHIGH])
tableAkt.set(0.177105936, [ErkHIGH, PKAAVG, AktLOW])
tableAkt.set(0.813732581, [ErkHIGH, PKAAVG, AktAVG])
tableAkt.set(0.009161483, [ErkHIGH, PKAAVG, AktHIGH])
tableAkt.set(0.9750859107, [ErkLOW, PKAHIGH, AktLOW])
tableAkt.set(0.0240549828, [ErkLOW, PKAHIGH, AktAVG])
tableAkt.set(0.0008591065, [ErkLOW, PKAHIGH, AktHIGH])
tableAkt.set(9.483619e-01, [ErkAVG, PKAHIGH, AktLOW])
tableAkt.set(5.154733e-02, [ErkAVG, PKAHIGH, AktAVG])
tableAkt.set(9.075234e-05, [ErkAVG, PKAHIGH, AktHIGH])
tableAkt.set(0.1703412073, [ErkHIGH, PKAHIGH, AktLOW])
tableAkt.set(0.8293963255, [ErkHIGH, PKAHIGH, AktAVG])
tableAkt.set(0.0002624672, [ErkHIGH, PKAHIGH, AktHIGH])
Akt.setDistribution(tableAkt)
tableErk = Erk.newDistribution().getTable()

tableErk.set(0.85051343, [MekLOW, PKALOW, ErkLOW])
tableErk.set(0.13872433, [MekLOW, PKALOW, ErkAVG])
tableErk.set(0.01076224, [MekLOW, PKALOW, ErkHIGH])
tableErk.set(0.3870326, [MekAVG, PKALOW, ErkLOW])
tableErk.set(0.4836913, [MekAVG, PKALOW, ErkAVG])
tableErk.set(0.1292761, [MekAVG, PKALOW, ErkHIGH])
tableErk.set(0.008682883, [MekHIGH, PKALOW, ErkLOW])
tableErk.set(0.187958884, [MekHIGH, PKALOW, ErkAVG])
tableErk.set(0.803358233, [MekHIGH, PKALOW, ErkHIGH])
tableErk.set(0.1177122, [MekLOW, PKAAVG, ErkLOW])
tableErk.set(0.6919357, [MekLOW, PKAAVG, ErkAVG])
tableErk.set(0.1903521, [MekLOW, PKAAVG, ErkHIGH])
tableErk.set(0.04895789, [MekAVG, PKAAVG, ErkLOW])
tableErk.set(0.72823961, [MekAVG, PKAAVG, ErkAVG])
tableErk.set(0.22280250, [MekAVG, PKAAVG, ErkHIGH])
tableErk.set(0.001153403, [MekHIGH, PKAAVG, ErkLOW])
tableErk.set(0.748558247, [MekHIGH, PKAAVG, ErkAVG])
tableErk.set(0.250288351, [MekHIGH, PKAAVG, ErkHIGH])
tableErk.set(0.07405991, [MekLOW, PKAHIGH, ErkLOW])
tableErk.set(0.70044614, [MekLOW, PKAHIGH, ErkAVG])
tableErk.set(0.22549395, [MekLOW, PKAHIGH, ErkHIGH])
tableErk.set(0.003663004, [MekAVG, PKAHIGH, ErkLOW])
tableErk.set(0.102564103, [MekAVG, PKAHIGH, ErkAVG])
tableErk.set(0.893772894, [MekAVG, PKAHIGH, ErkHIGH])
tableErk.set(0.03333333, [MekHIGH, PKAHIGH, ErkLOW])
tableErk.set(0.03333333, [MekHIGH, PKAHIGH, ErkAVG])
tableErk.set(0.93333333, [MekHIGH, PKAHIGH, ErkHIGH])
Erk.setDistribution(tableErk)
tableJnk = Jnk.newDistribution().getTable()

tableJnk.set(0.2899262, [PKALOW, PKCLOW, JnkLOW])
tableJnk.set(0.2457641, [PKALOW, PKCLOW, JnkAVG])
tableJnk.set(0.4643097, [PKALOW, PKCLOW, JnkHIGH])
tableJnk.set(5.766701e-01, [PKAAVG, PKCLOW, JnkLOW])
tableJnk.set(4.232872e-01, [PKAAVG, PKCLOW, JnkAVG])
tableJnk.set(4.271314e-05, [PKAAVG, PKCLOW, JnkHIGH])
tableJnk.set(9.961240e-01, [PKAHIGH, PKCLOW, JnkLOW])
tableJnk.set(3.806755e-03, [PKAHIGH, PKCLOW, JnkAVG])
tableJnk.set(6.921373e-05, [PKAHIGH, PKCLOW, JnkHIGH])
tableJnk.set(0.5794436587, [PKALOW, PKCAVG, JnkLOW])
tableJnk.set(0.4203206035, [PKALOW, PKCAVG, JnkAVG])
tableJnk.set(0.0002357379, [PKALOW, PKCAVG, JnkHIGH])
tableJnk.set(6.129037e-01, [PKAAVG, PKCAVG, JnkLOW])
tableJnk.set(3.870808e-01, [PKAAVG, PKCAVG, JnkAVG])
tableJnk.set(1.543138e-05, [PKAAVG, PKCAVG, JnkHIGH])
tableJnk.set(0.8623005877, [PKAHIGH, PKCAVG, JnkLOW])
tableJnk.set(0.1368597817, [PKAHIGH, PKCAVG, JnkAVG])
tableJnk.set(0.0008396306, [PKAHIGH, PKCAVG, JnkHIGH])
tableJnk.set(0.00456621, [PKALOW, PKCHIGH, JnkLOW])
tableJnk.set(0.99086758, [PKALOW, PKCHIGH, JnkAVG])
tableJnk.set(0.00456621, [PKALOW, PKCHIGH, JnkHIGH])
tableJnk.set(0.04468980, [PKAAVG, PKCHIGH, JnkLOW])
tableJnk.set(0.93495569, [PKAAVG, PKCHIGH, JnkAVG])
tableJnk.set(0.02035451, [PKAAVG, PKCHIGH, JnkHIGH])
tableJnk.set(0.155367232, [PKAHIGH, PKCHIGH, JnkLOW])
tableJnk.set(0.841807910, [PKAHIGH, PKCHIGH, JnkAVG])
tableJnk.set(0.002824859, [PKAHIGH, PKCHIGH, JnkHIGH])
Jnk.setDistribution(tableJnk)
tableMek = Mek.newDistribution().getTable()

tableMek.set(0.7451772095, [PKALOW, PKCLOW, RafLOW, MekLOW])
tableMek.set(0.2545984747, [PKALOW, PKCLOW, RafLOW, MekAVG])
tableMek.set(0.0002243158, [PKALOW, PKCLOW, RafLOW, MekHIGH])
tableMek.set(7.576915e-01, [PKAAVG, PKCLOW, RafLOW, MekLOW])
tableMek.set(2.422767e-01, [PKAAVG, PKCLOW, RafLOW, MekAVG])
tableMek.set(3.181572e-05, [PKAAVG, PKCLOW, RafLOW, MekHIGH])
tableMek.set(9.977281e-01, [PKAHIGH, PKCLOW, RafLOW, MekLOW])
tableMek.set(2.244485e-03, [PKAHIGH, PKCLOW, RafLOW, MekAVG])
tableMek.set(2.737176e-05, [PKAHIGH, PKCLOW, RafLOW, MekHIGH])
tableMek.set(0.7066581578, [PKALOW, PKCAVG, RafLOW, MekLOW])
tableMek.set(0.2931291215, [PKALOW, PKCAVG, RafLOW, MekAVG])
tableMek.set(0.0002127207, [PKALOW, PKCAVG, RafLOW, MekHIGH])
tableMek.set(7.148153e-01, [PKAAVG, PKCAVG, RafLOW, MekLOW])
tableMek.set(2.851753e-01, [PKAAVG, PKCAVG, RafLOW, MekAVG])
tableMek.set(9.338376e-06, [PKAAVG, PKCAVG, RafLOW, MekHIGH])
tableMek.set(0.9689835575, [PKAHIGH, PKCAVG, RafLOW, MekLOW])
tableMek.set(0.0306427504, [PKAHIGH, PKCAVG, RafLOW, MekAVG])
tableMek.set(0.0003736921, [PKAHIGH, PKCAVG, RafLOW, MekHIGH])
tableMek.set(0.854385965, [PKALOW, PKCHIGH, RafLOW, MekLOW])
tableMek.set(0.143859649, [PKALOW, PKCHIGH, RafLOW, MekAVG])
tableMek.set(0.001754386, [PKALOW, PKCHIGH, RafLOW, MekHIGH])
tableMek.set(8.256463e-01, [PKAAVG, PKCHIGH, RafLOW, MekLOW])
tableMek.set(1.743254e-01, [PKAAVG, PKCHIGH, RafLOW, MekAVG])
tableMek.set(2.831337e-05, [PKAAVG, PKCHIGH, RafLOW, MekHIGH])
tableMek.set(0.725950783, [PKAHIGH, PKCHIGH, RafLOW, MekLOW])
tableMek.set(0.272930649, [PKAHIGH, PKCHIGH, RafLOW, MekAVG])
tableMek.set(0.001118568, [PKAHIGH, PKCHIGH, RafLOW, MekHIGH])
tableMek.set(0.3846008, [PKALOW, PKCLOW, RafAVG, MekLOW])
tableMek.set(0.1231368, [PKALOW, PKCLOW, RafAVG, MekAVG])
tableMek.set(0.4922624, [PKALOW, PKCLOW, RafAVG, MekHIGH])
tableMek.set(0.343172087, [PKAAVG, PKCLOW, RafAVG, MekLOW])
tableMek.set(0.649403298, [PKAAVG, PKCLOW, RafAVG, MekAVG])
tableMek.set(0.007424615, [PKAAVG, PKCLOW, RafAVG, MekHIGH])
tableMek.set(0.9996370895, [PKAHIGH, PKCLOW, RafAVG, MekLOW])
tableMek.set(0.0001814553, [PKAHIGH, PKCLOW, RafAVG, MekAVG])
tableMek.set(0.0001814553, [PKAHIGH, PKCLOW, RafAVG, MekHIGH])
tableMek.set(0.2692763938, [PKALOW, PKCAVG, RafAVG, MekLOW])
tableMek.set(0.7304863582, [PKALOW, PKCAVG, RafAVG, MekAVG])
tableMek.set(0.0002372479, [PKALOW, PKCAVG, RafAVG, MekHIGH])
tableMek.set(0.27465766, [PKAAVG, PKCAVG, RafAVG, MekLOW])
tableMek.set(0.72002723, [PKAAVG, PKCAVG, RafAVG, MekAVG])
tableMek.set(0.00531511, [PKAAVG, PKCAVG, RafAVG, MekHIGH])
tableMek.set(0.854385965, [PKAHIGH, PKCAVG, RafAVG, MekLOW])
tableMek.set(0.143859649, [PKAHIGH, PKCAVG, RafAVG, MekAVG])
tableMek.set(0.001754386, [PKAHIGH, PKCAVG, RafAVG, MekHIGH])
tableMek.set(0.01190476, [PKALOW, PKCHIGH, RafAVG, MekLOW])
tableMek.set(0.97619048, [PKALOW, PKCHIGH, RafAVG, MekAVG])
tableMek.set(0.01190476, [PKALOW, PKCHIGH, RafAVG, MekHIGH])
tableMek.set(0.1054112554, [PKAAVG, PKCHIGH, RafAVG, MekLOW])
tableMek.set(0.8943722944, [PKAAVG, PKCHIGH, RafAVG, MekAVG])
tableMek.set(0.0002164502, [PKAAVG, PKCHIGH, RafAVG, MekHIGH])
tableMek.set(0.006060606, [PKAHIGH, PKCHIGH, RafAVG, MekLOW])
tableMek.set(0.987878788, [PKAHIGH, PKCHIGH, RafAVG, MekAVG])
tableMek.set(0.006060606, [PKAHIGH, PKCHIGH, RafAVG, MekHIGH])
tableMek.set(0.262181426, [PKALOW, PKCLOW, RafHIGH, MekLOW])
tableMek.set(0.001450275, [PKALOW, PKCLOW, RafHIGH, MekAVG])
tableMek.set(0.736368299, [PKALOW, PKCLOW, RafHIGH, MekHIGH])
tableMek.set(0.8652899, [PKAAVG, PKCLOW, RafHIGH, MekLOW])
tableMek.set(0.1010029, [PKAAVG, PKCLOW, RafHIGH, MekAVG])
tableMek.set(0.0337072, [PKAAVG, PKCLOW, RafHIGH, MekHIGH])
tableMek.set(0.9361046959, [PKAHIGH, PKCLOW, RafHIGH, MekLOW])
tableMek.set(0.0007698229, [PKAHIGH, PKCLOW, RafHIGH, MekAVG])
tableMek.set(0.0631254811, [PKAHIGH, PKCLOW, RafHIGH, MekHIGH])
tableMek.set(0.85065617, [PKALOW, PKCAVG, RafHIGH, MekLOW])
tableMek.set(0.10656168, [PKALOW, PKCAVG, RafHIGH, MekAVG])
tableMek.set(0.04278215, [PKALOW, PKCAVG, RafHIGH, MekHIGH])
tableMek.set(0.2814957, [PKAAVG, PKCAVG, RafHIGH, MekLOW])
tableMek.set(0.5851161, [PKAAVG, PKCAVG, RafHIGH, MekAVG])
tableMek.set(0.1333882, [PKAAVG, PKCAVG, RafHIGH, MekHIGH])
tableMek.set(0.498470948, [PKAHIGH, PKCAVG, RafHIGH, MekLOW])
tableMek.set(0.498470948, [PKAHIGH, PKCAVG, RafHIGH, MekAVG])
tableMek.set(0.003058104, [PKAHIGH, PKCAVG, RafHIGH, MekHIGH])
tableMek.set(0.3333333, [PKALOW, PKCHIGH, RafHIGH, MekLOW])
tableMek.set(0.3333333, [PKALOW, PKCHIGH, RafHIGH, MekAVG])
tableMek.set(0.3333333, [PKALOW, PKCHIGH, RafHIGH, MekHIGH])
tableMek.set(0.3333333, [PKAAVG, PKCHIGH, RafHIGH, MekLOW])
tableMek.set(0.3333333, [PKAAVG, PKCHIGH, RafHIGH, MekAVG])
tableMek.set(0.3333333, [PKAAVG, PKCHIGH, RafHIGH, MekHIGH])
tableMek.set(0.3333333, [PKAHIGH, PKCHIGH, RafHIGH, MekLOW])
tableMek.set(0.3333333, [PKAHIGH, PKCHIGH, RafHIGH, MekAVG])
tableMek.set(0.3333333, [PKAHIGH, PKCHIGH, RafHIGH, MekHIGH])
Mek.setDistribution(tableMek)
tableP38 = P38.newDistribution().getTable()

tableP38.set(0.30691159, [PKALOW, PKCLOW, P38LOW])
tableP38.set(0.06458648, [PKALOW, PKCLOW, P38AVG])
tableP38.set(0.62850193, [PKALOW, PKCLOW, P38HIGH])
tableP38.set(0.919186742, [PKAAVG, PKCLOW, P38LOW])
tableP38.set(0.078464036, [PKAAVG, PKCLOW, P38AVG])
tableP38.set(0.002349223, [PKAAVG, PKCLOW, P38HIGH])
tableP38.set(0.80737818, [PKAHIGH, PKCLOW, P38LOW])
tableP38.set(0.09163898, [PKAHIGH, PKCLOW, P38AVG])
tableP38.set(0.10098283, [PKAHIGH, PKCLOW, P38HIGH])
tableP38.set(0.6558227251, [PKALOW, PKCAVG, P38LOW])
tableP38.set(0.3439415370, [PKALOW, PKCAVG, P38AVG])
tableP38.set(0.0002357379, [PKALOW, PKCAVG, P38HIGH])
tableP38.set(8.149777e-01, [PKAAVG, PKCAVG, P38LOW])
tableP38.set(1.850069e-01, [PKAAVG, PKCAVG, P38AVG])
tableP38.set(1.543138e-05, [PKAAVG, PKCAVG, P38HIGH])
tableP38.set(0.3862301, [PKAHIGH, PKCAVG, P38LOW])
tableP38.set(0.1595298, [PKAHIGH, PKCAVG, P38AVG])
tableP38.set(0.4542401, [PKAHIGH, PKCAVG, P38HIGH])
tableP38.set(0.86757991, [PKALOW, PKCHIGH, P38LOW])
tableP38.set(0.12785388, [PKALOW, PKCHIGH, P38AVG])
tableP38.set(0.00456621, [PKALOW, PKCHIGH, P38HIGH])
tableP38.set(0.80313955, [PKAAVG, PKCHIGH, P38LOW])
tableP38.set(0.19272946, [PKAAVG, PKCHIGH, P38AVG])
tableP38.set(0.00413099, [PKAAVG, PKCHIGH, P38HIGH])
tableP38.set(0.765536723, [PKAHIGH, PKCHIGH, P38LOW])
tableP38.set(0.231638418, [PKAHIGH, PKCHIGH, P38AVG])
tableP38.set(0.002824859, [PKAHIGH, PKCHIGH, P38HIGH])
P38.setDistribution(tableP38)
tablePIP2 = PIP2.newDistribution().getTable()

tablePIP2.set(9.967915e-01, [PIP3LOW, PlcgLOW, PIP2LOW])
tablePIP2.set(3.169817e-03, [PIP3LOW, PlcgLOW, PIP2AVG])
tablePIP2.set(3.865631e-05, [PIP3LOW, PlcgLOW, PIP2HIGH])
tablePIP2.set(9.867112e-01, [PIP3AVG, PlcgLOW, PIP2LOW])
tablePIP2.set(1.326991e-02, [PIP3AVG, PlcgLOW, PIP2AVG])
tablePIP2.set(1.887612e-05, [PIP3AVG, PlcgLOW, PIP2HIGH])
tablePIP2.set(0.872401162, [PIP3HIGH, PlcgLOW, PIP2LOW])
tablePIP2.set(0.120070734, [PIP3HIGH, PlcgLOW, PIP2AVG])
tablePIP2.set(0.007528104, [PIP3HIGH, PlcgLOW, PIP2HIGH])
tablePIP2.set(0.997890295, [PIP3LOW, PlcgAVG, PIP2LOW])
tablePIP2.set(0.001054852, [PIP3LOW, PlcgAVG, PIP2AVG])
tablePIP2.set(0.001054852, [PIP3LOW, PlcgAVG, PIP2HIGH])
tablePIP2.set(0.9571651090, [PIP3AVG, PlcgAVG, PIP2LOW])
tablePIP2.set(0.0424454829, [PIP3AVG, PlcgAVG, PIP2AVG])
tablePIP2.set(0.0003894081, [PIP3AVG, PlcgAVG, PIP2HIGH])
tablePIP2.set(0.52180956, [PIP3HIGH, PlcgAVG, PIP2LOW])
tablePIP2.set(0.46245517, [PIP3HIGH, PlcgAVG, PIP2AVG])
tablePIP2.set(0.01573528, [PIP3HIGH, PlcgAVG, PIP2HIGH])
tablePIP2.set(0.2218092, [PIP3LOW, PlcgHIGH, PIP2LOW])
tablePIP2.set(0.4936493, [PIP3LOW, PlcgHIGH, PIP2AVG])
tablePIP2.set(0.2845415, [PIP3LOW, PlcgHIGH, PIP2HIGH])
tablePIP2.set(0.07672787, [PIP3AVG, PlcgHIGH, PIP2LOW])
tablePIP2.set(0.39110315, [PIP3AVG, PlcgHIGH, PIP2AVG])
tablePIP2.set(0.53216898, [PIP3AVG, PlcgHIGH, PIP2HIGH])
tablePIP2.set(0.02641691, [PIP3HIGH, PlcgHIGH, PIP2LOW])
tablePIP2.set(0.05235351, [PIP3HIGH, PlcgHIGH, PIP2AVG])
tablePIP2.set(0.92122959, [PIP3HIGH, PlcgHIGH, PIP2HIGH])
PIP2.setDistribution(tablePIP2)
tablePIP3 = PIP3.newDistribution().getTable()

tablePIP3.set(0.2184310, [PlcgLOW, PIP3LOW])
tablePIP3.set(0.4473238, [PlcgLOW, PIP3AVG])
tablePIP3.set(0.3342453, [PlcgLOW, PIP3HIGH])
tablePIP3.set(0.07796694, [PlcgAVG, PIP3LOW])
tablePIP3.set(0.21120158, [PlcgAVG, PIP3AVG])
tablePIP3.set(0.71083148, [PlcgAVG, PIP3HIGH])
tablePIP3.set(0.4237055, [PlcgHIGH, PIP3LOW])
tablePIP3.set(0.4396535, [PlcgHIGH, PIP3AVG])
tablePIP3.set(0.1366411, [PlcgHIGH, PIP3HIGH])
PIP3.setDistribution(tablePIP3)
tablePKA = PKA.newDistribution().getTable()

tablePKA.set(0.3864255, [PKCLOW, PKALOW])
tablePKA.set(0.3794243, [PKCLOW, PKAAVG])
tablePKA.set(0.2341501, [PKCLOW, PKAHIGH])
tablePKA.set(0.06039638, [PKCAVG, PKALOW])
tablePKA.set(0.92264651, [PKCAVG, PKAAVG])
tablePKA.set(0.01695712, [PKCAVG, PKAHIGH])
tablePKA.set(0.01577014, [PKCHIGH, PKALOW])
tablePKA.set(0.95873839, [PKCHIGH, PKAAVG])
tablePKA.set(0.02549147, [PKCHIGH, PKAHIGH])
PKA.setDistribution(tablePKA)
tablePKC = PKC.newDistribution().getTable()

tablePKC.set(0.42313152, [PKCLOW])
tablePKC.set(0.48163920, [PKCAVG])
tablePKC.set(0.09522928, [PKCHIGH])
PKC.setDistribution(tablePKC)
tablePlcg = Plcg.newDistribution().getTable()

tablePlcg.set(0.81213356, [PlcgLOW])
tablePlcg.set(0.08337962, [PlcgAVG])
tablePlcg.set(0.10448682, [PlcgHIGH])
Plcg.setDistribution(tablePlcg)
tableRaf = Raf.newDistribution().getTable()

tableRaf.set(0.06232176, [PKALOW, PKCLOW, RafLOW])
tableRaf.set(0.14724878, [PKALOW, PKCLOW, RafAVG])
tableRaf.set(0.79042946, [PKALOW, PKCLOW, RafHIGH])
tableRaf.set(0.4475056, [PKAAVG, PKCLOW, RafLOW])
tableRaf.set(0.3125747, [PKAAVG, PKCLOW, RafAVG])
tableRaf.set(0.2399197, [PKAAVG, PKCLOW, RafHIGH])
tableRaf.set(0.84288483, [PKAHIGH, PKCLOW, RafLOW])
tableRaf.set(0.12714563, [PKAHIGH, PKCLOW, RafAVG])
tableRaf.set(0.02996955, [PKAHIGH, PKCLOW, RafHIGH])
tableRaf.set(0.3694012, [PKALOW, PKCAVG, RafLOW])
tableRaf.set(0.3312117, [PKALOW, PKCAVG, RafAVG])
tableRaf.set(0.2993871, [PKALOW, PKCAVG, RafHIGH])
tableRaf.set(0.55082326, [PKAAVG, PKCAVG, RafLOW])
tableRaf.set(0.39291391, [PKAAVG, PKCAVG, RafAVG])
tableRaf.set(0.05626283, [PKAAVG, PKCAVG, RafHIGH])
tableRaf.set(0.74895046, [PKAHIGH, PKCAVG, RafLOW])
tableRaf.set(0.15952981, [PKAHIGH, PKCAVG, RafAVG])
tableRaf.set(0.09151973, [PKAHIGH, PKCAVG, RafHIGH])
tableRaf.set(0.86757991, [PKALOW, PKCHIGH, RafLOW])
tableRaf.set(0.12785388, [PKALOW, PKCHIGH, RafAVG])
tableRaf.set(0.00456621, [PKALOW, PKCHIGH, RafHIGH])
tableRaf.set(8.842572e-01, [PKAAVG, PKCHIGH, RafLOW])
tableRaf.set(1.156677e-01, [PKAAVG, PKCHIGH, RafAVG])
tableRaf.set(7.510891e-05, [PKAAVG, PKCHIGH, RafHIGH])
tableRaf.set(0.841807910, [PKAHIGH, PKCHIGH, RafLOW])
tableRaf.set(0.155367232, [PKAHIGH, PKCHIGH, RafAVG])
tableRaf.set(0.002824859, [PKAHIGH, PKCHIGH, RafHIGH])
Raf.setDistribution(tableRaf)

evidence = DefaultEvidence(network)
evidence_str = 'default'
# TODO set any evidence here if you need to...

sensitivity = SensitivityToParameters(network, RelevanceTreeInferenceFactory())
parameters_to_test = []
parameters_to_test.append(ParameterReference(Raf, [PKAAVG,PKCAVG,RafLOW]))

times = []
print("node	states	minimum	maximum	 time")

for parameter in parameters_to_test:

    start = time.time()

    oneWay = sensitivity.oneWay(
        evidence,
        RafLOW,
        parameter)

    try:
    
        print('')
        output = ParameterTuning.oneWaySimple(
                        oneWay,
                        Interval(
                            java.lang.Double(0.7),
                            java.lang.Double(1),
                            IntervalEndPoint.CLOSED,
                            IntervalEndPoint.CLOSED))
        end = time.time()


        param_states_text = '[' + ','.join([str(s.getVariable().getName()) + ' = ' + str(s.getName()) for s in parameter.getStates()]) + ']'
        print('{}	{}	{}	{}	{}'.format(
            parameter.getNode().getName(),
            param_states_text,
            output.getInterval().getMinimum(),
            output.getInterval().getMaximum(),
            end-start
        ))

    except ConstraintNotSatisfiedException:
        end = time.time()
        print(f"Ignoring here as solution not found for this parameter. (time: {end-start})")
    except ConstraintSatisfiedException:
        end = time.time()
        print(f"Ignoring here as constraint is already satisfied. (time: {end-start})")
    times.append(end-start)
print('')
print('Sum of times: ' + str(sum(times)) + 's')
