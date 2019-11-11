"""

Tries a strategy and show the results
============================================
Results of our strategy

"""
import matplotlib.pyplot as plt

from strat_2048_rvk.strategy import strategy
from ensae_teaching_cs.td_1a.cp2048 import evaluate_strategy
##############################
# The strategy :func:`strategy
# <strat_2048_rvk.strategy.strategy>`
#

gen1 = evaluate_strategy(strategy, 100)
res1 = list(gen1)

#########################################
# Finaly plots the gains obtained by the strategy.

plt.hist(res1)
plt.title('Results')
plt.show()
