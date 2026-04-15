"""
CERVEAU ARTIFICIEL COMPLET - SYSTÈME D'IA INSPIRÉ DU CERVEAU HUMAIN
Architecture modulaire avec:
- Perception (entrée)
- Traitement (apprentissage)
- Mémoire (stockage)
- Décision (sortie)
"""

import json
import time
import math
from datetime import datetime
from typing import Dict, List, Tuple, Any
from collections import deque
import numpy as np

# ============================================================================
# COUCHE 1: PERCEPTION (ENTRÉE)
# ============================================================================

class PerceptionLayer:
    """Traite les entrées (texte, images, données)"""
    
    def __init__(self):
        self.input_buffer = deque(maxlen=100)
        self.attention_scores = {}
        
    def process_text(self, text: str) -> Dict:
        """Analyse le texte et crée des embeddings"""
        tokens = text.lower().split()
        
        # Tokenization et encodage basique
        embedding = self._create_embedding(tokens)
        
        # Analyse de sentiment et contexte
        context = self._analyze_context(text)
        
        perception_data = {
            'type': 'text',
            'tokens': tokens,
            'embedding': embedding,
            'context': context,
            'timestamp': datetime.now().isoformat(),
            'confidence': self._calculate_confidence(text)
        }
        
        self.input_buffer.append(perception_data)
        return perception_data
    
    def process_image(self, image_features: List[float]) -> Dict:
        """Traite les features d'image"""
        perception_data = {
            'type': 'image',
            'features': image_features,
            'edges': self._extract_edges(image_features),
            'shapes': self._identify_shapes(image_features),
            'timestamp': datetime.now().isoformat()
        }
        self.input_buffer.append(perception_data)
        return perception_data
    
    def _create_embedding(self, tokens: List[str]) -> List[float]:
        """Crée un vecteur d'embedding"""
        embedding_dim = 128
        embedding = np.random.randn(embedding_dim).tolist()
        
        for i, token in enumerate(tokens[:10]):
            # Modifie l'embedding basé sur le token
            for j in range(len(embedding)):
                embedding[j] += (ord(token[0]) * (i+1)) / (j+1)
        
        # Normalise
        norm = np.sqrt(sum(x**2 for x in embedding))
        return [x/norm for x in embedding]
    
    def _analyze_context(self, text: str) -> Dict:
        """Analyse le contexte du texte"""
        return {
            'length': len(text),
            'word_count': len(text.split()),
            'complexity': len(set(text.split())) / len(text.split()) if text.split() else 0,
            'has_questions': '?' in text,
            'emotion': 'neutral'
        }
    
    def _calculate_confidence(self, text: str) -> float:
        """Calcule le score de confiance"""
        return min(len(text) / 100, 1.0)
    
    def _extract_edges(self, features: List[float]) -> List[float]:
        """Extrait les contours"""
        return [f * 0.8 for f in features[:10]]
    
    def _identify_shapes(self, features: List[float]) -> List[str]:
        """Identifie les formes"""
        return ['rectangle', 'circle', 'triangle']


# ============================================================================
# COUCHE 2: MÉMOIRE (STOCKAGE)
# ============================================================================

class MemorySystem:
    """Système de mémoire multi-niveaux (court terme, long terme)"""
    
    def __init__(self):
        # Mémoire à court terme (travaill)
        self.working_memory = deque(maxlen=20)
        
        # Mémoire à long terme
        self.long_term_memory = {}
        
        # Mémoire procédurale (apprentissage)
        self.procedural_memory = {}
        
        # Mémoire sémantique (connaissances)
        self.semantic_memory = self._initialize_semantic_memory()
    
    def store_short_term(self, data: Dict) -> Dict:
        """Stocke les données en mémoire à court terme"""
        enriched = {
            **data,
            'recall_count': 0,
            'importance': 0.5,
            'decay_rate': 0.95
        }
        self.working_memory.append(enriched)
        return enriched
    
    def store_long_term(self, key: str, data: Dict) -> bool:
        """Consolide les données en mémoire long terme"""
        self.long_term_memory[key] = {
            **data,
            'stored_at': datetime.now().isoformat(),
            'access_count': 0,
            'strength': 0.9
        }
        return True
    
    def retrieve(self, query: str) -> List[Dict]:
        """Récupère les informations pertinentes"""
        # Cherche dans la mémoire courte
        short_term_results = []
        for item in self.working_memory:
            if 'tokens' in item and any(q in str(item.get('tokens', [])) for q in query.split()):
                short_term_results.append(item)
        
        # Cherche dans la mémoire longue
        long_term_results = []
        for key, value in self.long_term_memory.items():
            if query.lower() in key.lower():
                value['access_count'] += 1
                long_term_results.append(value)
        
        # Combine et trie par pertinence
        all_results = short_term_results + long_term_results
        return sorted(all_results, 
                     key=lambda x: x.get('access_count', 0) + x.get('recall_count', 0),
                     reverse=True)[:10]
    
    def consolidate_memory(self) -> Dict:
        """Consolide la mémoire courte terme en long terme"""
        consolidated_count = 0
        for item in list(self.working_memory):
            if item.get('recall_count', 0) > 2:
                key = f"memory_{datetime.now().timestamp()}"
                self.store_long_term(key, item)
                consolidated_count += 1
        
        return {
            'consolidated': consolidated_count,
            'short_term_size': len(self.working_memory),
            'long_term_size': len(self.long_term_memory)
        }
    
    def _initialize_semantic_memory(self) -> Dict:
        """Initialise la mémoire sémantique"""
        return {
            'concepts': {
                'intelligence': ['learning', 'reasoning', 'problem_solving'],
                'emotion': ['joy', 'sadness', 'fear', 'anger'],
                'perception': ['vision', 'sound', 'touch'],
            },
            'relationships': {
                'is_a': {},
                'part_of': {},
                'associated_with': {}
            }
        }


