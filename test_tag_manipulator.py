from tag_manipulator import TagManipulator


def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_java_result_java():
    # arrange
    stringToSplit = "java"
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_java_python_result_java_python():
    # arrange
    stringToSplit = "java"
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult
