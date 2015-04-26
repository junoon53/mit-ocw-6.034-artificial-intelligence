#!/usr/bin/env python
"""
Copyright Vikram Pawar + MIT Guys
Implementation of the Extra Credit problem from the tutorials
from Quiz 2 of 2008.
"""
import sys
from csp import CSP, Variable, BinaryConstraint, solve_csp_problem, \
    basic_constraint_checker


if __name__ == "__main__":
    if len(sys.argv) > 1:
        problem_str = sys.argv[1]
    else:
        problem_str = "time_traveler"
        
    if problem_str == "map_coloring":
        import map_coloring_csp
        problem = map_coloring_csp.map_coloring_csp_problem
    elif problem_str == "moose":
        import moose_csp
        problem = moose_csp.moose_csp_problem
    elif problem_str == "sudoku":
        import sudoku_csp
        problem = sudoku_csp.sudoku_csp_problem
    elif problem_str == "ta_scheduling":
        import ta_scheduling_csp
        problem = ta_scheduling_csp.ta_scheduling_csp_problem
    elif problem_str == "time_traveler":
        import time_traveler_csp
        problem = time_traveler_csp.time_traveling_csp_problem

    if len(sys.argv) > 2:
        checker_type = sys.argv[2]
    else:
        checker_type = "fc"
        
    if checker_type == "dfs":
        checker = basic_constraint_checker
    elif checker_type == "fc":
        import lab4
        checker = lab4.forward_checking
    elif checker_type == "fcps":
        import lab4
        checker = lab4.forward_checking_prop_singleton
    else:
        checker = basic_constraint_checker

    solve_csp_problem(problem, checker, verbose=True)
