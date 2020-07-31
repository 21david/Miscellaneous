import java.util.*;

/*
From video:  youtube.com/watch?v=zaBhtODEL0w
(made a few minor modifications from the code in the video to make it work)
*/

public class DFSAndBFS {

	public static void main(String[] args) {
		/* Setting up the nodes and the graph */
		
		// Set up the nodes
		Graph.Node node1 = new Graph.Node(1);
		Graph.Node node2 = new Graph.Node(2);
		Graph.Node node3 = new Graph.Node(3);
		Graph.Node node4 = new Graph.Node(4);
		Graph.Node node5 = new Graph.Node(5);
		Graph.Node node6 = new Graph.Node(6);
		Graph.Node node7 = new Graph.Node(7);
		Graph.Node node8= new Graph.Node(8);
		
		// Create a graph object and fill up its lookup table with the nodes we made
		Graph graph = new Graph();
		graph.nodeLookup.put(1, node1);
		graph.nodeLookup.put(2, node2);
		graph.nodeLookup.put(3, node3);
		graph.nodeLookup.put(4, node4);
		graph.nodeLookup.put(5, node5);
		graph.nodeLookup.put(6, node6);
		graph.nodeLookup.put(7, node7);
		graph.nodeLookup.put(8, node8);
		
		// add edges between the nodes
		graph.addEdge(1,  2);
		graph.addEdge(1,  3);
		graph.addEdge(2,  4);
		graph.addEdge(3,  4);
		graph.addEdge(4,  5);
		graph.addEdge(5,  6);
		graph.addEdge(7,  8);
		
		/*
		 Graph:
		 (1) ---- (2)           (7) ---- (8)
		  |        | 
		  |        |
		 (3) ---- (4) ---- (5) ---- (6)
		 */
		
		
		/* Testing the DFS and BFS methods */
		
		// these should print true
		System.out.println(graph.hasPathDFS(1,  6));
		System.out.println(graph.hasPathDFS(1,  2));
		System.out.println(graph.hasPathDFS(3,  5));

		System.out.println(graph.hasPathBFS(1,  6));
		System.out.println(graph.hasPathBFS(1,  2));
		System.out.println(graph.hasPathBFS(3,  5));

		// these should print false
		System.out.println(graph.hasPathDFS(1,  7));
		System.out.println(graph.hasPathDFS(3,  8));
		System.out.println(graph.hasPathDFS(4,  7));
		System.out.println(graph.hasPathDFS(8,  6));

		System.out.println(graph.hasPathBFS(1,  7));
		System.out.println(graph.hasPathBFS(3,  8));
		System.out.println(graph.hasPathBFS(4,  7));
		System.out.println(graph.hasPathBFS(8,  2));
	}

}


class Graph {
    // mapping of node id to actual node
    public HashMap<Integer, Node> nodeLookup = new HashMap<Integer, Node>();
    
    public static class Node { 
        private int id; 
        LinkedList<Node> adjacent = new LinkedList<Node>();
        
        public Node(int id) { 
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
        d.adjacent.add(s);
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
        // the nodes we need to visit next (works as a queue data structure, FIFO style)
        LinkedList<Node> nextToVisit = new LinkedList<Node>();
        
        // nodes we have visited so far
        HashSet<Integer> visited = new HashSet<Integer>();
        
        nextToVisit.add(source);
        
        while(!nextToVisit.isEmpty()) {
            Node node = nextToVisit.remove(); // this remove() method removes from the beginning
            if(node == destination)
                return true;
                
            if(visited.contains(node.id)) 
                continue;
                
            visited.add(node.id);
            
            // add the children
            for(Node child : node.adjacent) 
                nextToVisit.add(child); // this add() method adds to the end
        }
        
        // if we get to the end without finding a path, return false
        return false;
    }
}
