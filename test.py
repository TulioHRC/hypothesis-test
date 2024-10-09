from hypothesis import given, example
from hypothesis.strategies import lists, integers
from main import right_find_element_in_list, no_element_error_find_element_in_list, no_element_error_2_find_element_in_list, always_minus_1

@given(element=integers(), lst=lists(integers()))
def test_right_find_element_in_list(element, lst):
    result = right_find_element_in_list(element, lst)
    
    # Verifica se o elemento está na lista e se o índice está correto
    if element in lst:
        assert result == lst.index(element)
    else:
        assert result == -1

@given(element=integers(), lst=lists(integers()))
def test_no_element_error_find_element_in_list(element, lst):
    result = no_element_error_find_element_in_list(element, lst)
    
    # Verifica se o elemento está na lista e se o índice está correto
    if element in lst:
        assert result == lst.index(element)
    else:
        assert result == -1

@given(element=integers(), lst=lists(integers()))
def test_no_element_error_2_find_element_in_list(element, lst):
    result = no_element_error_2_find_element_in_list(element, lst)
    
    # Verifica se o elemento está na lista e se o índice está correto
    if element in lst:
        assert result == lst.index(element)
    else:
        assert result == -1

@given(element=integers(), lst=lists(integers()))
def test_alqways(element, lst):
    result = always_minus_1(element, lst)
    
    # Verifica se o elemento está na lista e se o índice está correto
    if element in lst:
        assert result == lst.index(element)
    else:
        assert result == -1


@given(element=integers(), lst=lists(integers()))
def test_alaqways(element, lst):
    result = always_minus_1(element, lst)
    
    # Verifica se o elemento está na lista e se o índice está correto
    if element in lst:
        assert result == lst.index(element)
    else:
        assert result == -1


@given(element=integers(), lst=lists(integers()))
def test_alqwaysa(element, lst):
    result = always_minus_1(element, lst)
    
    # Verifica se o elemento está na lista e se o índice está correto
    if element in lst:
        assert result == lst.index(element)
    else:
        assert result == -1


@given(element=integers(), lst=lists(integers()))
def test_alqweays(element, lst):
    result = always_minus_1(element, lst)
    
    # Verifica se o elemento está na lista e se o índice está correto
    if element in lst:
        assert result == lst.index(element)
    else:
        assert result == -1