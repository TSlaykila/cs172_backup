"""A linear algebra module.

This is a collection of functions dealing with vectors and matrices.
"""

__author__ = 'Put your name here'

import math

def vmagnitude(v : list[float]) -> float:
    """Returns the magnitude of the vector v (which may be of any
    length).

    This is found by adding up the squares of all of the elements of v
    and taking the square root of the total.
    """

    total_sum = 0
    for num in v:
        total_sum += num * num 

    # '** 0.5' = square root#
    return total_sum ** 0.5 

def vsum(v : list[float], w : list[float]) -> list[float]:
    """Returns the sum of vectors v and w.

    This is a vector of the same length, each of whose elements is the
    sum of the corresponding elements in v and w.
    """
    i = 0
    sum_of_vectors = []
    while i < len(v) and i < len(w):
        sum_of_vectors.append(v[i] + w[i])
        i += 1

    return sum_of_vectors

def vdifference(v : list[float], w : list[float]) -> list[float]:
    """Returns the difference between vectors v and w.

    This is a vector of the same length, each of whose elements is the
    difference between the corresponding elements in v and w.
    """
    i = 0
    difference_of_vectors = []
    while i < len(v) and i < len(w):
        difference_of_vectors.append(v[i] - w[i])
        i += 1

    return difference_of_vectors


def velementwise_product(v : list[float], w : list[float]) -> list[float]:
    """Returns the element-wise between vectors v and w.

    This is a vector of the same length, each of whose elements is the
    product of the corresponding elements in v and w.
    """
    i = 0
    multiplication_of_vectors = []
    while i < len(v) and i < len(w):
        multiplication_of_vectors.append(v[i] * w[i])
        i += 1

    return multiplication_of_vectors


def vdot_product(v : list[float], w : list[float]) -> float:
    """Returns the dot product of vectors v and w.

    This is the sum of the products of the corresponding elements.
    """
    list_of_products = velementwise_product(v,w)

    return sum(list_of_products)

def mdimensions(m : list[list[float]]) -> list[int]:
    """Returns, as an array of two elements, the dimensions of matrix m."""
    matrice_dimensions = [0,0]
    matrice_dimensions[0] = len(m)
    matrice_dimensions[1] = len(m[0])
    return matrice_dimensions

def msum(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the element-wise sum of matrices m and n."""
    new_matrice = []
    matrice_dimensions = mdimensions(m)
    i = 0
    while i < matrice_dimensions[0]:
        j = 0
        temp_list = []
        while j < matrice_dimensions[1]:
            temp_list.append(m[i][j] + n[i][j])
            j = j + 1
        new_matrice.append(temp_list)
        i = i + 1
    return new_matrice

def melementwise_product(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the element-wise product of matrices m and n."""
    new_matrice = []
    matrice_dimensions = mdimensions(m)
    i = 0
    while i < matrice_dimensions[0]:
        j = 0
        temp_list = []
        while j < matrice_dimensions[1]:
            temp_list.append(m[i][j] * n[i][j])
            j = j + 1
        new_matrice.append(temp_list)
        i = i + 1
    return new_matrice

def mtranspose(m : list[list[float]]) -> list[list[float]]:
    """Returns the transpose of m, that is, a matrix where element i, j
    is element j, i from m.
    """
    transposed_list = []
    j = 0
    while j < len(m[0]):
        i = 0
        temp_list = []
        while i < len(m):
            temp_list.append(m[i][j])
            i = i + 1
        transposed_list.append(temp_list)
        j = j + 1

    return transposed_list

def mproduct(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the matrix product of m and n.

    (Search the web for a definition.)
    """
    m_lenght_dimensions = mdimensions(m)
    n_lenght_dimensions = mdimensions(n)

    #The if statement check if the product is even possible, m_rows lenght must match n_columns lenght 
    if (m_lenght_dimensions[1] == n_lenght_dimensions[0]):
        product_matrice = []
        i = 0
        while i < len(m): #iterates through each m_row
            j = 0
            k = 0
            temp_list = [] #temporary list to add the product of each m_column indexes with n_row indexes 
            temp_list2 = [] #temporary list to add the first temporary results and create a new matrice changing on m_row
            
            while k < len(n[0]): #iterates through each n_column
                while j < len(m[0]):
                    temp_list.append(m[i][j] * n[j][k])
                    j = j + 1
                temp_list2.append(sum(temp_list))
                temp_list = []
                j = 0
                k = k + 1
            product_matrice.append(temp_list2)
            temp_list2 = []
            i = i + 1
        return product_matrice
    return None
