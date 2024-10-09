def right_find_element_in_list(element, list):
  a = 0

  for i in list:
    if i == element: break
    a += 1

  if a >= len(list):
    return -1

  return a

def no_element_error_find_element_in_list(element, list):
  a = 0

  for i in list:
    if i == element: return a
    a += 1

def no_element_error_2_find_element_in_list(element, list):
  a = 0

  for i in list:
    if i == element: break
    a += 1

  return a

def always_minus_1(element, list):
  return -1