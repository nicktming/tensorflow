import tensorflow as tf 

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")

result = a + b

print(a.graph)
print(b.graph)
print(tf.get_default_graph())

print(a.graph == b.graph)