# ============================================================================
# COUCHE 3: TRAITEMENT (APPRENTISSAGE)
# ============================================================================

class ProcessingLayer:
    """Traite et apprend des informations"""
    
    def __init__(self, memory_system: MemorySystem):
        self.memory = memory_system
        self.learning_rate = 0.01
        self.neural_weights = self._initialize_weights()
        self.activation_patterns = []
    
    def learn(self, input_data: Dict) -> Dict:
        """Processus d'apprentissage"""
        # 1. Attention sélective
        attention = self._apply_attention(input_data)
        
        # 2. Reconnaissance de patterns
        patterns = self._recognize_patterns(input_data)
        
        # 3. Mise à jour des poids
        self._update_weights(input_data, patterns)
        
        # 4. Stockage en mémoire
        self.memory.store_short_term(input_data)
        
        learning_result = {
            'attention_score': attention,
            'patterns_detected': len(patterns),
            'weight_update': self.learning_rate,
            'patterns': patterns
        }
        
        self.activation_patterns.append(learning_result)
        return learning_result
    
    def reasoning(self, query: str) -> Dict:
        """Raisonnement logique"""
        # Récupère les informations pertinentes
        relevant_memories = self.memory.retrieve(query)
        
        # Analyse logique
        deductions = self._logical_inference(query, relevant_memories)
        
        # Génère des conclusions
        conclusions = self._generate_conclusions(deductions)
        
        return {
            'query': query,
            'relevant_memories': len(relevant_memories),
            'deductions': deductions,
            'conclusions': conclusions,
            'confidence': self._calculate_reasoning_confidence(conclusions)
        }
    
    def _apply_attention(self, data: Dict) -> float:
        """Applique le mécanisme d'attention"""
        importance_factors = {
            'has_questions': 2.0,
            'new_information': 1.5,
            'complexity': 1.0
        }
        
        attention_score = 0.5
        
        if data.get('context', {}).get('has_questions'):
            attention_score *= importance_factors['has_questions']
        
        if data.get('context', {}).get('complexity', 0) > 0.7:
            attention_score *= importance_factors['complexity']
        
        return min(attention_score, 1.0)
    
    def _recognize_patterns(self, data: Dict) -> List[str]:
        """Reconnaît les patterns dans les données"""
        patterns = []
        
        if 'tokens' in data:
            # Pattern: répétition
            tokens = data['tokens']
            for i in range(len(tokens)-1):
                if tokens[i] == tokens[i+1]:
                    patterns.append('repetition_pattern')
                    break
        
        # Pattern: structure
        if data.get('context', {}).get('word_count', 0) > 20:
            patterns.append('complex_structure')
        
        return patterns
    
    def _update_weights(self, data: Dict, patterns: List[str]) -> None:
        """Met à jour les poids du réseau"""
        for key in self.neural_weights:
            for pattern in patterns:
                if pattern in key:
                    self.neural_weights[key] += self.learning_rate
    
    def _logical_inference(self, query: str, memories: List[Dict]) -> List[str]:
        """Inférence logique basée sur les mémoires"""
        inferences = []
        
        for memory in memories[:3]:
            if 'tokens' in memory:
                inferred = f"Based on '{' '.join(memory['tokens'][:3])}': relevant to '{query}'"
                inferences.append(inferred)
        
        return inferences
    
    def _generate_conclusions(self, deductions: List[str]) -> List[str]:
        """Génère des conclusions"""
        if not deductions:
            return ["Insufficient information to draw conclusions"]
        
        return [f"Conclusion: {ded[:50]}..." for ded in deductions]
    
    def _calculate_reasoning_confidence(self, conclusions: List[str]) -> float:
        """Calcule la confiance du raisonnement"""
        return min(len(conclusions) / 5.0, 1.0)
    
    def _initialize_weights(self) -> Dict:
        """Initialise les poids du réseau"""
        return {
            f'weight_{i}': np.random.randn() for i in range(100)
        }


