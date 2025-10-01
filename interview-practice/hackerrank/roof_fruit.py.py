def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Problem: Count how many apples and oranges fall on Sam's house.

    Setup:
    - The house lies between points s and t on a number line.
    - An apple tree is at point a, and an orange tree is at point b.
    - Each element in apples[] and oranges[] represents the distance 
      (positive or negative) the fruit falls from its tree.

    Task:
    - Count how many apples land on the house (between s and t).
    - Count how many oranges land on the house (between s and t).
    - Print the counts (apples first, oranges second).

    Example:
    s = 7, t = 11, a = 5, b = 15
    apples = [-2, 2, 1], oranges = [5, -6]
    → Apples landing on house: 1
    → Oranges landing on house: 1
    """

    roof_apples = 0
    roof_oranges = 0

    for apple in apples:
        if s <= apple + a <= t:
            roof_apples += 1

    for orange in oranges:
        if s <= orange + b <= t:
            roof_oranges += 1

    print(roof_apples)
    print(roof_oranges)
