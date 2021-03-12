#!/usr/bin/python
'''
Your script should be able to be run from the command line
It should take any weighted edgelist as an input, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB"
For any given edgelist, your script should then create a weighed edgelist. This should be used to create a network visualization, which will be saved in a folder called viz.
It should also create a data frame showing the degree, betweenness, and eigenvector centrality for each node. It should save this as a CSV in a folder called output.


Tips

You should use argparse() in the Python standard library
Your code should contain a main() function
Don't worry too much about efficiency - networkx is really slow, there's no way around i!
If you have issues with pygraphviz, just use the built-in matplotlib functions in networkx.
You may want to create an argument for the user to define a cut-off point to filter data. E.g. only include node pairs with more than a certain edge weight.
Make sure to use all of the Python scripting skills you've learned so far, including in the workshops with Kristoffer Nielbo
'''

# Load necessary libraries
import os #system tools
import argparse #to take input from command line
import pandas as pd #for data manipulation/analysis
from tqdm import tqdm #progress bar
import spacy #NLP
nlp = spacy.load("en_core_web_sm")
import networkx as nx #network visualization
import pygraphviz 
import matplotlib.pyplot as plt
from collections import Counter #counter dictionary

#####################
#####################
#### TO DO TO DO #### 
#####################
#write: write python network.py --help to get instructions before running script
#add the libraries to requirements.txt
#make class


def calc_weights(edgelist):
    '''This function takes an edgelist and returns a weighted edgelist''' 
    counted_edges = [] #empty list for weighted edgelist

    # Iterate over items in Counter-dictionary of edgelist
    for pair, weight in Counter(edgelist).items():
        nodeA = pair[0] #extracting nodeA
        nodeB = pair[1] #extracting nodeB
        counted_edges.append((nodeA, nodeB, weight)) #appending tuple with nodeA, nodeB, and weight to list

    return counted_edges


def network_viz(G):
    '''This function takes a graph-object and creates and saves a visualization of the network'''
    # Plot 
    pos = nx.nx_agraph.graphviz_layout(G, prog="neato") #creates position for plot
    nx.draw(G, pos, with_labels=True, node_size=20, font_size=5) #draw plot
    
    # Save plot
    plot_path = os.path.join("out", "assignment4", "viz", "network.png")
    plt.savefig(plot_path, dpi=300, bbox_inches="tight")
    
    
def centrality_scores(G):
    '''This function takes a graph-object and calculates and saves centrality scores of nodes(degree, betweenness, eigenvector)'''
    #Calculate scores
    bc_metric = nx.betweenness_centrality(G) #creates dict with nodes and betweenness scores
    ev_metric = nx.eigenvector_centrality(G) #creates dict with nodes and eigenvector scores
    degrees = nx.degree(G) #creates iterator over (node, degree) pairs
    
    # Create df with scores 
    centrality_df = pd.DataFrame(bc_metric.items(), columns=["node", "betweenness"]) #create df with nodes and betweenness
    centrality_df["eigenvector"] = list(ev_metric.values()) #add eigenvector values as new column
    centrality_df["degree"] = [v for k, v in degrees] #extract degrees from iterator of (node, degree) pairs and add as new column
    
    # Save df as CSV
    csv_path = os.path.join("out", "assignment4", "output", "centrality.csv")
    centrality_df.to_csv(csv_path)
    
  
 
# Define main function
def main():
    ap = argparse.ArgumentParser(description="[INFO] This script takes an edgelist with column names \"nodeA\", \"nodeB\" as input and 1) creates a weighted edgelist, 2) creates and saves a network visualization, 3) calculates and saves centrality scores. It is possible to specify a cut-off value for which node pairs with edge weight lower than that are removed. This is recommended if the plot is too dense to interpret.")
    ap.add_argument("-e", 
                    "--edgelist", 
                    required=True, 
                    type=argparse.FileType('r'), 
                    help="dataframe, path to .csv-file with column headers nodeA, nodeB")
    ap.add_argument("-c", 
                    "--cutoff", 
                    required=False, 
                    type=int, 
                    default=0, 
                    help="int, cut-off value for filtering node pairs to only include those with edge weight higher than that") 

    args = vars(ap.parse_args())
    
    # Read edgelist from csv to df
    edgelist_df = pd.read_csv(args['edgelist'])
    
    # Turn df to edgelist (list of tuples with node pairs)
    def concat_names(x):
        ''' This function takes the 1st and 2nd index value of x and concatenates them in a tuple'''
        return (x[1], x[2]) 
    edgelist = list(edgelist_df.apply(concat_names, axis = 1)) #applying above function to create list of tuples with node pairs
    
    # Create weighted edgelist
    weighted_edgelist = calc_weights(edgelist)
    
    # Turn into df
    edges_df = pd.DataFrame(weighted_edgelist, columns=["nodeA", "nodeB", "weight"])
    
    # Filter data according to cut-off value
    filtered_df = edges_df[edges_df["weight"] > args['cutoff']]
    
    # Create graph taking nodeA and nodeB and including extra info (here weight)
    G = nx.from_pandas_edgelist(filtered_df, "nodeA", "nodeB", ["weight"])
    
    # Create network visualization and save as PNG
    network_viz(G)
    
    # Create df with degree, betweenness, eigenvector for each node and save as CSV
    centrality_scores(G)
    
    
# Define behaviour when called from command line
if __name__=="__main__":
    main()
    print()
    print("DONE! You can find the network visualization in \'out/assignment4/viz\'and the centrality measures in \'out/assignment4/output\'")
    print()