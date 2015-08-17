media_location = "media/"
css_location = "css/"
charset = "UTF-8"
title_of_page = 'Learning at Udacity'
css_name = 'style.css'
pagediv = {
    'id' : 'page'
}

h2_headings = [
{'id':'aboutme', 'class':'side', 'heading': 'About me', 'linkname': 'img0'},
{'id':'basicsofweb', 'class':'side', 'heading': '1. Basics of Web', 'linkname': 'web'},
{'id':'html', 'class':'side', 'heading': '2. HTML', 'linkname': 'HTML'},
{'id':'css', 'class':'side', 'heading': '3. CSS', 'linkname': 'CSS'},
{'id':'best', 'class':'side', 'heading': 'Best Practices', 'linkname': 'TIPS'},
]

images = {
'img0': {'id':'side', 'class':'pic', 'alt':'kranthi', 'src': media_location + 'images/Kranthi.jpg'}
}

page_lists = {
    'list1': {'listclass': 'none', 'itemclass': 'boxed'}
}

def generate_header(title, cssname):
    title_string = '<title>' + title +'</title>'
    css_string = '<link rel=stylesheet href=' + css_location + cssname + '>'
    encoding_string = '<meta charset="' + charset + '">'
    final_string = '''    <head>
        ''' + title_string + '''
        ''' + css_string + '''
        ''' + encoding_string + '''
    </head>'''

    return final_string

def generate_body(body_data):
    body = '''    <body>''' + '''
        ''' + body_data + '''
    </body>'''
    return body

def generate_html(title, cssname, body):
    header = generate_header(title, cssname)
    html = '''<!DOCTYPE HTML>
<html> 
''' + header + '''
''' + body + '''
</html>'''
    return html

def generate_html_list(ordered, list_class, list_items):
    '''
    Generates List from the data provided
    '''
    content = ''
    html_list = ''
    for item in list_items:
        content += '''
        <li class="''' + list_class['itemclass'] + '>' + item + '</li>' 

    if ordered:
        '''
        Ordered List
        '''
        html_list += '<ol class="' + list_class['listclass'] + '>' + content + '''
    </ol>'''
    else:
        '''
        Unordered List
        '''
        html_list += '<ul class="' + list_class['listclass'] + '>' + content + '''
    </ul>'''
    return html_list

def generate_link(hrefs_texts_class):
    '''
    Generates links
    '''
    links_list = []
    for key in hrefs_texts_class:
        lname = str(key['linkname'])
        if key['linkname'].startswith('img') or key['linkname'].find('img') == 0:
            lname = generate_other_html_elements('img', images['img0'] , False)
        string = '<a href="#' + key['id'] + '" class="' + key['class'] + '">' + lname + '</a>'
        links_list.append(string)
    return links_list

def generate_div(class_id_content, content):
    '''
    Generates Div blocks
    '''
    div_block = '''<div id=''' + class_id_content['id'] + '''>
            ''' + content + '''
        </div>'''
    return div_block



def generate_headings(heading_type, heading, id_class):
    '''
    Generates headings and sub-heading with necessary
    classes and ids
    '''

def generate_other_html_elements(tag_name, id_class, closetag, content=None):
    '''
    Generates other html elements
    '''
    element = '''<''' + tag_name
    for k in id_class.keys():
        element += " " + k + '="' + id_class[k] + '"'
    if closetag:
        if content is not None:
            element += '>' + '''
    ''' + content + '''
<''' + tag_name + '>'
        else:
            element += '>' + '<' + tag_name + '>'
    else:
        element += '>'
    return element


links_to_sections = generate_link(h2_headings)
nav_list = generate_html_list(False, page_lists['list1'], links_to_sections)
div = generate_div(pagediv, generate_other_html_elements('nav', {'class': 'sidebar'}, True, nav_list))
body = generate_body(div)
print generate_html(title_of_page, css_name, body)