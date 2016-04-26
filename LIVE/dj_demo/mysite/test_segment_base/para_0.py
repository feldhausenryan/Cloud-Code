### this should be moved into rml2pdf
def EmbedInRml2pdf():
    "make the para the default para implementation in rml2pdf"
    from rlextra.rml2pdf.rml2pdf import MapNode, Controller # may not need to use superclass?
    global paraMapper, theParaMapper, ulMapper
    class paraMapper(MapNode):
        #stylename = "para.defaultStyle"
        def translate(self, nodetuple, controller, context, overrides):
            (tagname, attdict, content, extra) = nodetuple
            stylename = tagname+".defaultStyle"
            stylename = attdict.get("style", stylename)
            style = context[stylename]
            mystyle = SimpleStyle(name="rml2pdf internal style", parent=style)
            mystyle.addAttributes(attdict)
            bulletText = attdict.get("bulletText", None)
            # can we use the fast implementation?
            import types
            result = None
            if not bulletText and len(content)==1:
                text = content[0]
                if type(text) in (StringType, UnicodeType) and "&" not in text:
                    result = FastPara(mystyle, text)
            if result is None:
                result = Para(mystyle, content, context=context, bulletText=bulletText) # possible ref loop on context, break later
            return result
    theParaMapper = paraMapper()
    class ulMapper(MapNode):
        # wrap in a default para and let the para do it
        def translate(self, nodetuple, controller, context, overrides):
            thepara = ("para", {}, [nodetuple], None)
            return theParaMapper.translate(thepara, controller, context, overrides)
    # override rml2pdf interpreters (should be moved to rml2pdf)
    theListMapper = ulMapper()
    Controller["ul"] = theListMapper
    Controller["ol"] = theListMapper
    Controller["dl"] = theListMapper
    Controller["para"] = theParaMapper
    Controller["h1"] = theParaMapper
    Controller["h2"] = theParaMapper
    Controller["h3"] = theParaMapper
    Controller["title"] = theParaMapper
