import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubscribeNode(Node):
    def __init__(self):
        super().__init__('subscribe_node')

        self.subscriber = self.create_subscription(String, "publish_test", self.sub_callback,
                                                   10)  # 第一个参数是消息类型， 第二个参数是topic名字， 第三个参数是回调函数， 第四个是qos_profile

    def sub_callback(self, msg):
        print(f"subscribe msg， {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    subs_node = SubscribeNode()
    rclpy.spin(subs_node)


    subs_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
