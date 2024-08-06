from setuptools import setup, find_packages

package_name = 'ros2_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),  # 注意这里一定要用find_packages(),否则不会打包子目录下的python文件
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pineai',
    maintainer_email='pineai@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "pub=ros2_tutorial.topic.publish:main",
            "sub=ros2_tutorial.topic.subscribe:main",
            "server=ros2_tutorial.service.server:main",
            "client=ros2_tutorial.service.client:main",
            "action_server=ros2_tutorial.action.server:main",
            "action_client=ros2_tutorial.action.client:main",
        ],
    },
)
