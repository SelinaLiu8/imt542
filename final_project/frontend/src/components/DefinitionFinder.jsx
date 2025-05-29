import React, { useState } from 'react';

function DefinitionFinder() {
  const [text, setText] = useState('');
  const [definitions, setDefinitions] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      // Step 1: PUT the input text
      await fetch('https://financedefinitionextractor-b9cjgycwckb2bjaw.westus-01.azurewebsites.net/input', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      // Step 2: GET the definitions
      const res = await fetch('https://financedefinitionextractor-b9cjgycwckb2bjaw.westus-01.azurewebsites.net/definitions');
      const data = await res.json();
      setDefinitions(data);
    } catch (err) {
      console.error('Error:', err);
      alert('Failed to fetch definitions');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: 'auto' }}>
      <h2>Investopedia Definition Finder</h2>
      <textarea
        rows="6"
        style={{ width: '100%' }}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste up to 100 words here..."
      />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? 'Analyzing...' : 'Get Definitions'}
      </button>

      {definitions.length > 0 && (
        <div style={{ marginTop: 20 }}>
          <h3>Found Definitions:</h3>
          {definitions.map((def, i) => (
            <div key={i} style={{ marginBottom: 15 }}>
              <strong>{def.term}</strong>: {def.definition}
              <br />
              <a href={def.url} target="_blank" rel="noopener noreferrer">Read more</a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default DefinitionFinder;
