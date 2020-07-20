# find built in modules

import sys
import textwrap

module_name = ', '.join(sorted(sys.builtin_module_names))
print(module_name)
print(textwrap.fill(module_name, width=70))

help(textwrap)