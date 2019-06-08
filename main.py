import Joint
import rref

import filters
import random


def add_connection(a, b):
    a.add_connection(b)
    b.add_connection(a)

def inch(x):
    return x * .0254

def cm(x):
    return x / 100

if __name__ == "__main__":
    print("-- The Amazing ME 174 Truss Solver! --")
    overall_load_mass = 4

    # define joints
    joints = list()

    # POINTS ARE RELATIVE TO J1, WHICH IS AT (0, 0, 0)

    A = Joint.Joint(0, 0, 0, name="A")
    B = Joint.Joint(0, 10, 0, name="B")
    C = Joint.Joint(10, 10, 0, name="C")
    D = Joint.Joint(10, 0, 0, name="D")
    E = Joint.Joint(5, 5, 15, name="E")

    add_connection(A, B)
    add_connection(B, C)
    add_connection(C, D)
    add_connection(D, A)

    add_connection(A, E)
    add_connection(B, E)
    add_connection(C, E)
    add_connection(D, E)

    overall_load_force = 100 * 9.81
    A.add_force(overall_load_force / 4, 0, 0, 1)
    B.add_force(overall_load_force / 4, 0, 0, 1)
    C.add_force(overall_load_force / 4, 0, 0, 1)
    D.add_force(overall_load_force / 4, 0, 0, 1)
    E.add_force(overall_load_force, 0, 0, -1)

    joints.append(A)
    joints.append(B)
    joints.append(C)
    joints.append(D)
    joints.append(E)

    # apex
    # A1 = Joint.Joint(0, 0, cm(8.3), name="A1") # good

    # B1 = Joint.Joint(cm(-4.284), cm(-.612), cm(6.3), name="B1") # good
    # B2 = Joint.Joint(cm(4.284), cm(-.612), cm(6.3), name="B2")
    # B3 = Joint.Joint(cm(-4.284), cm(.612), cm(6.3), name="B3")
    # B4 = Joint.Joint(cm(4.282), cm(.612), cm(6.3), name="B4")

    # C_x = 8.354
    # C1 = Joint.Joint(cm(-C_x), cm(-1.19), cm(3.9), name="C1") # good
    # C2 = Joint.Joint(cm(C_x), cm(-1.19), cm(3.9), name="C2")
    # C3 = Joint.Joint(cm(-C_x), cm(1.19), cm(3.9), name="C3")
    # C4 = Joint.Joint(cm(C_x), cm(1.19), cm(3.9), name="C4")

    # D1 = Joint.Joint(cm(-12.42), cm(-1.775), cm(2.5), name="D1") # good
    # D2 = Joint.Joint(cm(12.42), cm(-1.775), cm(2.5), name="D2")
    # D3 = Joint.Joint(cm(-12.42), cm(1.775), cm(2.5), name="D3")
    # D4 = Joint.Joint(cm(12.42), cm(1.775), cm(2.5), name="D4")

    # # bottom corners
    # E_x = 17.78
    # E1 = Joint.Joint(cm(-E_x), inch(-1), 0, name="E1") # good
    # E2 = Joint.Joint(cm(E_x), inch(-1), 0, name="E2")
    # E3 = Joint.Joint(cm(-E_x), inch(1), 0, name="E3")
    # E4 = Joint.Joint(cm(E_x), inch(1), 0, name="E4")

    # F1 = Joint.Joint(cm(-12.42), inch(-1), 0, name="F1") # good (x matches d)
    # F2 = Joint.Joint(cm(12.42), inch(-1), 0, name="F2")
    # F3 = Joint.Joint(cm(-12.42), inch(1), 0, name="F3")
    # F4 = Joint.Joint(cm(12.42), inch(1), 0, name="F4")

    # G1 = Joint.Joint(cm(-C_x), inch(-1), 0, name="G1") # good (x matched C)
    # G2 = Joint.Joint(cm(C_x), inch(-1), 0, name="G2")
    # G3 = Joint.Joint(cm(-C_x), inch(1), 0, name="G3")
    # G4 = Joint.Joint(cm(C_x), inch(1), 0, name="G4")

    # H1 = Joint.Joint(0, inch(-1), 0, name="H1") # good
    # H2 = Joint.Joint(0, inch(1), 0, name="H2")

    # I1 = Joint.Joint(cm(-11.89), 0, cm(2.75), name="I1") # good
    # I2 = Joint.Joint(cm(11.89), 0, cm(2.75), name="I2")

    # J1 = Joint.Joint(0, 0, 0, name="J1") # good

    # K1 = Joint.Joint(cm(-C_x), 0, cm(2.7), name="K1") # good (x matched c)
    # K2 = Joint.Joint(cm(C_x), 0, cm(2.7), name="K2")
    

    # # Add joints to joint list
    # joints.append(A1)

    # joints.append(B1)
    # joints.append(B2)
    # joints.append(B3)
    # joints.append(B4)

    # joints.append(C1)
    # joints.append(C2)
    # joints.append(C3)
    # joints.append(C4)

    # joints.append(D1)
    # joints.append(D2)
    # joints.append(D3)
    # joints.append(D4)

    # joints.append(E1)
    # joints.append(E2)
    # joints.append(E3)
    # joints.append(E4)

    # joints.append(F1)
    # joints.append(F2)
    # joints.append(F3)
    # joints.append(F4)

    # joints.append(G1)
    # joints.append(G2)
    # joints.append(G3)
    # joints.append(G4)

    # joints.append(H1)
    # joints.append(H2)

    # joints.append(I1)
    # joints.append(I2)

    # joints.append(J1)

    # joints.append(K1)
    # joints.append(K2)


    # # add joint connections
    
    # # Center Vertical
    # add_connection(A1, J1)

    # # Front
    # add_connection(A1, H1)

    # # Front left
    # add_connection(A1, B1)
    # add_connection(B1, C1)
    # add_connection(C1, D1)
    # add_connection(D1, E1)

    # add_connection(B1, H1)
    # add_connection(C1, H1)
    # add_connection(D1, F1)

    # add_connection(E1, F1)
    # add_connection(F1, G1)
    # add_connection(G1, H1)

    # # Front right
    # add_connection(A1, B2)
    # add_connection(B2, C2)
    # add_connection(C2, D2)
    # add_connection(D2, E2)

    # add_connection(B2, H1)
    # add_connection(C2, H1)
    # add_connection(D2, F2)

    # add_connection(E2, F2)
    # add_connection(F2, G2)
    # add_connection(G2, H1)

    # # Back
    # add_connection(A1, H2)

    # # Back left
    # add_connection(A1, B3)
    # add_connection(B3, C3)
    # add_connection(C3, D3)
    # add_connection(D3, E3)

    # add_connection(B3, H2)
    # add_connection(C3, H2)
    # add_connection(D3, F3)

    # add_connection(E3, F3)
    # add_connection(F3, G3)
    # add_connection(G3, H2)

    # # Back right
    # add_connection(A1, B4)
    # add_connection(B4, C4)
    # add_connection(C4, D4)
    # add_connection(D4, E4)

    # add_connection(B4, H2)
    # add_connection(C4, H2)
    # add_connection(D4, F4)

    # add_connection(E4, F4)
    # add_connection(F4, G4)
    # add_connection(G4, H2)

    # # Bottom
    #     # Diagonal zig-zag
    # add_connection(E3, G1)
    # add_connection(G1, H2)
    # add_connection(H2, G2)
    # add_connection(G2, E4)
    #     # Perpindicular connections
    # add_connection(E1, E3)
    # add_connection(G1, G3)
    # add_connection(G2, G4)
    # add_connection(E2, E4)
    #     # center joint connection
    # add_connection(H1, J1)
    # add_connection(J1, H2)

    # # Center supports
    #     # left cross vertical
    # add_connection(G1, K1)
    # add_connection(K1, C3)
    # add_connection(G3, K1)
    # add_connection(K1, C1)        
    #     # right cross vertical
    # add_connection(G2, K2)
    # add_connection(K2, C4)
    # add_connection(G4, K2)
    # add_connection(K2, C2)   

    #     # left cross angled
    # add_connection(E1, I1)
    # add_connection(I1, C3)
    # add_connection(E3, I1)
    # add_connection(I1, C1)        
    #     # right cross angled
    # add_connection(E2, I2)
    # add_connection(I2, C4)
    # add_connection(E4, I2)
    # add_connection(I2, C2)    
    
    #     # top horizontals
    # add_connection(B1, B3)
    # add_connection(C1, C3)
    # add_connection(B2, B4)
    # add_connection(C2, C4)    

    # # add external loads/reactions
    # overall_load_force = overall_load_mass * 9.81
    # H1.add_force(overall_load_force / 2, 0, 0, -1)
    # H2.add_force(overall_load_force / 2, 0, 0, -1)

    # E1.add_force(overall_load_force / 4, 0, 0, 1)
    # E2.add_force(overall_load_force / 4, 0, 0, 1)
    # E3.add_force(overall_load_force / 4, 0, 0, 1)
    # E4.add_force(overall_load_force / 4, 0, 0, 1)

    # generate force balance equations
    equations = list()
    for joint in joints:
        e_x, e_y, e_z = joint.force_balance_equations()
        # print(joint.name)
        # print(e_x)
        # print(e_y)
        # print(e_z)
        equations.append(e_x)
        equations.append(e_y)
        equations.append(e_z)

    # gather all unique force names
    force_names = []
    for equation in equations:
        for force_name in equation.keys():
            if force_name == "external":
                pass
            elif force_name not in force_names:
                force_names.append(force_name)

    filters.force_names = force_names
    #print(force_names)

    # construct base equation matrix
    equation_matrix = []

    # add to equation matrix from each joint, expanding equations to represent all variables
    for equation in equations:
        expanded_equation = list()  # create empty equation
        for force_name in force_names:  # for each force name overall, if there is a match fill it, if not keep 0
            multiplier = 0
            if force_name in equation.keys():
                multiplier = equation[force_name]
            expanded_equation.append(float(multiplier))
        expanded_equation.append(equation["external"] * -1)

        # add non-zero equations to equation matrix
        if len([x for x in expanded_equation if abs(x) > 0.00001]) != 0:
            equation_matrix.append(expanded_equation)

    #print("There are " + str(len(equation_matrix)) + " force balance equations")

    # remove overdefinitions
    equation_matrix = filters.simplify_overdefinitions(equation_matrix)

    step = len(force_names)+1

    # row reduce the first four equations
    sub_result = rref.ToReducedRowEchelonForm(equation_matrix)

    # round values
    for i in range(len(sub_result)):
        equation = sub_result[i]
        for j in range(len(sub_result)+1):
            rounded_value = round(equation[j], 5)
            equation[j] = rounded_value
        sub_result[i] = equation

    print()
    print("Results: ")
    for result in sub_result:
        output_string = "Force in beam " + str(force_names[result.index(1.0)]) + " : " + str(result[-1])
        print(output_string)

