class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # fout = open('output.html', 'w')
        # fout.write("<html><head><title>爬虫结果</title></head>")
        # fout.write("<body><table>")
        # for data in self.datas:
        #     fout.write("<tr>")
        #     fout.write("<td>"+data['title'].encode('utf-8')+"</td>")
        #     fout.write("<td>" + data['summary'].encode('utf-8') + "</td>")
        #     fout.write("<td>" + data['url'] + "</td>")
        #     fout.write("</tr>")
        #
        # fout.write("</talbe></body>")
        # fout.write("</html>")
        #
        # fout.close()
        for data in self.datas:
            print(data['title']+data['summary']+'/n')

