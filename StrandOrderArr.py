import numpy as np

person_data_def = [('name','S6'),('height','f8'),('weight','f8'),('age','i8')]
print(person_data_def)

[('name','S6'),('height','f8'),('weight','f8'),('age','i8')]

ppl_array = np.zeros((4), dtype=person_data_def)
print(ppl_array)

ppl_array[3] = ('Delta', 71, 215, 23)
ppl_array[0] = ('Alpha', 43, 173, 40)

print(ppl_array)
