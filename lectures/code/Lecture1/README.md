# Lecture 1 - bash commands :computer:

This lecture note contains some basic bash commands and some basic bash scripting. You can use this as base, but need to study on by yourself in the resources given and also do the exercises provided.

---
## Navigation :compass:

Where am I? How do I jump out to see my parents and then back in? 

```bash
pwd # print working directory
cd ..
cd <directory_name>
```

Okay, let's a directory called Lec0_bash using mkdir short for (make directory). Now change to this directory, aha cd stands for change directory. 

```bash
mkdir Lec0_bash
cd Lec0_bash
```

When working data engineering or data science it is nice to have a data directory, so we'll create it. Also we'll check the airquality in Göteborg in this lecture so we also create the subdirectory called **airquality**. 

```bash 
# cool that we can create subdirectory from the parent perspective 
mkdir data/airquality 
```

---
## Take a look at the manual 

Ahh what if I am on an interview or for other reason don't have access to an LLM such as ChatGPT, how should I know all these commands?? 

Check the manual, the old fashion way

```bash
man ls
man cd
man mkdir 
man <command>
```

---
## Print and format date :date:

Sometimes we want to make a joke and echo :rofl: it to the shell: "Hey siri, call a cab.
Siri says: Hello cab".

```bash
echo "Hey siri, call a cab.\nSiri says: Hello cab"
```

With this high quality joke we must record in our journal when we said it. Thus we will start with editing dates.

```bash
# todays date default formatting
date
# todays date: YYYY-MM-DD
date +%Y-%m-%d
# todays date: YY/MM/DD HH:MM
date "+%y/%m/%d %H:%M"
```

To write this, we will use something that varies (such as the value of US dollars value :dollar:), a variable

```bash
# Joke 2023-05-14 17:52
# Hey siri, call a cab.
# Siri says: Hello cab

echo "Joke made $(date '+%Y-%m-%d %H:%M')\nHey siri, call a cab.\nSiri says: Hello cab"

```
---
## Download and save json data :floppy_disk:

Now we have enough skills to download airquality data from API and save it in this format: YYMMDD_HH:00.json using. Link for finding [airquality in Göteborg](https://www.dataportal.se/sv/datasets/66_70346/luftkvalitet-api#ref=?p=1&q=g%C3%B6teborg&s=2&t=20&f=&rt=dataset%24esterms_IndependentDataService%24esterms_ServedByDataService&c=false).

Print out the downloaded json file using cat, meow :octocat:

```bash
cat <path_to_file>
```

---
## Simple script to structure your repo :open_file_folder:

Create a bash script and open it for editing. 

```bash
# creates an empty file
touch init_template_repo.sh

# simple text editor for editing directly in bash shell, if you are hardcore you can use vim
nano init_template_repo.sh 
```

We need to add a shebang line to tell the OS which interpreter to use when parsing the rest of the file

```bash
#!/bin/bash

echo "running initializations for this repo" 
sleep 1
mkdir theory code-alongs explorations  
touch theory/.gitkeep code-alongs/.gitkeep

for i in {1..5}; do
    echo "This is file $i" >> file$i.txt
done
```

Now lets run :runner: the shell script 

```bash
./init_template_repo.sh
```

Woops permission denied :x:. Lets check why

```bash
ls -al 
```

Aha right, there is no x that is execute for us. Let's give ourself the permission to do that and run it again.

```bash
chmod +x init_template_repo.sh
ls -al # ah now we can execute the shell script
./init_template_repo.sh
```

Woops seems like all .txt files didn't go into explorations as I intended. Let's move them in. 

```bash
mv *.txt explorations
```

Ah much better, now lets get some line count, word count and character count in a file. 

```bash
wc -l explorations/file1.txt
```

Okay cool, so we know for one file, can we combine two commands to count number of files in the folder? Yes we use piping.

```bash
ls explorations | wc -l
```

Piping is really cool, we can list just the files we want by searching.  

```bash
touch explorations/test1.py explorations/test2.py 
ls explorations | grep .py
```

Now clean up and remove these three folders 

```bash
rm -rf code-alongs explorations theory 
```