"""
Enhanced Turkish WordNet (KeNet) with Rich Semantic Relations
Author: Uğur Sürmeli (NK-Engine)
Contributed to: TurkishWordNet-Py

This module extends the original TurkishWordNet with:
- 236,690 semantic edges (HYPERNYM, HYPONYM, HOLONYM, etc.)
- 80,644 literal synonym relationships
- Sense and origin metadata for each literal
- CSV-based fast access to semantic relations

Original: XML-based wordnet
Extension: CSV-based relation graphs
"""

import csv
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


class EnhancedWordNet:
    """Extended WordNet with rich semantic relations from CSV data"""

    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            # Default to package data directory
            data_path = Path(__file__).parent / "data" / "csv"
        else:
            data_path = Path(data_path)

        self.data_path = data_path
        self._literals: Dict[str, List[Dict]] = {}
        self._synsets: Dict[str, Dict] = {}
        self._edges: Dict[str, List[Tuple[str, str]]] = {}  # synset -> [(target, type)]
        self._literal_graph: Dict[str, Set[str]] = {}  # literal -> {synonyms}

        self._load_data()

    def _load_data(self):
        """Load all CSV data files"""
        self._load_literals()
        self._load_synsets()
        self._load_edges()
        self._load_literal_graph()

    def _load_literals(self):
        """Load literals with sense and origin metadata"""
        csv_path = self.data_path / "trwordnet_literals_v0_1_0.csv"
        if not csv_path.exists():
            return

        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                synset_id = row['synset_id']
                literal = row['literal']

                entry = {
                    'synset_id': synset_id,
                    'literal': literal,
                    'sense': row.get('sense', ''),
                    'origin': row.get('origin', ''),
                    'groups': row.get('groups', '')
                }

                if synset_id not in self._literals:
                    self._literals[synset_id] = []
                self._literals[synset_id].append(entry)

                # Index by literal for quick lookup
                if literal not in self._literal_graph:
                    self._literal_graph[literal] = set()

    def _load_synsets(self):
        """Load synset definitions and metadata"""
        csv_path = self.data_path / "trwordnet_synsets_v0_1_0.csv"
        if not csv_path.exists():
            return

        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self._synsets[row['synset_id']] = {
                    'pos': row.get('pos', ''),
                    'definition': row.get('definition', ''),
                    'wiki': row.get('wiki', ''),
                    'example_count': row.get('example_count', '0'),
                    'literal_count': row.get('literal_count', '0')
                }

    def _load_edges(self):
        """Load semantic relations: HYPERNYM, HYPONYM, HOLONYM, etc."""
        csv_path = self.data_path / "trwordnet_edges_v0_1_0.csv"
        if not csv_path.exists():
            return

        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                src = row['src']
                dst = row['dst']
                edge_type = row['edge_type']

                if src not in self._edges:
                    self._edges[src] = []
                self._edges[src].append((dst, edge_type))

    def _load_literal_graph(self):
        """Load synonym relationships between literals"""
        csv_path = self.data_path / "trwordnet_literal_graph_v0_1_0.csv"
        if not csv_path.exists():
            return

        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                literal_a = row['literal_a']
                literal_b = row['literal_b']

                if literal_a in self._literal_graph:
                    self._literal_graph[literal_a].add(literal_b)
                if literal_b in self._literal_graph:
                    self._literal_graph[literal_b].add(literal_a)

    def get_synset(self, synset_id: str) -> Optional[Dict]:
        """Get synset definition and metadata"""
        return self._synsets.get(synset_id)

    def get_literals(self, synset_id: str) -> List[Dict]:
        """Get all literals for a synset with sense/origin info"""
        return self._literals.get(synset_id, [])

    def get_hypernyms(self, synset_id: str) -> List[str]:
        """Get hypernym synsets (more general concepts)"""
        edges = self._edges.get(synset_id, [])
        return [dst for dst, edge_type in edges if edge_type == 'HYPERNYM']

    def get_hyponyms(self, synset_id: str) -> List[str]:
        """Get hyponym synsets (more specific concepts)"""
        edges = self._edges.get(synset_id, [])
        return [dst for dst, edge_type in edges if edge_type == 'HYPONYM']

    def get_holonyms(self, synset_id: str) -> List[Tuple[str, str]]:
        """Get holonym synsets (whole-part relations)"""
        edges = self._edges.get(synset_id, [])
        return [(dst, edge_type) for dst, edge_type in edges
                if 'HOLONYM' in edge_type]

    def get_synonyms(self, literal: str) -> Set[str]:
        """Get synonyms for a literal from literal graph"""
        return self._literal_graph.get(literal, set())

    def find_path_to_root(self, synset_id: str) -> List[str]:
        """Find hypernym path to root (for semantic similarity)"""
        path = [synset_id]
        current = synset_id

        while True:
            hypernyms = self.get_hypernyms(current)
            if not hypernyms:
                break
            current = hypernyms[0]  # Take first hypernym
            path.append(current)

        return path

    def get_statistics(self) -> Dict:
        """Get dataset statistics"""
        return {
            'synsets': len(self._synsets),
            'literals': len(self._literals),
            'edges': sum(len(edges) for edges in self._edges.values()),
            'literal_relations': sum(len(syms) for syms in self._literal_graph.values()) // 2
        }


# Backward compatibility with original WordNet
if __name__ == "__main__":
    wn = EnhancedWordNet()
    stats = wn.get_statistics()
    print(f"Enhanced Turkish WordNet Statistics:")
    print(f"  Synsets: {stats['synsets']:,}")
    print(f"  Literals: {stats['literals']:,}")
    print(f"  Semantic edges: {stats['edges']:,}")
    print(f"  Literal relations: {stats['literal_relations']:,}")
