import re
from builder.Pars import Pars


class Builder:

    def __init__(self, template, parameters, script):
        self.template_file_name = template
        self.parameters_file_name = parameters
        self.script_file_name = script

    def build(self):

        parameters_file = open(self.parameters_file_name, 'r', encoding='utf-8')
        script_file = open(self.script_file_name, 'w', encoding='utf-8')
        parameters_names_list = parameters_file.readline().split(';')
        pars = Pars(parameters_names_list)
        for parameters_line in parameters_file:
            parameters_line_list = parameters_line.split(';')
            pars.add_items(parameters_line_list)
            template_file = open(self.template_file_name, 'r', encoding='utf-8')
            for template_line in template_file:
                if template_line != '\n':
                    regex = r"{[a-zA-Z0-9_$#@!%^&*()-+=\\\/.,`'|]+}"
                    parameters_template = re.findall(regex, template_line)
                    for item in parameters_template:
                        if item[1:-1] in pars.pars:
                            template_line = template_line.format(**pars.pars)
                            script_file.write(template_line)
                else:
                    script_file.write(template_line)
            template_file.close()
            script_file.write('\n')
        script_file.close()
        parameters_file.close()


