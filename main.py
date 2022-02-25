
import tensorflow as tf

x = tf.constant([[1, 2, 3], [4, 5, 6]])
print(x)
x = tf.constant(4, shape=(2, 2))
print(x)
x = tf.ones([2, 2])
print(x)
x = tf.zeros((3, 3))
print(x)
x = tf.random.normal((2, 2))
print(x)
eye = tf.eye(3)
print(eye)
