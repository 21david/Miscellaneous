/* In order to understand heaps better, I implemented one. This is a min heap which uses an array to store its elements
and several methods to keep the elements in order. I used this video: youtube.com/watch?v=t0Cq6tVNRBA

To run the code below, you can save it to a file named 'Main1.java' and compile and run it.
Or you can run my repl.it version at: repl.it/@davidespinosa/Heap-Implementation#Main.java
*/

import java.util.Arrays;

public class Main1 {
	public static void main(String[] a)
	{
		MinIntHeap heap = new MinIntHeap();
		
		int[] numbers = {6, -4, -2, 0, 3, 13, 26, 12, 6, 7, 0, -20, -14, 2};
		
		// add all these random numbers to the heap
		for(int n : numbers)
			heap.add(n);
		
		// try to use the poll() method until the heap runs out of numbers
		try {
			while(true) {
				System.out.print(heap.poll() + " ");
			}
		}
		catch (IllegalStateException ex)
		{
			System.out.println("\nNo more numbers in the heap.");
		}
		
		// Output of above code:
		// -20 -14 -4 -2 0 0 2 3 6 6 7 12 13 26 
		// No more numbers in the heap.
	}
}

class MinIntHeap {
    private int capacity = 10;
    private int size = 0;

    int[] items = new int[capacity];

    private int getLeftChildIndex(int parentIndex) { return 2 * parentIndex + 1; }
    private int getRightChildIndex(int parentIndex) { return 2 * parentIndex + 2; }
    private int getParentIndex(int childIndex) { return (childIndex - 1) / 2; }

    private boolean hasLeftChild(int index) { return getLeftChildIndex(index) < size; }
    private boolean hasRightChild(int index) { return getRightChildIndex(index) < size; }
    private boolean hasParent(int index) { return getParentIndex(index) >= 0; }

    private int leftChild(int index) { return items[getLeftChildIndex(index)]; }
    private int rightChild(int index) { return items[getRightChildIndex(index)]; }
    private int parent(int index) { return items[getParentIndex(index)]; }

    private void swap(int indexOne, int indexTwo) {
        int temp = items[indexOne];
        items[indexOne] = items[indexTwo];
        items[indexTwo] = temp;
    }

    private void ensureExtraCapacity() {
        if(size == capacity) {
            items = Arrays.copyOf(items, capacity * 2);
            capacity *= 2;
        }
    }
    
    // (04:04) peek method
    public int peek() {
        if(size == 0)
            throw new IllegalStateException();
        return items[0];
    }

    // (04:22) poll method
    public int poll() {
        if(size == 0)
            throw new IllegalStateException();
        int item = items[0];
        items[0] = items[size - 1]; // put the last element in the root element spot
        size--; // decrease size by 1

        heapifyDown(); // this will "bubble" the element down to its correct spot

        return item;
    }
    // (05:06) Example of "polling"

    // (05:27) add method
    public void add(int item) {
        ensureExtraCapacity(); // make sure there's actually space
        items[size] = item; // add element to the first available spot
        size++; // increase size

        heapifyUp(); // "bubble" the element up to its right spot
    }
    // (05:58) example of adding an element
    
    // (06:18) heapifyUp method
    public void heapifyUp() {
        int index = size - 1;

        while(hasParent(index) && parent(index) > items[index]) {
            swap(getParentIndex(index), index);
            index = getParentIndex(index);
        }
    }
    // (06:56) example of something "bubbling" up
    
    // (07:42) heapifyDown method
    public void heapifyDown() {
        int index = 0;
        
        while(hasLeftChild(index)) {
            int smallerChildIndex = getLeftChildIndex(index);
            if(hasRightChild(index) && rightChild(index) < leftChild(index)) {
                smallerChildIndex = getRightChildIndex(index);
            }

            if(items[index] < items[smallerChildIndex]) {
                break;
            }
            else {
                swap(index, smallerChildIndex);
            }

            index = smallerChildIndex;
        }
    }
    // (09:07) example of something "bubbling down"
}
