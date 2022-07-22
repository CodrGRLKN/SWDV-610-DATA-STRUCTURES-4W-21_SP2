import math


class State():
    def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.boat = boat
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.parent = None

    def isGoal(self):
        if self.cannibalLeft == 0 and self.missionaryLeft == 0:
            return True
        else:
            return False

    def isValid(self):
        if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
                   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
                   and self.missionaryRight == other.missionaryRight

    def __hash__(self):
        return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))

def successors(cur_state):
    children = [];
    if cur_state.boat == 'left':
        newState = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 2)
       
        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
        newState = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 1)
        
                #
        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
        newState = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 2, cur_state.missionaryRight)
        
      
        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
        newState = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)

        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
        newState = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight)
        ## One cannibal crosses left to right.
        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
    else:
        newState = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 2)
        
        
           
        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
        newState = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 2, cur_state.missionaryRight)
       
        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
        newState = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)
        
        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
        newState = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 1)
       
        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
        newState = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight)
      
        if newState.isValid():
            newState.parent = cur_state
            children.append(newState)
    return children

def BFSrch():
    initialState = State(3,3,'left',0,0)
    if initialState.isGoal():
        return initialState
    frontier = list()
    explored = set()
    frontier.append(initialState)
    while frontier:
        state = frontier.pop(0)
        if state.isGoal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return None

def printSolution(solution):
        path = []
        path.append(solution)
        parent = solution.parent
        while parent:
            path.append(parent)
            parent = parent.parent

        for t in range(len(path)):
            state = path[len(path) - t - 1]
            print ("("+ str(state.cannibalLeft) + "," + str(state.missionaryLeft) + "," + state.boat + "," + str(state.cannibalRight) + "," + str(state.missionaryRight)+ ")")

def main():
    solution = BFSrch()
    print ("CannibalLeft,  MissionaryLeft,  Boat,   CannibalRight,  MissionaryRight")
    printSolution(solution)


main()