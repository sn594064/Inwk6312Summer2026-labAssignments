from jinja2 import Environment, FileSystemLoader

# Set up the Jinja environment
ENV = Environment(loader=FileSystemLoader('.'))

# Load the template
template = ENV.get_template("template-task2.j2")


# Create a Python class
class NetworkInterface(object):

    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink


# Create an interface object
interface_obj = NetworkInterface(
    "GigabitEthernet0/1",
    "Server Port",
    10
)

# Render the template
print(template.render(interface=interface_obj))
