import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of COurse Reviews", classes="text-h3 text-center p-pa-md")
    p1 = jp.QDiv(a=wp, text="These Graphs Represent Course Review Analysis")

    return wp

jp.justpy(app)