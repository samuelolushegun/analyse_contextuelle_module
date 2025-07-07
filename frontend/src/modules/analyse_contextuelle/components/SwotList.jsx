export function SwotList({ items }) {
  if (!items.length) return <p>Aucun SWOT pour l’instant.</p>;
  return (
    <ul>
      {items.map(swot => (
        <li key={swot.id}>
          <strong>[{swot.type}]</strong> {swot.description}
        </li>
      ))}
    </ul>
  );
}
