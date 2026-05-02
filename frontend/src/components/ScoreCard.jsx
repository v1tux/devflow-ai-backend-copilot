import { ShieldCheck } from 'lucide-react';

export function ScoreCard({ analysis }) {
  if (!analysis) {
    return (
      <div className="card">
        <div className="row">
          <h2>Resultado</h2>
          <ShieldCheck />
        </div>
        <p>Execute uma análise para visualizar score, resumo técnico e recomendações.</p>
      </div>
    );
  }

  return (
    <div className="card">
      <div className="row">
        <h2>{analysis.project_name}</h2>
        <ShieldCheck />
      </div>
      <div className="score">{analysis.score}</div>
      <p>{analysis.summary}</p>
      <a href={`http://localhost:8000/api/analyses/${analysis.id}/report`} target="_blank" rel="noreferrer">
        Baixar relatório em PDF
      </a>
    </div>
  );
}
