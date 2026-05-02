export function FindingList({ findings = [] }) {
  return (
    <div className="card">
      <h2>Achados técnicos</h2>
      {findings.length === 0 && <p>Nenhum achado ainda.</p>}
      {findings.map((finding, index) => (
        <div className="finding" key={`${finding.file}-${index}`}>
          <div className="severity">{finding.severity} · {finding.category}</div>
          <strong>{finding.file || 'Projeto'}</strong>
          <p>{finding.message}</p>
          <p><b>Recomendação:</b> {finding.recommendation}</p>
        </div>
      ))}
    </div>
  );
}
