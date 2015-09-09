import webbrowser
import os
import string

CSSPATH = os.path.join(os.path.dirname(__file__), "css")
CSS = os.path.join(os.path.join(CSSPATH, "style.css"))

def launch_website(list_of_movies):
    '''
    function to launch website
    '''
    types = []
    videos_by_type = {}
    htmls = {}
    for each in list_of_movies:
        if each.type not in types:
            types.append(each.type)
            videos_by_type[each.type] = []
        videos_by_type[each.type].append(each)
    nav = gen_nav(types)
    body = gen_body(nav, videos_by_type, "home")
    htmls['home'] = gen_website_html("Video Gallery Home", body)
    for each in types:
        htmls[each] = gen_website_html("Video Gallery " + each, 
                                       gen_body(nav, videos_by_type, each))

    webbrowser.open(htmls['home'])

def gen_website_html(title, body):
    '''
    Generate a HTML Page
    '''
    html = '''<!DOCTYPE HTML>
<html>
''' + gen_title(title) + '''
''' + body + '''
</html>'''
    
    html_file = os.path.join(os.path.dirname(__file__),
                             title.replace(" ", "_").lower() + ".html")
    website = open(html_file, "w")
    website.write(html)
    website.close()
    return html_file

def gen_relative_path(path):
    '''
    Generates relative path from cwd
    '''
    html_loc = os.path.dirname(__file__)
    if html_loc == path:
        return path
    return path.split(html_loc + "\\")[1].replace("\\", "/")

def gen_title(title):
    '''
    Generate header section of the page
    '''
    if not os.path.exists(CSSPATH):
        os.makedirs(CSSPATH)
    if not os.path.isfile(CSS):
        css = open(CSS, "w")
        css.close()

    title = '''<head>
    <meta charset="utf-8">
    <title>''' + title + '''</title>
    <link rel=stylesheet href=''' + gen_relative_path(CSS) + '''>
</head>'''

    return title

def gen_body(pre_generated, video_objects, page):
    '''
    Generates actual body of the page
    '''
    dynamic_body = ''
    if page == "home":
        dynamic_body += '''<div class="tagline">A Great Collection of Videos</div>
    <div class=slideshow>
    '''
        for each in video_objects.keys():
            for vid in video_objects[each]:
                cssid = ''.join([i for i in vid.title.lower() if i in string.ascii_lowercase])
                href = "video_gallery_" + each.lower() + ".html#" + cssid
                dynamic_body += '''    <figure><a href="''' + href + '''"><img src="''' + vid.poster + '''"></a></figure>
    '''
        dynamic_body += '''</div>
    '''
    elif page.lower() in ["movie", "tvseries"]:
        dynamic_body += '''<div class="gallery">
    '''
        for each in video_objects.keys():
            if each == page:
                for vid in video_objects[each]:
                    dynamic_body += '''    <div class="video">
            <img src="''' + vid.poster + '''">
            <table class="content">
                <tr><td><b>Title</b></td><td>: ''' + vid.title + '''</td></tr>
                '''
                    if page.lower() == "movie":
                        dynamic_body += '''<tr><td><b>Release Date</b></td><td>: ''' + vid.release_date + '''</td></tr>
                <tr><td class="storyline"><b>Story Line</b></td><td>: ''' + vid.storyline + '''</td></tr>
                '''
                    elif page.lower() == "tvseries":
                        dynamic_body += '''<tr><td><b>Series Start Date</b></td><td>: ''' + vid.start_date + '''</td></tr>
                <tr><td><b>Series End Date</b></td><td>: ''' + vid.end_date + '''</td></tr>
                <tr><td><b>Seasons</b></td><td>: ''' + vid.seasons + '''</td></tr>
                <tr><td><b>Episodes</b></td><td>: ''' + vid.episodes + '''</td></tr>
                <tr><td class="storyline"><b>Plot</b></td><td>: ''' + vid.plot + '''</td></tr>
                '''
                    dynamic_body += '''<tr><td><b>Duration</b></td><td>: ''' + vid.duration + '''</td></tr>
            </table>
        </div>
    '''
        dynamic_body += '''</div>'''

    body = '''<body>
    ''' + pre_generated + '''
    ''' + dynamic_body + '''
</body>'''
    return body

def gen_nav(types):
    '''
    generates navigation header bar
    '''
    list_of_items = '''<nav>
        <ul>
            <li><a href="video_gallery_home.html">Home</a></li>'''
    for each in types:
        list_of_items += '''
            <li><a href="video_gallery_''' + each.lower() + '''.html">''' + each + '''</a></li>'''
    list_of_items += '''
        </ul>
    </nav>'''
    return list_of_items