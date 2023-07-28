import sys

def sort_file(filename):

  #open text file in read mode
  text_file = open(filename, "r")
   
  #read whole file to a string
  data = text_file.read()
   
  #close file
  text_file.close()
   
  thislist = data.replace("\n", "").split("$")

  thislist.sort()

  return thislist


def main():

  input_file_name = sys.argv[1]

  output_file_name = sys.argv[2]

  input_str = sort_file(input_file_name)

  output_file = open(output_file_name, "w")

  for L in input_str:
    if L:
      output_file.writelines(L) 
      output_file.writelines('\n\n')
    
  output_file.close()


if __name__ == '__main__':
  main()