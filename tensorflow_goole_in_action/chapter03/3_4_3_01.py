import tensorflow as tf 

w1 = tf.Variable(tf.random_normal((2,3), stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal((3,1), stddev=1, seed=1))

x = tf.constant([[0.7, 0.9]])

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	print(sess.run(init_op))
	# print(sess.run(w1.initializer))
	# print(sess.run(w2.initializer))
	print(sess.run(w1))
	print(sess.run(w2))
	print("tensor y:", y)
	print("y:", sess.run(y))


