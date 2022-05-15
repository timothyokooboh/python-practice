#!/usr/bin/env python3

import re

result = re.search(r'[l]?ove', 'i love the lord very much.', re.IGNORECASE)
print(result)