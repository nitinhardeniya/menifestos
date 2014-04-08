import sys
import re
import nltk
from collections import Counter
from nltk.corpus import stopwords

#from pytagcloud import create_tag_image, make_tags
#from pytagcloud.lang.counter import get_tag_counts

def clean_txt(s):
    #print s
    #print '*'*50
    cleanhtml=nltk.clean_html(str(s))

    #print "cleanhtml"
    #print cleanhtml
    clean=re.findall('[a-zA-Z]+',str(cleanhtml))
    #print "clean-word_only"
    print clean
    #print 
    clean_small=[x.lower() for x in clean if len(x)>2]
    print clean_small
    filtered = [w for w in clean_small if not w in stopwords.words('english')]

    print filtered

    
    #print "final sent"
    #print ' '.join(filtered)

    return ' '.join(filtered)

def read_csv(file_path,has_header = False):
    data = ' '
    fo=open(sys.argv[2],'w')
    with open(file_path,'rU') as f:
        if has_header: print f.readline()
        
        for line in f:
            alltxt= clean_txt(line)
            data=data+alltxt
    #tags = make_tags(get_tag_counts(data), maxsize=120)
    #create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')
    fo.write(data)
    #tokens = nltk.word_tokenize(data)
    #count = Counter(tokens)
    #print count.most_common(100)


def main():
    infile=sys.argv[1]
    read_csv(infile)

if __name__ == '__main__':
	main()