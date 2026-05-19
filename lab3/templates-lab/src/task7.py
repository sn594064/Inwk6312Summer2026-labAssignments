from jinja2 import Environment, FileSystemLoader
import yaml

# Set up Jinja environment
ENV = Environment(loader=FileSystemLoader('.'))

# Load template
template = ENV.get_template("template-task6.j2")

# Load YAML data
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)

# Render template
print(template.render(interface_list=interfaces))
