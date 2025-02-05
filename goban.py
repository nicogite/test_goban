import enum
from typing import List


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """

    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban:
    def __init__(self, goban: List[str]) -> None:
        self.goban = goban
        self.alreadyCheckedList = []

    def get_status(self, x: int, y: int) -> Status:
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if (
            not self.goban
            or x < 0
            or y < 0
            or y >= len(self.goban)
            or x >= len(self.goban[0])
        ):
            return Status.OUT
        elif self.goban[y][x] == ".":
            return Status.EMPTY
        elif self.goban[y][x] == "o":
            return Status.WHITE
        elif self.goban[y][x] == "#":
            return Status.BLACK
        raise ValueError(f"Unknown goban value {self.goban[y][x]}")

    def is_taken(self, x: int, y: int) -> bool:
        
        print('RUN TEEEEEST')
        print('Current coords : ')
        print([x, y])
        if (self.get_status(x, y) == Status.WHITE):
            occupiedStatus = [Status.BLACK, Status.OUT]
        else:
            occupiedStatus = [Status.WHITE, Status.OUT]
        
        print(self.get_status(x, y))

        checkList = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

        
        for coord in checkList:
            # Vérifier que les coordonnées n'ont pas déjà été testées
            print('Coords already checked :')
            print(self.alreadyCheckedList)
            alreadyCheck = False
            for checkedCoord in self.alreadyCheckedList:
                if (self.isCoordsEqual(coord, checkedCoord)):
                    print('already checked !')
                    alreadyCheck= True
            
            if alreadyCheck == False:          
                # Vérifier qu'on est toujours sur le kanban
                if (coord[0]>=0 and coord[1]>=0):
                    # Si occupied est false un moment, alors il y a un espace libre
                    occupied = self.is_occupied(x, y , coord[0], coord[1], occupiedStatus)
                    self.alreadyCheckedList.append(coord)
                    if (occupied == False) :
                        return False
                    
        
        return True 
        
        

        raise NotImplementedError

    def is_occupied(self, x, y, check_x: int, check_y: int, occupiedStatus) -> bool:

        print('Check if occupied')
        print([check_x, check_y])

        occupied = False
        if (self.get_status(check_x, check_y) in occupiedStatus) :
            print('space is occupied !')
            occupied = True
        elif (self.get_status(x, y) == self.get_status(check_x, check_y)) :
            # Si la case à la même couleur, alors on teste cette case avec la même méthode qu'au début
            print('same color !')
            occupied = self.is_taken(check_x, check_y)
        else: 
            print('free space found !')
            occupied = False
        
        print('is occupied : ')
        print(occupied)

        return occupied    
        
    def isCoordsEqual(self, coordsA, coordsB) -> bool:
        print('Check coords')
        print(coordsA)
        print(coordsB)
        for valeur_c1, valeur_c2 in zip(coordsA, coordsB):
            # si la valeur de c1 est différente de c2
            if valeur_c1 != valeur_c2:
                return False  # Les tableaux ne sont pas identiques
                # S'il n'y a pas eu de discordance entre les deux listes, on arrive ici et on revoie donc True
        return True