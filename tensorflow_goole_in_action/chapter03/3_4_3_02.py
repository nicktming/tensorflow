import tensorflow as tf 

w1 = tf.Variable(tf.random_normal((2,3), stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal((3,1), stddev=1, seed=1))

x = tf.placeholder(tf.float32, shape=(1,2), name="input")
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

c = [[0.7, 0.9]]

with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	print(sess.run(init_op))
	# print("x:", x)
	# print("tensor y:", y)
	print("y:", sess.run(y, feed_dict={x: c}))


