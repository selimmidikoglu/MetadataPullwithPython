#-------Selim Mıdıkoğlu 31.01.2018---------#
#Pulling metadata of radio broadcast using urrlib2 for sending Get request to the url and getting response from it


import urllib.request
import contextlib

#declaring the body of GET request
req = urllib.request.Request("http://192.99.41.102:5032/stream", headers={
    'User-Agent': 'User-Agent: VLC/2.0.5 LibVLC/2.0.5',
    'Icy-MetaData': '1'})
#sending the request here and taking the response
res = urllib.request.urlopen(req)
#taking the information about the metadata related interval
rangeofbytes = res.getheader('Icy-metaint')


#closing the res HttpRequest Object after with
with contextlib.closing(res) as response:

  countBytes = 0
  index1 = 0 #to keep the starting index of StreamTitle....


  while True:
       line = response.readline()
       countBytes += len(line)

       if b'StreamTitle' in line:

           index1 = line.index(b'StreamTitle')
           index2 = line.index(b';',index1)#index of ';'
           song = line[index1+13:index2-1].decode('utf-8')
           metadatalen = index2-index1+13
           countBytes -= metadatalen

       if countBytes >= int(rangeofbytes):
           break

file = open('song.txt', 'w')
file.write(song)
file.close()