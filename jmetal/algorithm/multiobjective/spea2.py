from typing import TypeVar, List
import pandas as pd
from random import randrange, uniform
import time
from typing import TypeVar, List, Generator

from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.config import store
from jmetal.core.operator import Mutation, Crossover
from jmetal.core.problem import Problem
from jmetal.operator import BinaryTournamentSelection
from jmetal.util.comparator import Comparator, MultiComparator
from jmetal.util.density_estimator import KNearestNeighborDensityEstimator
from jmetal.util.evaluator import Evaluator
from jmetal.util.generator import Generator
from jmetal.util.ranking import StrengthRanking
from jmetal.util.replacement import RankingAndDensityEstimatorReplacement, RemovalPolicyType
from jmetal.util.termination_criterion import TerminationCriterion

S = TypeVar('S')
R = TypeVar('R')


dataset=pd.read_csv('Player_List_With_Keeper.csv')
"""
.. module:: SPEA2
   :platform: Unix, Windows
   :synopsis: SPEA2  implementation. Note that we do not follow the structure of the original SPEA2 code. We consider
   SPEA2 as a genetic algorithm with binary tournament selection, with a comparator based on the strength fitness and 
   the KNN distance, and a sequential replacement strategy based in iteratively (sequentially) 
   removing the worst solution of the population + offspring population. The worst solutions is selected again 
   considering the strength fitness and KNN distance. Note that the implementation is exactly the same of NSGA-II, 
   but using the fast nondominated sorting and the crowding distance density estimator, and the replacement follows a 
   one-shot scheme (once the solutions are ordered, the best ones are selected without recomputing the ranking and
   density estimator).

.. moduleauthor:: Antonio J. Nebro <antonio@lcc.uma.es>
"""
def duplicacy(S):
    for i in range(len(S)):
        if(S[i]==True):
            return True
        else:
            continue
        return False

