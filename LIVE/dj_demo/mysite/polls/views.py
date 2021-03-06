from django.shortcuts import render
import cloud_code_search

# Create your views here.

from django.http import HttpResponse

def index(request):
  search_terms = request.GET.get('search', '')
  result_list = cloud_code_search.cloud_code_search(search_terms)
  #Test
  html_insert = ""
  '''
  <div class=SEARCH_RESULT>
      <div class=SEARCH_RESULT_TITLE>
          Return_Spliced_List_From_String() 
          <a href="http://stackoverflow.com/questions/796087/make-a-div-into-a-link"><span></span></a>
      </div>
      <div class=SEARCH_RESULT_DESC>
          Description of the code above
      </div>
  </div>
  '''
  for item in result_list:
    html_insert += "<div class=SEARCH_RESULT><div class=SEARCH_RESULT_TITLE>"
    html_insert += item[0]
    html_insert += '<a href="http://stackoverflow.com/questions/796087/make-a-div-into-a-link"><span></span></a></div><div class=SEARCH_RESULT_DESC>'
    html_insert += item[1]
    html_insert += "</div></div>"

  html_insert = html_insert.replace('\n', '<br>')
  
  HTML_RESPONSE = """<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Cloud Code</title>
    <meta name="description" content="A website searching code.">
    <link rel="stylesheet" href="static/request.css">
</head>

<body>
    <div class=FULL_WINDOW>
        <div class=FIVE_SPACER>

        </div>
        <div class=SEARCH_SECTION>
            <div class=TITLE2>
                <div style="margin-left:50px;">
                    Cloud-Code
                </div>


            </div>
            <div class=SEARCH>
                <div class=VER_SERACH>
                    <form action="response.html">
                        <input type="search" style="width: 250px;" name="search">
                        <input type="submit" value="Go">
                    </form>
                </div>
            </div>
        </div>

        <div class=GREY_LINE>
        
        </div>
        
        <div class=BOT_SPACER>
        </div>
        """ + html_insert + """
    </div>
</body>

</html>"""
  return HttpResponse(HTML_RESPONSE)
