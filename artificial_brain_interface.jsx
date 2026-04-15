import React, { useState, useEffect, useRef } from 'react';
import { Activity, Brain, Zap, Memory, Send, TrendingUp, Gauge } from 'lucide-react';

// Couleurs innovantes
const colors = {
  primary: '#6366f1',
  secondary: '#8b5cf6',
  accent: '#ec4899',
  success: '#10b981',
  danger: '#ef4444',
  warning: '#f59e0b',
  bg: '#0f172a',
  surface: '#1e293b',
  text: '#f1f5f9'
};

export default function ArtificialBrainUI() {
  const [input, setInput] = useState('');
  const [thoughts, setThoughts] = useState([]);
  const [brainState, setBrainState] = useState({
    active: true,
    energy: 100,
    learning_mode: true,
    memory_usage: 45
  });
  const [isThinking, setIsThinking] = useState(false);
  const [selectedThought, setSelectedThought] = useState(null);
  const canvasRef = useRef(null);

  // Simulation du cerveau qui pense
  const simulateBrain = async (text) => {
    setIsThinking(true);
    
    const thought = {
      id: Date.now(),
      input: text,
      timestamp: new Date(),
      process: {
        perception: { confidence: Math.random() * 0.3 + 0.7, tokens: text.split(' ').length },
        learning: { patterns: Math.floor(Math.random() * 5), attention: Math.random() },
        reasoning: { conclusions: Math.floor(Math.random() * 3), confidence: Math.random() * 0.4 + 0.6 },
        decision: { action: ['analyze', 'learn', 'reason', 'respond'][Math.floor(Math.random() * 4)], confidence: Math.random() * 0.3 + 0.7 }
      },
      output: `Processing: "${text.substring(0, 50)}..." - Neural pathways activated. Generating response...`
    };

    // Animation de pensée
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    setThoughts(prev => [thought, ...prev.slice(0, 9)]);
    setSelectedThought(thought);
    setBrainState(prev => ({
      ...prev,
      energy: Math.max(prev.energy - 15, 20),
      memory_usage: Math.min(prev.memory_usage + 8, 95)
    }));
    
    setIsThinking(false);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      simulateBrain(input);
      setInput('');
    }
  };

  // Visualisation du cerveau en 3D (animation)
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let animationId;
    let time = 0;

    const drawBrain = () => {
      const w = canvas.width;
      const h = canvas.height;
      
      ctx.fillStyle = colors.bg;
      ctx.fillRect(0, 0, w, h);

      // Grille de neurones
      ctx.strokeStyle = colors.primary + '33';
      ctx.lineWidth = 1;

      for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
          const x = (i + 1) * (w / 9);
          const y = (j + 1) * (h / 9);
          
          // Neurone
          const pulse = Math.sin(time * 0.05 + i + j) * 0.5 + 0.5;
          ctx.fillStyle = colors.secondary + Math.floor(pulse * 255).toString(16).padStart(2, '0');
          ctx.beginPath();
          ctx.arc(x, y, 3 + pulse * 2, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // Connexions
      for (let i = 0; i < 7; i++) {
        for (let j = 0; j < 7; j++) {
          const x1 = (i + 1) * (w / 9);
          const y1 = (j + 1) * (h / 9);
          const x2 = (i + 2) * (w / 9);
          const y2 = (j + 1) * (h / 9);
          
          const opacity = Math.sin(time * 0.03 + i * j) * 0.3 + 0.3;
          ctx.strokeStyle = colors.accent + Math.floor(opacity * 255).toString(16).padStart(2, '0');
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
          ctx.stroke();
        }
      }

      time++;
      animationId = requestAnimationFrame(drawBrain);
    };

    canvas.width = canvas.offsetWidth * 2;
    canvas.height = canvas.offsetHeight * 2;
    ctx.scale(2, 2);

    drawBrain();

    return () => cancelAnimationFrame(animationId);
  }, []);

  const ThoughtProcess = ({ thought, isSelected }) => (
    <div
      onClick={() => setSelectedThought(thought)}
      style={{
        background: isSelected ? colors.primary : colors.surface,
        borderLeft: `3px solid ${colors.accent}`,
        cursor: 'pointer',
        transition: 'all 0.3s ease'
      }}
      className="p-4 rounded-lg hover:bg-opacity-80 transform hover:scale-102"
    >
      <div className="flex justify-between items-start mb-2">
        <span className="font-bold text-sm" style={{ color: colors.text }}>{thought.process.decision.action}</span>
        <span className="text-xs" style={{ color: colors.warning }}>
          {Math.round(thought.process.decision.confidence * 100)}%
        </span>
      </div>
      <p className="text-sm line-clamp-2" style={{ color: colors.text }}>{thought.input}</p>
      <div className="mt-2 flex gap-2 text-xs">
        <span style={{ color: colors.success }}>Patterns: {thought.process.learning.patterns}</span>
      </div>
    </div>
  );

  return (
    <div style={{ background: colors.bg, color: colors.text }} className="min-h-screen p-8">
      <style>{`
        .line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .hover\\:scale-102:hover { transform: scale(1.02); }
        .pulse { animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        .glow { box-shadow: 0 0 20px ${colors.primary}88; }
        input, textarea { background: ${colors.surface} !important; color: ${colors.text} !important; border-color: ${colors.primary} !important; }
      `}</style>

      {/* Header */}
      <div className="mb-12">
        <div className="flex items-center gap-3 mb-4">
          <Brain size={40} style={{ color: colors.primary }} />
          <div>
            <h1 className="text-4xl font-bold">Artificial Brain</h1>
            <p style={{ color: colors.secondary }} className="text-sm">Interactive Neural Processing System</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-8 mb-8">
        
        {/* Colonne 1: Visualisation du cerveau */}
        <div style={{ background: colors.surface }} className="rounded-2xl p-6 col-span-1">
          <h3 className="font-bold mb-4 flex items-center gap-2">
            <Zap size={20} style={{ color: colors.accent }} />
            Neural Activity
          </h3>
          <canvas
            ref={canvasRef}
            style={{ background: colors.bg, borderRadius: '12px' }}
            className="w-full h-48 border border-opacity-20"
          />
        </div>

        {/* Colonne 2: État du cerveau */}
        <div style={{ background: colors.surface }} className="rounded-2xl p-6 col-span-1">
          <h3 className="font-bold mb-4 flex items-center gap-2">
            <Activity size={20} style={{ color: colors.success }} />
            Brain State
          </h3>
          
          <div className="space-y-4">
            {/* Énergie */}
            <div>
              <div className="flex justify-between text-sm mb-2">
                <span>Energy Level</span>
                <span>{brainState.energy}%</span>
              </div>
              <div style={{ background: colors.bg }} className="w-full h-3 rounded-full overflow-hidden">
                <div
                  style={{
                    background: brainState.energy > 50 ? colors.success : colors.danger,
                    width: `${brainState.energy}%`
                  }}
                  className="h-full transition-all duration-500"
                />
              </div>
            </div>

            {/* Mémoire */}
            <div>
              <div className="flex justify-between text-sm mb-2">
                <span>Memory Usage</span>
                <span>{brainState.memory_usage}%</span>
              </div>
              <div style={{ background: colors.bg }} className="w-full h-3 rounded-full overflow-hidden">
                <div
                  style={{
                    background: colors.primary,
                    width: `${brainState.memory_usage}%`
                  }}
                  className="h-full transition-all duration-500"
                />
              </div>
            </div>

            {/* Status */}
            <div className="mt-4 space-y-2">
              <p className="text-xs">
                <span style={{ color: colors.success }}>●</span> {' '}
                {brainState.active ? 'Active' : 'Idle'}
              </p>
              <p className="text-xs">
                <span style={{ color: colors.warning }}>●</span> {' '}
                Learning Mode {brainState.learning_mode ? 'ON' : 'OFF'}
              </p>
            </div>
          </div>
        </div>

        {/* Colonne 3: Statistiques */}
        <div style={{ background: colors.surface }} className="rounded-2xl p-6 col-span-1">
          <h3 className="font-bold mb-4 flex items-center gap-2">
            <TrendingUp size={20} style={{ color: colors.warning }} />
            Statistics
          </h3>

          <div className="space-y-3">
            <div>
              <p className="text-xs" style={{ color: colors.secondary }}>Thoughts Processed</p>
              <p className="text-2xl font-bold">{thoughts.length}</p>
            </div>
            <div>
              <p className="text-xs" style={{ color: colors.secondary }}>Avg Confidence</p>
              <p className="text-2xl font-bold">
                {thoughts.length > 0 ? Math.round(
                  thoughts.reduce((sum, t) => sum + t.process.decision.confidence, 0) / thoughts.length * 100
                ) : 0}%
              </p>
            </div>
            <div>
              <p className="text-xs" style={{ color: colors.secondary }}>Learning Rate</p>
              <p className="text-2xl font-bold">0.01</p>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-8">
        
        {/* Entrée */}
        <div style={{ background: colors.surface }} className="rounded-2xl p-6 col-span-2">
          <h3 className="font-bold mb-4">Input</h3>
          <form onSubmit={handleSubmit} className="space-y-4">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask the artificial brain anything..."
              className="w-full p-4 border rounded-lg resize-none focus:outline-none focus:ring-2"
              style={{ borderColor: colors.primary, minHeight: '100px' }}
              disabled={isThinking}
            />
            <button
              type="submit"
              disabled={isThinking || !input.trim()}
              style={{
                background: isThinking ? colors.secondary : colors.primary,
                opacity: isThinking || !input.trim() ? 0.5 : 1
              }}
              className="w-full py-3 rounded-lg font-bold flex items-center justify-center gap-2 transition-all"
            >
              <Send size={18} />
              {isThinking ? 'Thinking...' : 'Send to Brain'}
            </button>
          </form>
        </div>

        {/* Détails du pensée sélectionnée */}
        <div style={{ background: colors.surface }} className="rounded-2xl p-6">
          <h3 className="font-bold mb-4 flex items-center gap-2">
            <Memory size={20} style={{ color: colors.accent }} />
            Thought Details
          </h3>

          {selectedThought ? (
            <div className="space-y-3 text-sm">
              <div>
                <p style={{ color: colors.secondary }}>Input</p>
                <p className="truncate">{selectedThought.input}</p>
              </div>
              <div className="grid grid-cols-2 gap-2">
                <div style={{ background: colors.bg }} className="p-3 rounded">
                  <p style={{ color: colors.secondary }} className="text-xs mb-1">Perception</p>
                  <p className="font-bold">{Math.round(selectedThought.process.perception.confidence * 100)}%</p>
                </div>
                <div style={{ background: colors.bg }} className="p-3 rounded">
                  <p style={{ color: colors.secondary }} className="text-xs mb-1">Learning</p>
                  <p className="font-bold">{selectedThought.process.learning.patterns} patterns</p>
                </div>
              </div>
              <div className="grid grid-cols-2 gap-2">
                <div style={{ background: colors.bg }} className="p-3 rounded">
                  <p style={{ color: colors.secondary }} className="text-xs mb-1">Reasoning</p>
                  <p className="font-bold">{Math.round(selectedThought.process.reasoning.confidence * 100)}%</p>
                </div>
                <div style={{ background: colors.bg }} className="p-3 rounded">
                  <p style={{ color: colors.secondary }} className="text-xs mb-1">Decision</p>
                  <p className="font-bold capitalize">{selectedThought.process.decision.action}</p>
                </div>
              </div>
            </div>
          ) : (
            <p style={{ color: colors.secondary }} className="text-sm">Select a thought to view details</p>
          )}
        </div>
      </div>

      {/* Historique des pensées */}
      <div style={{ background: colors.surface }} className="rounded-2xl p-6 mt-8">
        <h3 className="font-bold mb-4">Thought History</h3>
        <div className="grid grid-cols-5 gap-4 max-h-64 overflow-y-auto">
          {thoughts.map((thought) => (
            <ThoughtProcess
              key={thought.id}
              thought={thought}
              isSelected={selectedThought?.id === thought.id}
            />
          ))}
          {thoughts.length === 0 && (
            <p style={{ color: colors.secondary }} className="col-span-5 text-center py-8">
              No thoughts yet. Start by asking the brain a question.
            </p>
          )}
        </div>
      </div>

      {/* Output */}
      {selectedThought && (
        <div style={{ background: colors.surface }} className="rounded-2xl p-6 mt-8">
          <h3 className="font-bold mb-4">Brain Output</h3>
          <p style={{ color: colors.text }} className="p-4 rounded-lg" style={{ background: colors.bg }}>
            {selectedThought.output}
          </p>
        </div>
      )}
    </div>
  );
}
