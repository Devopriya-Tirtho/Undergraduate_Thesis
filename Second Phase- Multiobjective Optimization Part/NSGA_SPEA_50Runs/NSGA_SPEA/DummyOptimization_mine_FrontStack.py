from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.algorithm.multiobjective.spea2 import SPEA2
from jmetal.operator import SBXCrossover, PolynomialMutation
from jmetal.operator.crossover import IntegerSBXCrossover,IntegerSinglePointCrossover,IntegerMultiPointCrossover
from jmetal.operator.mutation import ModifiedSimpleRandomMutation
from jmetal.problem import ZDT1
from jmetal.util.solution import get_non_dominated_solutions, read_solutions, print_function_values_to_file, \
    print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.core.solution import Solution, FloatSolution, BinarySolution, PermutationSolution, IntegerSolution
from jmetal.lab.visualization.plotting import Plot
from jmetal.lab.visualization.interactive import InteractivePlot
from jmetal.util.solution import get_non_dominated_solutions

"""  
Program to  configure and run the NSGA-II algorithm configured with standard settings.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from math import sqrt, pow, sin, pi, cos

from jmetal.core.problem import  IntegerProblem
from jmetal.core.solution import IntegerSolution
"""
.. module:: ZDT
   :platform: Unix, Windows
   :synopsis: ZDT problem family of multi-objective problems.
