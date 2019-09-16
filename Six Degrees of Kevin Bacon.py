def readFile():

    with open("filmovi.txt","r") as file:

        dic = {}
        dic_actors={}
          
        for line in file:

            line = line.strip()
            line = line.split(";")
            # filmovi kao ključevi i glumci koji su glumili u njima kao vrijednosti 
            dic[line[0]] = line[1:]
            
        # svi glumci kao ključevi
        for v in dic.values():
            for actor in v:                
                dic_actors[actor]=[]
        
                
        # vrijednosti-> gumci koji su glumili s određenim glumcem u filmovima
        for actor in dic_actors.keys():
            for i in dic.values():
                for j in i:
                    if actor in i:
                        if actor==j:
                            continue
                        else:
                            dic_actors[actor].append(j)
                    
    return dic_actors,dic



def bfs(graph, start, goal):
    # posjećeni čvorovi
    explored = []
    # dodaj početnog u red 
    queue = [[start]]
     
    while queue:
        # digni prvi put iz reda
        path = queue.pop(0)
        # dobavi zadnji čvor iz puta
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            #ide kroz sve susjedne čvorove i konstruira novi put i dodaje ga u red
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # ako smo došli do cilja vrati put 
                if neighbour == goal:
                    return new_path
 
            # stavi čvor u posjećene
            explored.append(node)
 
def actor_movie_connection(path,actor_movie):
    
    for i in range(len(path)-1):
        for k,v in actor_movie.items():
            if path[i] in v and path[i+1] in v:
                print(path[i],'Was with',path[i+1],'in',k)
    print(path[i+1],'has a Bacon number of',len(path)-1)
            

if __name__=='__main__':

    graf,act_mov = readFile()
    name = input('Unesite ime glumca:')
    if name not in graf.keys():
        print('Nema podataka za navedenog glumca, provjerite jeli ime ispravno. ')
    else:
        
        path=bfs(graf,'Kevin Bacon',name)
        actor_movie_connection(path,act_mov)
    
