def test(x, y, z=3, *books, **scores) :
    print(x, y, z)
    print(books)
    print(scores)


test(1, 2, 3, "C语言中文网" ,"Python教程", 语文=89, 数学=94)
