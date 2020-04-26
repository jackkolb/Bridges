# Bridges

Bridges calculates the geometric static loads in a 3D rigid structure given the structure's geometry, reaction forces, and external forces. 

It was designed to aid our team in UC Riverside's Machine Design (ME174) course project. We had to design a plastic straw bridge, with our grade dependent on how close our predicted failure load was to the actual failure load of the bridge. We used this tool to determine the maximum load of our bridge, and were able to achieve a ~2% error

This tool was not intended for general use, but may help others either looking to design a 3D truss solver or use one for their own projects. This solver is not optimized so be wary when using trusses with over ~20 members.

To use the solver, open main.py and look at the section with Joint.Joint, add_connection, add_force, and joints.append.

For every joint in your truss (where two members intersection), add a joint:
```
JOINT_NAME = Joint.Joint(X_LOCATION, Y_LOCATION, Z_LOCATION, name="JOINT NAME") 
```

For every member in your truss (connection between two joints), add a connection:
```
add_connection(JOINT_A, JOINT_B)  # note that you only need to add one connection two joints
```

Add each external force (including reaction forces):
```
JOINT_NAME.add_force(LOAD_AMOUNT, X_DIRECTION, Y_DIRECTION, Z_DIRECTION)
```

Add each joint to the master joint list:
```
joints.append(JOINT_NAME)
```

For further reference you can see the examples in main.py.

Once the structured is defined, simply run the main.py script and it will calculate the force in each joint. Positive results are compression, negative results are tension. Output for the example structure, a square pyramid, is shown below:
```
$> python3 main.py
-- The Amazing ME 174 Truss Solver! --
There are 12 valid force balance equations
Generating linked equation trees:
  Calculating for: AB
  Calculating for: AD
  Calculating for: BC
  Calculating for: CD
  16 unique equation sets found
  There are 2 fully defined equation sets

Results: 
Force in beam AB : 81.75
Force in beam AD : 81.75
Force in beam AE : -271.13408
Force in beam BC : 81.75
Force in beam BE : -271.13408
Force in beam CD : 81.75
Force in beam CE : -271.13408
Force in beam DE : -271.13408
```
