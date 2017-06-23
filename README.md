# Tic-tak-toe using machine learning

linear classifier is used in trainnig
v(b)=w1 + w2*x1+ w2*x2+ w3*x3+ w4*x4

## Features used
1. Number of ones(x1) 'o' rows
2. Number of two(x3)  'o' rows
3. NUmber of ones(x2) 'x' rows
4. number of two(x4)  'x' rows

randomTrainig.py will train the model by creating random moves for both player and then updates its weights.

all the weights train by randomTrainig.py are stored in vales.db(sqlite3 database is used)

by running Python robo.py we can play against Machine learning trained robot
