from tensorflow.examples.tutorials.mnist import input_data

print("starting test.")

mnist = input_data.read_data_sets("/Users/tingzhangming/Documents/work/data/MNIST_data/", one_hot=True)

batch_size = 100

xs, ys = mnist.train.next_batch(batch_size)

print "X shape:", xs.shape

print "Y shape:", ys.shape

