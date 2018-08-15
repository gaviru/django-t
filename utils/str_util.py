
class StrUtil():
    def strTohtml(text):
        text = text.replace("&", "&amp;")
        text = text.replace("#", "&#35;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        text = text.replace("%", "&#37;")
        text = text.replace("\"", "&quot;")
        text = text.replace("'", "&#39;")
        text = text.replace(" ", "&nbsp;")
        text = text.replace("\n", "<br>")
        return  text

    def htmlTostr(text):
        text = text.replace("&lt;", "<")
        text = text.replace("&gt;", ">")
        text = text.replace("&amp;", "&")
        text = text.replace("&#37", "%")
        text = text.replace("&quot;", "\"")
        text = text.replace("&#39", "'")
        text = text.replace("&#35", "#")
        text = text.replace("<br>", "\n")
        text = text.replace(" ", "&nbsp;")
        return text