# README: Data preprocessed by spliting into 250 rows

This script reads multiple CSV files from a specified input folder, splits each file into smaller CSV files with 250 rows each, and saves them in separate numbered folders. Any remaining rows that do not form a full chunk of 250 rows are discarded.


## Output Structure
After execution, the output folder will contain subfolders for each CSV file, named in a sequential format:
```
/output
│── 001_filename/
│   │── 001_filename_part_001.csv
│   │── 001_filename_part_002.csv
│   └── ...
│── 002_anotherfile/
│   │── 002_anotherfile_part_001.csv
│   │── 002_anotherfile_part_002.csv
│   └── ...
```

