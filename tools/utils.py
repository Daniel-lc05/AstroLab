import numpy as np

def attach(child, parent, p_parent_child, R_parent_child=None):
    
    if R_parent_child is None:
        R_parent_child = np.eye(3)

    p_parent_child = np.asarray(p_parent_child, dtype=float)#Positon vector
    R_parent_child = np.asarray(R_parent_child, dtype=float)#Rotation vector

    # Detach from previous parent
    if child.parent is not None and child in child.parent.children:
        child.parent.children.remove(child)

    # Set hierarchy
    child.parent = parent
    child.p_parent_child = p_parent_child
    child.R_parent_child = R_parent_child

    # Ensure parent has children list
    if not hasattr(parent, "children"):
        parent.children = []

    # Register child once
    if child not in parent.children:
        parent.children.append(child)

    # Optional: inherit stage from core parent
    if hasattr(parent, "core") and parent.core:
        if hasattr(parent, "stage"):
            child.stage = parent.stage

def get_pos_parts (part_a,AstroLab): #Gets distance from the CENTER of part A to the CENTER of MAIN PART ONLY FOR MAKE THE LOCAL POSITIONS OF THE PARTS
    stages = AstroLab.get_stages()
    for s in stages:
        for p in s.parts:
            if p.main:
                part_main=p

    if part_main.main==False:
        print ("The introduced part as main part, is not")

    if (part_main.stage == part_a.stage):
        child_pos = abs(part_a.p_parent_child[2])
        
    elif (part_main.stage != part_a.stage):
        part_a_pos=[]
        stage_a_index=part_a.stage#Stage a index
        stage_a = AstroLab.stages[part_a.stage-1]
        stage_main = AstroLab.stages[part_main.stage-1]
        stage_main_index=part_main.stage#Main Stage index
        stages_length=0
        for s in (stages[stage_main_index:stage_a_index]): #Gets the size of the stages between the parts (not the point stage)
            stages_length+= stage_length(s)

        stage_main_distance=0 #Distance from the centre of the main part to the bottom of the main stage
        for p in stage_main.get_parts():
            if p.core:
                stage_main_distance += abs(p.bottom)
            stage_main_distance+=p.length
            
        child_pos = (stage_length(stage_a)/2) - part_a.p_parent_child[2] + stages_length + stage_main_distance


    return (child_pos)


def stage_length(stage):
    points = []
    for part in stage.get_parts():
        points.append(part.top+part.p_parent_child[2])
        points.append(part.bottom+part.p_parent_child[2])
    length = (max(points)-min(points))
    return length


def calc_N_force (m,a): #Calculates the force, given the mass and the acceleartion usign Newtons Fst. Law
    return(m*a)


def order(data): #Trasposes the matrix, getting one property by row
    processed_data = []
    for j in range (len(data[0])):
        memory_list = list()
        for i in data:
            memory_list.append(i[j])
        processed_data.append(memory_list)

    return(processed_data)

