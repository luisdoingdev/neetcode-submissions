from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest_score = ["",0]
    for score in scores:
        if score[1] > highest_score[1]:
            highest_score = score
    name, score = highest_score
    return name
        
         



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
