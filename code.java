1a

public class LinearSearch
{

public static int linearSearch(int[] arr, int key)
{

    for(int i=0;i<arr.length;i++)
    {

        if(arr[i] == key)
        {

            return i;

        }

    }

    return -1;

}

public static void main(String a[])
{

    int[] a1={10,20,30,50,70,90};

    int key = 50;

    System.out.println(key+" is found at index: "+linearSearch(a1, key));

}

}


1.b



import java.io.*;

public class BinarySearch
{

public static void binarySearch(int arr[], int first, int last, int key)
{

    int mid = (first + last) / 2;

    while(first <= last)
    {

        if(arr[mid] < key)
        {

            first = mid + 1;

        }
        else if(arr[mid] == key)
        {

            System.out.println("Element is found at index: " + mid);

            break;

        }
        else
        {

            last = mid - 1;

        }

        mid = (first + last) / 2;

    }

    if(first > last)
    {

        System.out.println("Element is not found!");

    }

}

public static void main(String args[])
{

    int arr[] = {10,20,30,40,50};

    int key = 30;

    int last = arr.length - 1;

    binarySearch(arr,0,last,key);

}

}


2.a

import java.util.Stack;

public class StackEmptyMethodExample
{

public static void main(String[] args)
{

    //creating an instance of Stack class

    Stack<Integer> stk = new Stack<>();

    // checking stack is empty or not

    boolean result = stk.empty();

    System.out.println("Is the stack empty? " + result);

    // pushing elements into stack

    stk.push(78);

    stk.push(113);

    stk.push(90);

    stk.push(120);

    //prints elements of the stack

    System.out.println("Elements in Stack: " + stk);

    result = stk.empty();

    System.out.println("Is the stack empty? " + result);

}

}


2.b


import java.util.LinkedList;

import java.util.Queue;

public class QueueDemo
{

public static void main(String[] args)
{

    Queue<String> queue = new LinkedList<String>();

    queue.add("A");

    queue.add("B");

    queue.add("C");

    queue.add("D");

    System.out.println("The Front element is " + queue.peek());

    queue.remove();

    queue.remove();

    System.out.println("The Front element is " + queue.peek());

    System.out.println("The queue size is " + queue.size());

    if(queue.isEmpty())
    {

        System.out.println("The queue is empty");

    }
    else
    {

        System.out.println("The queue is not empty");

    }

}

}

