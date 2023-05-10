
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
network = Network('cancer')

#  add the nodes/variables

Pollutionlow = State('low')
Pollutionhigh = State('high')
Pollution = Node('Pollution', [Pollutionlow, Pollutionhigh])

SmokerTrue = State('True')
SmokerFalse = State('False')
Smoker = Node('Smoker', [SmokerTrue, SmokerFalse])

CancerTrue = State('True')
CancerFalse = State('False')
Cancer = Node('Cancer', [CancerTrue, CancerFalse])

Xraypositive = State('positive')
Xraynegative = State('negative')
Xray = Node('Xray', [Xraypositive, Xraynegative])

DyspnoeaTrue = State('True')
DyspnoeaFalse = State('False')
Dyspnoea = Node('Dyspnoea', [DyspnoeaTrue, DyspnoeaFalse])

nodes = network.getNodes()
nodes.add(Pollution)
nodes.add(Smoker)
nodes.add(Cancer)
nodes.add(Xray)
nodes.add(Dyspnoea)
links = network.getLinks()
links.add(Link(Pollution, Cancer));
links.add(Link(Smoker, Cancer));
links.add(Link(Cancer, Xray));
links.add(Link(Cancer, Dyspnoea));
tablePollution = Pollution.newDistribution().getTable()

tablePollution.set(0.9, [Pollutionlow])
tablePollution.set(0.1, [Pollutionhigh])
Pollution.setDistribution(tablePollution)
tableSmoker = Smoker.newDistribution().getTable()

tableSmoker.set(0.3, [SmokerTrue])
tableSmoker.set(0.7, [SmokerFalse])
Smoker.setDistribution(tableSmoker)
tableCancer = Cancer.newDistribution().getTable()

tableCancer.set(0.03, [Pollutionlow, SmokerTrue, CancerTrue])
tableCancer.set(0.97, [Pollutionlow, SmokerTrue, CancerFalse])
tableCancer.set(0.05, [Pollutionhigh, SmokerTrue, CancerTrue])
tableCancer.set(0.95, [Pollutionhigh, SmokerTrue, CancerFalse])
tableCancer.set(0.001, [Pollutionlow, SmokerFalse, CancerTrue])
tableCancer.set(0.999, [Pollutionlow, SmokerFalse, CancerFalse])
tableCancer.set(0.02, [Pollutionhigh, SmokerFalse, CancerTrue])
tableCancer.set(0.98, [Pollutionhigh, SmokerFalse, CancerFalse])
Cancer.setDistribution(tableCancer)
tableXray = Xray.newDistribution().getTable()

tableXray.set(0.9, [CancerTrue, Xraypositive])
tableXray.set(0.1, [CancerTrue, Xraynegative])
tableXray.set(0.2, [CancerFalse, Xraypositive])
tableXray.set(0.8, [CancerFalse, Xraynegative])
Xray.setDistribution(tableXray)
tableDyspnoea = Dyspnoea.newDistribution().getTable()

tableDyspnoea.set(0.65, [CancerTrue, DyspnoeaTrue])
tableDyspnoea.set(0.35, [CancerTrue, DyspnoeaFalse])
tableDyspnoea.set(0.3, [CancerFalse, DyspnoeaTrue])
tableDyspnoea.set(0.7, [CancerFalse, DyspnoeaFalse])
Dyspnoea.setDistribution(tableDyspnoea)

evidence = DefaultEvidence(network)
evidence_str = 'default'
# TODO set any evidence here if you need to...

sensitivity = SensitivityToParameters(network, RelevanceTreeInferenceFactory())
parameters_to_test = []
parameters_to_test.append(ParameterReference(Cancer, [Pollutionlow,SmokerFalse,CancerTrue]))

times = []
print("node	states	minimum	maximum	 time")

for parameter in parameters_to_test:
    start = time.time()
    oneWay = sensitivity.oneWay(
        evidence,
        DyspnoeaTrue,
        parameter)

    try:
    
        print('')
        output = ParameterTuning.oneWaySimple(
                        oneWay,
                        Interval(
                            java.lang.Double(0.4),
                            java.lang.Double(1.0),
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
