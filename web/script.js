document.getElementById('imageForm').addEventListener('submit', async function(e) {
    e.preventDefault();
  
    const input = document.getElementById('imageInput');
    const file = input.files[0];
  
    if (!file) return;
  
    const formData = new FormData();
    formData.append('image', file);
  
    const response = await fetch('/analyze', {
      method: 'POST',
      body: formData
    });
  
    const resultDiv = document.getElementById('result');
    const output = document.getElementById('output');
  
    if (response.ok) {
      const data = await response.json();
      output.textContent = JSON.stringify(data, null, 2);
      resultDiv.style.display = 'block';
    } else {
      output.textContent = 'Fehler bei der Analyse';
      resultDiv.style.display = 'block';
    }
  });
  