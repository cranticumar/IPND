import os
import re

def generate_htmlstring(title, concept):
    string = '''<div class="concept">
    <h3>''' + title + '''</h3>
    <p>
        ''' + concept + '''
    </p>
</div>'''
    return string