class SPEA2(GeneticAlgorithm[S, R]):

    def __init__(self,
                 problem: Problem,
                 population_size: int,
                 offspring_population_size: int,
                 mutation: Mutation,
                 crossover: Crossover,
                 termination_criterion: TerminationCriterion = store.default_termination_criteria,
                 population_generator: Generator = store.default_generator,
                 population_evaluator: Evaluator = store.default_evaluator,
                 dominance_comparator: Comparator = store.default_comparator):
        """
        :param problem: The problem to solve.
        :param population_size: Size of the population.
        :param mutation: Mutation operator (see :py:mod:`jmetal.operator.mutation`).
        :param crossover: Crossover operator (see :py:mod:`jmetal.operator.crossover`).
        """
        multi_comparator = MultiComparator([StrengthRanking.get_comparator(),
                                            KNearestNeighborDensityEstimator.get_comparator()])
        selection = BinaryTournamentSelection(comparator=multi_comparator)

        super(SPEA2, self).__init__(
            problem=problem,
            population_size=population_size,
            offspring_population_size=offspring_population_size,
            mutation=mutation,
            crossover=crossover,
            selection=selection,
            termination_criterion=termination_criterion,
            population_evaluator=population_evaluator,
            population_generator=population_generator
        )
        self.dominance_comparator = dominance_comparator
        
        
        
        
    ## Code of Repair
    def create_initial_solutions(self) -> List[S]:
        s = [self.population_generator.new(self.problem) for _ in range(self.population_size)]
       # print(s[0])
       # print(s[1])
       # print(s[2])
        ##Code for repair
        for k in range(len(s)) :
            S=pd.Series(s[k].variables).duplicated()
            while(duplicacy(S)):
                S=pd.Series(s[k].variables).duplicated()
                for i in range(len(S)):
                    if(S[i]==True):
                        if(s[k].variables[i]<=21):
                            value=randrange(0, 21)
                            s[k].variables[i]=value
                            s[k].objectives[0]=dataset.at[value,'Batting Performance']
                            s[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            s[k].objectives[2]=dataset.at[value,'Cost']
                        
                        elif(s[k].variables[i]>21 and s[k].variables[i]<=37):
                            value=randrange(22, 37)
                            s[k].variables[i]=value
                            #s[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(s[k].variables[i]>37 and s[k].variables[i]<=54):
                            value=randrange(38, 54)
                            s[k].variables[i]=value
                            #s[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                            s[k].objectives[0]=dataset.at[value,'Batting Performance']
                            s[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            s[k].objectives[2]=dataset.at[value,'Cost']
                            
                        elif(s[k].variables[i]>54 and s[k].variables[i]<=92):
                            value=randrange(55, 92)
                            s[k].variables[i]=value
                            s[k].objectives[0]=dataset.at[value,'Batting Performance']
                            s[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            s[k].objectives[2]=dataset.at[value,'Cost']
                            #s[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(s[k].variables[i]>92 and s[k].variables[i]<=151):
                            value=randrange(93, 151) 
                            s[k].variables[i]=value
                            s[k].objectives[0]=dataset.at[value,'Batting Performance']
                            s[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            s[k].objectives[2]=dataset.at[value,'Cost']
                            #s[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                       
        return s



    def reproduction(self, mating_population: List[S]) -> List[S]:
        number_of_parents_to_combine = self.crossover_operator.get_number_of_parents()
        if len(mating_population) % number_of_parents_to_combine != 0:
            raise Exception('Wrong number of parents')

        offspring_population = []
        for i in range(0, self.offspring_population_size, number_of_parents_to_combine):
            parents = []
            for j in range(number_of_parents_to_combine):
                parents.append(mating_population[i + j])

            offspring = self.crossover_operator.execute(parents)
            
            
        for k in range(len(offspring)) :
            S=pd.Series(offspring[k].variables).duplicated()
            while(duplicacy(S)):
                S=pd.Series(offspring[k].variables).duplicated()
                for i in range(len(S)):
                    if(S[i]==True):
                        if(offspring[k].variables[i]<=21):
                            value=randrange(0, 21)
                            offspring[k].variables[i]=value
                            offspring[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(offspring[k].variables[i]>21 and offspring[k].variables[i]<=37):
                            value=randrange(22, 37)
                            offspring[k].variables[i]=value
                            offspring[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(offspring[k].variables[i]>37 and offspring[k].variables[i]<=54):
                            value=randrange(38, 54)
                            offspring[k].variables[i]=value
                            offspring[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(offspring[k].variables[i]>54 and offspring[k].variables[i]<=92):
                            value=randrange(55, 92)
                            offspring[k].variables[i]=value
                            offspring[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(offspring[k].variables[i]>92 and offspring[k].variables[i]<=151):
                            value=randrange(93, 151)
                            offspring[k].variables[i]=value
                            offspring[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                            


            for solution in offspring:
                self.mutation_operator.execute(solution)
                offspring_population.append(solution)
                if len(offspring_population) >= self.offspring_population_size:
                    break
                ##Code for repair

            
        for k in range(len(offspring_population)) :
            S=pd.Series(offspring_population[k].variables).duplicated()
            while(duplicacy(S)):
                S=pd.Series(offspring_population[k].variables).duplicated()
                for i in range(len(S)):
                    if(S[i]==True):
                        if(offspring_population[k].variables[i]<=21):
                            value=randrange(0, 21)
                            offspring_population[k].variables[i]=value
                            offspring_population[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring_population[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring_population[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring_population[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(offspring_population[k].variables[i]>21 and offspring_population[k].variables[i]<=37):
                            value=randrange(22, 37)
                            offspring_population[k].variables[i]=value                            
                            offspring_population[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring_population[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring_population[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring_population[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(offspring_population[k].variables[i]>37 and offspring_population[k].variables[i]<=54):
                            value=randrange(38, 54)
                            offspring_population[k].variables[i]=value                           
                            offspring_population[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring_population[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring_population[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring_population[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(offspring_population[k].variables[i]>54 and offspring_population[k].variables[i]<=92):
                            value=randrange(55, 92)
                            offspring_population[k].variables[i]=value
                            offspring_population[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring_population[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring_population[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring_population[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
                        
                        elif(offspring_population[k].variables[i]>92 and offspring_population[k].variables[i]<=151):
                            value=randrange(93, 151)
                            offspring_population[k].variables[i]=value
                            offspring_population[k].objectives[0]=dataset.at[value,'Batting Performance']
                            offspring_population[k].objectives[1]=dataset.at[value,'Bowling Performance']
                            offspring_population[k].objectives[2]=dataset.at[value,'Cost']
                            #offspring_population[k].objectives[i]=dataset.at[value,'Batting Performance']+dataset.at[value,'Bowling Performance']
 
        print("repair on offspring")

        return offspring_population


    def replacement(self, population: List[S], offspring_population: List[S]) -> List[List[S]]:
        """ This method joins the current and offspring populations to produce the population of the next generation
        by applying the ranking and crowding distance selection.

        :param population: Parent population.
        :param offspring_population: Offspring population.
        :return: New population after ranking and crowding distance selection is applied.
        """
        ranking = StrengthRanking(self.dominance_comparator)
        density_estimator = KNearestNeighborDensityEstimator()

        r = RankingAndDensityEstimatorReplacement(ranking, density_estimator, RemovalPolicyType.SEQUENTIAL)
        solutions = r.replace(population, offspring_population)

        return solutions

    def get_result(self) -> R:
        return self.solutions

    def get_name(self) -> str:
        return 'SPEA2'