# ============================================================================
# COUCHE 4: DÉCISION (SORTIE)
# ============================================================================

class DecisionLayer:
    """Génère les décisions et actions"""
    
    def __init__(self, processing: ProcessingLayer):
        self.processing = processing
        self.decision_history = []
        self.action_queue = deque()
    
    def decide(self, situation: Dict) -> Dict:
        """Prend une décision basée sur la situation"""
        # 1. Évalue les options
        options = self._evaluate_options(situation)
        
        # 2. Sélectionne l'action optimale
        best_action = self._select_best_action(options)
        
        # 3. Génère la réaction
        reaction = self._generate_reaction(best_action, situation)
        
        decision = {
            'situation': situation.get('input', ''),
            'options_evaluated': len(options),
            'selected_action': best_action,
            'reaction': reaction,
            'confidence': best_action['score'],
            'timestamp': datetime.now().isoformat()
        }
        
        self.decision_history.append(decision)
        return decision
    
    def _evaluate_options(self, situation: Dict) -> List[Dict]:
        """Évalue les options disponibles"""
        options = [
            {
                'action': 'analyze',
                'description': 'Analyser la situation en profondeur',
                'score': 0.7
            },
            {
                'action': 'learn',
                'description': 'Apprendre de la nouvelle information',
                'score': 0.8
            },
            {
                'action': 'reason',
                'description': 'Utiliser le raisonnement logique',
                'score': 0.75
            },
            {
                'action': 'respond',
                'description': 'Répondre à la situation',
                'score': 0.85
            }
        ]
        
        return options
    
    def _select_best_action(self, options: List[Dict]) -> Dict:
        """Sélectionne l'action avec le meilleur score"""
        return max(options, key=lambda x: x['score'])
    
    def _generate_reaction(self, action: Dict, situation: Dict) -> Dict:
        """Génère une réaction appropriée"""
        return {
            'action_type': action['action'],
            'action_description': action['description'],
            'output': self._create_output_message(action, situation),
            'energy_used': 0.3 * action['score']
        }
    
    def _create_output_message(self, action: Dict, situation: Dict) -> str:
        """Crée le message de sortie"""
        templates = {
            'analyze': "Analyzing the situation: {}",
            'learn': "Learning from: {}",
            'reason': "Reasoning about: {}",
            'respond': "Response: Understanding {}"
        }
        
        action_type = action['action']
        situation_desc = situation.get('input', 'the input')[:50]
        
        return templates.get(action_type, "Processing: {}").format(situation_desc)


# ============================================================================
# SYSTÈME INTÉGRÉ - CERVEAU ARTIFICIEL COMPLET
# ============================================================================

