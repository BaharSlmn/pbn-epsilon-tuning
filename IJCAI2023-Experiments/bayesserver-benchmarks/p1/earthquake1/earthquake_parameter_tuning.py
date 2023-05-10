
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
network = Network('earthquake')

#  add the nodes/variables

BurglaryTrue = State('True')
BurglaryFalse = State('False')
Burglary = Node('Burglary', [BurglaryTrue, BurglaryFalse])

EarthquakeTrue = State('True')
EarthquakeFalse = State('False')
Earthquake = Node('Earthquake', [EarthquakeTrue, EarthquakeFalse])

AlarmTrue = State('True')
AlarmFalse = State('False')
Alarm = Node('Alarm', [AlarmTrue, AlarmFalse])

JohnCallsTrue = State('True')
JohnCallsFalse = State('False')
JohnCalls = Node('JohnCalls', [JohnCallsTrue, JohnCallsFalse])

MaryCallsTrue = State('True')
MaryCallsFalse = State('False')
MaryCalls = Node('MaryCalls', [MaryCallsTrue, MaryCallsFalse])

nodes = network.getNodes()
nodes.add(Burglary)
nodes.add(Earthquake)
nodes.add(Alarm)
nodes.add(JohnCalls)
nodes.add(MaryCalls)
links = network.getLinks()
links.add(Link(Burglary, Alarm));
links.add(Link(Earthquake, Alarm));
links.add(Link(Alarm, JohnCalls));
links.add(Link(Alarm, MaryCalls));
tableBurglary = Burglary.newDistribution().getTable()

tableBurglary.set(0.01, [BurglaryTrue])
tableBurglary.set(0.99, [BurglaryFalse])
Burglary.setDistribution(tableBurglary)
tableEarthquake = Earthquake.newDistribution().getTable()

tableEarthquake.set(0.02, [EarthquakeTrue])
tableEarthquake.set(0.98, [EarthquakeFalse])
Earthquake.setDistribution(tableEarthquake)
tableAlarm = Alarm.newDistribution().getTable()

tableAlarm.set(0.95, [BurglaryTrue, EarthquakeTrue, AlarmTrue])
tableAlarm.set(0.05, [BurglaryTrue, EarthquakeTrue, AlarmFalse])
tableAlarm.set(0.29, [BurglaryFalse, EarthquakeTrue, AlarmTrue])
tableAlarm.set(0.71, [BurglaryFalse, EarthquakeTrue, AlarmFalse])
tableAlarm.set(0.94, [BurglaryTrue, EarthquakeFalse, AlarmTrue])
tableAlarm.set(0.06, [BurglaryTrue, EarthquakeFalse, AlarmFalse])
tableAlarm.set(0.001, [BurglaryFalse, EarthquakeFalse, AlarmTrue])
tableAlarm.set(0.999, [BurglaryFalse, EarthquakeFalse, AlarmFalse])
Alarm.setDistribution(tableAlarm)
tableJohnCalls = JohnCalls.newDistribution().getTable()

tableJohnCalls.set(0.9, [AlarmTrue, JohnCallsTrue])
tableJohnCalls.set(0.1, [AlarmTrue, JohnCallsFalse])
tableJohnCalls.set(0.05, [AlarmFalse, JohnCallsTrue])
tableJohnCalls.set(0.95, [AlarmFalse, JohnCallsFalse])
JohnCalls.setDistribution(tableJohnCalls)
tableMaryCalls = MaryCalls.newDistribution().getTable()

tableMaryCalls.set(0.7, [AlarmTrue, MaryCallsTrue])
tableMaryCalls.set(0.3, [AlarmTrue, MaryCallsFalse])
tableMaryCalls.set(0.01, [AlarmFalse, MaryCallsTrue])
tableMaryCalls.set(0.99, [AlarmFalse, MaryCallsFalse])
MaryCalls.setDistribution(tableMaryCalls)

evidence = DefaultEvidence(network)
evidence_str = 'default'
# TODO set any evidence here if you need to...

sensitivity = SensitivityToParameters(network, RelevanceTreeInferenceFactory())
parameters_to_test = []
parameters_to_test.append(ParameterReference(Alarm, [BurglaryFalse,EarthquakeFalse,AlarmTrue]))

times = []
print("node	states	minimum	maximum	 time")

for parameter in parameters_to_test:
    start = time.time()
    oneWay = sensitivity.oneWay(
        evidence,
        MaryCallsTrue,
        parameter)

    try:
    
        print('')
        output = ParameterTuning.oneWaySimple(
                        oneWay,
                        Interval(
                            java.lang.Double(0.2),
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
