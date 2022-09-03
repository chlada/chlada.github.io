def write_body ():
    file = "seite11.html"

    for i in range (12,40):
        name = 'seite' + str (i) + '.html'
    
        da = open (file, 'r')
        lines = da.readlines ()
        da.close ()

        for line in lines:
            if 'Chlada - Katalog, Seite' in line:
                lines [lines.index(line)] = '\t\t<title>Chlada - Katalog, Seite ' + str (i) + '</title>\n'
            if '''class="prev"''' in line:
                lines [lines.index(line)] = '''\t\t\t<li><a href="seite''' + str (i-1) + '''.html" class="prev">&lt; Seite ''' + str (i-1) + '''</a></li>\n'''
            if '''class="here"''' in line:
                lines [lines.index(line)] = '''\t\t\t<li class="here">Seite ''' + str (i) + '''</li>\n'''
            if '''class="next"''' in line:
                lines [lines.index(line)] = '''\t\t\t<li><a href="seite''' + str (i+1) + '''.html" class="next">Seite ''' + str (i+1) + ''' &gt;</a></li>\n'''
        
        print (name)
        f = open (name, 'w')
        f.writelines (lines)
        f.close ()

write_body ()
