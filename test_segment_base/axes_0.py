# Sample functions.
def sample0a():
    "Sample drawing with one xcat axis and two buckets."
    drawing = Drawing(400, 200)
    data = [(10, 20)]
    xAxis = XCategoryAxis()
    xAxis.setPosition(75, 75, 300)
    xAxis.configure(data)
    xAxis.categoryNames = ['Ying', 'Yang']
    xAxis.labels.boxAnchor = 'n'
    drawing.add(xAxis)
    return drawing
