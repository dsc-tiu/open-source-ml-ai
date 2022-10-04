import numpy
from PIL import Image


def median_filter(matrix, filter):
    temp = []
    indexer = filter // 2
    matrix_final = []
    matrix_final = numpy.zeros((len(matrix),len(matrix[0])))

    for i in range(len(matrix)):

        for j in range(len(matrix[0])):

            for z in range(filter):
                if i + z - indexer < 0 or i + z - indexer > len(matrix) - 1:
                    for c in range(filter):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(matrix[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter):
                            temp.append(matrix[i + z - indexer][j + k - indexer])

            temp.sort()
            matrix_final[i][j] = temp[len(temp) // 2]
            temp = []

    return matrix_final


def main():
    img = Image.open("imgs/img_ex.jpg").convert(
        "L")
    data = numpy.array(img)
    img_median = median_filter(data, 3) 
    data = Image.fromarray(img_median)
    data.show()


main()