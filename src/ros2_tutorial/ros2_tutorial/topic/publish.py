import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublishNode(Node):
    def __init__(self):
        super().__init__('publish_node')

        self.publisher = self.create_publisher(String, "publish_test", 10)  # 第一个参数是消息类型， 第二个参数是topic名字， 第三个是qos_profile

        self.timer = self.create_timer(1, self.timer_callback)  # 第一个参数是定时间隔， 第二个是回调函数

    def timer_callback(self):
        msg = String()
        msg.data = "Hello world!"
        self.publisher.publish(msg)
        print(f"publish msg: {msg.data}")


def main(args=None):
    rclpy.init(args=args)  ## 初始化

    ###########################################
    publish_node = PublishNode()
    rclpy.spin(publish_node)    ## 运行节点， 只有这一部分需要改变，其他的都是固定的
    ##########################################

    publish_node.destroy_node()   ##销毁节点
    rclpy.shutdown()  ##关闭节点


if __name__ == '__main__':
    main()
