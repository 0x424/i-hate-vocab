import xlrd
import difflib

print("locating files..")
f1=xlrd.open_workbook("/Users/steve/Desktop/test_file.xlsx")
f1s=f1.sheet_by_index(0)
f2=xlrd.open_workbook("/Users/steve/Desktop/file2.xlsx")
f2s=f2.sheet_by_index(0)

for i in range(0, 30):
     print(f"\n\nYou are on question < {i+1} >\n")
     for j in range(0, 199):
          find = f1s.col_values(3)[i+4]
          if f2s.col_values(1)[j] == find:
               print(f"Exact match found: {f2s.col_values(0)[j]}")
          elif difflib.get_close_matches(find, f2s.col_values(1)[j], n=2) != []:
               print(f"Close match found: {f2s.col_values(0)[j]}")
