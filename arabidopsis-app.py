#! /usr/bin/env python3
# Author Gaurav Sablok
# Universitat Potsdam
# Date 2024-6-12
<<<<<<< Updated upstream
# coded this complete application in 15 minutes as have to go. 
# A streamlit application for the ids to ontology association for making the graphviz layout.
import streamlit as st
import pandas as pd
#import wget as wg
=======
# A streamlit application for the ids to ontology association for making the graphviz layout.
import streamlit as st
import pandas as pd

>>>>>>> Stashed changes
st.set_page_config(
                 page_title="Graph Ontology",
                 page_icon="Universitat Potsdam",
                 layout="centered",
                 initial_sidebar_state="expanded")
st.image("https://www.uni-potsdam.de/typo3conf/ext/up_template/Resources/Public/Images/logos/up_logo_international_2.png", width = 100)
st.header("A streamlit application for extracting the ontologies for graphs")
st.subheader("Developed by Gaurav Sablok, Academic Staff Member, Bioinformatics, Universitat Potsdam, Germany")
storingfile = st.text_input("Please provide the association file:")
storingobo = st.text_input("Please provide the obo file")
storingids = st.text_input("please enter the arabidopsis ID:")
termobo = st.text_input("please enter the obo term:")
storingtext = st.text_input("please enter the ontology term:")
if storingids and st.button("fetch associations"):
    with open(storingfile, "r") as openfile:
        with open(storingfile + ".txt", "w") as writefile:
            writefile.write("col1"+"\t"+"col2"+"\t"+"col3"+"\t"+"col4"+"\t"+"col5"+"\t"+"col6"+"\t"+"col7"+"\t"
                            +"col8"+"\t"+"col9"+"\t"+"col10"+"\t"+"col11"+"\t"+"col12"+"\t"+
                                   "col13"+"\t"+"col14"+"\t"+"col15"+"\t"+"col16"+"\t"+"col17"+"\n")
            for line in openfile.readlines():
                if not line.startswith("!"):
                    writefile.write(line)
            writefile.close()
    readfile = pd.read_csv(storingfile + ".txt", sep = "\t")
    locus = readfile["col2"].to_list()
    names = readfile["col3"].to_list()
    ontology = readfile["col5"]
    ids = readfile["col10"].to_list()
    functions = readfile["col11"].to_list()
    revisedfunctions = list(map(lambda n: n.replace("|", "-"),functions))
    for i in range(len(locus)):
        if ids[i] == storingids:
            st.write(f"{locus[i]}\n{names[i]}\n{ontology[i]}\n{ids[i]}\n{revisedfunctions[i]}")

if storingids and st.button("ontologies"):
    with open(storingfile, "r") as openfile:
        with open(storingfile + ".txt", "w") as writefile:
            writefile.write("col1"+"\t"+"col2"+"\t"+"col3"+"\t"+"col4"+"\t"+"col5"+"\t"+"col6"+"\t"+"col7"+"\t"
                            +"col8"+"\t"+"col9"+"\t"+"col10"+"\t"+"col11"+"\t"+"col12"+"\t"+
                                   "col13"+"\t"+"col14"+"\t"+"col15"+"\t"+"col16"+"\t"+"col17"+"\n")
            for line in openfile.readlines():
                if not line.startswith("!"):
                    writefile.write(line)
            writefile.close()
    readfile = pd.read_csv(storingfile + ".txt", sep = "\t")
    locus = readfile["col2"].to_list()
    names = readfile["col3"].to_list()
    ontology = readfile["col5"]
    ids = readfile["col10"].to_list()
    functions = readfile["col11"].to_list()
    revisedfunctions = list(map(lambda n: n.replace("|", "-"),functions))
    for i in range(len(locus)):
        if ids[i] == storingids:
            st.write(f"{locus[i]}\n{names[i]}\n{ontology[i]}\n{ids[i]}")

if storingobo and st.button("plantobo"):
    id = []
    name = []
    with open(storingobo, "r") as openobo:
        for line in openobo.readlines():
            if line.startswith("id:"):
                id.append(line.strip().split()[1])
            if line.startswith("name:"):
                name.append(' '.join(line.strip().split()[1:]))
            else:
                continue
            openobo.close()
    for i in range(len(id)):
         if id[i] == termobo:
             st.write(f"{id[i]}\n{name[i]}")

if storingtext and st.button("ontology"):
    with open(storingfile, "r") as openfile:
        with open(storingfile + ".txt", "w") as writefile:
            writefile.write("col1"+"\t"+"col2"+"\t"+"col3"+"\t"+"col4"+"\t"+"col5"+"\t"+"col6"+"\t"+"col7"+"\t"
                            +"col8"+"\t"+"col9"+"\t"+"col10"+"\t"+"col11"+"\t"+"col12"+"\t"+
                                   "col13"+"\t"+"col14"+"\t"+"col15"+"\t"+"col16"+"\t"+"col17"+"\n")
            for line in openfile.readlines():
                if not line.startswith("!"):
                    writefile.write(line)
            writefile.close()
    readfile = pd.read_csv(storingfile + ".txt", sep = "\t")
    locus = readfile["col2"].to_list()
    names = readfile["col3"].to_list()
    ontology = readfile["col5"]
    ids = readfile["col10"].to_list()
    functions = readfile["col11"].to_list()
    revisedfunctions = list(map(lambda n: n.replace("|", "-"),functions))
    for i in range(len(locus)):
        if ontology[i] == storingtext:
            st.write(f"{ontology[i]}\n{revisedfunctions[i]}")
