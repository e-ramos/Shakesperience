#Project 2: Hidden Markov Modeling
By E. A. Ramos
# Shakesperience: An HMM NLP Generator
## Files

 - **`main.py`** : the main event. Run this script 
 - **`mfunc.py`** : contains all helper functions used by main
 -  **`TrainModel.py`** : contains the *ShakesTrain* routine, which generates a HMM based trie which is then used to generate text
 -    **`WordNode.py`** : class definition for a prefix trie node
 - **/Data**: contains the dataset *Shakespeare_data.csv* and a binary *.pkl* to store our serialized model
 - **/Results**: contains images and misc
 ## Note
There is a default *WordList.pkl* model is trained using 20k lines. There are memory bugs that can occur when exceeding this number; although it may be platform specific (I am running on limited ram). 

If you choose to not use this model, you can generate a new one in the interface.

*.pkl* files are inherently **insecure** and deserializing them can lead to arbitrary code execution. This format was chosen for convenience only. Run instance in a safe place.

 ## Use
 ###### Dependencies:
 1. Anaconda 

 - ## Run main.py:
 It will automatically detect if there is a valid model. If not, it will generate a new one:
 ![Auto-Model Generation](https://github.com/e-ramos/Shakesperience/blob/master/Results/Self%20model%20write.png)
 - ## Menu:
 The main menu has 3 options:
 ![Menu](https://github.com/e-ramos/Shakesperience/blob/master/Results/Menu.png)
1. #### Generate new words:
	1. If you input an incomplete sentence, the model will complete it for you
			![Sentence Completion](https://github.com/e-ramos/Shakesperience/blob/master/Results/Sentence%20Completion.png)
	2. If you input an invalid, or blank sentence, the model will generate a random one:
		![Random Sentence](https://github.com/e-ramos/Shakesperience/blob/master/Results/New%20Sentence%20Generation.png)
2. #### Tweak Model:
	- Allows you to change the number of available branch paths down the trie structure; This effectively increases the variance of the model

3. #### Train Model:
	- Allows you to train a new model which is auto saved. The model search space is randomized on init, so every time you do this, your model will be distinct. 
	- Choosing the number of lines is likely system dependent: the algo can run out of memory if you choose more than, say, 30,000 lines. 
		- This is due to the inefficiency of my regex search function choice. Ideally, the data structure would be generated *in-place* while reading in the file. However, time constraints etc.

![Model Training](https://github.com/e-ramos/Shakesperience/blob/master/Results/Training.png)

 ## Implementation Strategy

### The Trie: a fun little data structure
- A naive approach would be to store every word in the English language and create a markov relation between every element in the state space **S ={*allwords*}** which would be incredibly inefficient.
- Instead, I chose an acyclic FSM known as the trie. Here the possible search space is reduced by only storing each English sequence as a set of prefixes. Ergo, order matters, and each search is **O**(N), since given a root, we only have to traverse a single path to find a solution.
	- In this context a **solution**  is a Markov Chain that ends in a period
	- 
![The Prefix Trie](https://github.com/e-ramos/Shakesperience/blob/master/Results/Trie.jpg)


Using the above strategy and generating frequency weights; the model was trained.