.. moduleauthor:: Antonio J. Nebro <antonio@lcc.uma.es>
"""
dataset=pd.read_csv('Player_List_With_Keeper.csv')
b=dataset.shape
print(b[0])
columnNumber=b[0]
Index=[]

X=[]
Y=[]
A=[]
B=[]
for i in range(0,columnNumber):
        a=dataset.at[i,'Index']
        b=dataset.at[i,'Batting Performance']
        c=dataset.at[i,'Bowling Performance']
        e=dataset.at[i,'Cost']
        d=dataset.at[i,'Foreign']
        Index.append(a)
        X.append(b)
        Y.append(c)
        A.append(e)
        B.append(d)





class Selection(IntegerProblem):
    """ Problem ZDT1.
    .. note:: Bi-objective unconstrained problem. The default number of variables is 30.
    .. note:: Continuous problem having a convex Pareto front
    """

    def __init__(self, number_of_variables: int=23):
        """ :param number_of_variables: Number of decision variables of the problem.
        """
        super(Selection, self).__init__()
        #Call here dataset
        self.number_of_variables = number_of_variables
        self.number_of_objectives = 3
        self.number_of_constraints = 1

        self.obj_directions = [self.MINIMIZE, self.MINIMIZE,self.MINIMIZE]
        self.obj_labels = ['Batting Performance', 'Bowling Performance', 'Cost']

        self.lower_bound =  [ 0, 0, 0, 0,22,22,22,38,38,38,55,55,55,55,55,93,93,93,93,93,93,93,93]
        self.upper_bound =  [21,21,21,21,37,37,37,54,54,54,92,92,92,92,92,151,151,151,151,151,151,151,151]

        
    def evaluate(self, solution: IntegerSolution) -> IntegerSolution:

        
        x=solution.variables
        
        result_bat=0
        result_ball=0
        result_cost=0
        
        for i in range(23):
            temp=x[i]
            result_bat+=X[temp]
            result_ball+=Y[temp]
            result_cost+=A[temp]

        
        solution.objectives[0] = result_bat*(-1)
        solution.objectives[1] = result_ball*(-1)
        solution.objectives[2] = result_cost*(1)
        
        self.__evaluate_constraints(solution)
        
        return solution




    def __evaluate_constraints(self, solution: IntegerSolution) -> None:
        x=solution.variables
        
        result_foreigner=0
        result_totalcost=0
        for i in range(23):
            temp=x[i]
            
            result_foreigner+=B[temp]
            result_totalcost+=A[temp]
        
        #solution.constraints[0] = 1 - (result_totalcost)/40
        
        solution.constraints[0] = 1 - (result_foreigner)/8
        


    def get_name(self):
        return 'Selection'
    

##################################################
############# Running the NSGAII Algorithm ######################   
##################################################

    
if __name__ == '__main__':
    problem = Selection()
    #problem.reference_front = read_solutions(filename='resources/reference_front/ZDT1.pf')
    
    
    ##Setting Up NSGAII algorithm for evaluation
    ####################################
    max_evaluations = 600000 #499800
    algorithm = NSGAII(
        problem=problem,
        population_size=300,
        offspring_population_size=300,
        mutation=ModifiedSimpleRandomMutation(probability=1 / problem.number_of_variables),
        crossover=IntegerSinglePointCrossover(probability=0.90), #0.90
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
    )
    ##############################################
    
    front1=[]
    
    # #Running the Algorithm
    for i in range(0,50): #30
          print(i)
          algorithm.run()
          solutions = algorithm.get_result()
          front1.append(get_non_dominated_solutions(algorithm.get_result()))
          print_function_values_to_file(get_non_dominated_solutions(algorithm.get_result()), 'FUN.'+ str(i+1) + algorithm.label)
          print_variables_to_file(get_non_dominated_solutions(algorithm.get_result()), 'VAR.'+str(i+1)+ algorithm.label)

    
    #Stacking values of front1 to front and frontNSGAII
    front = []
    frontNSGAII=[]
    for l in front1:
        front.extend(l)
        frontNSGAII.extend(l)

    #Plotting Interactive Graph of True Pareto NSGAII
    TrueFrontNSGAII=get_non_dominated_solutions(frontNSGAII)
    plot_front = InteractivePlot(axis_labels=['Batting Performance', 'Bowling Performance','Cost'])
    plot_front.plot(TrueFrontNSGAII, label='NSGAII',filename='True Pareto Front NSGAII')
    print_function_values_to_file(TrueFrontNSGAII, 'FUN.TruePareto' + algorithm.label)
    print_variables_to_file(TrueFrontNSGAII, 'VAR.TruePareto'+ algorithm.label)
    ########################################
    

    
    
    ##Setting Up SPEA2 algorithm for evaluation
    ########################################
    max_evaluations = 600000 #499800
    algorithm = SPEA2(
        problem=problem,
        population_size=300,
        offspring_population_size=300,
        mutation=ModifiedSimpleRandomMutation(probability=1 / problem.number_of_variables),
        crossover=IntegerSinglePointCrossover(probability=0.90), #0.90
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
    )
    ##############################################
    
    front2=[]
    
    # #Running the Algorithm
    for i in range(0,50): #30
          print(i)
          algorithm.run()
          solutions = algorithm.get_result()
          front2.append(get_non_dominated_solutions(algorithm.get_result()))
          print_function_values_to_file(get_non_dominated_solutions(algorithm.get_result()), 'FUN.'+ str(i+1) + algorithm.label)
          print_variables_to_file(get_non_dominated_solutions(algorithm.get_result()), 'VAR.'+str(i+1)+ algorithm.label)
    #front=(get_non_dominated_solutions(algorithm.get_result()))
    
    #Stacking values of front2 to front and frontSPEA2
    frontSPEA2=[]
    for l in front2:
        front.extend(l)
        frontSPEA2.extend(l)

     #Plotting Interactive Graph of True Pareto SPEA2   
    TrueFrontSPEA2=get_non_dominated_solutions(frontSPEA2)
    plot_front = InteractivePlot(axis_labels=['Batting Performance', 'Bowling Performance','Cost'])
    plot_front.plot(TrueFrontSPEA2, label='SPEA2',filename='True Pareto Front SPEA2')
    print_function_values_to_file(TrueFrontSPEA2, 'FUN.TruePareto' + algorithm.label)
    print_variables_to_file(TrueFrontSPEA2, 'VAR.TruePareto'+ algorithm.label)    
    
     #Plotting Interactive Graph of True Pareto NSGAII+SPEA2   
    TrueFront=get_non_dominated_solutions(front)
    plot_front = InteractivePlot(axis_labels=['Batting Performance', 'Bowling Performance','Cost'])
    plot_front.plot(TrueFront, label='NSGAII_SPEA2',filename='True Pareto Front(NSGAII_SPEA2)')
    print_function_values_to_file(TrueFront, 'FUN.TrueParetoALL')
    print_variables_to_file(TrueFront, 'VAR.TrueParetoALL')     
    
    #Plotting Interactive Graph of All points of NSGAII+SPEA2  
    ##Plotting the result    
    plot_front = InteractivePlot(axis_labels=['Batting Performance', 'Bowling Performance','Cost'])
    plot_front.plot(front, label='NSGAII_SPEA2',filename='NSGAII_SPEA2')



    # Save results to file
    print_function_values_to_file(front, 'FUN.ALL')
    print_variables_to_file(front, 'VAR.ALL')




    print('Algorithm (continuous problem): ' + algorithm.get_name())
    print('Problem: ' + problem.get_name())
    print('Computing time: ' + str(algorithm.total_computing_time))
    ###########################################################

    





# 0-30  top-4
#31-54  middle-6
# 55-92 all -5
# 93-151  bowler-8