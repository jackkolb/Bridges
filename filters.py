import random

force_names = []

def filter_variable_repeats(matrix):
    filtered_matrix = []

    # go through equations, filter out repeated variables sets
    variable_sets = []

    for equation in matrix:
        variables = collect_variables(equation)

        if variables not in variable_sets:
            variable_sets.append(variables)
            filtered_matrix.append(equation)
    return filtered_matrix


def filter_guaranteed_variable_compositions(matrix):
    filtered_matrix = []

    # go through equations, filter out equations consisting of guaranteed variables
    guaranteed_variables = collect_guaranteed_variables(matrix)
    for equation in matrix:
        variables = collect_variables(equation)
        if variables != guaranteed_variables:
            filtered_matrix.append(equation)

    return filtered_matrix

def filter_nonexistant_equations(matrix):
    filtered_matrix = [x for x in matrix if len(collect_variables(x)) != 0]
    return filtered_matrix


def collect_variables(equation):
    variables = [force_names[i] for i in range(len(equation) - 1) if equation[i] != 0]
    variables.sort()
    return variables


def collect_variable_sets(matrix):
    variable_sets = [collect_variables(x) for x in matrix]
    return variable_sets


def collect_guaranteed_variables(matrix):
    # gather guaranteed variables (1 var = external), remove equations using solely guaranteed variables
    guaranteed_variables = [x[0] for x in collect_variable_sets(matrix) if len(x) == 1]
    guaranteed_variables.sort()
    return guaranteed_variables


def collect_guaranteed_variable_equations(matrix):
    guaranteed_variables = collect_guaranteed_variables(matrix)
    guaranteed_equations = [x for x in matrix if collect_variables(x) in [[x] for x in guaranteed_variables]]
    return guaranteed_equations


# given unknown variable, return every possible route known
def collect_tree(matrix, target_variable, known_variables, parent_equations):
    # exit if current path > variables, hoping to raise efficiency
    if len(parent_equations) > len(matrix[0]) - 1:
        print("cut")
        return -1

    paths = []
    equations = [x for x in matrix if target_variable in collect_variables(x) and x not in parent_equations]
    known_variables.append(target_variable)

    for equation in equations:
        unknown_variables = [x for x in collect_variables(equation) if x not in known_variables]
        if unknown_variables == []:
            path = parent_equations[:]
            path.append(equation)
            paths.append(path)
        else:
            for unknown_variable in unknown_variables:
                path_root = parent_equations[:]
                path_root.append(equation)
                collection = collect_tree(matrix, unknown_variable, known_variables[:], path_root[:])
                # if path > variables
                if collection == -1:
                    continue

                for path in collection:
                    if path not in paths:
                        paths.append(path)
    return paths

# gets every combination of equations in paths
def get_combinations(variable_equations, parent_paths, index, results):
    for path in variable_equations[len(variable_equations)-1 - index]:
        if index == 0:
            result_path = parent_paths[:]
            result_path.append(path)
            results.append(result_path)
        else:
            parent_paths.append(path)
            get_combinations(variable_equations, parent_paths[:], index-1, results)

def remove_transitives(matrix):
    variables = force_names
    print("  All Variables: " + str(variables))
    guaranteed_variables = collect_guaranteed_variables(matrix)
    seeking_variables = [x for x in variables if x not in guaranteed_variables]

    print("  Guaranteed Variables: " + str(guaranteed_variables))
    print("  Seeking the Variables: " + str(seeking_variables))

    known_variables = guaranteed_variables

    forbidden_equations = []

    used_equations = collect_guaranteed_variable_equations(matrix)

    paths = []
    [paths.append([[x]]) for x in used_equations]

    # gather all paths
    print("  Finding equation paths for each variable")
    for variable in seeking_variables:
        print("Calculating for: " + variable)
        results = collect_tree(matrix, variable, known_variables[:], used_equations[:])
        paths.append(results)

    # collect all combinations of path equations
    print("  Generating all valid path combinations")
    path_combinations = []
    trace = ""
    get_combinations(paths, [], len(variables)-1, path_combinations)
    print("  " + str(len(path_combinations)) + " combinations found")
    #for path in path_combinations:
    #    print(path)
    #    print()

    # with all the path combinations, create a collection of equations required
    print("  Sorting the path combinations into equation sets")
    equation_sets = []
    for variables_path in path_combinations:
        equation_set = []
        for path in variables_path:
            [equation_set.append(equation) for equation in path if equation not in equation_set]
        equation_sets.append(equation_set)

    # remove duplicate equation sets
    print("  Removing duplicate equation sets")
    filtered_equation_sets = []
    [filtered_equation_sets.append(x) for x in equation_sets if x not in filtered_equation_sets]
    print("  " + str(len(filtered_equation_sets)) + " unique equation sets found")

    # filter those of length = variables
    print("  Removing overdefined/underdefined equation sets")
    valid_equation_sets = []
    for equation_set in filtered_equation_sets:
        if len(equation_set) == len(force_names):
            valid_equation_sets.append(equation_set)

    print("  There are " + str(len(valid_equation_sets)) + " fully defined equation sets")

    print("  Using the first fully defined set")
    sorted_matrix  = valid_equation_sets[0]

    return sorted_matrix


def simplify_overdefinitions(matrix):
    print("Starting the equations simplification with " + str(len(matrix)) + " equations")
    print("Filtering equations via simple means:")
    # filter "absurd" equations (no variables)    
    print("  Removing variableless equations")
    matrix = filter_nonexistant_equations(matrix)

    # filter variable repeats
    print("  Removing linearly dependent equations")
    matrix = filter_variable_repeats(matrix)

    # filter equations using solely guaranteed variables
    print("  Removing equations with solely guaranteed variables")
    matrix = filter_guaranteed_variable_compositions(matrix)

    filtered_matrix = []

    for equation in matrix:
        variables = collect_variables(equation)
        if variables != collect_variable_sets(filtered_matrix):
            filtered_matrix.append(equation)

    print("There are now " + str(len(matrix)) + " equations")

    # remove transitives
    print("Generating linked equation trees:")
    filtered_matrix = remove_transitives(filtered_matrix)

    if len(filtered_matrix) > len(force_names):
        print("overdefined")    
    if len(filtered_matrix) < len(force_names):
        print("underdefined")

    return filtered_matrix
