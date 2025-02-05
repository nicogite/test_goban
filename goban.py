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
        """
        Check if a given position is take or not

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            True if the position is taken
        """
        
        if (self.get_status(x, y) == Status.WHITE):
            occupiedStatus = [Status.BLACK, Status.OUT]
        else:
            occupiedStatus = [Status.WHITE, Status.OUT]

        checkList = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

        
        for coord in checkList:
            # Vérifier que les coordonnées n'ont pas déjà été testées
            alreadyCheck = False

            for checkedCoord in self.alreadyCheckedList:
                if (len(self.alreadyCheckedList) and self.isCoordsEqual(coord, checkedCoord)):
                    alreadyCheck= True
                    break
            
            if alreadyCheck == False:          
            
                # Si occupied est false un moment, alors il y a un espace libre
                occupied = self.is_occupied(x, y , coord[0], coord[1], occupiedStatus)
                
                print(self.alreadyCheckedList)
                if (occupied == False) :
                    self.alreadyCheckedList = []
                    return False
                
        
        return True 
        
        

        raise NotImplementedError

    def is_occupied(self, x, y, check_x: int, check_y: int, occupiedStatus) -> bool:
        """
        Given a set of coordinate, return True if another place is occupied

        Args:
            x: the x coordinate
            y: the y coordinate
            check_x: the x cordinate of the checked place
        Returns:
            a Status
        """
        self.alreadyCheckedList.append([check_x, check_y])
        occupied = False
        if (self.get_status(check_x, check_y) == Status.EMPTY) :
            return False
        elif (self.get_status(check_x, check_y) in occupiedStatus) :
            occupied = True
        elif (self.get_status(x, y) == self.get_status(check_x, check_y)) :
            occupied = self.is_taken(check_x, check_y)
        else: 
            occupied = False

        return occupied    
        
    def isCoordsEqual(self, coordsA, coordsB) -> bool:
        for valeur_c1, valeur_c2 in zip(coordsA, coordsB):
            # si la valeur de c1 est différente de c2
            if valeur_c1 != valeur_c2:
                return False  # Les tableaux ne sont pas identiques
                # S'il n'y a pas eu de discordance entre les deux listes, on arrive ici et on revoie donc True
        return True