For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/TurkishWordNet-Cy), [Java](https://github.com/starlangsoftware/TurkishWordNet), [C++](https://github.com/starlangsoftware/TurkishWordNet-CPP), or [C#](https://github.com/starlangsoftware/TurkishWordNet-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called DataStructure will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/TurkishWordNet-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `TurkishWordNet-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [WordNet](#wordnet)
+ [SynSet](#synset)
+ [Synonym](#synonym)

## WordNet

To load the WordNet KeNet,

	a = WordNet()

To load a particular WordNet,

	domain = WordNet("domain_wordnet.xml");

To bring all the synsets,

	synSetList(self) -> list

To bring a particular synset,

	getSynSetWithId(self, synSetId: str) -> SynSet

And, to bring all the meanings (Synsets) of a particular word, the following is used.

	getSynSetsWithLiteral(self, literal: str) -> list

## SynSet

Synonym is procured in order to find the synonymous literals of a synset.

	getSynonym(self) -> Synonym
	
In order to obtain the Relations inside a synset as index based, the following method is used.

	getRelation(self, index: int) -> Relation

For instance, all the relations in a synset,


	for i in range(synset.relationSize()):
		relation = synset.getRelation(i);
		...

## Synonym

The literals inside the Synonym are found as index based with the following method.

	getLiteral(self, index: int) -> Literal

For example, all the literals inside a synonym can be found with the following:

	for i in range(synonym.literalSize()):
		literal = synonym.getLiteral(i);
		...
