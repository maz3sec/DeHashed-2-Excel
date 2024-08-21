DeHashed-2-XLSX

DeHashed-2-Excel

--------------
by: maz3sec

* Reformats raw Dehashed JSON data to Excel (XLSX) *


Example Usage

- Retrieve Data From DeHashed in a JSON format

      curl 'https://api.dehashed.com/search?query=email:"$DOMAIN"&size=$RECORDS' -u '$EMAIL:$DEHASHED-API-KEY' -H 'Accept: application/json' -o "dehashed.json"

- Reformat DeHashed JSON data to Excel

      python3 dehashed-2-xlsx.py -i dehashed.json -o dehashed.xlsx
