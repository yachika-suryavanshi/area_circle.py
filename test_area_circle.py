# Area and circumference of a circle
def circle_area_circumference(r):
    area = 3.14159 * r * r
    circumference = 2 * 3.14159 * r
    return round(area, 2), round(circumference, 2)

def test_circle_area_circumference():
    assert circle_area_circumference(5) == (78.54, 31.42)
    assert circle_area_circumference(3) == (28.27, 18.85)
    assert circle_area_circumference(7) == (153.94, 43.98)