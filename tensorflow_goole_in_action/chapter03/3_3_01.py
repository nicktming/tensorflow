import tensorflow as tf 

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")

result = tf.add(a, b, name="add")

with tf.Session() as sess:
	# t = sess.run(result)
	# print("t:", t)
	print("t:", result.eval(session=sess))






