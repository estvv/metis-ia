from utils.vector import Vector

ROW_ANNOTATIONS = ["A", "B", "C", "D", "E", "F", "G", "H"]
COL_ANNOTATIONS = ["1", "2", "3", "4", "5", "6", "7", "8"]

def coordinates_to_annotations(coords: Vector) -> tuple[str, str]:
    return (ROW_ANNOTATIONS[coords.x], COL_ANNOTATIONS[coords.y])

def annotations_to_coordinates(letter: str, number: str) -> Vector:
    return Vector(ROW_ANNOTATIONS.index(letter.upper()), COL_ANNOTATIONS.index(number))

def is_annotations_correct(annotation: str) -> bool:
    if len(annotation) != 5:
        return False

    return len(annotation) == 5 and \
           annotation[1].upper() in ROW_ANNOTATIONS and annotation[3].upper() in ROW_ANNOTATIONS and \
           annotation[2] in COL_ANNOTATIONS and annotation[4] in COL_ANNOTATIONS
