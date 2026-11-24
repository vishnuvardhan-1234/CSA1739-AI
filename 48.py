from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([("Rain", "Wet")])

cpd1 = TabularCPD("Rain", 2, [[0.7], [0.3]])
cpd2 = TabularCPD("Wet", 2,
                  [[0.9, 0.2], [0.1, 0.8]],
                  evidence=["Rain"],
                  evidence_card=[2])

model.add_cpds(cpd1, cpd2)

infer = VariableElimination(model)
print(infer.query(["Wet"], evidence={"Rain": 1}))
