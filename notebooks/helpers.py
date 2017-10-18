# helper to display Pandas Table output side by side

from IPython.display import display_html

def highlight(data):
    return ['background-color: yellow' for x in data]

def display_side_by_side(subset, *args):
    html_str=''
    for i, df in enumerate(args):
        if i:
            html_str+=df.style.render()
        else:
            df.style.apply(highlight, subset)
            html_str+=df.style.render()
            
    display_html(html_str.replace('table','table style="display:inline"'),raw=True)
    

