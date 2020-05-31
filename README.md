## Next Destination

Python3 script that can: 
* Calculate distance between addresses by their coordinates(using a free Geo-Location API).
* Find the next closest destination using a linear algorithm(providing a current location starting point).
* Saves coordinates on the first request in a python dictionary, eliminating the need to keep sending requests to the API. 


### Big-O
#### Time-Complexity
* O n (provided a starting address)
* O n**2 (finding two closest locations from a list of addresses) 

#### Space-Complexity
* O n (python dictionary (hash-map) to save coordinates)

### Run the program on your computer

open a terminal in the downloaded program folder

```
pip3 install requirements.txt
```

```
python3 visit.py
```
