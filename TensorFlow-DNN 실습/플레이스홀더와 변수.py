import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

print(tf.__version__)   # 2.8.0
# 공식
    # H(x) = Wx + b

# X = 위 공식의 x 를 의미 ( placeholder ) 
# 실수형(float32) , 열은 3열 , 행은 정해지지 않음=입력할 때 결정(None)
X = tf.placeholder(tf.float32, [None, 3])
print(X)

# 2행 3열 ( 입력데이터 ) 
# 3행 , 10행 해도 상관없음 , 열은 3열로 고정
x_data = [[1,2,3,],[4,5,6]]

# W = 가중치 ( Variable )
# X가 3열이므로 W는 3행이여야 함 !! 
W = tf.Variable(tf.random_normal([3, 2]))
b = tf.Variable(tf.random_normal([2, 1]))

# X 와 W는 같은 행열이여야 함 ! 
# X와 W (행렬 곱) 한 후 + b 연산
expr = tf.matmul(X, W) + b

sess = tf.Session()

sess.run(tf.global_variables_initializer())

print("=== x_data ===")
print(x_data)
print("=== W ===")
print(sess.run(W))
print("=== b ===")
print(sess.run(b))
print("=== expr ===")

print(sess.run(expr, feed_dict={X: x_data}))

sess.close()

# W, b 는 TensorFlow가 담당하지만, X는 사용자가 입력값을 넣어야 함 ! 

