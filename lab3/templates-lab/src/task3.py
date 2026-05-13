from jinja2 import Environment, FileSystemLoader

# Set up Jinja environment
ENV = Environment(loader=FileSystemLoader('.'))

# Load template
template = ENV.get_template("template-task3.j2")


# Create interface class
class NetworkInterface(object):

    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink


# Create object
interface_obj = NetworkInterface(
    "GigabitEthernet0/1",
    "Server Port",
    10
)

# Render template
print(template.render(interface=interface_obj))
