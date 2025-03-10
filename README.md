 

---

# **TSP Solver using MCMC and Simulated Annealing**  

## **Overview**  
This project implements a **Markov Chain Monte Carlo (MCMC) approach with Simulated Annealing** to solve the **Traveling Salesman Problem (TSP)**. The algorithm leverages **Metropolis-Hastings sampling** to explore possible routes and optimize the shortest path.  

## **Key Features**  
- Implements **Metropolis-Hastings algorithm** for state transitions.  
- Uses **Simulated Annealing** to gradually refine the solution.  
- Supports **random city generation** and **custom datasets**.  
- Provides **visualization of the best-found tour**.  

## **Project Structure**  
```
tsp_mcmc_project/
│── tsp_mcmc.py      # Main script
│── utils.py         # Helper functions (optional)

```

## **Installation & Setup**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/tsp_mcmc_project.git  
   cd tsp_mcmc_project  
   ```  
2. Install dependencies:  
   ```bash
   pip install numpy matplotlib  
   ```  
3. Run the script:  
   ```bash
   python tsp_mcmc.py  
   ```  

## **How It Works**  
1. **City Generation**: Random cities are generated in a 2D space.  
2. **Initial Tour**: A random permutation of cities is chosen.  
3. **Markov Chain Transitions**: New tours are proposed by swapping cities.  
4. **Metropolis-Hastings Rule**: New tours are accepted probabilistically.  
5. **Simulated Annealing**: The temperature parameter is reduced over iterations.  
6. **Visualization**: The best-found tour is displayed with **Matplotlib**.  

## **Example Output**  
- Best Tour Sequence: `[3, 7, 1, 5, 10, ...]`  
- Best Distance Found: `320 units`
- 
## **Results**

Here is the optimized tour obtained using the MCMC Simulated Annealing algorithm:



 ![Markov_Chain_Monte_Carlo](https://github.com/user-attachments/assets/b545f1d3-50f6-4b86-ba93-420cee1274b4)


 *This image shows the shortest path found by the algorithm, connecting all cities efficiently.*
 *Best tour sequence was obtained as [0->12->4->1->6->10->14->9->2->7->11->8->13->3->5]*







## **Future Improvements**  
- Implement **parallel MCMC chains** for better exploration.  
- Optimize **temperature decay schedules** for better convergence.  

## **License**  
This project is open-source under the **MIT License**.  

---

