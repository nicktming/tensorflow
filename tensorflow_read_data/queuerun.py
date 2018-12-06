import tensorflow as tf

q = tf.FIFOQueue(10, "float")  
counter = tf.Variable(0.0)
increment_op = tf.assign_add(counter, 1.0)
enqueue_op = q.enqueue(counter)

qr = tf.train.QueueRunner(q, enqueue_ops=[increment_op, enqueue_op])
 
with tf.Session() as sess:  
    sess.run(tf.initialize_all_variables())  
    enqueue_threads = qr.create_threads(sess, start=True)  
    for i in range(10):              
        # print (sess.run(q.dequeue())) 
        print (sess.run(increment_op))
