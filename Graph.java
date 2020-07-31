import java.util.*;

/*
From video:  youtube.com/watch?v=zaBhtODEL0w
*/

public class Graph {
    // mapping of node id to actual node
    private HashMap<Integer, Node> nodeLookup = new HashMap<Integer, Node>();
    
    public static class Node { 
        private int id; 
        LinkedList<Node> adjacent = new LinkedList<Node>();
        
        private Node(int id) { 
            this.id = id;
        }
    }
    
    private Node getNode(int id) {
        return nodeLookup.get(id);
    }
    
    public void addEdge(int source, int destination) { 
        Node s = getNode(source);
        Node d = getNode(destination);
        s.adjacent.add(d);
    }
    
    
    // DFS
    public boolean hasPathDFS(int source, int destination) {
        Node s = getNode(source);
        Node d = getNode(destination);
        
        HashSet<Integer> visited = new HashSet<Integer>(); 
        return hasPathDFS(s, d, visited);
    }
    
    private boolean hasPathDFS(Node source, Node destination, HashSet<Integer> visited) {
        if(visited.contains(source.id))
            return false;
            
        visited.add(source.id);
        
        // if we are at the destination, return true because we know there is a path
        if(source == destination)
            return true;
            
        // else if not, then we will check all the children for a path
        for(Node child : source.adjacent)
        {
            if(hasPathDFS(child, destination, visited))
                return true;  // if there is a path, it will bubble up all the way to the top of the stack & return true
        }
        
        // if nothing was able to find a path, we return false
        return false;
    }
    
    
    // BFS
    public boolean hasPathBFS(int source, int destination) {
        return hasPathBFS(getNode(source), getNode(destination));
    }
    
    public boolean hasPathBFS(Node source, Node destination) {
        // the nodes we need to visit next
        LinkedList<Node> nextToVisit = new LinkedList<Node>();
        HashSet<Integer> visited = new HashSet<Integer>();
        nextToVisit.add(source);
        
        while(!nextToVisit.isEmpty()) {
            Node node = nextToVisit.remove();
            if(node == destination)
                return true;
                
            if(visited.contains(node.id)) 
                continue;
                
            visited.add(node.id);
            
            // add the children
            for(Node child : node.adjacent) 
                nextToVisit.add(child);
        }
                
        // if we get to the end without finding a path, return false
        return false;
    }
}
    
    
