# Geometry Project

## Exercice POO: héritage, associations

- Compléter les classes Shape, WeightedPoint, ColoredPoint, ColoredWeightedPoint, Segment, Circle, Polygon
à partir du diagramme UML: https://github.com/matthcol/python202503perf/blob/main/schemas.svg

- rendre la classe Shape et sa méthode translate abstraites

## Interfaces
Ajouter les interfaces (au sens UML) suivantes:
- Mesurable1D avec la méthode length() -> float
- Mesurable2D avec les méthodes perimeter() -> float et area() -> float

La classe Segment implémente Mesurable1D.
Les classes Circle et Polygon implémentent Mesurable2D.
