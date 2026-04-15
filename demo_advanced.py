#!/usr/bin/env python3
"""
DÉMONSTRATION AVANCÉE - Cerveau Artificiel Complet
Showcase des capacités principales du système
"""

from artificial_brain_system import ArtificialBrain
import json
from datetime import datetime

def print_header(title):
    """Affiche un header stylisé"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def print_section(title):
    """Affiche une section"""
    print(f"\n{title}")
    print("-" * 70)

def demo_1_basic_thinking():
    """Démo 1: Pensée basique"""
    print_header("DÉMO 1: Pensée Basique")
    
    brain = ArtificialBrain()
    
    questions = [
        "What is artificial intelligence?",
        "How do neural networks work?",
        "Explain machine learning in simple terms"
    ]
    
    for i, question in enumerate(questions, 1):
        print_section(f"Question {i}: {question}")
        
        result = brain.think(question)
        
        print(f"  Entrée: {result['thought_process']['perception']['tokens'][:5]}")
        print(f"  Sortie: {result['output']}")
        print(f"  Confiance: {result['confidence']:.2%}")

def demo_2_learning_and_memory():
    """Démo 2: Apprentissage et Mémoire"""
    print_header("DÉMO 2: Apprentissage et Mémoire")
    
    brain = ArtificialBrain()
    
    # Données d'apprentissage
    training_data = [
        "Deep learning uses neural networks with many layers",
        "Convolutional networks are excellent for image processing",
        "Recurrent networks are designed for sequential data",
        "Transformers revolutionized natural language processing",
        "Attention mechanisms allow models to focus on important features",
        "Transfer learning enables reuse of pre-trained models",
        "Backpropagation is the key algorithm for training networks",
        "Regularization prevents overfitting in machine learning"
    ]
    
    print_section("Phase 1: Entraînement")
    print(f"  Nombre d'exemples: {len(training_data)}")
    
    training_result = brain.train(training_data)
    
    print(f"  Entraînement complété: {training_result['training_complete']}")
    print(f"  Confiance moyenne: {training_result['avg_confidence']:.2%}")
    
    # Informations sur la mémoire
    print_section("Phase 2: État de la Mémoire")
    status = brain.get_status()
    memory = status['memory_status']
    
    print(f"  Mémoire de travail: {memory['working_memory']} items")
    print(f"  Mémoire long terme: {memory['long_term_memory']} items")
    print(f"  Patterns détectés: {memory['total_patterns_detected']}")
    
    # Consolidation
    print_section("Phase 3: Consolidation de Mémoire")
    consolidation = brain.memory.consolidate_memory()
    
    print(f"  Items consolidés: {consolidation['consolidated']}")
    print(f"  Nouvelle taille mémoire court terme: {consolidation['short_term_size']}")
    print(f"  Nouvelle taille mémoire long terme: {consolidation['long_term_size']}")
    
    # Récherche
    print_section("Phase 4: Recherche dans la Mémoire")
    results = brain.memory.retrieve("neural network")
    
    print(f"  Requête: 'neural network'")
    print(f"  Résultats trouvés: {len(results)}")
    if results:
        print(f"  Premier résultat: {str(results[0])[:100]}...")

def demo_3_reasoning_and_inference():
    """Démo 3: Raisonnement et Inférence"""
    print_header("DÉMO 3: Raisonnement et Inférence")
    
    brain = ArtificialBrain()
    
    # Entraîner d'abord
    print_section("Préparation (Entraînement)")
    brain.train([
        "All mammals are animals",
        "Dogs are mammals",
        "Cats are mammals",
        "Elephants are mammals",
        "Birds are animals but not mammals"
    ])
    print("  ✓ Cerveau entraîné")
    
    # Raisonnement
    print_section("Raisonnement Logique")
    
    queries = [
        "What is a dog?",
        "Are cats animals?",
        "What are mammals?"
    ]
    
    for query in queries:
        print(f"\n  Requête: {query}")
        reasoning = brain.processing.reasoning(query)
        
        print(f"  Mémoires pertinentes trouvées: {reasoning['relevant_memories']}")
        print(f"  Conclusions générées: {len(reasoning['conclusions'])}")
        print(f"  Confiance: {reasoning['confidence']:.2%}")
        
        for i, conclusion in enumerate(reasoning['conclusions'][:2], 1):
            print(f"    {i}. {conclusion}")

def demo_4_decision_making():
    """Démo 4: Prise de Décision"""
    print_header("DÉMO 4: Prise de Décision")
    
    brain = ArtificialBrain()
    
    situations = [
        "Received a complex technical problem to solve",
        "Need to make an important business decision",
        "Encountered unexpected error in the system",
        "Must choose between multiple options"
    ]
    
    print_section("Évaluation des Situations")
    
    for i, situation in enumerate(situations, 1):
        print(f"\n  Situation {i}: {situation}")
        
        decision = brain.decision.decide({'input': situation})
        
        print(f"    Action sélectionnée: {decision['selected_action']['action']}")
        print(f"    Description: {decision['selected_action']['description']}")
        print(f"    Confiance: {decision['confidence']:.2%}")

def demo_5_advanced_analysis():
    """Démo 5: Analyse Avancée"""
    print_header("DÉMO 5: Analyse Avancée du Système")
    
    brain = ArtificialBrain()
    
    # Processus complet
    print_section("Processus Complet de Pensée")
    
    complex_input = "How does the human brain process visual information?"
    
    print(f"  Entrée: {complex_input}\n")
    
    # 1. Perception
    print("  1️⃣  PERCEPTION")
    perception = brain.perception.process_text(complex_input)
    print(f"     - Tokens: {perception['tokens']}")
    print(f"     - Type: {perception['type']}")
    print(f"     - Confiance: {perception['confidence']:.2%}")
    print(f"     - Complexité: {perception['context']['complexity']:.2%}")
    
    # 2. Apprentissage
    print("\n  2️⃣  APPRENTISSAGE")
    learning = brain.processing.learn(perception)
    print(f"     - Score d'attention: {learning['attention_score']:.2%}")
    print(f"     - Patterns détectés: {learning['patterns_detected']}")
    print(f"     - Taux d'apprentissage: {learning['weight_update']}")
    
    # 3. Mémoire
    print("\n  3️⃣  MÉMOIRE")
    memory_status = brain.memory.consolidate_memory()
    print(f"     - Mémoire de travail: {len(brain.memory.working_memory)}")
    print(f"     - Mémoire long terme: {len(brain.memory.long_term_memory)}")
    
    # 4. Raisonnement
    print("\n  4️⃣  RAISONNEMENT")
    reasoning = brain.processing.reasoning(complex_input)
    print(f"     - Mémoires pertinentes: {reasoning['relevant_memories']}")
    print(f"     - Conclusions: {len(reasoning['conclusions'])}")
    print(f"     - Confiance: {reasoning['confidence']:.2%}")
    
    # 5. Décision
    print("\n  5️⃣  DÉCISION")
    decision = brain.decision.decide({'input': complex_input})
    print(f"     - Action: {decision['selected_action']['action']}")
    print(f"     - Réaction: {decision['reaction']['output'][:80]}...")
    print(f"     - Confiance: {decision['confidence']:.2%}")

def demo_6_statistics_and_monitoring():
    """Démo 6: Statistiques et Monitoring"""
    print_header("DÉMO 6: Statistiques et Monitoring")
    
    brain = ArtificialBrain()
    
    # Entraîner avec un flux de données
    print_section("Traitement d'un Flux de Données")
    
    data_stream = [
        "First piece of information",
        "Second important detail",
        "Third interesting data",
        "Fourth key insight",
        "Fifth valuable knowledge"
    ]
    
    for i, data in enumerate(data_stream, 1):
        result = brain.think(data)
        print(f"  Entrée {i}: {data[:40]}... | Confiance: {result['confidence']:.2%}")
    
    # Afficher les statistiques
    print_section("Statistiques Finales")
    
    stats = brain.get_status()
    stats_data = stats['statistics']
    
    print(f"  Inputs traités: {stats_data['inputs_processed']}")
    print(f"  Décisions prises: {stats_data['decisions_made']}")
    print(f"  Événements d'apprentissage: {stats_data['learning_events']}")
    print(f"  Consolidations mémoire: {stats_data['memories_consolidated']}")
    
    # État du cerveau
    print_section("État du Cerveau")
    brain_state = stats['brain_state']
    
    print(f"  État: {'ACTIF' if brain_state['active'] else 'INACTIF'}")
    print(f"  Niveau d'énergie: {brain_state['energy_level']:.2%}")
    print(f"  Mode apprentissage: {'ON' if brain_state['learning_mode'] else 'OFF'}")
    
    # Memory Status
    print_section("État de la Mémoire")
    memory = stats['memory_status']
    
    print(f"  Mémoire de travail: {memory['working_memory']} items")
    print(f"  Mémoire court terme: {memory['short_term_memory']} items")
    print(f"  Mémoire long terme: {memory['long_term_memory']} items")
    print(f"  Patterns détectés: {memory['total_patterns_detected']}")
    print(f"  Historique décisions: {stats['decision_history_size']}")

def demo_7_performance_benchmark():
    """Démo 7: Benchmark de Performance"""
    print_header("DÉMO 7: Benchmark de Performance")
    
    import time
    
    brain = ArtificialBrain()
    
    # Test 1: Vitesse de pensée
    print_section("Test 1: Vitesse de Pensée")
    
    start = time.time()
    for i in range(10):
        brain.think(f"Test input number {i}")
    elapsed = time.time() - start
    
    print(f"  10 pensées traitées en {elapsed:.3f}s")
    print(f"  Moyenne: {elapsed/10*1000:.2f}ms par pensée")
    print(f"  Débit: {10/elapsed:.1f} pensées/seconde")
    
    # Test 2: Consommation mémoire
    print_section("Test 2: Consommation Mémoire")
    
    status = brain.get_status()
    memory = status['memory_status']
    
    total_items = (memory['working_memory'] + 
                   memory['short_term_memory'] + 
                   memory['long_term_memory'])
    
    print(f"  Items en mémoire: {total_items}")
    print(f"  Mémoire de travail: {memory['working_memory']}")
    print(f"  Mémoire court terme: {memory['short_term_memory']}")
    print(f"  Mémoire long terme: {memory['long_term_memory']}")
    
    # Test 3: Scalabilité
    print_section("Test 3: Scalabilité d'Apprentissage")
    
    sizes = [10, 20, 50]
    
    for size in sizes:
        training_data = [f"Training example number {i}" for i in range(size)]
        
        start = time.time()
        brain.train(training_data)
        elapsed = time.time() - start
        
        print(f"  {size} exemples en {elapsed:.3f}s ({elapsed/size*1000:.2f}ms par exemple)")

def main():
    """Exécute toutes les démos"""
    
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║  DÉMONSTRATION COMPLÈTE - CERVEAU ARTIFICIEL v1.0         ║
    ║  Advanced AI System Inspired by the Human Brain           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Exécuter les démos
        demo_1_basic_thinking()
        demo_2_learning_and_memory()
        demo_3_reasoning_and_inference()
        demo_4_decision_making()
        demo_5_advanced_analysis()
        demo_6_statistics_and_monitoring()
        demo_7_performance_benchmark()
        
        # Résumé final
        print_header("RÉSUMÉ FINAL")
        print("""
        ✅ Toutes les démos ont été exécutées avec succès!
        
        Ce système démontre:
        🧠 Perception avancée du texte et des images
        🧠 Système de mémoire multi-niveaux (comme le cerveau)
        🧠 Apprentissage continu et adaptation
        🧠 Raisonnement logique et inférence
        🧠 Prise de décision intelligente
        🧠 Performance et scalabilité
        
        Prochaines étapes:
        1. Lancer l'API: python brain_api_server.py
        2. Utiliser l'interface web (React)
        3. Intégrer dans votre application
        
        Documentation complète: voir README.md et DOCUMENTATION.md
        """)
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
