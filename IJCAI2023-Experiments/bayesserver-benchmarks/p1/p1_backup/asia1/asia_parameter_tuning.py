
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
network = Network('asia')

#  add the nodes/variables

asiayes = State('yes')
asiano = State('no')
asia = Node('asia', [asiayes, asiano])

tubyes = State('yes')
tubno = State('no')
tub = Node('tub', [tubyes, tubno])

smokeyes = State('yes')
smokeno = State('no')
smoke = Node('smoke', [smokeyes, smokeno])

lungyes = State('yes')
lungno = State('no')
lung = Node('lung', [lungyes, lungno])

broncyes = State('yes')
broncno = State('no')
bronc = Node('bronc', [broncyes, broncno])

eitheryes = State('yes')
eitherno = State('no')
either = Node('either', [eitheryes, eitherno])

xrayyes = State('yes')
xrayno = State('no')
xray = Node('xray', [xrayyes, xrayno])

dyspyes = State('yes')
dyspno = State('no')
dysp = Node('dysp', [dyspyes, dyspno])

nodes = network.getNodes()
nodes.add(asia)
nodes.add(tub)
nodes.add(smoke)
nodes.add(lung)
nodes.add(bronc)
nodes.add(either)
nodes.add(xray)
nodes.add(dysp)
links = network.getLinks()
links.add(Link(asia, tub));
links.add(Link(smoke, lung));
links.add(Link(smoke, bronc));
links.add(Link(lung, either));
links.add(Link(tub, either));
links.add(Link(either, xray));
links.add(Link(bronc, dysp));
links.add(Link(either, dysp));
tableasia = asia.newDistribution().getTable()

tableasia.set(0.01, [asiayes])
tableasia.set(0.99, [asiano])
asia.setDistribution(tableasia)
tabletub = tub.newDistribution().getTable()

tabletub.set(0.05, [asiayes, tubyes])
tabletub.set(0.95, [asiayes, tubno])
tabletub.set(0.01, [asiano, tubyes])
tabletub.set(0.99, [asiano, tubno])
tub.setDistribution(tabletub)
tablesmoke = smoke.newDistribution().getTable()

tablesmoke.set(0.5, [smokeyes])
tablesmoke.set(0.5, [smokeno])
smoke.setDistribution(tablesmoke)
tablelung = lung.newDistribution().getTable()

tablelung.set(0.1, [smokeyes, lungyes])
tablelung.set(0.9, [smokeyes, lungno])
tablelung.set(0.01, [smokeno, lungyes])
tablelung.set(0.99, [smokeno, lungno])
lung.setDistribution(tablelung)
tablebronc = bronc.newDistribution().getTable()

tablebronc.set(0.6, [smokeyes, broncyes])
tablebronc.set(0.4, [smokeyes, broncno])
tablebronc.set(0.3, [smokeno, broncyes])
tablebronc.set(0.7, [smokeno, broncno])
bronc.setDistribution(tablebronc)
tableeither = either.newDistribution().getTable()

tableeither.set(1.0, [lungyes, tubyes, eitheryes])
tableeither.set(0.0, [lungyes, tubyes, eitherno])
tableeither.set(1.0, [lungno, tubyes, eitheryes])
tableeither.set(0.0, [lungno, tubyes, eitherno])
tableeither.set(1.0, [lungyes, tubno, eitheryes])
tableeither.set(0.0, [lungyes, tubno, eitherno])
tableeither.set(0.0, [lungno, tubno, eitheryes])
tableeither.set(1.0, [lungno, tubno, eitherno])
either.setDistribution(tableeither)
tablexray = xray.newDistribution().getTable()

tablexray.set(0.98, [eitheryes, xrayyes])
tablexray.set(0.02, [eitheryes, xrayno])
tablexray.set(0.05, [eitherno, xrayyes])
tablexray.set(0.95, [eitherno, xrayno])
xray.setDistribution(tablexray)
tabledysp = dysp.newDistribution().getTable()

tabledysp.set(0.9, [broncyes, eitheryes, dyspyes])
tabledysp.set(0.1, [broncyes, eitheryes, dyspno])
tabledysp.set(0.7, [broncno, eitheryes, dyspyes])
tabledysp.set(0.3, [broncno, eitheryes, dyspno])
tabledysp.set(0.8, [broncyes, eitherno, dyspyes])
tabledysp.set(0.2, [broncyes, eitherno, dyspno])
tabledysp.set(0.1, [broncno, eitherno, dyspyes])
tabledysp.set(0.9, [broncno, eitherno, dyspno])
dysp.setDistribution(tabledysp)

evidence = DefaultEvidence(network)
evidence_str = 'default'
# TODO set any evidence here if you need to...

sensitivity = SensitivityToParameters(network, RelevanceTreeInferenceFactory())
parameters_to_test = []
parameters_to_test.append(ParameterReference(lung, [smokeno,lungno]))

for parameter in parameters_to_test:
    start = time.time()

    oneWay = sensitivity.oneWay(
        evidence,
        xrayyes,
        parameter)

    try:

        output = ParameterTuning.oneWaySimple(
                        oneWay,
                        Interval(
                            java.lang.Double(0.2),
                            java.lang.Double(0.25),
                            IntervalEndPoint.CLOSED,
                            IntervalEndPoint.CLOSED))
    start = time.time()


        param_states_text = '[' + ','.join([str(s.getVariable().getName()) + ' = ' + str(s.getName()) for s in parameter.getStates()]) + ']'
        print('{}       {}      {}      {}      {}'.format(
            parameter.getNode().getName(),
            param_states_text,
            output.getInterval().getMinimum(),
            output.getInterval().getMaximum(),
            end-start
        ))

    except ConstraintNotSatisfiedException:
    start = time.time()
    print(f"Ignoring here as constraint is already satisfied. (time: {end-start})")
    times.append(end-start)
    print('')
    print('Sum of times: ' + str(sum(times)) + 's')
