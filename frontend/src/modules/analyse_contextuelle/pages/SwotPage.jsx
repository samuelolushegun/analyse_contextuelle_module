import { useEffect, useState } from 'react';
import { api } from '../services/api';
import { SwotForm } from '../components/SwotForm';
import { SwotList } from '../components/SwotList';

export default function SwotPage() {
  const [items, setItems] = useState([]);

  // Charger la liste au montage
  useEffect(() => {
    api.get('/swot/').then(res => setItems(res.data));
  }, []);

  // Après création, on rafraîchit la liste
  const handleCreated = newItem => {
    setItems(prev => [newItem, ...prev]);
  };

  return (
    <div>
      <h1>SWOT Analysis</h1>
      <SwotForm onCreated={handleCreated} />
      <SwotList items={items} />
    </div>
  );
}