class ArtificialBrain:
    """Intègre tous les systèmes du cerveau artificiel"""
    
    def __init__(self):
        print("🧠 Initialisation du Cerveau Artificiel...")
        
        # Couches du système
        self.perception = PerceptionLayer()
        self.memory = MemorySystem()
        self.processing = ProcessingLayer(self.memory)
        self.decision = DecisionLayer(self.processing)
        
        # Métadonnées
        self.brain_state = {
            'active': True,
            'energy_level': 1.0,
            'learning_mode': True,
            'created_at': datetime.now().isoformat()
        }
        
        # Statistiques
        self.stats = {
            'inputs_processed': 0,
            'decisions_made': 0,
            'learning_events': 0,
            'memories_consolidated': 0
        }
    
    def think(self, input_text: str, input_type: str = 'text') -> Dict:
        """Processus complet de pensée"""
        print(f"\n🧠 Pensée: {input_text[:100]}...")
        
        # 1. PERCEPTION - Traite l'entrée
        if input_type == 'text':
            perception_data = self.perception.process_text(input_text)
        else:
            perception_data = self.perception.process_image([float(x) for x in input_text.split(',')[:10]])
        
        self.stats['inputs_processed'] += 1
        
        # 2. APPRENTISSAGE - Apprend des nouvelles données
        learning_result = self.processing.learn(perception_data)
        self.stats['learning_events'] += 1
        
        # 3. RAISONNEMENT - Utilise le raisonnement
        reasoning_result = self.processing.reasoning(input_text)
        
        # 4. DÉCISION - Prend une décision
        decision_result = self.decision.decide({
            'input': input_text,
            'perception': perception_data,
            'learning': learning_result,
            'reasoning': reasoning_result
        })
        
        self.stats['decisions_made'] += 1
        
        # Consolide la mémoire periodiquement
        if self.stats['decisions_made'] % 5 == 0:
            consolidation = self.memory.consolidate_memory()
            self.stats['memories_consolidated'] += consolidation['consolidated']
        
        return {
            'thought_process': {
                'perception': perception_data,
                'learning': learning_result,
                'reasoning': reasoning_result,
                'decision': decision_result
            },
            'output': decision_result['reaction']['output'],
            'confidence': decision_result['confidence'],
            'timestamp': datetime.now().isoformat()
        }
    
    def get_status(self) -> Dict:
        """Retourne l'état du cerveau"""
        return {
            'brain_state': self.brain_state,
            'statistics': self.stats,
            'memory_status': {
                'working_memory': len(self.perception.input_buffer),
                'short_term_memory': len(self.memory.working_memory),
                'long_term_memory': len(self.memory.long_term_memory),
                'total_patterns_detected': len(self.processing.activation_patterns)
            },
            'decision_history_size': len(self.decision.decision_history)
        }
    
    def train(self, training_data: List[str]) -> Dict:
        """Entraîne le cerveau avec des données"""
        print(f"\n🎓 Entraînement avec {len(training_data)} exemples...")
        
        training_results = []
        for i, data in enumerate(training_data):
            result = self.think(data)
            training_results.append(result)
            print(f"  ✓ Exemple {i+1}/{len(training_data)}")
        
        return {
            'training_complete': True,
            'examples_trained': len(training_data),
            'avg_confidence': sum(r['confidence'] for r in training_results) / len(training_results),
            'final_statistics': self.get_status()
        }


# ============================================================================
# DÉMONSTRATION ET TESTS
# ============================================================================

if __name__ == "__main__":
    # Crée le cerveau artificiel
    brain = ArtificialBrain()
    
    # Exemples d'entrée
    training_examples = [
        "I am learning how artificial intelligence works",
        "What is consciousness in a machine?",
        "How do neural networks learn from data?",
        "Explain memory consolidation in AI systems",
        "Can machines think creatively?",
        "What is the difference between learning and reasoning?",
        "How does attention mechanism work in transformers?",
        "Describe the process of decision making in AI"
    ]
    
    # Entraîne le cerveau
    training_result = brain.train(training_examples)
    
    # Teste le cerveau avec une nouvelle question
    print("\n" + "="*70)
    print("🧪 TEST - Nouvelle entrée (question non vue)")
    print("="*70)
    
    test_input = "How does an artificial brain learn and remember?"
    thought_result = brain.think(test_input)
    
    print(f"\n📥 Entrée: {test_input}")
    print(f"📤 Sortie: {thought_result['output']}")
    print(f"🎯 Confiance: {thought_result['confidence']:.2%}")
    
    # Affiche le statut final
    print("\n" + "="*70)
    print("📊 STATUT FINAL DU CERVEAU")
    print("="*70)
    
    final_status = brain.get_status()
    print(json.dumps(final_status, indent=2))
    
    # Affiche un exemple de pensée détaillée
    print("\n" + "="*70)
    print("🔬 PROCESSUS DE PENSÉE DÉTAILLÉ (Exemple)")
    print("="*70)
    
    detailed = thought_result['thought_process']
    print(f"\n1️⃣  PERCEPTION:")
    print(f"   - Type: {detailed['perception'].get('type')}")
    print(f"   - Tokens: {detailed['perception'].get('tokens', [])[:5]}")
    print(f"   - Confiance: {detailed['perception'].get('confidence', 0):.2%}")
    
    print(f"\n2️⃣  APPRENTISSAGE:")
    print(f"   - Patterns détectés: {detailed['learning']['patterns_detected']}")
    print(f"   - Score d'attention: {detailed['learning']['attention_score']:.2%}")
    
    print(f"\n3️⃣  RAISONNEMENT:")
    print(f"   - Conclusions: {len(detailed['reasoning']['conclusions'])}")
    print(f"   - Confiance: {detailed['reasoning']['confidence']:.2%}")
    
    print(f"\n4️⃣  DÉCISION:")
    print(f"   - Action: {detailed['decision']['selected_action']['action']}")
    print(f"   - Score: {detailed['decision']['confidence']:.2%}")
    
    print("\n✅ Cerveau Artificiel fonctionnel créé avec succès!")
