from os import listdir, path

source = "C:/Users/chall/Google Drive/pineapple999.org/mysite/pineapple999.net/static/problem_resources"

CODEBLOCK = "```"

START_TERMS = ["challenge", "task", "step"]




for folder in listdir(source):
     

     if not path.isdir(source+"/"+folder):   continue

     if "instructions.md" in listdir(source+"/"+folder):

          subheading_syntax = "## "

          new_path = source+"/"+folder+"/instructions.md"

          code_block_open = False

          count = 0

          with open(folder + "_instructions.md", "w", encoding="utf8") as new_f:
               with open(new_path, encoding="utf8") as orig_f:
                    lines = orig_f.readlines()

                    for i, line in enumerate(lines):

                         if line.startswith(CODEBLOCK) and not code_block_open:
                              line = line[3:]
                              code_block_open = True
                              count += 1
                         if code_block_open:
                              line = "\t" + line
                         if line.strip().endswith(CODEBLOCK) and code_block_open:
                              code_block_open = False
                              line = line.replace(CODEBLOCK, "")

                         prev_line = lines[i-1].strip()
                         try:
                              next_line = lines[i+1].strip()
                         except IndexError:
                              next_line = None

                         skip_line = False

                         if line.strip() == "":

                              skip_line = True

                              for check_line in [prev_line, next_line]:

                                   if check_line is not None and len(check_line):
                                        
                                        if "------" in check_line:
                                             skip_line = False
                                        elif check_line.startswith("**"):
                                             skip_line = False
                                        elif "\\." in check_line[:5]:
                                             skip_line = False
                                        elif check_line[0] == "#":
                                             skip_line = False
                                        elif len(check_line) > 100:
                                             skip_line = False

                         if len(line) < 15 and "section" in line.lower():
                              line = subheading_syntax + line
                              subheading_syntax = "### "

                         elif line.strip().startswith("**") and (any(w in line.lower() for w in START_TERMS) or len(line) > 10):
                              line = subheading_syntax + line
                         elif any(line.lower().startswith(w) for w in START_TERMS):
                              line = subheading_syntax + line
                         else:
                              if i > 10:
                                   if line.strip().startswith("##"):
                                        line = line.replace("##", "**")
                                        line = line.strip() + "**\n"
                                   elif line.startswith("#"):
                                        line = line.replace("#", "**")
                                        line += "**"
                                   
                              
                         if not skip_line:
                              new_f.write(line)

          print(f"Finished writing {folder}_instructions.md")
          print(f"{count} code blocks modified")

                    
