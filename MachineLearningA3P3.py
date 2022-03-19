import numpy as np


def read_input(file_name):
    examplars = []
    file = open(file_name, 'r')
    for line in file:
        data = list(float(x) for x in line.split())
        examplars.append(data)
    return examplars


def read_output(file_name):
    result = []
    file = open(file_name, 'r')
    for line in file:
        data = float(line)
        result.append(data)
    return result


input_1 = read_input('pred1.dat')
input_2 = read_input('pred2.dat')
output_1 = read_output('resp1.dat')
output_2 = read_output('resp2.dat')
# print(input_1, input_2, output_1, output_2)
y_1 = np.matrix(output_1[0:500]).transpose()
y_2 = np.matrix(output_2[0:500]).transpose()
a_1 = np.matrix(input_1[0:500])
a_2 = np.matrix(input_2[0:500])
a_1_t = a_1.transpose()
a_2_t = a_2.transpose()
w_ml_1 = np.linalg.inv(a_1_t.dot(a_1)).dot(a_1_t).dot(y_1)
w_ml_2 = np.linalg.inv(a_2_t.dot(a_2)).dot(a_2_t).dot(y_2)
y_predict_1 = np.matrix(input_1[500:]).dot(w_ml_1)
y_predict_2 = np.matrix(input_2[500:]).dot(w_ml_2)
error_1 = y_predict_1 - np.matrix(output_1[500:]).transpose()
error_2 = y_predict_2 - np.matrix(output_2[500:]).transpose()
sse_1 = sum(err * err for err in error_1)
sse_2 = sum(err * err for err in error_2)
print("w^ for pred1.dat/resp1.dat:")
print(w_ml_1)
# print((np.array(w_ml_1).reshape(-1, ).tolist()))
print()
print("w^ for pred2.dat/resp2.dat:")
print(w_ml_2)
# print(np.array(w_ml_2).reshape(-1, ).tolist())
print()
print("SSE for pred1.dat/resp1.dat:")
print(np.array(sse_1)[0].tolist())
print()
print("SSE for pred2.dat/resp2.dat:")
print(np.array(sse_2)[0].tolist())
print()
