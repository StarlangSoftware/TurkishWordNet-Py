For Developers
============

You can also see [Java](https://github.com/starlangsoftware/TurkishWordNet), [C++](https://github.com/starlangsoftware/TurkishWordNet-CPP), or [C#](https://github.com/starlangsoftware/TurkishWordNet-CS) repository.

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

Türkçe WordNet KeNet'i yüklemek için

	a = WordNet()

Belirli bir WordNet'i yüklemek için

	domain = WordNet("domain_wordnet.xml");

Tüm synsetleri getirmek için

	synSetList(self) -> list

Belirli bir synseti getirmek için

	getSynSetWithId(self, synSetId: str) -> SynSet

Belirli bir kelimenin tüm anlamlarını (Synsetlerini) getirmek için

	getSynSetsWithLiteral(self, literal: str) -> list

## SynSet

Bir synsetin eş anlamlı literallerini bulmak için Synonym elde edilir.

	getSynonym(self) -> Synonym
	
Bir synsetin içindeki Relation'ları indeks bazlı elde etmek için

	getRelation(self, index: int) -> Relation

metodu ile bulunur. Örneğin, bir synsetin içindeki tüm ilişkiler

	for i in range(synset.relationSize()):
		relation = synset.getRelation(i);
		...

## Synonym

Synonym'in içindeki literaller indeks bazlı

	getLiteral(self, index: int) -> Literal

metodu ile bulunur. Örneğin, bir synonym içindeki tüm literaller

	for i in range(synonym.literalSize()):
		literal = synonym.getLiteral(i);
		...
