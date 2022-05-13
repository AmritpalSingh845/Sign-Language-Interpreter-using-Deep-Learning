import tensorflow as tf
print("hellO")
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))