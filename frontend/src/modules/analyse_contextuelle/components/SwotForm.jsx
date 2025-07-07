import { useState } from 'react';
import { api } from '../services/api';

export function SwotForm({ onCreated }) {
  const [type, setType] = useState('Strength');
  const [description, setDescription] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    const { data } = await api.post('/swot/', { type, description });
    onCreated(data);
    setDescription('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Type
        <select value={type} onChange={e => setType(e.target.value)}>
          <option>Strength</option>
          <option>Weakness</option>
          <option>Opportunity</option>
          <option>Threat</option>
        </select>
      </label>
      <label>
        Description
        <textarea
          value={description}
          onChange={e => setDescription(e.target.value)}
          required
        />
      </label>
      <button type="submit">Ajouter</button>
    </form>
  );
}
