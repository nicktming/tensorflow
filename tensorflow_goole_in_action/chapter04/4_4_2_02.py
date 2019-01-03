import tensorflow as tf 

def get_weight(shape, l):
	var = tf.Variable(tf.random_normal(shape), dtype=tf.float32)
	tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(l)(var))
	return var

x  = tf.placeholder(tf.float32, shape=(None, 2))
y_ = tf.placeholder(tf.float32, shape=(None, 1))

batch_size = 8

layer_dimension = [2, 10, 10, 10, 1]

n_layers = len(layer_dimension)

print(n_layers) 