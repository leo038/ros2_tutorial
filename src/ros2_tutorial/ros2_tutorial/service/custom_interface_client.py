import rclpy
from custom_interface.srv import MySum  # 使用自定义的消息类型
from rclpy.node import Node


class Client(Node):

    def __init__(self):
        super().__init__('minimal_client')
        self.client = self.create_client(MySum, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            print('service not available, waiting...')
        self.req = MySum.Request()

    def send_request(self):
        self.req.a = 41
        self.req.b = 1
        self.req.c = 3
        return self.client.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    client = Client()
    future = client.send_request()
    rclpy.spin_until_future_complete(client, future)
    # rclpy.spin(client)
    response = future.result()
    print(f"requset: a= {client.req.a}, b= {client.req.b}, c= {client.req.c},response: sum={response.sum}")

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
