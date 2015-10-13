import os
import re

def generate_htmlstring(title, concept):
    string = '''<div class="concept">
    <h3 class="''' + ''.join(title.lower().split()) + '''>''' + title + '''</h3>
    <p>
        ''' + concept + '''
    </p>
</div>'''
    return string