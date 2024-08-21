DeHashed-2-Excel
--------------
by: maz3sec

* Reformats raw Dehashed JSON data to Excel (XLSX) *


Example Usage

- DeHashed API call to retrieve data in JSON format

      curl 'https://api.dehashed.com/search?query=email:"$DOMAIN"&size=$RESULTS' -u '$EMAIL:$DEHASHED-API-KEY' -H 'Accept: application/json' -o "dehashed.json"

- Reformat DeHashed JSON data to Excel (XLSX) format

      python3 dehashed-2-excel.py -i dehashed.json -o dehashed.xlsx
