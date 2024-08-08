import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class Client(Node):

    def __init__(self):
        super().__init__('minimal_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            print('service not available, waiting...')
        self.req = AddTwoInts.Request()

    def send_request(self):
        self.req.a = 41
        self.req.b = 1
        return self.client.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    client = Client()
    future = client.send_request()
    rclpy.spin_until_future_complete(client, future)
    # rclpy.spin(client)
    response = future.result()
    print(f"requset: a= {client.req.a}, b= {client.req.b}, response: sum={response.sum}")

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
