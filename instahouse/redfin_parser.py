# redfin_parser.py
 
"""
Two simple code to read the primary information from redfin
<td class="property_detail_label left_column">$/Sq. Ft.:</td>
<td class="property_detail_value right_column"> $216     </td>
<h1 class="adr">
        <span id="address_line_1" class="street-address"> 5160 N 1ST St </span>
        <span id="address_line_2">
        <span class="locality"> San Jose</span>,
        <span class="region">CA</span>
        <span class="postal-code">95002</span>
 
"""
import urllib2
import BeautifulSoup
import pprint
 
def read_refinpage(urlStr):
    fileHandle = urllib2.urlopen(urlStr)
    page = fileHandle.read()
 
    adict={}
    adict['URL'] = urlStr
 
    start = 0
    count = 0
    class_pattern = '<td class="property_detail_label left_column">'
    value_pattern = '<td class="property_detail_value right_column">'
 
    while (start < len(page)) and (count<15):
        inx1_a = page.find(class_pattern, start)
        if inx1_a == -1:
            break
        inx1_b = page.find('</td>', inx1_a)
        subj = page[inx1_a+len(class_pattern):inx1_b]
        subj = subj.replace(":", "")
        subj = subj.strip()
 
        inx2_a = page.find(value_pattern, inx1_b)
        inx2_b= page.find('</td>', inx2_a)
        value_temp = page[inx2_a+len(value_pattern):inx2_b]
 
        value = value_temp.replace('\t',"").replace('\n',"").strip()
 
        start = inx2_b
        if "County" in subj:
            pass
        else:
            adict[subj] = value
            count+=1
 
    pprint.pprint(adict)
    print("\n\n")
    return adict
 
def beat_read_refin(urlStr):
    fileHandle = urllib2.urlopen(urlStr)
    page = fileHandle.read()
    soup = BeautifulSoup.BeautifulSoup(page)
 
    adict={}
    adict['URL'] = urlStr
 
    adict['Address'] = str(soup.findAll('span', {"class": "street-address"})[0].contents[0].strip())
    adict['Locality'] = str(soup.findAll('span', {"class": "locality"})[0].contents[0].strip())
    adict['Region'] = str(soup.findAll('span', {"class": "region"})[0].contents[0].strip())
    adict['Zip'] = str(soup.findAll('span', {"class": "postal-code"})[0].contents[0].strip())

    # now get mls number, etc
    # table = soup.find('table', id="property_basic_details")
    # rows = table.findAll('tr')
    # for tr in rows:
    #     subj = tr.findAll('td', {"class":"property_detail_label left_column"})[0].find(text=True)
    #     subj = subj.replace(":", "").strip()
    #     value = tr.findAll('td', {"class":"property_detail_value right_column"})[0].find(text=True)
    #     value = value.replace('\t',"").replace('\n',"").strip()
    #     if "County" in subj:
    #         pass
    #     else:
    #         adict[str(subj)] = str(value)
 
    pprint.pprint(adict)
    print("\n\n")
    return adict
 
if __name__=="__main__":
    urllist = ['https://www.redfin.com/WA/Bellevue/12600-SE-7th-Pl-98005/home/507266']
 
    result_list=[None]*len(urllist)
    for i, url in enumerate(urllist):
        result_list[i] = beat_read_refin(url)
 
    result_list2=[]
    for url in urllist:
        result_list2.append(read_refinpage(url))
        print("\n\n")
 
    ofile  = open('housing_result.txt', "wb")
    for res in result_list:
        for k, v in res.items():
            row = k + "\t" + v + "\n"
            ofile.write(row)
        ofile.write("\n\n")
 
    ofile.close()