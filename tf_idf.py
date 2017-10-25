import sys
import re, os
import glob
import math 


def idf_word_global(word,file_list):
  count = 0
  for file in file_list:
    if word in file.split():
      count += 1
  return count
  
def idf_final(word, file_list):
  lenList = len(file_list)
  numCount = idf_word_global(word, file_list)
  return math.log(lenList/1+numCount)

def tf_doc(word):
  
  if "word" in tf_local:
    tf_local["word"] += 1
  else:
    tf_local["word"] = 1 



def main():

  idf_global = dict()
  tf_global = []
  doc_list = []
  tf_idf = dict()
  index = 0
  path = 'p2_data/*.txt'
  list_of_files = glob.glob(path)           # create the list of file

  for file_name in list_of_files:
    FI = open(file_name, 'r')
    index += 1
    tf_local = dict()
    idf_local = dict()
    for line in FI:
      dataOld = line.strip()
      words = re.sub(r'[^a-zA-Z0-9]', " ",dataOld).split()
      for word in words: 
        if word in tf_local:
          tf_local[word] += 1
        else:
          tf_local[word] = 1
        idf_local[word] = idf_final(word, list_of_files)

   
     #   for key, value in tf_local.iteritems():
     #     if key in idf_global:
     #       tf_idf[key] = int(tf_local[key]) * int(idf_local[key])

    
        
    tf_global.append(tf_doc)
     
    output = open('output{0}.txt'.format(index), 'w')
    for key, value in tf_local.items():
      #print '{0}\t{1}'.format(key, value)      
      output.write("%s\t"%key)
      output.write("%s\t"%value)
      if key in idf_local:
        x = int(tf_local[key]) * float(idf_local[key])
        output.write("%s\n"%x)
    output.close()
  
if __name__ == "__main__":
    main()
