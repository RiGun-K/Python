import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

print(tf.__version__)

x_data = [1,2,3]
y_data = [1,2,3]

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

X = tf.placeholder