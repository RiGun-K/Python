from pickletools import optimizer
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

print(tf.__version__)

x_data = [1,2,3]
y_data = [1,2,3]

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

    # name: 나중에 텐서보드 등으로 값의 변화를 추적하거나 살펴보기 쉽게하기 위해 이름설정
X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")
print(X)
print(Y)

    # X 와 Y의 상관관계를 분석하기 위한 가설 수식을 작성합니다.
    # y = W * x + b
    # W와 X가 행렬이 아니므로 tf.matmul 이 아니라 기본 곱셈 기호를 사용
hypothesis = W * X + b

    # 손실 함수 작성
    # mean(h - Y)^2 : 예측값과 실제값의 거리를 비용(손실) 함수로 정한다.
cost = tf.reduce_mean(tf.square(hypothesis - Y))
    
    # 텐서플로우에 기본적으로 포함되어 있는 함수를 이용해 경사 하강법 최적화를 수행
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
    # 비용을 최소화 하는것이 최종 목표
train_op = optimizer.minimize(cost)

    # 세션을 생성하고 초기화 작업
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    # 최적화를 100번 수행
    for step in range(100):
        # sess.run 을 통해 train_op 와 cost 그래프를 계산
        # 이 때, 가설 수식에 넣어야 할 실제값을 feed_dict 을 통해 전달 
        _, cost_val = sess.run([train_op, cost], feed_dict={X: x_data, Y: y_data})
        
        print(step, cost_val, sess.run(W), sess.run(b))
        
    # 최적화가 완료된 모델에 테스트 값을 넣고 결과 확인 !
    print("\n=== Test ===")
    print("X: 5, Y: ", sess.run(hypothesis, feed_dict={X: 5}))
    print("X: 2.5 Y: ", sess.run(hypothesis, feed_dict={X: 2.5}))