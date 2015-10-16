#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re,sys,codecs

out1 = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
    <script>
        function filter_it() {
            var keyword = document.getElementById("keyword").value;
            var patt1=new RegExp(keyword);
            labels = document.getElementsByTagName("label");
            for (var i=0;i<labels.length;i++) {
                content = labels[i].innerText;
                if (!patt1.test(content)) {
                    labels[i].style.display = "none";
                } else {
                    labels[i].style.display = "block";
                }
            }
        }
    </script>
    <style>
        body{
        background-color:#C7EDCC;
        }
        label{
        font-size: 15px;
        line-height: 22px;
        }
        .line_V {
        display:block;
        color:#676262;
        }
        .line_D {
        display:block;
        color:#0070BB;
        }
        .line_I {
        display:block;
        color:#48BB31;
        }
        .line_W {
        display:block;
        color:#BBBB23;
        }
        .line_E {
        display:block;
        color:#FF0006;

        }
        .line_A {
        display:block;
        color:#8F0005;
        }
    </style>
</head>
<body>
please input keywords<input id="keyword" style="width:500px"><input type="button" onclick="filter_it();" value="filter">
<div>"""
out2 = """
</div>
</body>
</html>
"""

id_index = 0
divContent=""
pattern = re.compile(
    r'[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{3}\s([DWIVE])[\s\S]*')
with codecs.open("log.html","w", 'utf-8') as h5:
    h5.write(out1)
    h5.write("<label>")
    with codecs.open("log.txt","r", 'utf-8') as f:
        for line in f:
            match = pattern.match(line)
            line = line.replace(' ', '&nbsp;').replace('\n', '<br/>')
            if match:
                type = match.group(1)
                if type == 'I':
                    divContent = "</label><label class=\"line_I\" id='index_"+str(id_index)+"'>" + line.replace('\t',"&nbsp;&nbsp;&nbsp;&nbsp;")
                elif type == 'D':
                    divContent = "</label><label class=\"line_D\" id='index_"+str(id_index)+"'>" + line.replace('\t',"&nbsp;&nbsp;&nbsp;&nbsp;")
                elif type == 'V':
                    divContent = "</label><label class=\"line_V\" id='index_"+str(id_index)+"'>" + line.replace('\t',"&nbsp;&nbsp;&nbsp;&nbsp;")
                elif type == 'W':
                    divContent = "</label><label class=\"line_W\" id='index_"+str(id_index)+"'>" + line.replace('\t',"&nbsp;&nbsp;&nbsp;&nbsp;")
                elif type == 'E':
                    divContent = "</label><label class=\"line_E\" id='index_"+str(id_index)+"'>" + line.replace('\t',"&nbsp;&nbsp;&nbsp;&nbsp;")
            else:
                divContent = line.replace('\t',"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
            h5.write(divContent)
            id_index+=1
    h5.write("</label>")
    h5.write(out2)
