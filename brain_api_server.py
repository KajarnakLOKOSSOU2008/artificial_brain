"""
API BACKEND - Cerveau Artificiel
Flask API exposant le système complet du cerveau artificiel
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
from artificial_brain_system import ArtificialBrain

# Initialisation
app = Flask(__name__)
CORS(app)

# Instance globale du cerveau
brain = None

def init_brain():
    """Initialise le cerveau artificiel"""
    global brain
    if brain is None:
        brain = ArtificialBrain()
        print("✅ Cerveau artificiel initialisé")
    return brain


# ============================================================================
# ROUTES API
# ============================================================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Vérifie l'état du serveur"""
    return jsonify({
        'status': 'healthy',
        'brain_initialized': brain is not None,
        'timestamp': datetime.now().isoformat()
    })


@app.route('/api/brain/init', methods=['POST'])
def initialize_brain():
    """Initialise le cerveau artificiel"""
    try:
        global brain
        brain = ArtificialBrain()
        return jsonify({
            'success': True,
            'message': 'Cerveau artificiel initialisé',
            'brain_state': brain.get_status()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/think', methods=['POST'])
def think():
    """Envoie une pensée au cerveau"""
    try:
        init_brain()
        
        data = request.json
        input_text = data.get('input', '')
        input_type = data.get('type', 'text')
        
        if not input_text:
            return jsonify({
                'success': False,
                'error': 'Input cannot be empty'
            }), 400
        
        # Processus de pensée
        result = brain.think(input_text, input_type)
        
        return jsonify({
            'success': True,
            'thought': {
                'input': input_text,
                'output': result['output'],
                'confidence': result['confidence'],
                'process': {
                    'perception_confidence': result['thought_process']['perception'].get('confidence', 0),
                    'patterns_detected': result['thought_process']['learning']['patterns_detected'],
                    'reasoning_conclusions': len(result['thought_process']['reasoning']['conclusions']),
                    'decision_action': result['thought_process']['decision']['selected_action']['action']
                },
                'timestamp': result['timestamp']
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/status', methods=['GET'])
def get_status():
    """Retourne l'état du cerveau"""
    try:
        init_brain()
        status = brain.get_status()
        return jsonify({
            'success': True,
            'status': status
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/memory', methods=['GET'])
def get_memory_info():
    """Retourne des infos sur le système de mémoire"""
    try:
        init_brain()
        
        return jsonify({
            'success': True,
            'memory': {
                'working_memory_size': len(brain.memory.working_memory),
                'long_term_memory_size': len(brain.memory.long_term_memory),
                'semantic_concepts': len(brain.memory.semantic_memory.get('concepts', {})),
                'memory_types': {
                    'working': list(brain.memory.working_memory)[:5] if brain.memory.working_memory else [],
                    'long_term_keys': list(brain.memory.long_term_memory.keys())[:10]
                }
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/search', methods=['POST'])
def search_memory():
    """Cherche dans la mémoire"""
    try:
        init_brain()
        
        data = request.json
        query = data.get('query', '')
        
        if not query:
            return jsonify({
                'success': False,
                'error': 'Query cannot be empty'
            }), 400
        
        results = brain.memory.retrieve(query)
        
        return jsonify({
            'success': True,
            'query': query,
            'results_found': len(results),
            'results': results[:10]
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/learn', methods=['POST'])
def train_brain():
    """Entraîne le cerveau avec plusieurs exemples"""
    try:
        init_brain()
        
        data = request.json
        training_data = data.get('training_data', [])
        
        if not training_data:
            return jsonify({
                'success': False,
                'error': 'Training data cannot be empty'
            }), 400
        
        training_result = brain.train(training_data)
        
        return jsonify({
            'success': True,
            'training': training_result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/reason', methods=['POST'])
def reason():
    """Utilise le raisonnement pour répondre"""
    try:
        init_brain()
        
        data = request.json
        query = data.get('query', '')
        
        if not query:
            return jsonify({
                'success': False,
                'error': 'Query cannot be empty'
            }), 400
        
        reasoning_result = brain.processing.reasoning(query)
        
        return jsonify({
            'success': True,
            'reasoning': reasoning_result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/decision', methods=['POST'])
def make_decision():
    """Fait une décision basée sur la situation"""
    try:
        init_brain()
        
        data = request.json
        situation = data.get('situation', {})
        
        if not situation:
            return jsonify({
                'success': False,
                'error': 'Situation cannot be empty'
            }), 400
        
        decision_result = brain.decision.decide(situation)
        
        return jsonify({
            'success': True,
            'decision': decision_result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/consolidate', methods=['POST'])
def consolidate_memory():
    """Consolide la mémoire courte terme en long terme"""
    try:
        init_brain()
        
        consolidation_result = brain.memory.consolidate_memory()
        
        return jsonify({
            'success': True,
            'consolidation': consolidation_result,
            'memory_status': {
                'working_memory': len(brain.memory.working_memory),
                'long_term_memory': len(brain.memory.long_term_memory)
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/stats', methods=['GET'])
def get_statistics():
    """Retourne les statistiques du cerveau"""
    try:
        init_brain()
        
        stats = brain.get_status()
        
        return jsonify({
            'success': True,
            'statistics': {
                'inputs_processed': stats['statistics']['inputs_processed'],
                'decisions_made': stats['statistics']['decisions_made'],
                'learning_events': stats['statistics']['learning_events'],
                'memories_consolidated': stats['statistics']['memories_consolidated'],
                'brain_state': stats['brain_state'],
                'memory_summary': stats['memory_status']
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/perception', methods=['POST'])
def process_perception():
    """Traite une entrée perceptuelle"""
    try:
        init_brain()
        
        data = request.json
        input_data = data.get('input', '')
        input_type = data.get('type', 'text')
        
        if input_type == 'text':
            perception = brain.perception.process_text(input_data)
        else:
            perception = brain.perception.process_image([float(x) for x in input_data.split(',')[:10]])
        
        return jsonify({
            'success': True,
            'perception': perception
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/brain/process', methods=['POST'])
def process():
    """Traite et apprend des données"""
    try:
        init_brain()
        
        data = request.json
        input_text = data.get('input', '')
        
        # Perception
        perception = brain.perception.process_text(input_text)
        
        # Learning
        learning = brain.processing.learn(perception)
        
        # Reasoning
        reasoning = brain.processing.reasoning(input_text)
        
        return jsonify({
            'success': True,
            'processing': {
                'perception': {
                    'type': perception['type'],
                    'tokens': perception['tokens'][:10],
                    'confidence': perception['confidence']
                },
                'learning': {
                    'patterns_detected': learning['patterns_detected'],
                    'attention_score': learning['attention_score']
                },
                'reasoning': {
                    'conclusions': len(reasoning['conclusions']),
                    'confidence': reasoning['confidence']
                }
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# ============================================================================
# ROUTES UTILITAIRES
# ============================================================================

@app.route('/api/system/info', methods=['GET'])
def system_info():
    """Infos système"""
    return jsonify({
        'name': 'Artificial Brain API',
        'version': '1.0.0',
        'description': 'API pour le Cerveau Artificiel Complet',
        'endpoints': [
            '/api/health',
            '/api/brain/init',
            '/api/brain/think',
            '/api/brain/status',
            '/api/brain/memory',
            '/api/brain/search',
            '/api/brain/learn',
            '/api/brain/reason',
            '/api/brain/decision',
            '/api/brain/consolidate',
            '/api/brain/stats',
            '/api/brain/perception',
            '/api/brain/process'
        ]
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


# ============================================================================
# DÉMARRAGE
# ============================================================================

if __name__ == '__main__':
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║     ARTIFICIAL BRAIN API SERVER - Démarrage              ║
    ║     Serveur: http://localhost:5000                       ║
    ║     Documentation: http://localhost:5000/api/system/info ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Initialise le cerveau au démarrage
    init_brain()
    
    # Lance le serveur
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=False
    )
