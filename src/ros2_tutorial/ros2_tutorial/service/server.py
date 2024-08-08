import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts  # 使用系统自带的消息类型


class Service(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.service = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        print(f"收到请求，a:{request.a}, b:{request.b}")

        return response


def main(args=None):
    rclpy.init(args=args)
    service_node = Service()
    rclpy.spin(service_node)
    service_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
