#! /usr/bin/env python3
# Author Gaurav Sablok
# Date 2024-6-12
# coded this complete application in 15 minutes as have to go. 
# A streamlit application for the ids to ontology association for making the graphviz layout.
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
st.set_page_config(
                 page_title="Graph Ontology",
                 layout="centered",
                 initial_sidebar_state="expanded")
st.header("A streamlit application for extracting the ontologies for graphs")
st.subheader("Developed by Gaurav Sablok")

components.iframe("https://www.arabidopsis.org/", height=100)

help = st.button("Display the help file")
if help:
    st.write("1. if association file has been provided then you can search using the ontologies button")
    st.write("2. if plant obo file has been provided then you can search using the plantobo term")
    st.write("3. if plant obo term and plant obo file then you can search for the define ontology")
    st.write("4. if association file is provided only with the Arabidopsis AGI then you can search the fetch associations, ontolgies")
    st.write("5. if the association file and the plant ontology file along with the Arabidopsis AGI and the Plant obo term has provied then you can search for the fetch association, ontolgies, plantobo, defineontology")

toggle = st.button("Display the link to the page where i can download the ontologies")
if toggle:
    components.iframe("https://www.arabidopsis.org/download/list?dir=GO_and_PO_Annotations", height=100)
    st.write("You can download the files from https://www.arabidopsis.org/download/list?dir=GO_and_PO_Annotations")

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

if storingobo and termobo and st.button("defineontology"):
    jsonidvalue = {}
    with open(storingobo, "r") as openobo:
        readobo = openobo.readlines()
        for i in range(len(readobo)):
            for j in range(len(readobo)):
                if readobo[i].startswith("id:"):
                    if readobo[j].startswith("def:"):
                        jsonidvalue[readobo[i].strip().split()[1]] = ' '.join(readobo[j].strip()[3:])
    selected = dict([(k,v) for k,v in jsonidvalue.items() if k == termobo])
    for k,v in selected.items():
        st.write(f"{k}\n{v}")
