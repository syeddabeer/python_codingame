import sys
import math
import numpy
import itertools


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

links=[]

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links.append([n1,n2])

links=numpy.array(links)

exits=[]

for i in range(e):
    ei = int(input())  # the index of a gateway node
    exits.append(ei)
    
def check_exits(times,exits,e):
    result=True
    for ei in range(e):
        if times[exits[ei]]>-1:
            result=False 
    return result 

def links_to_graph(links,n,l):
    graph=[[] for i in range(n)]
    for i in range(l):
        graph[links[i][0]].append(links[i][1])
        graph[links[i][1]].append(links[i][0])
    return graph 
        

def get_length(graph,entry,exits,n,e):
    length=0
    nodes=[entry]
    nodes_time=numpy.full(n,-1)
    nodes_time[entry]=0
    while check_exits(nodes_time,exits,e) and length<=n:
        length+=1
        
        new_nodes=[]
        for i in nodes:
            for j in graph[i]: 
                if nodes_time[j]==-1:
                    nodes_time[j]=length
                    new_nodes.append(j)  
        nodes=new_nodes
    
    for i in range(e):
        if nodes_time[exits[i]]>-1:
            break
    
    e1=i
    
                
    return length, e1 
    

def get_bad(graph,exits,n):
    bad_nodes=exits[:]
    bad_cnt=len(bad_nodes)
    old_bad_cnt=0
    
    bad_time=numpy.full(n,-1)
    length=0
    
    bad_links=[set({}) for i in range(n)]
    
    while bad_cnt>old_bad_cnt:
        length+=1
        old_bad_cnt=bad_cnt
        old_bad_nodes=bad_nodes[:]
        #print(bad_links,file=sys.stderr)
        for i in range(n):
            sect=list(set(old_bad_nodes).intersection(graph[i]))
            #print(sect,file=sys.stderr)
            check=len(sect)
            if check>1 and not i in bad_nodes:
                tmp_bad_links=bad_links[i]
                #must_cut=0
                for j in range(len(sect)):
                    if sect[j] in exits: #add link to exit
                        #print(sect[j],file=sys.stderr)
                        for k in range(l):
                            if (links[k][0]==i and links[k][1]==sect[j]) or (links[k][1]==i and links[k][0]==sect[j]):
                                max_l=k
                                break
                        tmp_bad_links=tmp_bad_links.union({max_l})
                        #must_cut+=1
                    else: #add links already in list
                        tmp_bad_links=tmp_bad_links.union(bad_links[sect[j]])
                        #must_cut+=len(bad_links[sect[j]])-1
                
                if len(tmp_bad_links)>length and i!=si:
                    bad_nodes.append(i)
                    bad_time[i]=length
                    bad_links[i]=tmp_bad_links
            
        bad_cnt=len(bad_nodes)   
                
    return bad_cnt, bad_nodes, bad_time, bad_links
    



# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    cutable=[]

    for i in range(l):
        if links[i][0] in exits or links[i][1] in exits:
            cutable.append(i)

    print(cutable,file=sys.stderr)

    graph=links_to_graph(links,n,l)
    #print(graph, file=sys.stderr)
    
    len1, e1=get_length(graph,si,exits,n,e)
    print("Length "+str(len1), file=sys.stderr)
    
    max_len=len1
    max_l=-1
    
    if (max_len==1):
        for i in range(l):
           if (links[i][0]==si and links[i][1] in exits) or (links[i][1]==si and links[i][0] in exits):
               max_l=i
               break
    else:
        
        #cutable_dist=numpy.zeros((len(cutable),2),dtype=int)
        #for c in range(len(cutable)):
        #    c1=links[cutable[c]][1]
        #    c2=links[cutable[c]][0]
            
        #    cutable_dist[c][1], e1=get_length(graph,si,[c1,c2],n,2)
        #    cutable_dist[c][0]=cutable[c]
        
        #cutable_dist.view('i8,i8').sort(order=['f1'], axis=0)
        #print(cutable_dist,file=sys.stderr)
        
        bad_cnt, bad_nodes, bad_time, bad_links = get_bad(graph,exits,n)
        
        print(bad_nodes,file=sys.stderr)
        print(bad_time,file=sys.stderr)
        print(bad_links,file=sys.stderr)
        
        bad_dist=numpy.zeros((bad_cnt,2),dtype=int)
        for c in range(bad_cnt):
            
            bad_dist[c][1], e1=get_length(graph,si,[bad_nodes[c]],n,1)
            bad_dist[c][0]=bad_nodes[c]
            bad_dist[c][1]-=len(bad_links[bad_nodes[c]])
            bad_dist[c][1]+=bad_time[bad_nodes[c]]
        
        bad_dist.view('i8,i8').sort(order=['f1'], axis=0)
        print(bad_dist,file=sys.stderr)
                
        print(bad_links[bad_dist[0][0]],file=sys.stderr)
        
        if len(bad_links[bad_dist[0][0]])>0:
            min_dist=bad_dist[0][1]
            remove_candidates=bad_links[bad_dist[0][0]] 
            i=1
            while bad_dist[i][1]==min_dist:
                remove_candidates=remove_candidates & bad_links[bad_dist[i][0]]
                i=i+1
                
            print(remove_candidates,file=sys.stderr)
            max_l=list(remove_candidates)[0]
        #tested_hyp=[[[]] for i in range(cutable_dist[-1][1])]

    
        #for i in range(min(len(cutable)-2,10)):

        #    hyp=[[cutable_dist[i][0]]]
        #    for j in range(min(cutable_dist[i][1]-1,i)):
        #        for k in range(len(tested_hyp[j])):

        #            hyp=hyp+[numpy.concatenate((tested_hyp[j][k],[cutable_dist[i][0]]))]
            

            
        #    for h in range(len(hyp)):
            
        #        h1=hyp[h]

            
            
            
        
          #      test_links=numpy.delete(links,h1,axis=0)
          #      test_graph=links_to_graph(test_links,n,l-len(h1))
          #      test_len, e1=get_length(test_graph,si,exits,n,e)
                
          #      if len(tested_hyp[len(h1)-1][0])==0:
          #          tested_hyp[len(h1)-1]=[hyp[h]]
          #      else:
          #          tested_hyp[len(h1)-1]=numpy.concatenate((tested_hyp[len(h1)-1],[hyp[h]]))
                
                

        
        
           #     if test_len-len(h1)>max_len:
            #        max_len=test_len-len(h1)
            #        max_l=h1[0]
            #        print("hyp: {}".format(h1), file=sys.stderr)
            #        print("test len {}".format(test_len),file=sys.stderr)

    
        print(max_l, file=sys.stderr)
    
    if max_l==-1:
       print("Remove one of exits", file=sys.stderr)
       for i in range(l):
           if links[i][0] in exits  or links[i][1] in exits:
               max_l=i
               break
    
    print(str(links[max_l][0])+" "+str(links[max_l][1]))
    l=l-1
    links=numpy.delete(links,max_l,axis=0)
    #cutable.remove(max_l)
        
        

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    #print("0 1")