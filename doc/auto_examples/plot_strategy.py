"""

Tries a strategy and show the results
============================================
Results of our strategy

"""
import numpy
import matplotlib.pyplot as plt

from strat_2048_rvk.strategy import strategy
from strat_2048_rvk import evaluate_strategy, Game2048

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
